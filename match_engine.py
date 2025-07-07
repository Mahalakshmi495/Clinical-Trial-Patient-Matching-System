def is_eligible(patient, trial_criteria):
    if not (trial_criteria["min_age"] <= patient["age"] <= trial_criteria["max_age"]):
        return False
    if not trial_criteria["conditions"].intersection(set(patient["conditions"])):
        return False
    if trial_criteria["excluded_conditions"].intersection(set(patient["conditions"])):
        return False
    if trial_criteria["location"] != patient["location"]:
        return False
    return True
