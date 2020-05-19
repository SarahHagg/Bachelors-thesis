# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:02:28 2020

@author: Sarah Haggenmüller 
"""


#%%information for using this script

''' This script is for plotting a scatter plot out
of the 3 experiments with different biological replicates
of the TESEC strain TS149. The raw data of all the excel 
files are extracted, sorted in data of drugs and data of 
DMSO (first and last column of all the 16 original 96-well-
plates of the Prestwick Chemical Library). Afterwards the 
median values out of the 3 replicates are determined and
plotted. The DMSO values (negative controls) are plotted 
seperately. The area with hit like compounds is marked in 
the plot and the median values of the drugs appended to the
excel file of all the PCL compounds. This is saved in a new
excel file, as well as all the hit like compounds in an other
seperate excel file. Finally, the plot is saved. If any of
the excel files or the plot exists already, you will be asked
if the existing file should be overwritten or not (not 
recommended). '''


#%% import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import tkinter as tk
from matplotlib import collections


#%% definitions
def check_existance_save_excel(file, filename):
    check = os.path.exists(filename)
            
    if check is True:
        result = tk.messagebox.askquestion("File exists already", "The excel file with path " + str(filename) + " exists already. Do you want to overwrite the existing file?", icon='warning')
        if result == 'yes':
            file.to_excel(filename)
            tk.messagebox.showinfo(' ', 'The existing file was overwritten.')
        else:
            tk.messagebox.showinfo(' ', 'The existing file was not overwritten.')
        
    else: 
        file.to_excel(filename)
        

def check_existance_save(filename):
    check = os.path.exists(filename)
            
    if check is True:
        result = tk.messagebox.askquestion("File exists already", "The file with the plot exists already. Do you want to overwrite the existing file?", icon='warning')
        if result == 'yes':
#            plt.savefig((filename), dpi = 300)
            fig.savefig((filename), dpi = 300)
            tk.messagebox.showinfo(' ', 'The existing file was overwritten.')
        else:
            tk.messagebox.showinfo(' ', 'The existing file was not overwritten.')
        
    else: 
#        plt.savefig((filename), dpi = 300)
        fig.savefig((filename), dpi = 300)


        
#%% import data of all 3 experiments
number_loops = 0 


#extracting current working directory
pathfile = os.getcwd()
pathbegin = os.path.dirname(pathfile)



experiments = ['20200226_TS149_Prestwick1', '20200303_TS149_Prestwick2', '20200312_TS149_Prestwick3']

for element in experiments:
    #G:/Shared drives/Wintermute Lab/Projects/TB TESEC/Result Colections/20200313_TS149_PrestwickScreen/RawData/20200226_TS149_Prestwick1/time0/low_1.xlsx
    # time zero data (0h)
    df11 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time0', 'low_1.xlsx')).iloc[50:66, 1:]
    df21 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time0', 'low_2.xlsx')).iloc[50:66, 1:]
    df31 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time0', 'low_3.xlsx')).iloc[50:66, 1:]
    df41 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time0', 'low_4.xlsx')).iloc[50:66, 1:]
    
    df51 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time0', 'high_1.xlsx')).iloc[50:66, 1:]
    df61 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time0', 'high_2.xlsx')).iloc[50:66, 1:]
    df71 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time0', 'high_3.xlsx')).iloc[50:66, 1:]
    df81 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time0', 'high_4.xlsx')).iloc[50:66, 1:]
    
    
    #%% after incubation data
    df12 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time8', 'low_1.xlsx')).iloc[50:66, 1:]
    df22 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time8', 'low_2.xlsx')).iloc[50:66, 1:]
    df32 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time8', 'low_3.xlsx')).iloc[50:66, 1:]
    df42 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time8', 'low_4.xlsx')).iloc[50:66, 1:]
    
    df52 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time8', 'high_1.xlsx')).iloc[50:66, 1:]
    df62 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time8', 'high_2.xlsx')).iloc[50:66, 1:]
    df72 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time8', 'high_3.xlsx')).iloc[50:66, 1:]
    df82 = pd.read_excel(os.path.join(pathbegin, 'RawData', str(element), 'time8', 'high_4.xlsx')).iloc[50:66, 1:]
    
    # after incubation - time zero data
    plate1_low = df12 - df11
    plate2_low = df22 - df21
    plate3_low = df32 - df31
    plate4_low = df42 - df41
    
    plate1_high = df52 - df51
    plate2_high = df62 - df61
    plate3_high = df72 - df71
    plate4_high = df82 - df81
    
    
    # sort all the data new
    total_drugs1 = np.array(0)
    DMSO_1 = np.array(0)
    for df in (plate1_low, plate2_low, plate3_low, plate4_low):
        plate1 = pd.DataFrame(df.iloc[0:15:2, 0:23:2]).to_numpy()
        plate1_drugs = plate1[:, 1:11].reshape(80,1)
        plate1_DMSO = plate1[:, 0:12:11].reshape(16,1)
        
        plate2 = pd.DataFrame(df.iloc[0:15:2, 1:24:2]).to_numpy()
        plate2_drugs = plate2[:, 1:11].reshape(80,1)
        plate2_DMSO = plate2[:, 0:12:11].reshape(16,1)
        
        plate3 = pd.DataFrame(df.iloc[1:16:2, 0:23:2]).to_numpy()
        plate3_drugs = plate3[:, 1:11].reshape(80,1)
        plate3_DMSO = plate3[:, 0:12:11].reshape(16,1)
        
        plate4 = pd.DataFrame(df.iloc[1:16:2, 1:24:2]).to_numpy()
        plate4_drugs = plate4[:, 1:11].reshape(80,1)
        plate4_DMSO = plate4[:, 0:12:11].reshape(16,1)
        
        
        total_drugs2 = np.vstack((plate1_drugs, plate2_drugs, plate3_drugs, plate4_drugs))
        total_DMSO = np.vstack((plate1_DMSO, plate1_DMSO, plate3_DMSO, plate4_DMSO))
        
        global all_array_low
        all_array_low = np.vstack((total_drugs1, total_drugs2))
        total_drugs1 = all_array_low
        
        global all_DMSO_low
        all_DMSO_low = np.vstack((DMSO_1, total_DMSO))
        DMSO_1 = all_DMSO_low
            
    if number_loops == 0:
        all_array_low_1 = all_array_low[1:]
        all_DMSO_low_1 = all_DMSO_low[1:]
        
    if number_loops == 1:
        all_array_low_2 = all_array_low[1:]
        all_DMSO_low_2 = all_DMSO_low[1:]
        
    if number_loops == 2:
        all_array_low_3 = all_array_low[1:]
        all_DMSO_low_3 = all_DMSO_low[1:]
    
    total_drugs3 = np.array(0)
    DMSO_1 = np.array(0)
    for df in (plate1_high, plate2_high, plate3_high, plate4_high):
        plate1 = pd.DataFrame(df.iloc[0:15:2, 0:23:2]).to_numpy()
        plate1_drugs = plate1[:, 1:11].reshape(80,1)
        plate1_DMSO = plate1[:, 0:12:11].reshape(16,1)
        
        plate2 = pd.DataFrame(df.iloc[0:15:2, 1:24:2]).to_numpy()
        plate2_drugs = plate2[:, 1:11].reshape(80,1)
        plate2_DMSO = plate2[:, 0:12:11].reshape(16,1)
        
        plate3 = pd.DataFrame(df.iloc[1:16:2, 0:23:2]).to_numpy()
        plate3_drugs = plate3[:, 1:11].reshape(80,1)
        plate3_DMSO = plate3[:, 0:12:11].reshape(16,1)
        
        plate4 = pd.DataFrame(df.iloc[1:16:2, 1:24:2]).to_numpy()
        plate4_drugs = plate4[:, 1:11].reshape(80,1)
        plate4_DMSO = plate4[:, 0:12:11].reshape(16,1)
        
        
        total_drugs4 = np.vstack((plate1_drugs, plate2_drugs, plate3_drugs, plate4_drugs))
        total_DMSO = np.vstack((plate1_DMSO, plate1_DMSO, plate3_DMSO, plate4_DMSO))
        
        global all_array_high
        all_array_high = np.vstack((total_drugs3, total_drugs4))
        total_drugs3 = all_array_high
        
        global all_DMSO_high
        all_DMSO_high = np.vstack((DMSO_1, total_DMSO))
        DMSO_1 = all_DMSO_high
    
    
    if number_loops == 0:
        all_array_high_1 = all_array_high[1:]
        all_DMSO_high_1 = all_DMSO_high[1:]
        
    if number_loops == 1:
        all_array_high_2 = all_array_high[1:]
        all_DMSO_high_2 = all_DMSO_high[1:]
        
    if number_loops == 2:
        all_array_high_3 = all_array_high[1:]
        all_DMSO_high_3 = all_DMSO_high[1:]
    
    number_loops = number_loops + 1


#%% combine the data of hte experiments and determine the median value
low_drug = np.concatenate([all_array_low_1, all_array_low_2, all_array_low_3], axis = 1)
high_drug = np.concatenate([all_array_high_1, all_array_high_2, all_array_high_3], axis = 1)
#print(low_drug)

low_DMSO = np.concatenate([all_DMSO_low_1, all_DMSO_low_2, all_DMSO_low_3], axis = 1)
high_DMSO = np.concatenate([all_DMSO_high_1, all_DMSO_high_2, all_DMSO_high_3], axis = 1)

value_low_drug = np.median(low_drug, axis = 1)
value_high_drug = np.median(high_drug, axis = 1)
value_low_DMSO = np.median(low_DMSO, axis = 1)
value_high_DMSO = np.median(high_DMSO, axis =1)
#print(value_low_drug)

#%% print graph
sns.set_style('whitegrid')
fig, ax = plt.subplots()

ax.scatter(value_low_drug, value_high_drug, s=5)
ax.scatter(value_low_DMSO, value_high_DMSO, s=5)

plt.axhspan(0.1, 0.23, 0.150, 0.29, color='red', alpha=0.1)


from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

points = [[-0.01, 0.04], [-0.01, 0.24], [0.145, 0.24]]
p = plt.Polygon(points, color = 'red', alpha = 0.25)
ax.add_patch(p)




ax.set_xlabel('low arabinose')
ax.set_ylabel('high arabinose')
ax.grid(True)
ax.legend(('possible hits', 'Prestwick Chemicals', 'DMSO'))
ax.set_title('Prestwick Library Screen with TS149')
ax.set_xlim(-0.1, 0.5)
ax.set_ylim(-0.1, 0.5)


pd.set_option('display.max_columns', 5)
pd.options.display.max_rows = 150


#%% import prestwick data

prestwick = pd.read_excel(os.path.join(pathbegin, 'Prestwick Chemical Library Simplified.xlsx'))
prestwick_full = prestwick.dropna(subset=['Position'])

columnnames = ['OD_lowAra', 'OD_highAra']
for col in prestwick_full.columns: 
    columnnames.append(col)


# append columns for OD values and save frame in seperate excel file
final_array = np.concatenate((value_low_drug.reshape(1280,1), value_high_drug.reshape(1280,1), prestwick_full), axis=1)
pan = pd.DataFrame(final_array, columns = [columnnames])
#check_existance_save_excel(pan, (os.path.join(pathbegin, 'Results & Plots', 'sorted_excel_files', 'PRESTWICK_median_complete.xlsx')))
data = pd.read_excel(os.path.join(pathbegin, 'Results & Plots', 'sorted_excel_files', 'PRESTWICK_median_complete.xlsx'))
data = data.drop(['Unnamed: 0'], axis=1)


# identify hits and save them as an seperate excel file
#hits = data.loc[(data['OD_lowAra'] < 0.07)& (data['OD_highAra'] > 0.1)]
#hits = data.loc[(((data['OD_highAra'] / data['OD_lowAra']) > 1.36986) & (data['OD_highAra'] < 0.24) & (data['OD_highAra'] > 0.04)& (data['OD_lowAra'] < 0.14)& (data['OD_lowAra'] > -0.01))]
hits = data.loc[(data['OD_lowAra'] < 0.3)& (data['OD_lowAra'] > 0.2) & (data['OD_highAra'] < 0.03)]
print(hits)
#check_existance_save_excel(hits, (os.path.join(pathbegin, 'Results & Plots', 'sorted_excel_files', 'PRESTWICK_median_hits.xlsx')) )

# positive control: identify antibiotics with low growth in both arabinose conditions
antibiotics = data.loc[(data['OD_lowAra']< 0.05) & (data['OD_highAra'] < 0.05)]
print(antibiotics)
#check_existance_save_excel(antibiotics, (os.path.join(pathbegin, 'Results & Plots', 'sorted_excel_files', 'PRESTWICK_median_antibiotics-control_05.xlsx')) )

#%% check if file exists already when saving

#check_existance_save(os.path.join(pathbegin, 'Results & Plots', 'Prestwick_mean_scatterplot_DMSO(3).png'))



#end of script



