import pandas as pd

def df_frames(files):
    dframes = []
    for file in files:
        dframes.append(pd.read_csv(file))
    return dframes