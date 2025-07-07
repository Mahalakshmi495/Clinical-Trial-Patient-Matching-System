from matcher.match_engine import is_eligible
from parser.criteria_parser import parse_criteria
from scorer.score_engine import score_match


def recommend_trials(patient, trials):
    recommendations = []
    for trial in trials:
        criteria = parse_criteria(trial)
        if is_eligible(patient, criteria):
            score = score_match(patient, criteria)
            recommendations.append((trial["id"], score))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
