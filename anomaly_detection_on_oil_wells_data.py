

# Author: Caner Burc BASKAYA

# data source: 
# 3W Dataset - Undesirable events in oil wells
# https://www.kaggle.com/afrniomelo/3w-dataset

# related research articles:
# A realistic and public dataset with rare undesirable real events in oil wells
# Vargas et al., October 2019
# https://www.sciencedirect.com/science/article/abs/pii/S0920410519306357

# event names are checked from the following repository:
# https://github.com/ricardovvargas/3w_dataset/blob/master/demo_1_benchmark_impact_of_using_simulated_and_hand-drawn_instances.ipynb


import os
import pandas as pd
import numpy as np

main_dataset_folder = 'data/3W'
data_sub_folders = sorted(os.listdir(main_dataset_folder))[:]



data_first_sample = pd.read_csv( 
    os.path.join(main_dataset_folder, data_sub_folders[0], 
                             sorted( os.listdir(
                                 os.path.join(main_dataset_folder, data_sub_folders[0])) 
                                 )[4] 
                             )  )

column_names = data_first_sample.columns.tolist()

del data_first_sample

def load_data_to_df(first_n_subfolders=1, first_m_files=20):
    
    data = pd.DataFrame(columns=column_names)
    
    # in case first_n_subfolders is more than the total subfolder count
    first_n_subfolders = min(first_n_subfolders, len(data_sub_folders))

    for n,_ in enumerate(data_sub_folders):
        
        if first_n_subfolders - 1 == n:
            # in case first_m_files is more than the total file count in that subfolder
            first_m_files = min(first_m_files, len(sorted(os.listdir(os.path.join(main_dataset_folder, data_sub_folders[n])))))
        elif n >= first_n_subfolders:
            break
        
        for f in sorted(os.listdir(os.path.join(main_dataset_folder, data_sub_folders[n])))[:first_m_files]:
            # print("loading", f)
            cr_df = pd.read_csv(os.path.join(main_dataset_folder, data_sub_folders[0], f))
            data = data.append(cr_df)
        
    return data


data = load_data_to_df(first_m_files=100)
data['class'].value_counts()

data.shape

data_head = data.iloc[:5]

data.isnull().sum()















