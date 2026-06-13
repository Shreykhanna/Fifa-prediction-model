from utils.phik_matrix_calculation import phik_matrix_calculation

def halftime_betting_predictions(dataset):
    dataFrame = dataset[[
        'opponent_name', 'team_name', 'passes_completed', 'passes_attempted',
        'possession_h1', 'shots_h1', 'shots_on_target_h1',
        'fouls_h1', 'yellow_cards_h1', 'red_cards_h1', 'outcome'
    ]].copy()
    dataFrame['shot_accuracy_h1'] = dataFrame['shots_on_target_h1'] / (dataFrame['shots_h1'] + 1e-5)
    dataFrame['pass_completion_rate'] = dataFrame['passes_completed'] / (dataFrame['passes_attempted'] + 1e-5)
    final_features = [
        'opponent_name', 'team_name',
        'possession_h1', 'shot_accuracy_h1', 'pass_completion_rate',
        'red_cards_h1',
        'outcome'
    ]
    dataFrame_final = dataFrame[final_features]
    phik_matrix_calculation(dataFrame_final)
    return dataFrame

