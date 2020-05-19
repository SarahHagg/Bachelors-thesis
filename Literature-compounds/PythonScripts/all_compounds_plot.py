# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:11:17 2020

@author: Sarah Haggenmüller
"""


#%%information for using this script

''' This script is for plotting the data of the screen of the
8 compounds in 3 different ways. The median value of the 4 
technical replicates per setting are calculated and plotted
(in case of compound 7, there was the high drug concentration
only in column 11 and 12, therefore the mean/middle value of 
these 2 replicates are calculated). In plot 2, the median values
of the 3 biological replicates are plotted. In plot 3 a heatmap
of the 96-well-plate is displayed for better understanding and 
for easy detection of possible contaminations in parts of the 
plate. The whole figure is saved in the folder 'Results & Plots',
unless the files exist already. In this case you will be asked, 
if you want to overwrite the existing files (not recommended). 

The 8 compounds are the following:
    
     - Compound 1: 3,5-Pyrazoledicarboxylic acid monohydrate
     - Compound 2: Curcumin
     - Compound 3: Rosmarinic acid
     - Compound 4: DL-2,3-Diaminoproprionic acid
     - Compound 5: 2,2',4,4'-Tetrahydroxybenzophenone
     - Compound 6: N-Iodosuccinimide
     - Compound 7: 2,3-Dichloro-1,4-nahthoquinone
     - Compound 8: Phtaldialdeyde
     
'''


#%% import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import tkinter as tk

sns.set_style('whitegrid')




def check_existance_save(filename):
    check = os.path.exists(filename)
    if n == 1:        
        if check is True:
            global result
            result = tk.messagebox.askquestion("Saving plots", "The file of compound 1 exists already. Do you want to overwrite the existing file of compound 1 and also the files of all following compounds (if they exist)?", icon='warning')
        else: 
    #        plt.savefig((filename), dpi = 300)
            fig.savefig((filename),bbox_inches='tight', dpi = 300)
            result = 'yes'
        if result == 'no':
            tk.messagebox.showinfo(' ', 'The existing files were not overwritten.')
        if check is True and result == 'yes':
            tk.messagebox.showinfo(' ', 'The existing files were overwritten.')
            
    if result == 'yes':
    #          plt.savefig((filename), dpi = 300)
        fig.savefig((filename),bbox_inches='tight', dpi = 300)

    if check is False:
        fig.savefig((filename),bbox_inches='tight', dpi = 300)

#%% extracting current working directory
# path=os.path.abspath(os.getcwd())
# pathbegin = "/".join(path.split('\\')[:-1])
#%%
pathfile = os.getcwd()
pathbegin = os.path.dirname(pathfile)
# pathbegin = os.path.join(str(os.path.split(pathfile)[:-1]))
print(pathbegin)
#%%
# time zero data (0h)
df11 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time0', 'P1.xlsx')).iloc[42:50, 1:13]
df21 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time0', 'P2.xlsx')).iloc[42:50, 1:13]
df31 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time0', 'P3.xlsx')).iloc[42:50, 1:13]
df41 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time0', 'P4.xlsx')).iloc[42:50, 1:13]
df51 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time0', 'P5.xlsx')).iloc[42:50, 1:13]
df61 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time0', 'P6.xlsx')).iloc[42:50, 1:13]
df71 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time0', 'P7.xlsx')).iloc[42:50, 1:13]
df81 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time0', 'P8.xlsx')).iloc[42:50, 1:13]

# after incubation data (8h)
df12 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time8', 'P1.xlsx')).iloc[42:50, 1:13]
df22 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time8', 'P2.xlsx')).iloc[42:50, 1:13]
df32 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time8', 'P3.xlsx')).iloc[42:50, 1:13]
df42 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time8', 'P4.xlsx')).iloc[42:50, 1:13]
df52 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time8', 'P5.xlsx')).iloc[42:50, 1:13]
df62 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time8', 'P6.xlsx')).iloc[42:50, 1:13]
df72 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time8', 'P7.xlsx')).iloc[42:50, 1:13]
df82 = pd.read_excel(os.path.join(pathbegin, 'RawData', 'time8', 'P8.xlsx')).iloc[42:50, 1:13]

# after incubation - time zero data
plate1 = df12 - df11
plate2 = df22 - df21
plate3 = df32 - df31
plate4 = df42 - df41
plate5 = df52 - df51
plate6 = df62 - df61
plate7 = df72 - df71
plate8 = df82 - df81

#%%
all_plates = [plate1, plate2, plate3, plate4, plate5, plate6, plate7, plate8]

n = 1
for plate in all_plates:
    # sort data from plate
    
    
        
    strain149_1_low_DMSO = pd.DataFrame(plate.iloc[0, 0:4]).to_numpy().reshape(4,1)
    strain149_2_low_DMSO = pd.DataFrame(plate.iloc[2, 0:4]).to_numpy().reshape(4,1)
    strain149_3_low_DMSO = pd.DataFrame(plate.iloc[4, 0:4]).to_numpy().reshape(4,1)
    strain149_t_low_DMSO = pd.DataFrame(plate.iloc[0:5:2, 0:4]).to_numpy().reshape(12,1)
    
    strain149_1_high_DMSO = pd.DataFrame(plate.iloc[1, 0:4]).to_numpy().reshape(4,1)
    strain149_2_high_DMSO = pd.DataFrame(plate.iloc[3, 0:4]).to_numpy().reshape(4,1)
    strain149_3_high_DMSO = pd.DataFrame(plate.iloc[5, 0:4]).to_numpy().reshape(4,1)
    strain149_t_high_DMSO = pd.DataFrame(plate.iloc[1:6:2, 0:4]).to_numpy().reshape(12,1)
    
    strain163_DMSO = pd.DataFrame(plate.iloc[6, 0:4]).to_numpy().reshape(4,1)
    no_cells_DMSO = pd.DataFrame(plate.iloc[7, 0:4]).to_numpy().reshape(4,1)
    
    
    if plate is plate7:
        strain149_1_low_lowDrug = pd.DataFrame(plate.iloc[0, 8:12]).to_numpy().reshape(4,1)
        strain149_2_low_lowDrug = pd.DataFrame(plate.iloc[2, 8:12]).to_numpy().reshape(4,1)
        strain149_3_low_lowDrug = pd.DataFrame(plate.iloc[4, 8:12]).to_numpy().reshape(4,1)
        strain149_t_low_lowDrug = pd.DataFrame(plate.iloc[0:5:2, 8:12]).to_numpy().reshape(12,1)
        
        strain149_1_high_lowDrug = pd.DataFrame(plate.iloc[1, 8:12]).to_numpy().reshape(4,1)
        strain149_2_high_lowDrug = pd.DataFrame(plate.iloc[3, 8:12]).to_numpy().reshape(4,1)
        strain149_3_high_lowDrug = pd.DataFrame(plate.iloc[5, 8:12]).to_numpy().reshape(4,1)
        strain149_t_high_lowDrug = pd.DataFrame(plate.iloc[1:6:2, 8:12]).to_numpy().reshape(12,1)
        
        strain163_lowDrug = pd.DataFrame(plate.iloc[6, 8:12]).to_numpy().reshape(4,1)
        no_cells_lowDrug = pd.DataFrame(plate.iloc[7, 8:12]).to_numpy().reshape(4,1)
    else:
        strain149_1_low_lowDrug = pd.DataFrame(plate.iloc[0, 4:8]).to_numpy().reshape(4,1)
        strain149_2_low_lowDrug = pd.DataFrame(plate.iloc[2, 4:8]).to_numpy().reshape(4,1)
        strain149_3_low_lowDrug = pd.DataFrame(plate.iloc[4, 4:8]).to_numpy().reshape(4,1)
        strain149_t_low_lowDrug = pd.DataFrame(plate.iloc[0:5:2, 4:8]).to_numpy().reshape(12,1)
        
        strain149_1_high_lowDrug = pd.DataFrame(plate.iloc[1, 4:8]).to_numpy().reshape(4,1)
        strain149_2_high_lowDrug = pd.DataFrame(plate.iloc[3, 4:8]).to_numpy().reshape(4,1)
        strain149_3_high_lowDrug = pd.DataFrame(plate.iloc[5, 4:8]).to_numpy().reshape(4,1)
        strain149_t_high_lowDrug = pd.DataFrame(plate.iloc[1:6:2, 4:8]).to_numpy().reshape(12,1)
        
        strain163_lowDrug = pd.DataFrame(plate.iloc[6, 4:8]).to_numpy().reshape(4,1)
        no_cells_lowDrug = pd.DataFrame(plate.iloc[7, 4:8]).to_numpy().reshape(4,1)
    
    if plate is plate3:
        strain149_1_low_highDrug = pd.DataFrame(plate.iloc[0, 8:10]).to_numpy().reshape(2,1)
        strain149_2_low_highDrug = pd.DataFrame(plate.iloc[2, 8:10]).to_numpy().reshape(2,1)
        strain149_3_low_highDrug = pd.DataFrame(plate.iloc[4, 8:10]).to_numpy().reshape(2,1)
        strain149_t_low_highDrug = pd.DataFrame(plate.iloc[0:5:2, 8:10]).to_numpy().reshape(6,1)
        
        strain149_1_high_highDrug = pd.DataFrame(plate.iloc[1, 8:10]).to_numpy().reshape(2,1)
        strain149_2_high_highDrug = pd.DataFrame(plate.iloc[3, 8:10]).to_numpy().reshape(2,1)
        strain149_3_high_highDrug = pd.DataFrame(plate.iloc[5, 8:10]).to_numpy().reshape(2,1)
        strain149_t_high_highDrug = pd.DataFrame(plate.iloc[1:6:2, 8:10]).to_numpy().reshape(6,1)
        
        strain163_highDrug = pd.DataFrame(plate.iloc[6, 8:10]).to_numpy().reshape(2,1)
        no_cells_highDrug = pd.DataFrame(plate.iloc[7, 8:10]).to_numpy().reshape(2,1)        
    elif plate is plate7: 
        strain149_1_low_highDrug = pd.DataFrame(plate.iloc[0, 4:8]).to_numpy().reshape(4,1)
        strain149_2_low_highDrug = pd.DataFrame(plate.iloc[2, 4:8]).to_numpy().reshape(4,1)
        strain149_3_low_highDrug = pd.DataFrame(plate.iloc[4, 4:8]).to_numpy().reshape(4,1)
        strain149_t_low_highDrug = pd.DataFrame(plate.iloc[0:5:2, 4:8]).to_numpy().reshape(12,1)
        
        strain149_1_high_highDrug = pd.DataFrame(plate.iloc[1, 4:8]).to_numpy().reshape(4,1)
        strain149_2_high_highDrug = pd.DataFrame(plate.iloc[3, 4:8]).to_numpy().reshape(4,1)
        strain149_3_high_highDrug = pd.DataFrame(plate.iloc[5, 4:8]).to_numpy().reshape(4,1)
        strain149_t_high_highDrug = pd.DataFrame(plate.iloc[1:6:2, 4:8]).to_numpy().reshape(12,1)
        
        strain163_highDrug = pd.DataFrame(plate.iloc[6, 4:8]).to_numpy().reshape(4,1)
        no_cells_highDrug = pd.DataFrame(plate.iloc[7, 4:8]).to_numpy().reshape(4,1)        
    else:
        strain149_1_low_highDrug = pd.DataFrame(plate.iloc[0, 8:12]).to_numpy().reshape(4,1)
        strain149_2_low_highDrug = pd.DataFrame(plate.iloc[2, 8:12]).to_numpy().reshape(4,1)
        strain149_3_low_highDrug = pd.DataFrame(plate.iloc[4, 8:12]).to_numpy().reshape(4,1)
        strain149_t_low_highDrug = pd.DataFrame(plate.iloc[0:5:2, 8:12]).to_numpy().reshape(12,1)
        
        strain149_1_high_highDrug = pd.DataFrame(plate.iloc[1, 8:12]).to_numpy().reshape(4,1)
        strain149_2_high_highDrug = pd.DataFrame(plate.iloc[3, 8:12]).to_numpy().reshape(4,1)
        strain149_3_high_highDrug = pd.DataFrame(plate.iloc[5, 8:12]).to_numpy().reshape(4,1)
        strain149_t_high_highDrug = pd.DataFrame(plate.iloc[1:6:2, 8:12]).to_numpy().reshape(12,1)
        
        strain163_highDrug = pd.DataFrame(plate.iloc[6, 8:12]).to_numpy().reshape(4,1)
        no_cells_highDrug = pd.DataFrame(plate.iloc[7, 8:12]).to_numpy().reshape(4,1)
        
    
    def middlevalues(data):
        list_means = []
        for elem in data:
            mean = np.median(elem)
            list_means.append(mean)
        return list_means
        
    x_axis = [1, 2, 3]
    strain149_1_low = middlevalues([strain149_1_low_DMSO, strain149_1_low_lowDrug, strain149_1_low_highDrug])
    strain149_2_low = middlevalues([strain149_2_low_DMSO, strain149_2_low_lowDrug, strain149_2_low_highDrug])
    strain149_3_low = middlevalues([strain149_3_low_DMSO, strain149_3_low_lowDrug, strain149_3_low_highDrug])
    strain149_t_low = middlevalues([strain149_t_low_DMSO, strain149_t_low_lowDrug, strain149_t_low_highDrug])
    
    strain149_1_high = middlevalues([strain149_1_high_DMSO, strain149_1_high_lowDrug, strain149_1_high_highDrug])
    strain149_2_high = middlevalues([strain149_2_high_DMSO, strain149_2_high_lowDrug, strain149_2_high_highDrug])
    strain149_3_high = middlevalues([strain149_3_high_DMSO, strain149_3_high_lowDrug, strain149_3_high_highDrug])
    strain149_t_high = middlevalues([strain149_t_high_DMSO, strain149_t_high_lowDrug, strain149_t_high_highDrug])
    
    strain163 = middlevalues([strain163_DMSO, strain163_lowDrug, strain163_highDrug])
    no_cells = middlevalues([no_cells_DMSO, no_cells_lowDrug, no_cells_highDrug])
    
    
    def standardabweichung(data2):
        elements=[]
        for element in data2:
            deviations = np.std(element)
            elements.append(deviations)
        return elements

    d_strain149_1_low = standardabweichung([strain149_1_low_DMSO, strain149_1_low_lowDrug, strain149_1_low_highDrug])
    d_strain149_2_low = standardabweichung([strain149_2_low_DMSO, strain149_2_low_lowDrug, strain149_2_low_highDrug])
    d_strain149_3_low = standardabweichung([strain149_3_low_DMSO, strain149_3_low_lowDrug, strain149_3_low_highDrug])
    d_strain149_t_low = standardabweichung([strain149_t_low_DMSO, strain149_t_low_lowDrug, strain149_t_low_highDrug])
    
    d_strain149_1_high = standardabweichung([strain149_1_high_DMSO, strain149_1_high_lowDrug, strain149_1_high_highDrug])
    d_strain149_2_high = standardabweichung([strain149_2_high_DMSO, strain149_2_high_lowDrug, strain149_2_high_highDrug])
    d_strain149_3_high = standardabweichung([strain149_3_high_DMSO, strain149_3_high_lowDrug, strain149_3_high_highDrug])
    d_strain149_t_high = standardabweichung([strain149_t_high_DMSO, strain149_t_high_lowDrug, strain149_t_high_highDrug])
    
    d_strain163 = standardabweichung([strain163_DMSO, strain163_lowDrug, strain163_highDrug])
    d_no_cells = standardabweichung([no_cells_DMSO, no_cells_lowDrug, no_cells_highDrug])  
 
    
    
    #%% plot
    fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(5,10))
    plt.subplots_adjust(bottom = None, top= 0.93, hspace = 0.25)
    plots_all = [strain149_1_low, strain149_2_low, strain149_3_low, strain149_t_low, strain149_1_high, strain149_2_high, strain149_3_high, strain149_t_high, strain163, no_cells]
    plots_middle = [strain149_t_low, strain149_t_high, strain163, no_cells]
    
    
    #%% plot all data
    
    ax1.plot(x_axis, strain149_1_low, ) #yerr = d_strain149_1_low)
    ax1.plot(x_axis, strain149_2_low, ) #yerr = d_strain149_2_low)
    ax1.plot(x_axis, strain149_3_low, ) #yerr = d_strain149_3_low)
    
    ax1.plot(x_axis, strain149_1_high, ) #yerr = d_strain149_1_high)
    ax1.plot(x_axis, strain149_2_high, ) #yerr = d_strain149_2_high)
    ax1.plot(x_axis, strain149_3_high, ) #yerr = d_strain149_3_high)
    
    ax1.plot(x_axis, strain163, ) #yerr = d_strain163)
    ax1.plot(x_axis, no_cells, ) #yerr = d_no_cells)
    
    ax1.legend(('strain149_1_low', 'strain149_2_low', 'strain149_3_low', 'strain149_1_high', 'strain149_2_high', 'strain149_3_high',  'strain163', 'no_cells'), bbox_to_anchor=(1, 0.85))
    
    #fig.suptitle('Testing of 8 Compounds', fontsize = 15)
    ax1.set_title('All data')
    ax1.set_xticks([1, 2, 3])
    ax1.set_xticklabels(['DMSO', '100uM', '1mM'])
    
    #%% plot mean of three biological replicates
    
    ax2.plot(x_axis, strain149_t_low, ) #yerr = d_strain149_t_low)
    ax2.plot(x_axis, strain149_t_high, ) #yerr = d_strain149_t_high)
    ax2.plot(x_axis, strain163, ) #yerr = d_strain163)
    ax2.plot(x_axis, no_cells, ) #yerr = d_no_cells)
    
    ax2.legend(('strain149_t_low', 'strain149_t_high', 'strain163', 'no_cells'),  bbox_to_anchor=(1.43, 0.85))
    ax2.set_title('Median values of 3 biological replicates')
    ax2.set_xticks([1, 2, 3])
    ax2.set_xticklabels(['DMSO', '100uM', '1mM'])
    
    
    #%% plot heatmap of each plate
    
    test = plate.astype(float) 
    p3 = sns.heatmap(test, cmap="BuPu", square = True, ax=ax3, yticklabels = True, linewidths=4, cbar_kws = {'label': 'OD600 after 8h'})
    
    ax3.vlines([0, 12], *ax3.get_xlim(), linewidths = 2)
    ax3.vlines([4,8], *ax3.get_xlim(), linewidth = 0.5)
    ax3.hlines([0, 8], *ax3.get_xlim(), linewidth = 2)
    
    ax3.set_title('Heatmap of plate')
    ax3.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    ax3.set_xticklabels(['','DMSO', '', '', '', '100uM', '', '', '', '1mM'], rotation='horizontal')
    ax3.set_yticklabels(['TS149-1 low', 'TS149-1 high', 'TS149-2 low', 'TS149-2 high', 'TS149-3 low', 'TS149-3 high', 'TS163', 'no cells'], rotation='horizontal')
    ax3.yaxis.set_ticks_position('left')
    
    
    #%% title of figure and saving 
    compound_name = ['3,5-Pyrazoledicarboxylic acid monohydrate', 'Curcumin', 'Rosmarinic acid', 'DL-2,3-Diaminoproprionic acid', '2,2,4,4-Tetrahydroxybenzophenone', 'N-Iodosuccinimide', '2,3-Dichloro-1,4-nahthoquinone', 'Phtaldialdeyde']

    fig.suptitle('Compound '+str(n) + ' - "' + str(compound_name[n-1]) + '"', fontsize = 15)
    
    check_existance_save(os.path.join(pathbegin, 'Results & Plots', ('20200312_' + str(n) + '.png')))
    n = n+1



# end of script
    
    
    