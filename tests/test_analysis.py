import copy
import unittest
from analysis.compare_runs import compare
from analysis.fleet import CAPABILITIES, POLICIES, return_time, simulate, workload
from analysis.sweep import SCENARIOS

class FleetTests(unittest.TestCase):
    def test_reproducible_workloads(self):
        self.assertEqual(workload(42), workload(42))
        self.assertNotEqual(workload(42), workload(43))

    def test_schedule_invariants_for_all_policies(self):
        jobs=workload(14,jobs=90)
        for policy in POLICIES:
            with self.subTest(policy=policy):
                result=simulate(jobs,policy)
                self.assertLessEqual(result['delivered'],result['submitted'])
                self.assertLessEqual(result['on_time'],result['delivered'])
                self.assertGreaterEqual(result['utilization'],0)
                self.assertLessEqual(result['utilization'],1+1e-10)
                events=result['events']
                self.assertEqual(len({e['id'] for e in events}),len(events))
                for event in events:
                    self.assertIn(event['family'],CAPABILITIES[event['capsule']])
                    self.assertGreaterEqual(event['start'],event['arrival'])
                    self.assertGreaterEqual(event['finish'],event['start']+event['actual'])
                    self.assertGreaterEqual(event['delivery']+1e-9,event['finish'])
                    if event['delivered']:
                        self.assertTrue(event['succeeds'])
                        self.assertLessEqual(event['delivery'],120)
                for capsule in range(3):
                    sequence=sorted((e for e in events if e['capsule']==capsule),key=lambda e:e['start'])
                    for first,second in zip(sequence,sequence[1:]):self.assertLessEqual(first['finish'],second['start']+1e-9)

    def test_empty_and_zero_delivery_cases(self):
        self.assertEqual(simulate([], 'fifo')['on_time_rate'],0)
        result=simulate(workload(4,failure_rate=1),'coordinated')
        self.assertEqual(result['delivered'],0)
        self.assertIsNone(result['cost_per_delivered'])
        self.assertGreater(result['delivery_wait'],0)

    def test_exact_return_boundary(self):
        self.assertEqual(return_time(24,0,24),24)
        self.assertEqual(return_time(24.1,0,24),48)
        self.assertEqual(return_time(8,1,24),8)

    def test_no_assignment_uses_hidden_outcome(self):
        jobs=workload(5)
        for j in jobs:j['arrival']=0
        alternate=copy.deepcopy(jobs)
        for j in alternate:j['actual']*=2;j['succeeds']=not j['succeeds']
        for policy in POLICIES:
            a=simulate(jobs,policy)['events'][:3]
            b=simulate(alternate,policy)['events'][:3]
            self.assertEqual([(e['id'],e['capsule']) for e in a],[(e['id'],e['capsule']) for e in b])

    def test_dedicated_avoids_changeovers(self):
        self.assertEqual(simulate(workload(7),'dedicated')['setup_hours'],0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):simulate([], 'missing')
        with self.assertRaises(ValueError):simulate([], 'fifo',cadence=0)

    def test_sensitivity_grid(self):
        self.assertEqual(len(SCENARIOS),24)
        self.assertEqual(len({tuple(sorted(s.items())) for s in SCENARIOS}),24)

class MaterialsTests(unittest.TestCase):
    def row(self,pair,block,flight,earth):
        return dict(pair_id=pair,block_id=block,metric='viscosity',unit='cP',flight_value=flight,earth_value=earth)

    def test_replicates_do_not_inflate_independent_units(self):
        result=compare([self.row('a','flight-1',2,4),self.row('b','flight-1',4,4),self.row('c','flight-2',6,4)])
        self.assertEqual(result['independent_blocks'],2)
        self.assertEqual(result['effect_flight_minus_earth'],.5)
        self.assertIsNone(result['effect_ci'])

    def test_matching_and_unit_validation(self):
        a=self.row('a','flight-1',2,4)
        with self.assertRaises(ValueError):compare([a,a])
        b=self.row('b','flight-2',2,4);b['unit']='Pa s'
        with self.assertRaises(ValueError):compare([a,b])
        with self.assertRaises(ValueError):compare([self.row('a','',2,4)])
        with self.assertRaises(ValueError):compare([self.row('a','b',float('nan'),4)])

    def test_zero_effect_interval(self):
        result=compare([self.row(str(i),str(i),4,4) for i in range(3)])
        self.assertEqual(result['effect_ci']['low'],0)
        self.assertEqual(result['effect_ci']['high'],0)

if __name__=='__main__':unittest.main()
