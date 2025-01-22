#!/usr/bin/env python3

import os
import argparse
import time
import sys


class bcolors:
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'

parser = argparse.ArgumentParser(description="Send lines from a file as input via ADB.")
parser.add_argument('-w', '--wordlist', required=True, help="Path to the file containing lines of text.")
parser.add_argument('-d', '--delay', type=float, help="Optional delay (in seconds) between each input.")
parser.add_argument('--overwrite', help="Overwrite previous input between each try.", action="store_true")
parser.add_argument('--pop-up', help="clic on 'enter' if there is a pop-up between every try", action='store_true')
parser.add_argument('--semi-automated', help="If the pop-up need multiple 'enter' keypress, give a word from the error message.")
parser.add_argument('--tabs-after-input', type=int, help="Number of tabs after the input")
args = parser.parse_args()

def banner():
    print('''
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░        
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░   by S1rN3tZ
                                                                                                                             
                                                                                                                             

''')

def display_typing_animation():
    for dots in range(1, 4):
        sys.stdout.write(f"\rTyping{'.' * dots} ")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\r")
    sys.stdout.flush()

def is_pop_up_displayed(keyword):
    os.system("adb shell uiautomator dump /sdcard/view.xml")
    UI_data = os.popen(f"adb shell cat /sdcard/view.xml").read()
    time.sleep(1)
    if keyword in UI_data:
        return True
    else:
        return False

def keycode_tab(number):
    for _ in range(number):
        os.system("adb shell input keyevent KEYCODE_TAB")

def main():
    file_path = args.wordlist
    dots = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        display_typing_animation()
        newline = line.strip()
        previous_line = len(newline)
        os.system(f"adb shell input text \"{newline}\"")
        if args.tabs_after_input:
            keycode_tab(args.tab_after_input)
        os.system("adb shell input keyevent 66")

        if args.delay:
            time.sleep(args.delay)

        if args.pop_up:
            for _ in range(args.pop_up):
                os.system("adb shell input keyevent 66")
        
        if args.semi_automated:
            while is_pop_up_displayed(args.semi_automated):
                os.system("adb shell input keyevent 66")
            else:
                pass  
            

        if args.overwrite:
            os.system("adb shell input keyevent KEYCODE_MOVE_END")
            for _ in range(previous_line):
                os.system("adb shell input keyevent KEYCODE_DEL")
                

try:
        banner()
        main()
        print(bcolors.INFO+"[*] "+bcolors.RESET+"Script finished.")
except Exception as e:
        print(e)
except KeyboardInterrupt:
        print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")
