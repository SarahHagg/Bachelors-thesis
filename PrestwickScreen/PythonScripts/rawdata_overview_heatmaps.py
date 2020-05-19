# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:53:04 2020

@author: Sarah Haggenmüller
"""


#%%information for using this script

''' This python script can be used to plot the data of Prestwick 
Chemical Library Screens. It will print a collection of heatmaps 
for every plate at 0h, 8h and also the difference. The script
automatically extracts the filepath, and automatically saves the
plot in the folder 'Results & Plots'. At the beginning a seperate 
window will pop up, where you can select the experiment, you want
to plot the data from. This script works only when the whole folder 
'20200313_TS149_PrestwickScreen' is copied to a device, the file
of the script not moved somewhere else and no filenames of the 
RawData are changed. '''


#%% import necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import tkinter as tk

#%% select experiment

root = tk.Tk()
root.title('Select Prestwick screen')
root.geometry('500x220')

canvas1 = tk.Canvas(root)
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
mylistbox.insert(1, '20200226_TS149_Prestwick1')
mylistbox.insert(2, ' ')
mylistbox.insert(3, '20200303_TS149_Prestwick2')
mylistbox.insert(4, ' ')
mylistbox.insert(5, '20200312_TS149_Prestwick3')
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
# path=os.path.abspath(os.getcwd())
# a = "/".join(path.split('\\')[:-1])

pathfile = os.getcwd()
pathbegin = os.path.dirname(pathfile)


# time zero data (0h)
df11 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time0', 'low_1.xlsx')).iloc[50:66, 1:].astype(float)
df21 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time0', 'low_2.xlsx')).iloc[50:66, 1:].astype(float)
df31 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time0', 'low_3.xlsx')).iloc[50:66, 1:].astype(float)
df41 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time0', 'low_4.xlsx')).iloc[50:66, 1:].astype(float)

df51 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time0', 'high_1.xlsx')).iloc[50:66, 1:].astype(float)
df61 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time0', 'high_2.xlsx')).iloc[50:66, 1:].astype(float)
df71 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time0', 'high_3.xlsx')).iloc[50:66, 1:].astype(float)
df81 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time0', 'high_4.xlsx')).iloc[50:66, 1:].astype(float)

# after incubation data (8h)
df12 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time8', 'low_1.xlsx')).iloc[50:66, 1:].astype(float)
df22 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time8', 'low_2.xlsx')).iloc[50:66, 1:].astype(float)
df32 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time8', 'low_3.xlsx')).iloc[50:66, 1:].astype(float)
df42 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time8', 'low_4.xlsx')).iloc[50:66, 1:].astype(float)

df52 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time8', 'high_1.xlsx')).iloc[50:66, 1:].astype(float)
df62 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time8', 'high_2.xlsx')).iloc[50:66, 1:].astype(float)
df72 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time8', 'high_3.xlsx')).iloc[50:66, 1:].astype(float)
df82 = pd.read_excel(os.path.join(pathbegin, 'RawData', value, 'time8', 'high_4.xlsx')).iloc[50:66, 1:].astype(float)

# after incubation - time zero data
plate1_low = df12 - df11
plate2_low = df22 - df21
plate3_low = df32 - df31
plate4_low = df42 - df41

plate1_high = df52 - df51
plate2_high = df62 - df61
plate3_high = df72 - df71
plate4_high = df82 - df81


timezero = [df11, df51, df21, df61, df31, df71, df41, df81]
timeeight = [df12, df52, df22, df62, df32, df72, df42, df82]
growth = [plate1_low, plate1_high, plate2_low, plate2_high, plate3_low, plate3_high, plate4_low, plate4_high]

#%% plotting the subplots

fig, ax_plots = plt.subplots(8, 3,figsize=(7,15))
n=0
for elem in timezero:
    sns.heatmap(elem, ax=ax_plots[n,0], cmap="BuPu", linewidth = 0.2, linecolor = 'black', square = True, yticklabels = False, xticklabels = False, cbar=True,vmin=0,vmax=0.5, cbar_ax = fig.add_axes([0.95,.125,.03,.75]))
    ax_plots[n,0].vlines([6, 12, 18], *ax_plots[n,0].get_xlim(), linewidth = 1, color = 'black')
    ax_plots[n,0].hlines([4, 8, 12], *ax_plots[n,0].get_xlim(), linewidth = 1, color = 'black')
    n = n+1

m = 0
for elem in timeeight:
    im = sns.heatmap(elem, ax=ax_plots[m,1], cmap="BuPu", linewidth = 0.2, linecolor = 'black', square = True, yticklabels = False, xticklabels = False, cbar=True,vmin=0,vmax=0.5, cbar_ax = fig.add_axes([0.95,.125,.03,.75]))
    ax_plots[m,1].vlines([6, 12, 18], *ax_plots[m,1].get_xlim(), linewidth = 1, color = 'black')
    ax_plots[m,1].hlines([4, 8, 12], *ax_plots[m,1].get_xlim(), linewidth = 1, color = 'black')
    m = m+1

l = 0
for elem in growth:
    sns.heatmap(elem, ax=ax_plots[l,2], cmap="BuPu", linewidth=0.2, linecolor = 'black', square = True, yticklabels = False, xticklabels = False, cbar=True,vmin=0,vmax=0.5, cbar_ax = fig.add_axes([0.95,.125,.03,.75]))
    ax_plots[l,2].vlines([6, 12, 18], *ax_plots[l,2].get_xlim(), linewidth = 1, color = 'black')
    ax_plots[l,2].hlines([4, 8, 12], *ax_plots[l,2].get_xlim(), linewidth = 1, color = 'black')
    l = l+1    


#%% naming the two axes 
ax_plots[0,0].set_title('time 0h')
ax_plots[0,1].set_title('time 8h')
ax_plots[0,2].set_title('difference (cellgrowth)')

ax_plots[0,0].set_ylabel('Plate1 - low ara')
ax_plots[1,0].set_ylabel('Plate1 - high ara')
ax_plots[2,0].set_ylabel('Plate2 - low ara')
ax_plots[3,0].set_ylabel('Plate2 - high ara')
ax_plots[4,0].set_ylabel('Plate3 - low ara')
ax_plots[5,0].set_ylabel('Plate3 - high ara')
ax_plots[6,0].set_ylabel('Plate4 - low ara')
ax_plots[7,0].set_ylabel('Plate4 - high ara')

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

fig.savefig("test.svg", format="svg")

# end of script


