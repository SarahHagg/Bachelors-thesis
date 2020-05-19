# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:15:29 2019

@author: Sarah Haggenmüller
"""

#%%information for using this script

''' This script sortes the raw data accordingly to the arabinose concentrations.
For each arabinose concentration is a seperate column made at the middle value
of the correspondant OD values calculated. This middle value is appended in each
column at the bottom. When runnin this script, a seperate file explorer should open,
where one can select the excel file. The code will automatically save the newly 
sorted excel file in the folder 'sorted_data_with_middle_values' and name it 
accordingly to the selected file name. If the file exist already, you will be 
asked if the existing file should be overwritten (not recommended). '''


#%% import necessary libraries

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os


#%% extracting current working directory
# path=os.path.abspath(os.getcwd())
# pathbegin = "/".join(path.split('\\')[:-1])

pathfile = os.getcwd()
pathbegin = os.path.dirname(pathfile)


#%% open file
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
value = os.path.basename(filename)

#read in RawData
raw = pd.read_excel(filename)

#%% define the rows of OD-data [start-2 : end-1]
    #e.g. starts in excel row 52, last one in row 67 -> [50:66]
df = (raw.iloc[50:66])
print(df.head())
print(df.tail())


#%% convert panda dataframe to numpy arraya and sort new, according to the arabinose concentrations
arr = pd.DataFrame(df).to_numpy()


#sort the array: every arabinose concentration in one column
totalArray = np.hstack([np.concatenate([arr[0:15:2, w:w+2].reshape(16,1) for w in range(1, 24,2)], axis=1), \
                        np.concatenate([arr[1:16:2, w:w+2].reshape(16,1) for w in range(1, 24,2)], axis=1)])

    
#%% arabinose concentrations as list
arabinose = []
for a in range (0, 24, 1):
    b = 1 * (0.5 ** a)
    arabinose.append(b)


#%% add new row underneath with middle values of each column
middleValues = np.mean(totalArray, axis=0)
combined = np.vstack((totalArray, middleValues))


#%% save sorted and complete array as new excel file, with arabinose concentration as column names
pan = pd.DataFrame(combined, columns = [arabinose])

check = os.path.exists(os.path.join(pathbegin, 'Results & Plots', 'sorted_data_with_middle_values', value))
        
if check is True:
    result = tk.messagebox.askquestion("File exists already", "The file exists already. Do you want to overwrite the existing file?", icon='warning')
    if result == 'yes':
        pan.to_excel(os.path.join(pathbegin, 'Results & Plots', 'sorted_data_with_middle_values', value))
        tk.messagebox.showinfo(' ', 'The existing file was overwritten.')
    else:
        tk.messagebox.showinfo(' ', 'The existing file was not overwritten.')
    
else: 
    pan.to_excel(os.path.join(pathbegin, 'Results & Plots', 'sorted_data_with_middle_values', value))



# end of script
    
    
    
    