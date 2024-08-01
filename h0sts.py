#!/usr/bin/python3

# Author: Cyb3rW1ll
# Created: 5/24/2023
# Revised: 8/1/2024
# UPDATES ARE CURRENTLY UNDER DEV WITH OTHER FIXES AS WELL

import re
import sys
import os
import time
import random
import shutil
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)

# DEFINE DAT MAIN, BRUH
def main():
    print(f"What would you like to do?")
    watcha_doin()
# THIS WILL BACKUP THE CURRENT /ETC/HOSTS ONLY ON INTIAL EXECUTION
def backup_hosts():
    original = '/etc/hosts'
    backup = '/etc/hosts.backup'
    if os.path.exists(original):
        shutil.copy2(original, backup)
        time.sleep(1)
        print(f'{original} backed up to {backup}.')
    else:
        print(f'Source file {original} does not exist. No backup created.')

# MAKE A CHOICE FOOL (WITH A SECRECT BUILT IN!!!)
def watcha_doin():
    options = {'1.': 'Add' , '2.': 'Delete', '3.': 'Update', '4.': 'Exit'}
    for k,v in options.items():
        print(f'{k} {v}')
    uinput = str(input("Choose:"))
    if uinput == '1' or uinput == 'Add' or uinput == 'add' or uinput == 'a' or uinput == 'A':
        get_hosts()
        add_host()
    elif uinput == '2' or uinput == 'Delete' or uinput == 'del' or uinput == 'd' or uinput == 'D':
        del_host()
    elif uinput == '3' or uinput == 'Update' or uinput == 'up' or uinput == 'u' or uinput == 'U':
        update_hosts()
    elif uinput == '4' or uinput == 'Exit' or uinput == 'ex' or uinput == 'e' or uinput == 'E':
        print(f'\nK, thx, bb!!\n')
        exit()
    elif uinput == '5':
        get_rando()
        main()
    else:
        get_mrT()
        print(f'Enter a valid option, mmmm ice cream, yum yum!')
        time.sleep(1)
        main()

# GET DEM DIGITS, BRUH
def get_hosts():
    #/ETC/HOSTS CURRENT CONTENTS, MY DUDE
    with open('/etc/hosts', mode='r') as file:
        hostfile = file.read()
        lines = re.split(r'\n', hostfile)
        file.close()
        s_pattern = re.compile(r'([\da-fA-F.:]+)\s+([^\n]+)?')
        match_index = s_pattern.findall(hostfile)
        match_dict = dict(match_index)
        ips = match_dict.keys()
        domains = match_dict.values()
        print(f'\n',"Here's the current list of hosts:")
        count = 0
        table = PrettyTable()
        table.field_names = [Fore.RED + 'No.' + Style.RESET_ALL,Fore.BLUE + 'IP' + Style.RESET_ALL, Fore.BLUE + 'Domain(s)' + Style.RESET_ALL]
        for ips,domains in match_dict.items():
            count += 1
            table.add_row([Fore.RED + str(count) + Style.RESET_ALL,Fore.WHITE + ips + Style.RESET_ALL, Fore.WHITE + domains + Style.RESET_ALL])
        print(table)

# ADD THEM DIGITS, YEET!
def add_host():
    print(f'\n Enter IP')
    ip = input(f'IP:')
    pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    match = pattern.match(ip)
    if not match:
        get_mrT()
        print(f"Use the standard IPv4 format!")
        add_host()
    else:
        hostname = input(f'Hostname(s):')
        with open('/etc/hosts', mode='a') as file:
            if len(ip) > 7:
                file.write(f'{ip}\t{hostname}\n')
                file.close()
            else:
                file.write(f'{ip}\t\t{hostname}\n')
                file.close()
        get_hosts()
    main()

# DELETE HOST ENTRIES
def del_host():
    get_hosts()
    with open('/etc/hosts', mode='r') as hosts:
        content = hosts.read()
        hosts.close()
        s_pattern = re.compile(r'([\da-fA-F.:]+)\s+([^\n]+)?')
        match_index = s_pattern.findall(content)
        user_input = input('Remove which line entry?')
        index = int(user_input) -1
        if 0 <= index < len(match_index): 
            print(f'\n','Removing entry',user_input,'\n','Is this correct?','\n',match_index[index])
        elif index != int:
            get_mrT()
            print(f'Index does not exist. Use 1 though',len(match_index))
            time.sleep(1)
            del_host()
        confirm = str(input('(y) or (n)?'))
        if confirm == 'n':
            print(f"Let's try that again...")
            time.sleep(1)
            del_host()
        elif confirm == 'y':
            del match_index[index]
            try:
                with open('/etc/hosts', mode='w') as file:
                    for k,v in match_index:
                        if len(k) > 7:
                            file.write(f'{k}\t{v}\n')
                        else:
                            file.write(f'{k}\t\t{v}\n')
                print(f'/etc/hosts sucessfully updated')
            except PermissionError:
                print(f'Please run the updater with sudo priveleges.')
            except Exception as e:
                print(f'Error, please run the updater again: {e}')
                file.close()
        get_hosts()
        main()

# GOTTA UPDATE THOSE HOSTS!!!
def update_hosts():
    get_hosts()
    with open('/etc/hosts', mode='r') as file:
        contents= file.read()
        entries = re.split(r'[\n]', contents)
        search = re.compile(r'([^\s]+)')
        sublist = []
        for i in entries:
            matches = search.findall(i)
            if matches:
                sublist.append(matches)
        get_index = input("Which entry number do you need to update?")
        entry = int(get_index)-1
        count = 0
        for i in sublist[entry]:
            count += 1
            print(f'{count}. {i}')
        user_choice = input("Which entry would you like to update?")
        choice = int(user_choice)-1
        if 0 <= choice < len(sublist[entry]):
            update_entry = input("Please enter your update: ")
            sublist[entry][choice] = update_entry
            get_hosts()
        else:
            print("That is not a valid entry. Please try again.")
            time.sleep(1)
            update_hosts()
        try:
            with open('/etc/hosts', mode='w') as file:
                for i in sublist:
                    ip = i[0]
                    host = i[1:]
                    if len(ip) > 7:
                        file.write(f"{ip}\t{' '.join(host)}\n")
                    else:
                        file.write(f"{ip}\t\t{' '.join(host)}\n")
                    print(f'/etc/hosts sucessfully updated')
        except PermissionError:
            print(f'Please run the updater with sudo priveleges.')
        except Exception as e:
            print(f'Error, please run the updater again: {e}')
            file.close()
    get_hosts()
    main()

# LEMME GET DEM LULZ, BRUH
def get_rando():
    rando = ['/usr/local/bin/lul/lul1.txt', '/usr/local/bin/lul/lul2.txt', '/usr/local/bin/lul/lul3.txt', '/usr/local/bin/lul/lul4.txt', '/usr/local/bin/lul/lul5.txt',
             '/usr/local/bin/lul/lul6.txt', '/usr/local/bin/lul/lul7.txt', '/usr/local/bin/lul/lul8.txt', '/usr/local/bin/lul/lul9.txt', '/usr/local/bin/lul/lul10.txt',
             '/usr/local/bin/lul/lul11.txt','/usr/local/bin/lul/lul12.txt', '/usr/local/bin/lul/lul13.txt', '/usr/local/bin/lul/lul14.txt', '/usr/local/bin/lul/lul15.txt',
             '/usr/local/bin/lul/lul16.txt', '/usr/local/bin/lul/lul17.txt', '/usr/local/bin/lul/lul18.txt', '/usr/local/bin/lul/lul19.txt', '/usr/local/bin/lul/mrt.txt']
    random_lulz = random.choice(rando)
    with open(random_lulz, mode='r') as file:
        for lulz in file:
            lulz = lulz.rstrip()
            print(lulz)

# I PITTY THE FOOL!
def get_mrT():
    with open('/usr/local/bin/lul/mrt.txt', mode='r') as file:
        for tea in file:
            tea = tea.rstrip()
            print(tea)

# JUST MY MAIN, BRUH
if __name__ == '__main__':
    backup_hosts()
    get_rando()
    main()
