import pandas as pd

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
def scores():
    score = df_final['score']
    bins = (0, 3, 5, 6, 8, 9, 10)
    labels = ('Pésimo', 'Flojo', 'Para fans', 'Recomendado', 'Muy bueno', 'Obra maestra')
    groups = pd.cut(score, bins=bins, labels=labels)
    return scores

# Funciones para los gráficos.
def plt_score():
    colors = ('#28C3A6', '#2893C3', '#2845C3', '#5828C3', '#A628C3', '#C32893')
    ax = scores.plot.bar(rot=0, color=colors, figsize=(16,10))
    plt.title("Ranking score by reviewers", fontsize=16)
    plt.ylabel('No. Albums', fontsize=14)
    plt.xlabel('Scores', fontsize=14)
    return plt.show()

def plt_genre():
    colors = ('#DAF7A6', '#FFE99F', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845')
    ax = loved_genres.plot.bar(rot=0, color=colors, figsize=(16,10))
    plt.title("Genres preferred by Pitchfork Reviewers", fontsize=16)
    plt.ylabel('No. Votes Scored: #10', fontsize=14)
    plt.xlabel('Genres', fontsize=14)
    return plt.show()


# Funciones para la API.
def res_api():
    key = open(".env").read()
    url = 'http://ws.audioscrobbler.com/2.0/'
    response = requests.get(url+"?method=album.getinfo&api_key={}&artist=Cher&album=Believe&format=json".format(key))
    res = response.json()
    return res