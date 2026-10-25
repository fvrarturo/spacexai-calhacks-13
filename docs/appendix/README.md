# Appendix — methods notes

Each big-data workstream has its own methods note. A note lists the data sources (with sizes and access dates), the processing steps, the Slurm job IDs on MIT Engaging, the statistics, the limitations and the commands to reproduce the result. The website's Appendix tab (`appendix.html`) renders the same information from the result files in `data/results/bigdata/`.

| Note | Pillar | What it covers |
|---|---|---|
| [pdb.md](pdb.md) | Materials · protein crystals | Every space-grown crystal structure in the Protein Data Bank, matched against Earth-grown structures of the same protein |
| [matdb.md](matdb.md) | Materials · drug crystals, MOFs, photonic colloids | Polymorphism in the Crystallography Open Database; MOF pore-window screen; colloid sedimentation physics |
| [psi.md](psi.md) | Materials · cooling; Foundry · observation | NASA PSI ISS physical-science archive inventory; DECLIC-DSI solidification image analysis |
| [orbit.md](orbit.md) | Foundry · orbit selection; Network · congestion | Residual drag acceleration, orbital lifetime, shell crowding and sunlight fraction from the full satellite tracking history |
| [logistics.md](logistics.md) | Network · scale and demand; Foundry · SpaceX | Launch and return cadence (GCAT), clinical-trial demand for subcutaneous biologics, the literature and partner map (OpenAlex) |
| [AGENT_BRIEF.md](AGENT_BRIEF.md) | All | The shared conventions every workstream followed: evidence labels, result schema, cluster rules |

Grok reviews of each result (if run with `python3 -m analysis.grok_review`) are saved in `data/results/bigdata/reviews/`.
