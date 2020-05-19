# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:25:29 2020

@author: Sarah Haggenmüller
"""

#%%information for using this script

''' This script plots 5 different media conditions as
histograms. The arabinose concentration is resembled 
by a color gradient, and a legend on the right side of 
the plot. As a source are the sorted excel files used, 
which were generated with the python script named
'sorting_rawdata.py'. The figure is saved automatically
in the folder 'Results & Plots' with the filename 
'TS149_different_media'. If the file exists already,
you will be asked if you want to overwrite it (not 
recommended).'''


#%% import necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import os
import tkinter as tk
from tkinter import messagebox

#%% extracting current working directory
# path=os.path.abspath(os.getcwd())
# pathbegin = "/".join(path.split('\\')[:-1])

pathfile = os.getcwd()
pathbegin = os.path.dirname(pathfile)


#%% import the sorted excel files

df4 = pd.read_excel(os.path.join(pathbegin, 'Results & Plots', 'sorted_data_with_middle_values', '20200129_OD_TS149_ara_8h.xlsx'))
df5 = pd.read_excel(os.path.join(pathbegin, 'Results & Plots', 'sorted_data_with_middle_values', '20200130_OD_TS149_ara_7h.xlsx'))
df1 = pd.read_excel(os.path.join(pathbegin, 'Results & Plots', 'sorted_data_with_middle_values', '20200110_OD_TS149_ara_8h.xlsx'))
df2 = pd.read_excel(os.path.join(pathbegin, 'Results & Plots', 'sorted_data_with_middle_values', '20191219_OD_TS149_ara.xlsx'))
df3 = pd.read_excel(os.path.join(pathbegin, 'Results & Plots', 'sorted_data_with_middle_values', '20200108_OD_TS149_ara.xlsx'))


mv1 = df1.iloc[17, 1:]
mv2 = df2.iloc[17, 1:]
mv3 = df3.iloc[17, 1:]
mv4 = df4.iloc[17, 1:]
mv5 = df5.iloc[17, 1:]


frames = [mv1, mv2, mv3, mv4, mv5]
aa = pd.concat(frames)
  
# Declare a list that is to be converted into a column 
strain = ['TS149', 'TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149', 'TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149','TS149', 'TS163', 'TS163','TS163','TS163','TS163','TS163','TS163','TS163','TS163','TS163','TS163','TS163', 'TS163', 'TS163','TS163','TS163','TS163','TS163','TS163','TS163','TS163','TS163','TS163','TS163'] 

media = []
m4 = 'LB /-AA'
for number in range(1, 25, 1):
    media.append(m4) 
m5 = 'LB / SulfurDropout'
for number in range(1, 25, 1):
    media.append(m5) 
m1 = 'M9 TESEC -AA'
for number in range(1, 25, 1):
    media.append(m1) 
m2 = 'M9 TESEC SulfurDropout'
for number in range(1, 25, 1):
    media.append(m2) 
m3 = 'M9 TESEC complete'
for number in range(1, 25, 1):
    media.append(m3)     
    
    
aaa = pd.DataFrame(aa) 
aaa.insert(1, "Strain", media, True) 

aaa.to_excel(os.path.join(pathbegin, 'excelfileforhistoplot.xlsx'))
new = pd.read_excel(os.path.join(pathbegin, 'excelfileforhistoplot.xlsx'))
new.columns = ["Arabinose", "OD600", "Strain"]

arabinose_concentrations = list(df1.columns)
sns.set_style("whitegrid")

#%% plot graph
ax = sns.catplot(x="Arabinose", y="OD600", col="Strain",
                data=new, saturation=5,
                kind="bar", ci=None, palette='Greens')

#ax.fig.suptitle("Growth after 8h", y = 1.05, fontsize=20)
ax.set_titles("{col_name}")
plt.xticks([])

pal = sns.color_palette('Greens', n_colors=24)
farben = pal.as_hex()

ara_legende = []
for elem in arabinose_concentrations[1:]:
    elem_r = format(elem, '.2e')
    ara_legende.append(elem_r)

legende = dict(zip((ara_legende), reversed(farben)))
print(legende)

patches = [matplotlib.patches.Patch(color=v, label=k) for k,v in legende.items()]

ax.add_legend(handles=patches)

#%% save figure

# =============================================================================
# check = os.path.exists(os.path.join(pathbegin, 'Results & Plots', 'TS149_different_media.png'))
#         
# if check is True:
#     result = tk.messagebox.askquestion("File exists already", "The file exists already. Do you want to overwrite the existing file?", icon='warning')
#     if result == 'yes':
#         plt.savefig((os.path.join(pathbegin, 'Results & Plots', 'TS149_different_media.png')), dpi = 300)
#         tk.messagebox.showinfo(' ', 'The existing file was overwritten.')
#     else:
#         tk.messagebox.showinfo(' ', 'The existing file was not overwritten.')
#     
# else: 
#     plt.savefig((os.path.join(pathbegin, 'Results & Plots', 'TS149_different_media.png')), dpi = 300)
# 
# 
# os.remove(os.path.join(pathbegin, 'excelfileforhistoplot.xlsx'))
# 
# 
# =============================================================================


# end of script


