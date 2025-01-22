# Androholic
[Beta testing] Android bruteforcing tool for apps pentesting simulating manual user typing with adb

/!\ This tool is more a template than a complete tool as it depends on the feature you are testing.
For example, login features may unfocus the password field between each try so you will sometimes need to had Tabs keyevents...

## Disclaimer

This tool have been designed only for pentesting and to test your own apps, DO NOT USE IT ON APPS THAT YOU DOES NOT OWN!

Also, be careful when you use this tool as you risk to lock your device if the tool is running on your device pin / password

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

https://github.com/user-attachments/assets/0f407ab3-c622-4503-9b93-7c5f7db1c238


## To do

- Checks UI dynamiques






