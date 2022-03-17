from panos.firewall import Firewall
import xmltodict
import os
from rich import print as rprint 

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
firewall_ip = "192.168.1.4"

def show_environment(firewall_ip):
    firewall = Firewall(firewall_ip, api_username=username, api_password=password)
    env_response = firewall.op("show system environmentals", xml=True)
    xml_response = xmltodict.parse(env_response, dict_constructor=dict)
    rprint(xml_response)

show_environment(firewall_ip)