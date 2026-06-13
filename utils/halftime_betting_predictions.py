import pandas as pd

def halftime_betting_predictions(dataset):
    dataFrame = pd.DataFrame(dataset['opponent_name','team_name','passes_completed','passes_attempted','possesion_h1','shots_h1','shots_on_target_h1','corners_h1','fouls_h1','yello_cards_h1','red_Cards_h1','outcome'])

    