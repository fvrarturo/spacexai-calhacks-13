export const $ = (selector, root = document) => root.querySelector(selector);
export const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export async function readJSON(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Could not load ${url} (${response.status})`);
  return response.json();
}
export function failure(target, error) {
  $(target).innerHTML = `<div class="error" role="alert">This result is unavailable. ${esc(error.message)}. Rebuild the project after running the analysis.</div>`;
}
export const fixed = (value, digits = 1) => Number(value).toFixed(digits);
