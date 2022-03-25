from panos.firewall import Firewall
from panos.network import Zone
import os
import xmltodict
from rich import print as rprint

firewall = Firewall("192.168.1.4", api_username=os.getenv('USERNAME'), api_password=os.getenv('PASSWORD'))
retrieve_zone = firewall.op("show zone-protection", xml=True)
zone_response = xmltodict.parse(retrieve_zone, dict_constructor=dict)
rprint(zone_response)
