# función que elimine duplicados
# función que detecte cuántos registros hay para cada tipo de elemento
# función que detecte cuántos nulls hay para cada tipo de elemento
# otra función que haga que los ids sean únicos y que, además, nos diga cuántos ha cambiado
# función que me elimine las columnas que tengan más de un porcentaje de nulls



def column_duplicates(df, column, columnwonulls):
    return df.groupby(column).count()[[columnwonulls]].sort_values(columnwonulls, ascending=False)
