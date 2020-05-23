import sys


def elo_rating(rating_a, rating_b, rating_point_advantage, k_upper, k_lower, winner=None):
    coefficient_1, coefficient_2 = calculate_coefficient(rating_a, rating_b, rating_point_advantage)

    expected_score_a = 1/(1 + coefficient_1)

    expected_score_b = 1/(1 + coefficient_2)

    s_1, s_2, k_1, k_2 = calculate_k_and_s(rating_a, rating_b, k_upper, k_lower, winner)

    new_rating_a = rating_a + k_1 * (s_1 - expected_score_a)
    new_rating_b = rating_b + k_2 * (s_2 - expected_score_b)

    return new_rating_a, new_rating_b


def calculate_coefficient(rating_a, rating_b, rating_point_advantage):
    power_coefficient_1 = (rating_b - rating_a) / rating_point_advantage
    coefficient_1 = 10 ** power_coefficient_1

    power_coefficient_2 = (rating_a - rating_b) / rating_point_advantage
    coefficient_2 = 10 ** power_coefficient_2

    return coefficient_1, coefficient_2


def calculate_k_and_s(rating_a, rating_b, k_upper, k_lower, winner):
    k_1 = k_2 = k_lower
    s_1 = s_2 = 0

    if winner == 'first':
        if rating_a < rating_b:
            k_1 = k_upper
            k_2 = k_upper
        s_1 = 1

    elif winner == 'second':
        if rating_b < rating_a:
            k_1 = k_upper
            k_2 = k_upper
        s_2 = 1
    else:
        if rating_b < rating_a:
            k_2 = k_upper
        if rating_a < rating_b:
            k_1 = k_upper

        s_1 = s_2 = 0.5

    return s_1, s_2, k_1, k_2
