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
parser.add_argument('-d', '--delay', type=float, default=0, help="Optional delay (in seconds) between each input.")
parser.add_argument('--overwrite', help="Overwrite previous input between each try.", action="store_true")
parser.add_argument('--pop-up', help="clic on 'enter' if there is a pop-up between every try", action="store_true")
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
        time.sleep(0.1)
    sys.stdout.write("\r")
    sys.stdout.flush()

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
        os.system("adb shell input keyevent 66")

        if args.delay > 0:
            time.sleep(args.delay)

        if args.pop_up:
            os.system("adb shell input keyevent 66")

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
