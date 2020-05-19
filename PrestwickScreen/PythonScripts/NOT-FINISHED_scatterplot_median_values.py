# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:17:48 2020

@author: Sarah Haggenmüller
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

#%% read in the two excel files for TS149-1 and TS149-2

data1 = pd.read_excel('G:/My Drive/cri_py/sorted_excel_files/PRESTWICK1.1.xlsx')
data1 = data1.drop(['Unnamed: 0'], axis=1)

data2 = pd.read_excel('G:/My Drive/cri_py/sorted_excel_files/PRESTWICK2.2.xlsx')
data2 = data2.drop(['Unnamed: 0'], axis=1)

data3 = pd.read_excel('G:/My Drive/cri_py/sorted_excel_files/PRESTWICK_3.3.xlsx')
data3 = data3.drop(['Unnamed: 0'], axis=1)


#%% calculate the median values 

low1 = data1.iloc[1:, 0]
low2 = data2.iloc[1:, 0]
low3 = data3.iloc[1:, 0]

high1 = data1.iloc[1:, 1]
high2 = data2.iloc[1:, 1]
high3 = data3.iloc[1:, 1]

low = pd.concat([low1, low2, low3], axis = 1)
high = pd.concat([high1, high2, high3], axis = 1)

value_low = low.median(axis = 1)
value_high = high.median(axis = 1)
print(value_low)

#%% plot the graph

fig, ax = plt.subplots()

ax.scatter(value_low, value_high, s=5)
plt.axhspan(0.1, 0.23, 0.150, 0.27, color='red', alpha=0.25)

ax.set_xlabel('low arabinose')
ax.set_ylabel('high arabinose')
ax.grid(True)
ax.legend(('possible hits', 'Prestwick Chemicals', 'DMSO'))
ax.set_title('Prestwick Library Screen with TS149')
ax.set_xlim(-0.1, 0.5)
ax.set_ylim(-0.1, 0.5)


#%%
# =============================================================================
# # import prestwick data
# prestwick = pd.read_excel('G:/My Drive/cri_py/prestwick_screen/Prestwick Chemical Library Simplified.xlsx')
# prestwick_full = prestwick.dropna(subset=['Position'])
# 
# columnnames = ['OD_lowAra', 'OD_highAra']
# for col in prestwick_full.columns: 
#     columnnames.append(col)
#     
# # append columns for OD values to prestwick data and save dataframe
# final_array = np.concatenate((data_mean, prestwick_full), axis=1)
# pan = pd.DataFrame(final_array, columns = [columnnames])
# pan.to_excel('G:/My Drive/cri_py/sorted_excel_files/PRESTWICK_mean.xlsx')
# data = pd.read_excel('G:/My Drive/cri_py/sorted_excel_files/PRESTWICK_mean.xlsx')
# data = data.drop(['Unnamed: 0'], axis=1)
# 
# # extract possible hits and save in excel file
# hits = data.loc[(data['OD_lowAra'] < 0.1)& (data['OD_highAra'] > 0.1)]
# print(hits)
# 
# hits.to_excel('G:/My Drive/cri_py/hits_screen_mean_0.1_0.1.xlsx')
# 
# =============================================================================
