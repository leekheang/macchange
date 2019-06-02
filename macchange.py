#!/usr/bin/env python
import subprocess
import optparse 
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="New Mac address")
    (options, arguments )= parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please spacify an interface, use --help for more info.")
    elif not options.mac:
        parser.error("[-] Please spacify a new mac , use --help for more info")
    
    return options

def change_mac(interface, mac):
    print("[+] Change MAC address for "+ interface + " to " + mac)
    subprocess.call(["sudo","ifconfig", interface ,"down"])
    subprocess.call(["sudo","ifconfig", interface ,"hw" ,"ether", mac ])
    subprocess.call(["sudo","ifconfig", interface ,"up"])

options = get_arguments()
change_mac(options.interface, options.mac)

ifconfig_result = str(subprocess.check_output(["ifconfig", options.interface]))
print(ifconfig_result) 


mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if mac_address_search_result:
    print("\n\n"+ mac_address_search_result.group(0))
else: 
    print("[-] Could not read MAC address.")    
