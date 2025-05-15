#!/usr/bin/env python3

import os
import argparse
import time
import sys
from colorama import Fore, Style, init

KEY_CODES = {
    "TABULATION": "KEYCODE_TAB",
    "ENTER": "66",
    "MOVE_END": "KEYCODE_MOVE_END",
    "DEL": "KEYCODE_DEL"
}

init()

parser = argparse.ArgumentParser(description="Send lines from a file as input via ADB.")
parser.add_argument('-w', '--wordlist', required=True, help="Path to the file containing lines of text.")
parser.add_argument('-d', '--delay', type=float, help="Optional delay (in seconds) between each input.")
parser.add_argument('--overwrite', help="Overwrite previous input between each try.", action="store_true")
parser.add_argument('--pop-up', help="Clic on 'Enter' if there is a pop-up between every try", action='store_true')
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
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░   
                                                        by S1rN3tZ
                                                                                                                             
''')


def is_pop_up_displayed(keyword):
    os.system("adb shell uiautomator dump /sdcard/view.xml")
    ui_data = os.popen(f"adb shell cat /sdcard/view.xml").read()
    os.system("adb shell rm /sdcard/view.xml")
    return keyword in ui_data


def input_key(key, times=1):
    for _ in range(times):
        os.system(f"adb shell input keyevent {key}")


def main():

    with open(args.wordlist, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        previous_line = None

        for line in lines:            
            print(f"{Fore.WHITE}[*] Writing input to device: \"{line}\"{Style.RESET_ALL}")
            os.system(f"adb shell input text \"{line}\"")
            
            if args.tabs_after_input:
                input_key(KEY_CODES['TABULATION'], args.tab_after_input)
            
            # Press ENTER to validate form
            input_key(KEY_CODES['ENTER'])            

            if args.delay:
                time.sleep(args.delay)

            # Press ENTER if pop-up appeared
            if args.pop_up:
                input_key(KEY_CODES['ENTER']) 
            
            if args.semi_automated:
                count = 0
                while is_pop_up_displayed(args.semi_automated):
                    input_key(KEY_CODES['ENTER']) 
                    count += 1

                    if count == 10:
                        print(f"{Fore.RED}[!] Pressed ENTER {count} times. Something seems to be wrong.{Style.RESET_ALL}")
                        break
                

            if args.overwrite and previous_line:
                # Move at the end of the input
                input_key(KEY_CODES['MOVE_END']) 
                # Delete previous x caracters 
                input_key(KEY_CODES['DEL'], len(previous_line))
               
            previous_line = line
                    

if __name__ == "__main__":
    try:
        banner()
        main()
        print(f"{Fore.BLUE}[>] Script finished...{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[!] An error occured...{Style.RESET_ALL}", e)

    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}[>] Script canceled...{Style.RESET_ALL}")
