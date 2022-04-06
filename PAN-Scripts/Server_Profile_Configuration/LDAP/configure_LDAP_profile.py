from panos.firewall import Firewall
from panos.device import LdapServerProfile
from os import getenv
from rich import print
import xmltodict


firewall_list = ["192.168.0.21", "192.168.0.22", "192.168.0.23"]
username = getenv("USERNAME")
password = getenv("PASSWORD")

def create_ldap_server(firewall_ip, username, password):
    
    
# for firewall in firewall_list:
#     fw = Firewall(firewall, api_username=username, api_password=password)

