# to csv file:
def importing_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df

def raw(df):
    print('shape:',df.shape)
    print('\n columns:',df.columns)
    print('\n variables info:')    
    return df.info(),df.describe()

def replace_Nan_with0(data,num_var):
    for nv in num_var: 
        data[nv].fillna("0", inplace = True, downcast='infer')
    return data

def split_datetime(df,datetime):
    year,month,date,time = str(datetime+'_year'),str(datetime+'_month'),str(datetime+'_date'),str(datetime+'_time')
    df[year] = pd.to_datetime(df[datetime]).dt.year
    df[month] = pd.to_datetime(df[datetime]).dt.month
    df[date] = pd.to_datetime(df[datetime]).dt.date
    df[time] = pd.to_datetime(df[datetime]).dt.time
    return df[[datetime,year,month,date,time]]

def second_to_min(df,second):
    minutes = str(second+'_min')
    df[minutes]=df[second]/60
    return df[minutes,second]

def centavos_a_pesos(df,centavos):
    pesos = str(centavos+'_pesos')
    df[pesos] = df[centavos]/100
    return df[pesos,centavos]

# to count values:
def valcount(df, var):
    return df[var].value_counts()

# to replace ',' with '.':
def replace_comma_per_dot(data,var):
    for v in var:
        data[v].apply(lambda x: str(x).replace(',','.').strip())
        #data[v].astype(str).replace(',','.')
    return data

# then we convert to numeric / float (recommend if var contains some NaN):
def convert_to_float(data,float_var):
    for fv in float_var:
        data[fv].apply(pd.to_numeric, errors='coerce')
        #pd.to_numeric(data[fv],errors='coerce') 
    return data

# other way to convert to numeric / float (if no NaN):
def convert_to_float2(data,float_var):
    for fv in float_var:
        data[fv].apply(lambda x: str(x).astype('float64', copy=False))
        #data[fv].astype('float64', copy=False)
    return data

# to convert to numeric / int:
def convert_to_int(data,int_var):
    for iv in int_var:
        data[iv].apply(lambda x: str(x).astype('int64', copy=False))
        #data[iv].astype('int64', copy=False)
    return data

# convert to category format: 'vehicle_type_id', 'start_type', 'source','end_state'
def convert_to_category(data,cat_var):
    for cv in cat_var: 
        data[cv].astype('category')
    return data