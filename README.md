# Androholic
[Beta testing] Android bruteforcing tool for apps pentesting simulating manual user typing with adb

/!\ This tool is more a template than a complete tool as it depends on the feature you are testing.
For example, login features may unfocus the password field between each try so you will sometimes need to manually had Tabs or other keyevents in the code...

## Disclaimer

This tool have been designed only for pentesting and to test your own apps, DO NOT USE IT ON APPS THAT YOU DOES NOT OWN OR HAVE PERMISSION TO TEST!

Also, be careful when you use this tool as you risk to lock your device if the tool is running on your device pin / password

## Pre-requisites

- Python3
- adb
- Android device with developer mode activated

## Install

```
$ git clone https://github.com/mathis2001/Androholic
$ cd Androholic
$ python3 androholic.py
```

## Usage

```
$ python3 androholic.py -w wordlist.txt [-d 3] [--overlay] [--pop-up] [--semi-automatic KEYWORD] [--tabs-after-input 5]
```

## Options

```
options:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        Path to the file containing lines of text.
  -d DELAY, --delay DELAY
                        Optional delay (in seconds) between each input.
  --overwrite           Overwrite previous input between each try.
  --pop-up              clic on 'enter' if there is a pop-up between every try
  --semi-automated SEMI_AUTOMATED
                        If the pop-up need multiple 'enter' keypress, give a word from the error message.
  --tabs-after-input TABS_AFTER_INPUT
                        If the focus is losed after the text/code is typed, Number of tabs needed to focus on the validation button.
```

## Screenshots and records

https://github.com/user-attachments/assets/46dcfc58-bb91-4ca5-b897-49527897ffed

https://github.com/user-attachments/assets/0f407ab3-c622-4503-9b93-7c5f7db1c238


## To do

- More Dynamic checks
- Alternative to the uiautomator dump check (faster alternative)






