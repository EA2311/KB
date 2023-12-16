

def assessment(unit, rules):
    for rule in rules:
        if unit.operating_mode == rule.operating_mode and unit.duration_of_operation == rule.duration_of_operation and unit.structural_risk == rule.structural_risk and unit.functional_risk == rule.functional_risk and unit.damage == rule.damage:
            return rule.system_condition_assessment, rule.expert_assessment
    return 0, 0
