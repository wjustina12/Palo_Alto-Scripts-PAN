from panos.firewall import Firewall
from panos.network import Zone
import os 
import xmltodict
from rich import print as rprint 

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
firewall_ip = "192.168.1.4"

firewall = Firewall(firewall_ip, api_username=username, api_password=password)

def create_zone():
    name = input("What do you want the name of the zone to be?\n")
    mode = input("What type of security zone? Available: tap, virtual-wire, layer2, layer3, external\n")
    interface = list(input("What interface or interfaces do you want this security zone applied to?"))
    zone_profile = input("What zone protection profiles would you like to apply to the interface?\n")
    log_setting = 
    
