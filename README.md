# Androholic
[Beta testing] Android bruteforcing tool simulating manual user typing with adb

/!\ This tool is more a tamplate than a complete tool as it depends on the feature you are testing.
For example, login features may unfocus the password field between each try so you will sometimes need to had Tabs keyevents...

## Disclaimer

This tool have been designed only for pentesting and private usage!

## Install

```
$ git clone https://github.com/mathis2001/Androholic
$ cd Androholic
$ python3 androholic.py
```

## Usage

```
$ python3 androholic.py -w wordlist.txt [-d 3] [--overlay] [--pop-up]
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
```

## Screenshots and records

https://github.com/user-attachments/assets/46dcfc58-bb91-4ca5-b897-49527897ffed

## To do

- Checks UI dynamiques
