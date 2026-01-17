const API_BASE = 'https://your-rgholdings-backend.onrender.com';

async function refreshBankroll(){
  const res = await fetch(API_BASE + '/bankroll_status');
  const data = await res.json();
  document.getElementById('balance').textContent = data.current_balance;
  document.getElementById('remaining').textContent = data.predictions_remaining;
}

async function predictLive(){
  const match_id = document.getElementById('match_id').value;
  const hs = parseFloat(document.getElementById('hs').value);
  const aw = parseFloat(document.getElementById('aw').value);
  const res = await fetch(API_BASE + '/predict_live', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({match_id, home_strength: hs, away_strength: aw})
  });
  const data = await res.json();
  document.getElementById('result').textContent = JSON.stringify(data,null,2);
  refreshBankroll();
}

async function buildAccumulator(){
  const matches = JSON.parse(document.getElementById('matches').value);
  const res = await fetch(API_BASE + '/accumulator_live', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({matches})
  });
  const data = await res.json();
  document.getElementById('result').textContent = JSON.stringify(data,null,2);
}

setInterval(refreshBankroll,60000);
refreshBankroll();
