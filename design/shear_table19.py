import pandas as pd

table19 = pd.read_csv("database/shear_table19.csv")

def get_tau_c(p, fck):

    row = table19.iloc[(table19['p']-p).abs().argsort()[:1]]

    return row[f"fck{fck}"].values[0]
