import os
#import data science libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

#set working directory to CSV to access data
path = os.chdir('./CSV')
csv_files_dir = os.listdir(path)

#define main where functions are run
if __name__ == "__main__":

    #initialize dataframe
    df = pd.DataFrame()

    #read files into dataframe
    for files in csv_files_dir:
        data = pd.read_csv(files)
        df = df.append(data)
    
    #print description to terminal
    print(df.describe())


    