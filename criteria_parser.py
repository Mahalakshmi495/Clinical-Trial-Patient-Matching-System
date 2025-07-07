def parse_criteria(trial):
    return {
        "min_age": trial.get("min_age"),
        "max_age": trial.get("max_age"),
        "conditions": set(trial.get("conditions", [])),
        "excluded_conditions": set(trial.get("excluded_conditions", [])),
        "location": trial.get("location")
    }
