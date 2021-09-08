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

#FUNCTIONS TO BE USED
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
            shutil.copy(full_name, verso_path)
        elif filename.__contains__('.'):
            continue
        else:
            new_folder = path1 + '/' + filename
            copy_wavs(new_folder)
    
def rename(): #functional
    global verso_path
    for filename in os.listdir(verso_path):
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

def open_final():
    path = verso_path
    path = os.path.realpath(path)
    os.startfile(path)

#main:
proffie_path = requestDestination(proffie_path) #grabs the proffie folder
verso_path = requestDestination(verso_path) #grabs verso destination
verso_path = verso_path + '/Verso_' + font_name() #creates new font name
os.mkdir(verso_path) #makes new font folder in destination
copy_wavs(proffie_path) #copies audio files over
rename() #renames all files properly
stitch() #properly stitches bgnlock with lock to create proper lockup sound for verso
open_final()
#now to make stuff for the config file!