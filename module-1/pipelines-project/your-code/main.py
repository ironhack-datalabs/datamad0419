
from functionspipe import *

if __name__ == "__main__":
    data = agrupar()
    database = df_frames(files)
    datacleaning = cleaning(df)
    duplicates = sort_dupl(dframe)
    bins = create_bins(df_final)
    filtered = filter_score(df_final)
    apimport = apireq(artist, album)
    api = apiloop()
    apidata = apimerge(pitch, answer)
    save = savecsv(final)
    plotscore = plt_score(df_final)
    plotgenre = plt_genre(pitch)

