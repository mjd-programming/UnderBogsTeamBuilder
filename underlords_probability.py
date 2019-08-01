level_percents = [
    [1, 0, 0, 0, 0],
    [0.7, 0.3, 0, 0, 0],
    [0.6, 0.35, 0.05, 0, 0],
    [0.5, 0.35, 0.15, 0, 0],
    [0.4, 0.35, 0.23, 0.02, 0],
    [0.33, 0.3, 0.3, 0.7, 0],
    [0.3, 0.3, 0.3, 0.1, 0],
    [0.24, 0.3, 0.3, 0.15, 0.01],
    [0.22, 0.25, 0.25, 0.20, 0.03],
    [0.19, 0.25, 0.25, 0.25, 0.06],
    [0.13, 0.20, 0.25, 0.3, 0.12]
]

tier_amounts = [45, 30, 25, 15, 10]

tier_uniques = [14, 14, 13, 13, 6]

def get_chance_appear_shop(num_find, level, t, units, tier_units):
    tier = t - 1
    tier_units_left = (tier_amounts[tier] * tier_uniques[tier]) - tier_units
    units_left = tier_amounts[tier] - units
    temp_percent = 1
    for i in range(5):
        temp_percent *= (tier_units_left-units_left-i)/(tier_units_left-i)
    return (level_percents[level][tier]*(1-temp_percent))**num_find if num_find < 6 else 0

def get_estimated_gold(shop_chance):
    return 100/shop_chance * 2