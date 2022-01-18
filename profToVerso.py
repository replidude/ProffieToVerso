import tkinter as tk
from tkinter import filedialog
from time import sleep
import os
import shutil
from pydub import AudioSegment

#global variables:
proffie_path = ""
verso_path = ""
first = True
lockup = False
lock_count = 0 #for keeping track of lockup sounds made

#global dictionary for finding files to be renamed
versoDict = {
    "swng01.wav" : "aswing1.wav",
    "swng02.wav" : "aswing2.wav",
    "swng03.wav" : "aswing3.wav", 
    "swng04.wav" : "aswing4.wav",
    "swng05.wav" : "aswing5.wav",
    "swng06.wav" : "aswing6.wav",
    "swng07.wav" : "aswing7.wav",
    "swng08.wav" : "aswing8.wav",
    "swng09.wav" : "aswing9.wav",
    "swng10.wav" : "aswing10.wav",
    "swng11.wav" : "aswing11.wav",
    "swng12.wav" : "aswing12.wav",
    "swng13.wav" : "aswing13.wav",
    "swng14.wav" : "aswing14.wav",
    "swng15.wav" : "aswing15.wav",
    "swng16.wav" : "aswing16.wav",
    "swng1.wav" : "aswing1.wav",
    "swng2.wav" : "aswing2.wav",
    "swng3.wav" : "aswing3.wav", #proffie accepts number schemes with and without leading zeros
    "swng4.wav" : "aswing4.wav",
    "swng5.wav" : "aswing5.wav",
    "swng6.wav" : "aswing6.wav",
    "swng7.wav" : "aswing7.wav",
    "swng8.wav" : "aswing8.wav",
    "swng9.wav" : "aswing9.wav",
    "font.wav" : "font.wav",
    "clsh01.wav" : "clash1.wav",
    "clsh02.wav" : "clash2.wav",
    "clsh03.wav" : "clash3.wav",
    "clsh04.wav" : "clash4.wav",
    "clsh05.wav" : "clash5.wav",
    "clsh06.wav" : "clash6.wav",
    "clsh07.wav" : "clash7.wav",
    "clsh08.wav" : "clash8.wav",
    "clsh09.wav" : "clash9.wav",
    "clsh10.wav" : "clash10.wav",
    "clsh11.wav" : "clash11.wav",
    "clsh12.wav" : "clash12.wav",
    "clsh13.wav" : "clash13.wav",
    "clsh14.wav" : "clash14.wav",
    "clsh15.wav" : "clash15.wav",
    "clsh16.wav" : "clash16.wav",
    "clsh1.wav" : "clash1.wav",
    "clsh2.wav" : "clash2.wav",
    "clsh3.wav" : "clash3.wav",
    "clsh4.wav" : "clash4.wav",
    "clsh5.wav" : "clash5.wav",
    "clsh6.wav" : "clash6.wav",
    "clsh7.wav" : "clash7.wav",
    "clsh8.wav" : "clash8.wav",
    "clsh9.wav" : "clash9.wav",
    "blst01.wav" : "deflc1.wav",
    "blst02.wav" : "deflc2.wav",
    "blst03.wav" : "deflc3.wav",
    "blst04.wav" : "deflc4.wav",
    "blst05.wav" : "deflc5.wav",
    "blst06.wav" : "deflc6.wav",
    "blst07.wav" : "deflc7.wav",
    "blst08.wav" : "deflc8.wav",
    "blst1.wav" : "deflc1.wav",
    "blst2.wav" : "deflc2.wav",
    "blst3.wav" : "deflc3.wav",
    "blst4.wav" : "deflc4.wav",
    "blst5.wav" : "deflc5.wav",
    "blst6.wav" : "deflc6.wav",
    "blst7.wav" : "deflc7.wav",
    "blst8.wav" : "deflc8.wav",
    "color.wav" : "color.wav",
    "endlock.wav" : "endlock1.wav",
    "endlock1.wav" : "endlock1.wav",
    "endlock2.wav" : "endlock2.wav",
    "endlock3.wav" : "endlock3.wav",
    "endlock4.wav" : "endlock4.wav",
    "hum01.wav" : "hum.wav",
    "hum.wav" : "hum.wav",
    "in.wav" : "off1.wav",
    "in01.wav" : "off1.wav",
    "in02.wav" : "off2.wav",
    "lock01.wav" : "lockup.wav", #note: proffie has the begin lockup separate, not the case for verso, I can use pydub to stitch the individual audio files together holy crap
    "lock.wav" : "lockup.wav",
    "lowbatt.wav" : "lowbatt.wav",
    "out.wav" : "on1.wav",
    "out01.wav" : "on1.wav",
    "out02.wav" : "on2.wav",
    "out03.wav" : "on3.wav",
    "out04.wav" : "on4.wav",
    "swingh01.wav" : "swingh1.wav",
    "swingh02.wav" : "swingh2.wav",
    "swingh03.wav" : "swingh3.wav",
    "swingh04.wav" : "swingh4.wav",
    "swingl01.wav" : "swingl1.wav",
    "swingl02.wav" : "swingl2.wav",
    "swingl03.wav" : "swingl3.wav",
    "swingl04.wav" : "swingl4.wav",
    "swingh1.wav" : "swingh1.wav",
    "swingh2.wav" : "swingh2.wav",
    "swingh3.wav" : "swingh3.wav",
    "swingh4.wav" : "swingh4.wav",
    "swingl1.wav" : "swingl1.wav",
    "swingl2.wav" : "swingl2.wav",
    "swingl3.wav" : "swingl3.wav",
    "swingl4.wav" : "swingl4.wav",
    "ccchange.wav" : "scroll.wav",
    "bgnlock.wav" : "bgnlock1.wav",
    "bgnlock1.wav" : "bgnlock1.wav",
    "bgnlock2.wav" : "bgnlock2.wav",
    "bgnlock3.wav" : "bgnlock3.wav",
    "bgnlock4.wav" : "bgnlock4.wav"
    } #still dont have mute, unmute, or select, not necessary though, can run fine without, most fonts seem to

#file dialog setup
root = tk.Tk()
root.withdraw()
prof_win = tk.Tk()

#finds screen center
center_x = prof_win.winfo_screenwidth()
center_x = int(center_x/2 - 300)
center_y = prof_win.winfo_screenheight()
center_y = int(center_y/2 - 200)


#FUNCTIONS TO BE USED
def verso_grab():
    global verso_path
    verso_path = filedialog.askdirectory()
    if verso_path != "":
        error_lbl_verso.place_forget()
    return verso_path

def proffie_grab():
    global proffie_path
    proffie_path = filedialog.askdirectory()
    if proffie_path != "":
        error_lbl_prof.place_forget()
    return proffie_path

def convert(): #functional
    global verso_path
    global proffie_path
    bad_conv = 0
    if verso_path == "":
        error_lbl_verso.place(x = 100, y = 350)
        bad_conv += 1
    if proffie_path == "":
        error_lbl_prof.place(x = 100, y = 300)
        bad_conv += 1
    if bad_conv > 0:
        return
    verso_path = verso_path + '/Verso_' + font_name()
    os.mkdir(verso_path)
    copy_wavs(proffie_path)
    rename()
    stitch()
    open_final()
    verso_path = ""
    proffie_path = ""
    converted_lbl.place(x = 220, y = 100)
    return


def requestDestination(path): #functional
    global first
    if first == True:
        print("please select the Proffie folder to be converted...")
        first = False 
    else:
        print("please select the end destination for the verso font...")
    sleep(2)
    path = filedialog.askdirectory() 
    print(path)
    return path

def copy_wavs(path1): #functional 
    global lockup
    for filename in os.listdir(path1):
        if filename in versoDict:
            full_name = path1 + '/' + filename
            if filename.__contains__("font"):
                shutil.copy(full_name, verso_path)
                os.rename(verso_path + '/' + filename, verso_path + '/boot1.wav')
                sleep(1)
            shutil.copy(full_name, verso_path)
        elif filename.__contains__('.'):
            continue
        else:
            new_folder = path1 + '/' + filename
            copy_wavs(new_folder)
    
def rename(): #functional
    global verso_path
    for filename in os.listdir(verso_path):
        if filename in versoDict:
            temp = versoDict[filename]
            os.rename(verso_path + '/' + filename, verso_path + '/' + temp)


def stitch(): #functional
    global verso_path, lock_count
    for filename in os.listdir(verso_path):
        if filename.__contains__('bgnlock'):
            bg_lock = AudioSegment.from_file(verso_path + '/' + filename, format="wav")
            lock = AudioSegment.from_file(verso_path + '/lockup.wav', format="wav")
            combined = bg_lock + lock
            lock_count += 1
            file_handle = combined.export(verso_path + '/lockup' + str(lock_count) + '.wav', format="wav")
            os.remove(verso_path + '/' + filename)
    if lock_count == 0: 
        os.rename(verso_path + '/lockup.wav', verso_path + '/lockup1.wav')
    else:
        os.remove(verso_path + '/lockup.wav')
            

def font_name(): #functional
    hold = proffie_path
    temp_list = hold.split("/")
    hold = temp_list[-1]
    hold = hold.casefold()
    hold = hold.replace("proffie","")
    return hold

def open_final(): #functional
    path = verso_path
    path = os.path.realpath(path)
    os.startfile(path)

def end_program():
    prof_win.destroy()
    root.destroy()
    return


#screen setup
prof_win.geometry(f'600x400+{center_x}+{center_y}')
prof_win.title('Proffie to Verso Conversion')
prof_win.resizable(False,False)

error_lbl_verso = tk.Label(prof_win, text = "No Verso folder was selected, please select a destination", bg = "red", fg = "white")
error_lbl_verso.place(x = 100, y = 350)
error_lbl_verso.place_forget()

error_lbl_prof = tk.Label(prof_win, text = "No Proffie folder was selected, please select a destination", bg = "red", fg = "white")
error_lbl_prof.place(x = 100, y = 300)
error_lbl_prof.place_forget()

converted_lbl = tk.Label(prof_win, text = "Font Conversion Successful!", bg = "green", fg = "white")
converted_lbl.place(x = 250, y = 100)
converted_lbl.place_forget()

text_lab = tk.Label(prof_win, text = "Please select the Proffie font folder and the Verso font destination")
text_lab.place(x=130,y=150)

profSelect_btn = tk.Button(prof_win, text = "Select Proffie Folder", bd = '10', command=proffie_grab)
profSelect_btn.place(x = 130, y = 200)

versoSelect_btn = tk.Button(prof_win, text = "Select Verso Destination", bd = '10', command=verso_grab)
versoSelect_btn.place(x = 330, y = 200)

finish_btn = tk.Button(prof_win, text = "Convert", bd = '10', command=convert)
finish_btn.place(x = 520, y = 350)

quit_btn = tk.Button(prof_win, text = "Exit", bd = '10', command=end_program)
quit_btn.place(x = 5, y = 350)

#begins program run
prof_win.mainloop()

#still need to add option to enter the font name...
#still need to try and grab smoothswing config settings to output a config option...
