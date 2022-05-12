def predict(x):
    idle, months_since_longest_blank_period, months_since_last_blank_period, rel_units_avg_3_6, rel_units_avg_3_6_df, rel_units_avg_3_12, rel_units_avg_3_12_df, rel_units_avg_6_12, rel_units_avg_6_12_df, rel_units_avg_3_lifetime, rel_units_avg_6_lifetime, rel_units_avg_12_lifetime, avg_monthly_units_over_blank_periods, total_units_before_last_blank_period, total_units_before_longest_blank_period, units_avg_3_rank, units_avg_6_rank, units_avg_12_rank, lifetime_monthly_units_rank, lifetime_total_units_rank, lifetime_total_transactions_rank, lifetime_rank, total_blank_periods_rank, last_blank_period_length_rank, longest_blank_period_length_rank, cv_monthly_units_over_blank_periods_rank, vending_category_is_healthfacilities, vending_category_is_nonresidential, vending_category_is_residential, vending_category_is_smallindustries = x
    if (rel_units_avg_3_6 > -0.26) and (idle <= 0.5) and (units_avg_12_rank > -3.28843):
        return {'proba': 0.0, 'samples': 0, 'rule': '(rel_units_avg_3_6 > -0.26) and (idle <= 0.5) and (units_avg_12_rank > -3.28843)'}
    if (rel_units_avg_3_6 <= -0.26):
        return {'proba': 1.0, 'samples': 92, 'rule': '(rel_units_avg_3_6 <= -0.26)'}
    if (rel_units_avg_3_6 > -0.26) and (idle > 0.5) and (rel_units_avg_3_6 <= 0.2305) and (cv_monthly_units_over_blank_periods_rank > -0.58063):
        return {'proba': 0.6032, 'samples': 63, 'rule': '(rel_units_avg_3_6 > -0.26) and (idle > 0.5) and (rel_units_avg_3_6 <= 0.2305) and (cv_monthly_units_over_blank_periods_rank > -0.58063)'}
    if (rel_units_avg_3_6 > -0.26) and (idle > 0.5) and (rel_units_avg_3_6 > 0.2305):
        return {'proba': 1.0, 'samples': 49, 'rule': '(rel_units_avg_3_6 > -0.26) and (idle > 0.5) and (rel_units_avg_3_6 > 0.2305)'}
    if (rel_units_avg_3_6 > -0.26) and (idle <= 0.5) and (units_avg_12_rank <= -3.28843) and (cv_monthly_units_over_blank_periods_rank <= 0.73445):
        return {'proba': 0.0, 'samples': 0, 'rule': '(rel_units_avg_3_6 > -0.26) and (idle <= 0.5) and (units_avg_12_rank <= -3.28843) and (cv_monthly_units_over_blank_periods_rank <= 0.73445)'}
    if (rel_units_avg_3_6 > -0.26) and (idle <= 0.5) and (units_avg_12_rank <= -3.28843) and (cv_monthly_units_over_blank_periods_rank > 0.73445):
        return {'proba': 0.4286, 'samples': 5, 'rule': '(rel_units_avg_3_6 > -0.26) and (idle <= 0.5) and (units_avg_12_rank <= -3.28843) and (cv_monthly_units_over_blank_periods_rank > 0.73445)'}
    if (rel_units_avg_3_6 > -0.26) and (idle > 0.5) and (rel_units_avg_3_6 <= 0.2305) and (cv_monthly_units_over_blank_periods_rank <= -0.58063):
        return {'proba': 0.0, 'samples': 0, 'rule': '(rel_units_avg_3_6 > -0.26) and (idle > 0.5) and (rel_units_avg_3_6 <= 0.2305) and (cv_monthly_units_over_blank_periods_rank <= -0.58063)'}
