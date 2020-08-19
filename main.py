import os
#import data science libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

#set working directory to CSV to access data
path = os.chdir('./CSV')
csv_files_dir = os.listdir(path)

def descriptive_statistics():

    salary_desc = salary_df[['early_career_pay','mid_career_pay']].describe()
    tuition_desc = tuition_df[['in_state_tuition','out_of_state_tuition']].describe()
    
    print('Salary description:\n')
    print(salary_desc)
    print('\nTuition description:\n')
    print(tuition_desc)

     

def scatter_pay_v_STEM():
    
    ax = plt.axes()

    ax.plot(salary_df['early_career_pay'],salary_df['stem_percent'],'o')

    plt.title(r'Pay Versus STEM %')
    plt.xlabel('Pay')
    plt.ylabel('% STEM')
    plt.show()

def out_of_state_tuition_bar():

    ax = tuition_df.plot.bar(x="name", y="out_of_state_total", rot=0, title="Out of State Tuition Total Cost")
    plt.show(block=True)

def in_state_tuition_bar():

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

    descriptive_statistics()

    scatter_pay_v_STEM()
    out_of_state_tuition_bar()
    in_state_tuition_bar()
