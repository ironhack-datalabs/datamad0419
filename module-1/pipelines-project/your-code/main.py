import pandas as pd
import os
import requests
import quandl
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
from collections import Counter

DataFrame='movie_metadata.csv'
token=open(".env").read()

from analysis import *

if __name__=="__main__":

    run = read(DataFrame)
    CPI_index = API_input(token)
    imdb = set_up(run)
    imdb = data_cleaning(imdb)
    imdb = data_wrangling(imdb)
    imdb = data_binning(imdb)
    imdb = data_embellish(imdb)
    imdb = merge(imdb, CPI_index)
    csv = toCSV(imdb)
    plot1 = plot_genre(imdb)
    plot2 = plot_bins(imdb)
    plot3 = plot_yearVSmovies(imdb)
    plot4 = plot_yearVSvotes(imdb)
    plot5 = plot_top10budget(imdb)
    plot6 = plot_worsttop10(imdb)
    plot7 = plot_corr_coreVSbudget(imdb)
    output1 = categorizer(imdb)
    output2 = director(imdb)
    
