from flask import Flask, request, jsonify
import json, datetime

app = Flask(__name__)
audit_log = 'audit_log.jsonl'
bankroll = 50
predictions_remaining = 5

@app.route('/bankroll_status')
def bankroll_status():
    return jsonify({'current_balance': bankroll, 'predictions_remaining': predictions_remaining})

@app.route('/predict_live', methods=['POST'])
def predict_live():
    global predictions_remaining
    if predictions_remaining <= 0:
        return jsonify({'error': 'No predictions remaining'}), 403
    data = request.json
    # Simple placeholder prediction logic
    result = {'expected_goals_home': 1.5, 'expected_goals_away': 1.0, 'p_over_2_5': 0.55, 'p_btts': 0.6}
    predictions_remaining -= 1
    # Audit log
    with open(audit_log, 'a') as f:
        entry = {'timestamp': datetime.datetime.now().isoformat(), 'action': 'predict_match', 'data': data, 'result': result}
        f.write(json.dumps(entry) + '\n')
    return jsonify(result)

@app.route('/accumulator_live', methods=['POST'])
def accumulator_live():
    data = request.json
    matches = data.get('matches', [])
    results = []
    for match in matches:
        results.append({'match_id': match.get('match_id'), 'predicted': 'win'})
    return jsonify({'accumulator_results': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
