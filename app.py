from flask import Flask, render_template, request, jsonify
import json
from parser.criteria_parser import parse_criteria
from matcher.match_engine import is_eligible
from scorer.score_engine import score_match
from recommender.recommender import recommend_trials

app = Flask(__name__)

with open('data/clinical_trials.json') as f:
    trials = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    patient = request.get_json()
    results = recommend_trials(patient, trials)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
