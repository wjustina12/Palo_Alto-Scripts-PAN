from panos.firewall import Firewall
import os
import xmltodict
from rich import print as rprint 

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

firewall_ip = Firewall("192.168.1.4", api_username=username, api_password=password)

info_response = firewall_ip.op("show system info", xml=True)
xml_response = xmltodict.parse(info_response, dict_constructor=dict)
rprint(xml_response)


    
    
