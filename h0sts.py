#!/usr/bin/python3

import re
import sys
import os
import time
import random
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)

# DEFINE DAT MAIN, BRUH
def main():
    print("What would you like to do?")
    watcha_doin()

# MAKE A CHOICE FOOL
def watcha_doin():
    options = {'1.': 'Add' , '2.': 'Delete', '3.': 'Update', '4.': 'Exit'}
    for k,v in options.items():
        print(f"{k} {v}")
    uinput = str(input("Choose:"))
    if uinput == '1' or uinput == 'Add' or uinput == 'add':
        get_hosts()
        add_host()
    elif uinput == '2' or uinput == "Delete" or uinput == 'del':
        del_host()
    elif uinput == '3' or uinput == 'Update' or uinput == 'up':
        print("gatcha3")
        #update_hosts()
        exit()
    elif uinput == '4' or uinput == 'Exit' or uinput == 'ex':
        print("\nK, thx, bb!!\n")
        exit()
    elif uinput == '5':
        get_rando()
        main()
    else:
        get_mrT()
        print("Enter a valid option, mmmm ice cream, yum yum!")
        time.sleep(1)
        main()

#GET DEM DIGITS, BRUH
def get_hosts():
    #/ETC/HOSTS CURRENT CONTENTS, MY DUDE
    with open("hosts.temp", 'r', encoding="utf-8") as file:
        hostfile = file.read()
        lines = re.split(r'\n', hostfile)
#        for i in lines:                                        #test print to read ASCII ouput
#            print(f'{i}')
        file.close()
        s_pattern = re.compile(r'([\da-fA-F.:]+)\s+([^\n]+)?')
        match_index = s_pattern.findall(hostfile)
#       print(match_index)
        match_dict = dict(match_index)
#       print(match_dict)
        ips = match_dict.keys()
        domains = match_dict.values()
        print('\n',"Here's the current list of hosts:")
        count = 0
        table = PrettyTable()
        table.field_names = [Fore.RED + "Line" + Style.RESET_ALL,Fore.BLUE + "IP" + Style.RESET_ALL, Fore.BLUE + "Domain(s)" + Style.RESET_ALL]
        for ips,domains in match_dict.items():
            count += 1
            table.add_row([Fore.RED + str(count) + Style.RESET_ALL,Fore.WHITE + ips + Style.RESET_ALL, Fore.WHITE + domains + Style.RESET_ALL])
        print(table)

#ADD THEM DIGITS, YEET!
def add_host():
    print(f"\n Enter IP")
    ip = input("IP:")
    pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    match = pattern.match(ip)
    if not match:
        get_mrT()
        print("Use the standard IPv4 format!")
        add_host()
    else:
        hostname = input(f"Hostname(s):")
        with open("hosts.temp", mode="a") as file:
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
    with open('hosts.temp', 'r', encoding = 'utf-8') as hosts:
        content = hosts.read()
        hosts.close()
        #print(lines[0])
        s_pattern = re.compile(r'([\da-fA-F.:]+)\s+([^\n]+)?')
        match_index = s_pattern.findall(content)
        #print(match_index)
        match_dict = dict(match_index)
        #print(match_dict)
        ips = match_dict.keys()
        #print(ips)
        domains = match_dict.values()
        #print(domains)
        user_input = input('Remove which line entry?')
        index = int(user_input) -1
        if 0 <= index < len(match_index): 
            print('\n','Removing entry',user_input,'\n','Is this correct?','\n',match_index[index])
        elif index != int:
            get_mrT()
            print('Index does not exist. Use 1 though',len(match_index))
            time.sleep(1)
            del_host()
        confirm = str(input('(y) or (n)?'))
        if confirm == 'n':
            print("Let's try that again...")
            time.sleep(1)
            del_host()
        elif confirm == 'y':
            del match_index[index]
            try:
                with open('hosts.temp', mode = 'w', encoding = 'UTF-8') as file:
                    for k,v in match_index:
                        if len(k) > 7:
                            file.write(f'{k}\t{v}\n')
                        else:
                            file.write(f'{k}\t\t{v}\n')
                print("/etc/hosts sucessfully updated")
            except PermissionError:
                print("Please run the updater with sudo priveleges.")
            except Exception as e:
                print(f"Error, please run the updater again: {e}")
                file.close()
        get_hosts()
        main()

# LEMME GET DEM LULZ, BRUH
def get_rando():
    rando = ["lul1.txt", "lul2.txt", "lul3.txt", "lul4.txt", "lul5.txt",
             "lul6.txt", "lul7.txt", "lul8.txt", "lul9.txt", "lul10.txt",
             "lul11.txt","lul12.txt", "lul13.txt", "lul14.txt", "lul15.txt",
             "lul16.txt", "lul17.txt", "lul18.txt", "lul19.txt"]
    random_lulz = random.choice(rando)
    with open(random_lulz, mode='r') as file:
        for lulz in file:
            lulz = lulz.rstrip()
            print(lulz)


# I PITTY THE FOOL!
def get_mrT():
    with open('mrt.txt', mode='r') as file:
        for tea in file:
            tea = tea.rstrip()
            print(tea)


# JUST MY MAIN, BRUH
if __name__ == "__main__":
    get_rando()
    main()
