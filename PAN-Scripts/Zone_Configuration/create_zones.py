from panos.firewall import Firewall
from panos.network import Zone
import os 
import xmltodict
from rich import print as rprint 

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
firewall_ip_list = ["192.168.0.21", "192.168.0.22", "192.168.0.23"]



def create_zone():
    name = input("What do you want the name of the zone to be?\n")
    mode = input("What type of security zone? Available: tap, virtual-wire, layer2, layer3, external\n")
    interface = list(input("What interface or interfaces do you want this security zone applied to?"))
    zone_profile = input("What zone protection profiles would you like to apply to the interface?\n")
    #log_setting = 

def create_zone_static(firewall):
    create_zone = Zone(name='example_zone', mode='layer3', enable_user_identification=False, enable_packet_buffer_protection=True)
    firewall.add(create_zone)
    create_zone.create()
    firewall.commit()
   

for firewall in firewall_ip_list:
    fw = Firewall(firewall, api_username=username, api_password=password)
    create_zone_static(fw)


