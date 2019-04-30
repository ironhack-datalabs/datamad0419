import pandas as pd

# Función para importar los archivos csv.
def df_frames(files):
    dframes = []
    for file in files:
        dframes.append(pd.read_csv(file))
    return dframes


# Función para dejar los elementos con nota 10 en el dataset.
def filter_score(dfx): 
    dfx = dfx[dfx['score'] == 10.0]
    return dfx


# Función para los bins de score.


# Funciones para los gráficos.


def save_viz(plt, title):
    plt = ax.get_figure()
    plt.savefig(title + '.png')
    return plt


# Funciones para la API.