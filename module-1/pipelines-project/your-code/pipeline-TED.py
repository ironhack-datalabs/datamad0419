import pandas as pd
import requests
import requests_mock
import matplotlib.pyplot as plt
import seaborn as sns
import ast
import json



#Funciones de adquisición secundarias: género de los speakers a partir de su nombre.

#Funciones para la obtención del set de nombres de los speakers, que luego pasaremos a la API para obtener el género.
def chunks(l, n):
    for i in range(0, len(l), n):
        yield tuple(l[i:i + n])

def get_speaker_names(df):
    names = [(name.split())[0] for name in df['main_speaker']]
    names = set(names)
    names = list(map(lambda x: x.strip(), names))
    return (list(chunks(names, 10)))

    
#FUNCIÓN ORIGINAL que devuelve el diccionario de nombres-género gracias a la API.
def acquire_genre(df):
    names_chunked = get_speaker_names(df)
    name_genre_dict = {}
    base_url = "https://api.genderize.io/?"
    for names in names_chunked:
        names_url = '&'.join('name[{}]={}'.format(i, name) for i, name in enumerate(names))
        response = requests.get(base_url + names_url)
    for name in response.json():
        name_genre_dict[name['name']] = name['gender']
    return name_genre_dict


#FUNCIÓN MOCKEADA que evita las múltiples llamadas a la API (devuelve 'api_response' como la respuesta, que usamos para
#generar el diccionario de nombres).
def acquire_genre_mock(df):
    names_chunked = get_speaker_names(df)
    name_genre_dict = {}
    base_url = "https://api.genderize.io/?"
    adapter.register_uri('GET', 'mock://api.genderize.io/?', json = api_response )
    response = session.get('mock://api.genderize.io/?')
    for name in response.json():
        name_genre_dict[name['name']] = name['gender']
    return name_genre_dict



#DATA WRANGLING

#Funciones para añadir la columna de etiquetas-vistas al DF original.
def tags_views(row):
    result = []
    for tag in row['tags']:
        result.append([tag, row['views']])
    return result

def get_tags_views_column(df):
    df['tag_views'] = df.apply(lambda row: tags_views(row), axis = 1)
    return df


#Funciones para añadir la columna de género del speaker
def get_gender(row, name_genre_dict):
    try:
        gender = name_genre_dict[(row['main_speaker'].split())[0]].strip()
        if gender == 'None':
            gender = 'NA'
    except:
        gender = 'NA'
    return gender

def get_gender_column(df, name_genre_dict):
    df['speaker_gender'] = df.apply(lambda row: get_gender(row, name_genre_dict), axis = 1)
    return df


#Función para generar el DataFrame (a partir del DF original + las columnas añadidas) que vamos a usar para el análisis.
def get_target_dataframe(df):
    new_dataframes = []
    new_columns = ['main_speaker', 'speaker_gender', 'tag', 'views']
    for index, row in df.iterrows():
        for tag in row['tag_views']:
            new_dataframes.append(pd.DataFrame([[row['main_speaker'], row['speaker_gender'], tag[0], tag[1]]]))
        
    concat_dataframe = pd.concat(new_dataframes, ignore_index=True)
    concat_dataframe.columns = new_columns
    return concat_dataframe

def visualize1(most_viewed_tags):
    fig, ax = plt.subplots(figsize=(20, 8))
    plt.xticks(rotation=70)
    barchart = sns.barplot(most_viewed_tags.head(30)['tag'], most_viewed_tags.head(30)['views/tag_count'])
    plt.xlabel('Subjects')
    plt.ylabel('total views/number of talks')
    plt.title('Most atractive TED subjects')
    return barchart

def visualize2(df_views_per_speaker_by_genre):
    fig, ax = plt.subplots(figsize=(20, 8))
    plt.xticks(rotation=70)
    barchart = sns.barplot(df_views_per_speaker_by_genre['speaker_gender'], df_views_per_speaker_by_genre['total_views/(male/female speakers)'])
    plt.xlabel('Gender')
    plt.ylabel('total views/total_views/(male/female speakers)')
    plt.title('Rate of views per speaker, per speaker gender')
    return barchart

def save_viz(barchart1, barchart2):
    fig1 = barchart1.get_figure()
    fig2 = barchart2.get_figure()
    fig1.savefig('./output/Most atractive TED subjects.png')
    fig2.savefig('./output/Rate of views per speaker, per speaker gender.png')

#Función de adquisición primaria del DF a partir del dataset. Usamos 'utf-8' para 
def acquire(file):
    df = pd.read_csv(file, encoding='utf-8')
    df = df.sort_values('views', ascending = False)
    df = df.applymap(lambda x: x.strip() if type(x) is str else x)
    return df.head(1000)

#Función de modificación del DF original y generación del DF objetivo.
def wrangle(df):
    df['tags'] = df['tags'].apply(ast.literal_eval)
    df = get_tags_views_column(df)
    name_genre_dict = acquire_genre_mock(df)
    df = get_gender_column(df, name_genre_dict)
    return get_target_dataframe(df)

#Función para el análisis
def analyze(df):
    most_viewed_tags = df[["tag","views"]].groupby("tag").agg({'views':'sum', 'tag':'count'}).sort_values('views', ascending = False)
    most_viewed_tags['views/tag'] = most_viewed_tags['views']/most_viewed_tags['tag']
    most_viewed_tags.columns = ['total_views', 'tag_count', 'views/tag_count']
    most_viewed_tags = most_viewed_tags.reset_index()
    most_viewed_tags = most_viewed_tags.sort_values('views/tag_count', ascending = False)
    df_views_per_speaker_by_genre = df.groupby('speaker_gender').agg({'views': lambda x: x.sum()/len(x)})
    df_views_per_speaker_by_genre.columns = ['total_views/(male/female speakers)']
    df_views_per_speaker_by_genre = df_views_per_speaker_by_genre.reset_index()
    df_views_per_speaker_by_genre = df_views_per_speaker_by_genre[df_views_per_speaker_by_genre['speaker_gender'] != 'NA']
    return most_viewed_tags, df_views_per_speaker_by_genre

if __name__ == "__main__":

    session = requests.Session()
    adapter = requests_mock.Adapter()
    session.mount('mock', adapter)
    api_response = None

    with open('mock_response.txt') as json_file:  
        api_response = json.load(json_file)
    
    adapter.register_uri('GET', 'mock://test.com', json = api_response )

    data = acquire('ted_main.csv')
    transformed_data = wrangle(data)
    most_viewed_tags, df_views_per_speaker_by_genre = analyze(transformed_data)
    barchart1 = visualize1(most_viewed_tags)
    barchart2 = visualize2(df_views_per_speaker_by_genre)
    save_viz(barchart1, barchart2)
    















