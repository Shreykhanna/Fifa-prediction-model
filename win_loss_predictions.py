import pandas as pd

def win_loss_predicions(fifa_dataset):
    dataFrame = pd.DataFrame(fifa_dataset.drop(
        columns=['match_date', 'match_time', 'stadium_name', 'city_name', 'result', 'team_code', 'stage_name',
                 'group_name', 'opponent_code', 'possession_h1', 'shots_h1', 'shots_on_target_h1', 'possession_h1',
                 'possession_h2', 'h2h_prior_matches', 'h2h_prior_win_rate', 'yellow_cards', 'red_cards',
                 'passes_attempted_h1', 'corners_h1', 'corners_h2', 'yellow_cards_h1', 'shots_h1', 'shots_h2',
                 'shots_on_target', 'shots_on_target_h1', 'shots_on_target_h2', 'shots', 'passes_completed',
                 'passes_attempted', 'passes_completed_h1', 'red_cards_h2', 'knockout_stage', 'group_stage',
                 'opp_curr_goals_scored_avg', 'opp_curr_goals_conceded_avg', 'team_curr_goals_conceded_avg',
                 'team_curr_goals_scored_avg']))
    # print(dataFrame.info())
    dataFrame['team_avg_goals_scored'] = dataFrame.groupby('team_name')['goals_for'].transform(
        lambda x: x.shift(1).rolling(3, min_periods=1).mean())
    dataFrame['team_avg_goals_conceded'] = dataFrame.groupby('team_name')['goals_against'].transform(
        lambda x: x.shift(1).rolling(3, min_periods=1).mean())
    dataFrame['goals_differential_avg'] = dataFrame['team_avg_goals_scored'] - dataFrame['team_avg_goals_conceded']
    dataFrame['opp_goal_diff_avg'] = dataFrame['opp_prior_goals_scored_avg'] - dataFrame['opp_prior_goals_conceded_avg']
    return dataFrame

