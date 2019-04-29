from config import SALIDA_PATH

def save_viz(chart, title):
    fig = chart.get_figure()
    fig.savefig(SALIDA_PATH + title + '.png')    

def guardar_csv(data, title):
    data.to_csv(SALIDA_PATH + title + '.csv', index = False)    