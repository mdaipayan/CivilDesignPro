import pandas as pd

interaction = pd.read_csv("database/sp16_interaction.csv")

def column_design(Pu, Mu):

    safe = interaction[
        (interaction['Pu']>=Pu) &
        (interaction['Mu']>=Mu)
    ]

    return safe.iloc[0]
