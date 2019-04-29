def missing_pct(dataframe): 
    total_values = dataframe.count()
    missing_values = dataframe.isnull().sum() 
    missing_pct = (missing_values / total_values * 100).sort_values(0, ascending=False)    
    return missing_pct 