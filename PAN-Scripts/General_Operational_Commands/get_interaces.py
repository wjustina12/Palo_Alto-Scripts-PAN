from panos.firewall import Firewall
import xmltodict
import os
from rich import print as rprint 

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
firewall_ip = "192.168.1.4"

def get_interfaces(ip, username, password):
    firewall = Firewall(ip, api_username=username, api_password=password)
    interface_request = firewall.op('show interface "all"', xml=True)
    interface_response = xmltodict.parse(interface_request, dict_constructor=dict)
    rprint(interface_response)

get_interfaces(firewall_ip, username, password)
    