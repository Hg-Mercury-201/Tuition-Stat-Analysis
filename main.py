import os
#import data science libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


'''

This is the Python file that contains the code for generating the visualizations for the project.
You can run this file on either Windows or MacOS provided that Python 3.8 is installed.
The files that the data for the visualizations are taken from are located in the CSV folder in the repository

The structure of the file is that the analysis is split up into named functions and then run in the if __main__ section

'''

#set working directory to CSV to access data
path = os.chdir('./CSV')
csv_files_dir = os.listdir(path)

def descriptive_statistics():

    #assign variables for descriptive stats from data frame
    salary_desc = salary_df[['early_career_pay','mid_career_pay']].describe()
    tuition_desc = tuition_df[['in_state_tuition','out_of_state_tuition']].describe()
    #print out descriptions
    print('Salary description:\n')
    print(salary_desc)
    print('\nTuition description:\n')
    print(tuition_desc)

def scatter_pay_v_STEM():
    #set axes object
    ax = plt.axes()
    #define X and Y axes
    ax.plot(salary_df['early_career_pay'],salary_df['stem_percent'],'o')
    #label graph and display
    plt.title(r'Pay Versus STEM %')
    plt.xlabel('Pay')
    plt.ylabel('% STEM')
    plt.show()

def out_of_state_tuition_bar():
    #define bar plot and attributes and display
    ax = tuition_df.plot.bar(x="name", y="out_of_state_total", rot=0, title="Out of State Tuition Total Cost")
    plt.show(block=True)

def in_state_tuition_bar():
    #define bar plot and attributes and display
    ax = tuition_df.plot.bar(x="name", y="in_state_total", rot=0, title="In State Tuition Total Cost")
    plt.show(block=True)

    

#define main where functions are run
if __name__ == "__main__":

    #define dataframes
    salary_df = pd.read_csv(csv_files_dir[0])
    tuition_df = pd.read_csv(csv_files_dir[1])
    
    #print dataframe summary
    print(salary_df)
    print(tuition_df)

    #random sample of ten rows
    salary_df = salary_df.sample(n=10)
    tuition_df = tuition_df.sample(n=10)
    
    #print random sample
    print(salary_df)
    print(tuition_df)

    #call to functions with visualizations
    descriptive_statistics()
    out_of_state_tuition_bar()
    in_state_tuition_bar()
    scatter_pay_v_STEM()