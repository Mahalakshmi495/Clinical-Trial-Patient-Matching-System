def score_match(patient, trial_criteria):
    score = 0
    score += len(set(patient["conditions"]).intersection(trial_criteria["conditions"])) * 10
    score -= abs(patient["age"] - (trial_criteria["min_age"] + trial_criteria["max_age"]) // 2)
    score += 20 if patient["location"] == trial_criteria["location"] else 0
    return score
