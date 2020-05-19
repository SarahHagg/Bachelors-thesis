# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:01:04 2020

@author: Sarah_Haggenmüller
"""

#%%information for using this script

''' I created this script to be able to easy compare the
OD data of different measurements of 384-well-plates (with 
arabinose gradients done with the TECAN robot). 
When run, a seperate window should open with the interface.
There you can open the file you want to plot the data from 
with a file explorer. The file has to be an excel file. The 
data in the excel file has to be from B52 to Y67. Also the 
arabinose gradient has to be in 2-fold series and has to 
have been done with the TECAN robot in order to having the 
same order on the plate (because this script is automatically 
sorting the data, calculating the middle values and standard 
deviations for each arabionse concentration as well). The 
information about name of the strain, duration of incubation 
and type of media, which can be filled in, are used to generate
automatically a title of the graph. If wished otherwise, there
is also the option to name the graph in any other way. Naming 
the strain is also important for generating the legend. After 
plotting, another file can be selected, and be plotted in the 
same graph. The y-axis will adjust automatically to the datasets
and all the plotted file names are listed in the bottom right 
corner of the interface. The graph can be saved with a file 
explorer. In case that you have entered a file name which does
already exist, you are asked if you want to overwrite the existing
file (not recommended). Have fun! '''

#%% import necessary libraries

import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import statistics


#%% define basic structure of interface
height_canvas = 700
width_canvas = 1400
root = tk.Tk()

    #center pop-up window on screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

    #calculate position x and y coordinates
x = (screen_width/2) - (width_canvas/2)
y = (screen_height/2.3) - (height_canvas/2)
root.geometry('%dx%d+%d+%d' % (width_canvas, height_canvas, x, y))


canvas = tk.Canvas(root, height = height_canvas, width = width_canvas)
canvas.pack()

strain = 'TS149'
media = 'LB'
time = '8h'
all_files = []

#%%define commands for later use
def select_file():
    global file_path 
    file_path = filedialog.askopenfilename()
    global file_name 
    file_name = os.path.basename(file_path)
    
    if file_path.endswith('.xlsx'):
        all_files.append(file_name)
        
        label2 = tk.Label(frame1, bg = '#b8f772', anchor='w', text = 'The selected  file is "'+file_name+'".')
        label2.place(relx = 0.1, relwidth = 0.8, rely = 0.6, relheight = 0.14)
        
        button2 = tk.Button(frame1, text = 'Change selected file', command = change_file)
        button2.place(relx = 0.6, relwidth = 0.3, rely = 0.82, relheight = 0.14)
    else:
        messagebox.showerror("Error", "You have to select an excel file!!")
        
        
def change_file():
    global file_path 
    file_path = filedialog.askopenfilename()
    global file_name 
    file_name = os.path.basename(file_path)
    if file_path.endswith('.xlsx'):
        all_files.append(file_name)
        
        label2 = tk.Label(frame1, anchor='w', bg = '#b8f772', text = 'The selected  file is "'+file_name+'".')
        label2.place(relx = 0.1, relwidth = 0.8, rely = 0.6, relheight = 0.1)

    else:
        messagebox.showerror("Error", "You have to select an excel file!!")
        
    
def set_settings():
    global strain
    strain = entry1.get()
    
    global media
    media = entry2.get()
    
    global time
    time = entry3.get()
    
    label7 = tk.Label(frame2, bg = '#c9f598', anchor='w', text = 'The settings were set to:   ' + strain + '  -  ' + media + '  -  '+ time + '.')
    label7.place(relx = 0.1, relwidth = 0.5, rely = 0.85, relheight = 0.1)

    
num=0
label_deviations = 'standard deviation'
maxvalues = []
maxdeviations = []
plot_title = ' '

def plot_graph():
    
    global strain
    strain = entry1.get()
    
    global media
    media = entry2.get()
    
    global time
    time = entry3.get()
    
    label7 = tk.Label(frame2, bg = '#c9f598', anchor='w', text = 'The settings were set to:   ' + strain + '  -  ' + media + '  -  '+ time + '.')
    label7.place(relx = 0.1, relwidth = 0.5, rely = 0.85, relheight = 0.1)

    global frame3
    frame3 = tk.Frame(root, bg = 'white')
    frame3.place(relx = 0.475, relwidth = 0.5, rely = 0.025, relheight = 0.55)

    frame3.destroy()

    frame3 = tk.Frame(root, bg = 'white')
    frame3.place(relx = 0.475, relwidth = 0.5, rely = 0.025, relheight = 0.55)

    sns.set_style("whitegrid")
    global fig
    fig = plt.figure(1)
    raw = pd.read_excel(file_path)
        
    df_raw = (raw.iloc[50:66])
    arr = pd.DataFrame(df_raw).to_numpy()

#sort the array: every arabinose concentration in one column
    totalArray = np.hstack([np.concatenate([arr[0:15:2, w:w+2].reshape(16,1) for w in range(1, 24,2)], axis=1), \
                        np.concatenate([arr[1:16:2, w:w+2].reshape(16,1) for w in range(1, 24,2)], axis=1)])

    
#add new row underneath with middle values of each column
    middleValues = np.mean(totalArray, axis=0)
    combined = np.vstack((totalArray, middleValues))

#arabinose concentrations as list
    arabinose = []
    for a in range (0, 24, 1):
        b = 1 * (0.5 ** a)
        arabinose.append(b)
    
    df = pd.DataFrame(combined, columns = [arabinose])


#calculate standard deviations     
    deviations = []
    for i in range (0, 24, 1):
        column_values = df.iloc[0:16, i]
        deviation = statistics.stdev(column_values)
        deviations.append(deviation)

#plot and edit graph
    plt.plot(arabinose, middleValues, label = strain, \
         marker = '.', markersize = 6, markerfacecolor='black', markeredgecolor = 'black', \
        linestyle = '-', color = color, linewidth = '0.8')
    plot_title = entry4.get()
    if len(entry4.get()) == 0:
        plot_title = strain + ' growth in ' + media + ' after ' + time
        
        if len(entry1.get()) == 0 and len(entry2.get()) == 0 and len(entry3.get()) == 0:
            plot_title = 'Growth in 2-fold arabinose gradient'    
        
        elif len(entry1.get()) == 0:
            plot_title = 'Growth in ' + media + ' after ' + time
        
        elif len(entry2.get()) == 0:
            plot_title = strain + ' growth after ' + time
        
        elif len(entry3.get()) == 0:
            plot_title = strain + ' growth in ' + media
        
                
    plt.title (plot_title)
    plt.xlabel ('arabinose concentration in 2-fold series [in M]')
    plt.ylabel ('OD600')
   
    maxvalues.append(max(middleValues))  
    maxdeviations.append(max(deviations))

    limit = (max(maxvalues) + max(maxdeviations) + 0.05*(max(maxvalues)))
    plt.ylim(top= limit)
    plt.ylim(bottom=0)
    plt.xscale('log')
    
#errorbars with standard deviations
    global num
    num = num + 1
    if num == 1:
        print('ok2')
        global label_deviations
        label_deviations = '_nolegend_'
        #plt.errorbar(yerr = deviations, label = 'standard deviation')
    plt.errorbar(arabinose, middleValues, yerr = deviations, fmt = ' ', capsize = 2, ecolor = 'grey', elinewidth = 0.5, label = label_deviations)
    plt.legend(loc="upper right") 

#place plot in canvas
    global canvas2
    canvas2 = FigureCanvasTkAgg(fig, master=frame3)
    canvas2.get_tk_widget().pack(side='top')

    entry1.delete(0, "end")

#add filename to list in textbox
    global textbox
    textbox = tk.Text(frame5)
    for x in all_files:
        textbox.insert('end', x + '\n')
    textbox.place(relx = 0.1, relwidth = 0.8, rely = 0.225, relheight = 0.55)

color = 'black'
def choose_linecolor():
    color_select = colorchooser.askcolor()
    global color
    color = color_select[1]
    
    button8 = tk.Button(frame4, text = ' ', bg = color, command = choose_linecolor)
    button8.place(relx=0.725, relwidth = 0.175, rely = 0.25, relheight = 0.1)
    
def color_TS149():
    global color
    color = '#b32025'

    button8 = tk.Button(frame4, text = ' ', bg = color, command = choose_linecolor)
    button8.place(relx=0.725, relwidth = 0.175, rely = 0.25, relheight = 0.1)
    
def color_TS163():
    global color
    color = '#21b844'
    
    button8 = tk.Button(frame4, text = ' ', bg = color, command = choose_linecolor)
    button8.place(relx=0.725, relwidth = 0.175, rely = 0.25, relheight = 0.1)

    
def save_graph():
    folder_selected = filedialog.askdirectory()
    name_save = simpledialog.askstring("Filename", "How do you want to name the file? The graph will be saved as a '.png'.",
                                parent=root)
    
    
    check = os.path.exists(os.path.join(folder_selected, str(name_save + '.png')))
        
    if check is True:
        result = tk.messagebox.askquestion("File exists already", "The file exists already. Do you want to overwrite the existing file?", icon='warning')
        if result == 'yes':
            fig.savefig(os.path.join(folder_selected, str(name_save + '.png')), dpi =300)
            tk.messagebox.showinfo(' ', 'The existing file was overwritten.')
        else:
            tk.messagebox.showinfo(' ', 'The existing file was not overwritten.')
        
    else: 
        fig.savefig(os.path.join(folder_selected, str(name_save + '.png')), dpi =300)

     
def close():
    root.destroy()

def reset_everything():    
    global strain
    strain = 'TS149'
    global media
    media = 'LB'
    global time
    time = '8h'
    global all_files
    all_files = []
    global color
    color = 'black'
    global num
    num=0
    global label_deviations
    label_deviations = 'standard deviation'
    global maxvalues
    maxvalues = []
    global maxdeviations
    maxdeviations = []
    global plot_title
    plot_title = ' '
    textbox.destroy()
    entry4.delete(0, "end")
    entry3.delete(0, "end")
    entry2.delete(0, "end")
    entry1.delete(0, "end")
    plt.close(fig)
    
    labelwhite = tk.Label(frame3, text = ' ', bg = 'white')
    labelwhite.place(relx = 0, relwidth = 1, rely = 0, relheight = 1)
    
    labelwhite2 = tk.Label (frame5, text = '', bg = 'white')
    labelwhite2.place(relx = 0.1, relwidth = 0.8, rely = 0.225, relheight = 0.55)


#%% fill in the frames of interface 
    
    #frame1
frame1 = tk.Frame(root, bg = '#b8f772')
frame1.place(relx = 0.05, relwidth = 0.4, rely = 0.025, relheight = 0.2)

label1 = tk.Label(frame1, bg= '#b8f772',font='Helvetica 10 bold', text = 'Select the excel file you want to plot the data from.')
label1.place(relx = 0.1, relwidth = 0.8, rely = 0.1, relheight = 0.14)

button1 = tk.Button(frame1, text = 'Open file explorer', command = select_file)
button1.place(relx = 0.6, relwidth = 0.3, rely = 0.32, relheight = 0.14)


    #frame2
frame2 = tk.Frame(root, bg = '#c9f598')
frame2.place(relx = 0.05, relwidth = 0.4, rely = 0.25, relheight = 0.325)

label3a = tk.Label(frame2, text = 'Enter details about your data.',font='Helvetica 10 bold', bg = '#c9f598')
label3a.place(relx = 0.125, relwidth = 0.4, rely = 0.1, relheight = 0.1)

label3b = tk.Label(frame2, text = '(They will be set as the title of the plot)', bg='#c9f598')
label3b.place(relx = 0.5, relwidth = 0.4, rely = 0.1, relheight = 0.1)

label4 = tk.Label(frame2, anchor='w', text = 'What strain is the data from? (e.g. TS163)', bg = '#c9f598')
label4.place(relx = 0.1, relwidth = 0.5, rely = 0.25, relheight = 0.1)
entry1 = tk.Entry(frame2)
entry1.place(relx= 0.65, relwidth = 0.25, rely = 0.25, relheight = 0.1)

label5 = tk.Label(frame2, anchor='w', text = 'In which media did the bacteria grow? (e.g. LB)', bg = '#c9f598')
label5.place(relx = 0.1, relwidth = 0.5, rely = 0.4, relheight = 0.1)
entry2 = tk.Entry(frame2)
entry2.place(relx= 0.65, relwidth = 0.25, rely = 0.4, relheight = 0.1)

label6 = tk.Label(frame2, anchor='w', text = 'How long were the bacteria incubated? (e.g. 8h)', bg = '#c9f598')
label6.place(relx = 0.1, relwidth = 0.5, rely = 0.55, relheight = 0.1)
entry3 = tk.Entry(frame2)
entry3.place(relx= 0.65, relwidth = 0.25, rely = 0.55, relheight = 0.1)

button3 = tk.Button(frame2, text = "Set settings", command = set_settings)
button3.place(relx= 0.65, relwidth = 0.25, rely = 0.7, relheight = 0.1)


    #frame4
frame4 = tk.Frame(root, bg ='#dcffb5')
frame4.place(relx =0.05, relwidth = 0.4, rely = 0.6, relheight = 0.325)

label9 = tk.Label(frame4, text = 'Change the color and the title of the plot (optional).',font='Helvetica 10 bold', bg = '#dcffb5')
label9.place(relx = 0.1, relwidth = 0.8, rely = 0.1, relheight = 0.1)

button4 = tk.Button(frame4, text = "Plot the graph.", command = plot_graph)
button4.place(relx= 0.725, relwidth = 0.25, rely = 0.85, relheight = 0.1)

label10 = tk.Label(frame4, bg ='#dcffb5', text = 'Choose the color of the line:', anchor = 'w')
label10.place(relx=0.1, relwidth = 0.3, rely = 0.25, relheight = 0.1)

button11 = tk.Button(frame4, text = 'open colors', command = choose_linecolor)
button11.place(relx = 0.5, relwidth = 0.2, rely = 0.25, relheight = 0.1)

button8 = tk.Button(frame4, text = ' ', bg = color, command = choose_linecolor)
button8.place(relx=0.725, relwidth = 0.175, rely = 0.25, relheight = 0.1)

label7 = tk.Label(frame4, text = 'Default colors:', bg ='#dcffb5', anchor='w')
label7.place(relx = 0.2, relwidth =0.25, rely = 0.4, relheight = 0.1)

button9 = tk.Button(frame4, text = 'TS149', bg = '#b32025', command = color_TS149)
button9.place(relx=0.375, relwidth = 0.25, rely = 0.4, relheight = 0.1)

button10 = tk.Button(frame4, text = 'TS163', bg = '#21b844', command = color_TS163)
button10.place(relx=0.65, relwidth = 0.25, rely = 0.4, relheight = 0.1)

label8 = tk.Label(frame4, text = 'Change the title:', bg ='#dcffb5', anchor='w')
label8.place(relx = 0.1, relwidth =0.25, rely = 0.6, relheight = 0.1)

entry4 = tk.Entry(frame4)
entry4.place(relx = 0.3, relwidth =0.6, rely = 0.6, relheight = 0.1)


    #frame5
frame5 = tk.Frame(root, bg ='#dcffb5')
frame5.place(relx =0.475, relwidth = 0.5, rely = 0.6, relheight = 0.325)

label11 = tk.Label(frame5, text = 'All plotted files:', font='Helvetica 10 bold', bg = '#dcffb5')
label11.place(relx = 0.1, relwidth = 0.8, rely = 0.1, relheight = 0.1) 

button11 = tk.Button(frame5, text = 'Reset', command = reset_everything)
button11.place(relx = 0.35, rely = 0.85, relwidth = 0.2, relheight = 0.1)

button12 = tk.Button(frame5, text = 'Safe graph', command = save_graph)
button12.place(relx = 0.1, rely = 0.85, relwidth = 0.2, relheight = 0.1)

button13 = tk.Button(frame5, text = 'Close Interface', command = close)
button13.place(relx=0.7, rely = 0.85, relwidth = 0.2, relheight = 0.1)

frame6 = tk.Frame(root, bg = '#e8ffcf')
frame6.place(relx = 0.05, rely =0.95, relheight = 0.025, relwidth = 0.925)

labelsignature = tk.Label(frame6, text = 'by Sarah Haggenmueller', anchor = 'e', font = 'Helvetica 8 italic')
labelsignature.place(relx = 0.1, rely = 0.1, relheight = 1, relwidth = 0.9)

root.mainloop()

#end of script