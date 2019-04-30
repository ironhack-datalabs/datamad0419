from pipeline import *

if __name__ == '__main__':
    data = acquisition()
    cleaned = wrangling(data)
    dfs = analysis(cleaned)
    report(dfs[0], dfs[1])
