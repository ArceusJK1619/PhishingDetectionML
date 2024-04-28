async function getCurrentTab() {
    let queryOptions = { active: true, lastFocusedWindow: true };
    let [tab] = await chrome.tabs.query(queryOptions);
    return tab;
  }
  
  async function updatePopup() {
    let tab = await getCurrentTab();
    if (tab) {
      document.getElementById('tab-info').textContent = `Title: ${tab.title}, URL: ${tab.url}`;
    } else {
      document.getElementById('tab-info').textContent = 'No active tab found';
    }
  }
  
  document.addEventListener('DOMContentLoaded', updatePopup);
  