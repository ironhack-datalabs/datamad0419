import pandas as pd
import os
import requests
import quandl
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
from collections import Counter

from analysis import *

if __name__=="__main__":

    csv_name='movie_metadata.csv'
    token = 'BbhyEKhqsxJFzs52ERfm' #open('.env').read()

    run = read(csv_name)
    CPI_index = API_input(token)
    imdb = set_up(run)
    imdb = data_cleaning(imdb)
    imdb = data_wrangling(imdb)
    imdb = data_binning(imdb)
    imdb = data_embellish(imdb)
    imdb = merge(imdb, CPI_index)
    toCSV(imdb)
    plot_genre(imdb)
    plot_bins(imdb)
    plot_yearVSmovies(imdb)
    plot_yearVSvotes(imdb)
    plot_top10budget(imdb)
    plot_worsttop10(imdb)
    plot_corr_coreVSbudget(imdb)
    output1 = categorizer(imdb)
    output2 = director(imdb)
    
