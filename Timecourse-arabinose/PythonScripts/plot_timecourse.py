# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:16:51 2020

@author: Sarah Haggenmüller 
        - Jakes template edited -
"""

#%%information for using this script

''' This python script can be used to plot the data of the timecourse
experiments. The script automatically extracts the filepath, and 
automatically saves the plot in the folder 'Results & Plots'. At 
the beginning a seperate window will pop up, where you can select 
the experiment, you want to plot the data from. This script works 
only when the whole folder '20200313_TS149_PrestwickScreen' is copied 
to a device, the file of the script not moved somewhere else and no 
filenames of the RawData are changed. Because the experiment of the
11. Feb 2020 was disrupted, just the data after approximately 5.5h 
were saved. Therefore, the x-axis values start for this plot at 5.5h.'''


#%% import necessary libraries
import pandas as pandas
import matplotlib.pyplot as pyplot
import numpy as np
import seaborn as sns
import os
import tkinter as tk

sns.set_style("whitegrid")


#%% select experiment

root = tk.Tk()
root.title('Select the Timecourse experiment')
root.geometry('500x220')

canvas1 = tk.Canvas(root, bg='black')
canvas1.pack()

frame1 = tk.Frame(canvas1)
frame1.pack()

labelspace = tk.Label(frame1, text = ' ')
labelspace.pack()

label = tk.Label(frame1, text = 'Select the experiment you want to plot the data from:')
label.pack()

labelspace2 = tk.Label(frame1, text = ' ')
labelspace2.pack()

mylistbox = tk.Listbox(frame1, width=50, height=7, bg= 'black')
mylistbox.insert(0, ' ')
mylistbox.insert(1, '20200211_Timecourse_disrupted')
mylistbox.insert(2, ' ')
mylistbox.insert(3, '20200212_Timecourse')
mylistbox.insert(4, ' ')
mylistbox.insert(5, '20200213_Timecourse')
mylistbox.itemconfigure('1', bg='#fcba03')
mylistbox.itemconfigure('3', bg = '#ffd04f')
mylistbox.itemconfigure('5', bg = '#ffe49c')
mylistbox.pack()

def selection(event):
    w = event.widget
    idx = int(w.curselection()[0])
    global value
    value = w.get(idx)
    print(value)
    mylistbox.destroy()
    root.destroy()
mylistbox.bind('<<ListboxSelect>>', selection)

root.mainloop()


#%% extracting current working directory
pathfile = os.getcwd()
pathbegin = os.path.dirname(pathfile)


# The path to the raw data Excel file
Data_Path = os.path.join(pathbegin, 'RawData', str(value + '.xlsx'))

# Import the timecourse measurements of the growing strains
Raw_Data = {};

Raw_Data['Sheet Data'] = pandas.read_excel(Data_Path);
Raw_Data['OD Values'] = Raw_Data['Sheet Data'].iloc[60:156, 1:74].astype(float).values;


# Import the time points and convert to hours
Raw_Data['Time (Seconds)'] = Raw_Data['Sheet Data'].iloc[58, 1:74].astype(float).values; #53 is the time column in seconds

if value == '20200211_Timecourse_disrupted':
    Raw_Data['Time (Hours)'] = Raw_Data['Time (Seconds)'] / (60*60) + 5.5;    
else:
    Raw_Data['Time (Hours)'] = Raw_Data['Time (Seconds)'] / (60*60);


# Organize and process the OD data
Processed_Data = {};

# The Master array is organized as plate row, plate column, timepoint
Processed_Data['Master'] = np.reshape(Raw_Data['OD Values'], (8, 12, -1));

# Take the mean and standard deviation of each sample across all time points
Processed_Data['Mean'] = np.mean(Processed_Data['Master'], 1);
Processed_Data['Std'] = np.std(Processed_Data['Master'], 1);

Processed_Data['Time (Hours)'] = (Raw_Data['Time (Hours)']);


# Plot the mean ODs for each treatment for all time points
Fig_handle, Ax_handle = pyplot.subplots();

Treatment_Num = 0; #(Control strain) with no arabinose
Ax_handle.errorbar(Processed_Data['Time (Hours)'], Processed_Data['Mean'][Treatment_Num, :], yerr=Processed_Data['Std'][Treatment_Num, :])

Treatment_Num = 1; #(Cysh) with no arabinose
Ax_handle.errorbar(Processed_Data['Time (Hours)'], Processed_Data['Mean'][Treatment_Num, :], yerr=Processed_Data['Std'][Treatment_Num, :])

Treatment_Num = 2; #(Control strain) low Arabinose
Ax_handle.errorbar(Processed_Data['Time (Hours)'], Processed_Data['Mean'][Treatment_Num, :], yerr=Processed_Data['Std'][Treatment_Num, :])

Treatment_Num = 3; #(CysH) low Arabinose
Ax_handle.errorbar(Processed_Data['Time (Hours)'], Processed_Data['Mean'][Treatment_Num, :], yerr=Processed_Data['Std'][Treatment_Num, :])

Treatment_Num = 4; #(Control strain) Medium arabinose
Ax_handle.errorbar(Processed_Data['Time (Hours)'], Processed_Data['Mean'][Treatment_Num, :], yerr=Processed_Data['Std'][Treatment_Num, :])

Treatment_Num = 5; #(CysH) Medium arabinose
Ax_handle.errorbar(Processed_Data['Time (Hours)'], Processed_Data['Mean'][Treatment_Num, :], yerr=Processed_Data['Std'][Treatment_Num, :])

Treatment_Num = 6; #Control strain) High arabinose
Ax_handle.errorbar(Processed_Data['Time (Hours)'], Processed_Data['Mean'][Treatment_Num, :], yerr=Processed_Data['Std'][Treatment_Num, :])

Treatment_Num = 7; #(CysH) High arabinose
Ax_handle.errorbar(Processed_Data['Time (Hours)'], Processed_Data['Mean'][Treatment_Num, :], yerr=Processed_Data['Std'][Treatment_Num, :])

Ax_handle.set_xlabel('Time (Hours)', fontsize = 15)
Ax_handle.set_ylabel('OD600', fontsize = 15)
Ax_handle.legend(('No bacteria', 'TS149 no Ara','TS149 low Ara','TS149 middle Ara','TS149 high Ara','TS149 very high Ara', 'TS149 DAP', 'Control middle Ara'), fontsize=15)

Ax_handle.set_title('TS149 and TS163 Timecourse in LB / SulfurDropout', fontsize = 20)

fig = pyplot.gcf()
fig.set_size_inches(18.5, 10.5)

#%% saving figure in correct folder

def check_existance_save(filename):
    check = os.path.exists(filename)
            
    if check is True:
        result = tk.messagebox.askquestion("File exists already", "The file with the plot exists already. Do you want to overwrite the existing file?", icon='warning')
        if result == 'yes':
#            plt.savefig((filename), dpi = 300)
            fig.savefig((filename),bbox_inches='tight', dpi = 300)
            tk.messagebox.showinfo(' ', 'The existing file was overwritten.')
        else:
            tk.messagebox.showinfo(' ', 'The existing file was not overwritten.')
        
    else: 
#        plt.savefig((filename), dpi = 300)
        fig.savefig((filename),bbox_inches='tight', dpi = 300)


check_existance_save(os.path.join(pathbegin, 'Results & Plots', str(value + '.png')))



# end of script




