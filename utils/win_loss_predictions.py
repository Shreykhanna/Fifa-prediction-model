from utils.phik_matrix_calculation import phik_matrix_calculation

def win_loss_predictions(fifa_dataset):
    dataFrame = fifa_dataset[[
        'opponent_name', 'team_name',
        'team_prior_goals_scored_avg', 'team_prior_goals_conceded_avg',
        'opp_prior_goals_scored_avg', 'opp_prior_goals_conceded_avg',
        'outcome'
    ]].copy()

    dataFrame['goals_differential_avg'] = dataFrame['team_prior_goals_scored_avg'] - dataFrame[
        'team_prior_goals_conceded_avg']
    dataFrame['opp_goal_diff_avg'] = dataFrame['opp_prior_goals_scored_avg'] - dataFrame['opp_prior_goals_conceded_avg']

    dataFrame['net_goal_diff'] = dataFrame['goals_differential_avg'] - dataFrame['opp_goal_diff_avg']

    final_features = [
        'opponent_name', 'team_name',
        'goals_differential_avg', 'opp_goal_diff_avg', 'net_goal_diff',
        'outcome'
    ]

    data_frame_final = dataFrame[final_features]

    print(data_frame_final.head())

    phik_matrix_calculation(data_frame_final)

    return data_frame_final