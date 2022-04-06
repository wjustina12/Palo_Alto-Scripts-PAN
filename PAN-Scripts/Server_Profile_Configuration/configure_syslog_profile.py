from panos.firewall import Firewall
from panos.device import SyslogServer
from panos.device import SyslogServerProfile
from rich import print 
from os import getenv 

username = getenv('USERNAME')
password = getenv('PASSWORD')

with open("/home/jwilliams/Documents/Firewall_IPAddresses/Firewalls_ip.txt", 'r') as file:
    firewall_list = file.read().splitlines()

def create_syslog_server(firewall_ip, username, password):
    """This function is used to create a syslog server profile."""
    
    server_name = input("What's the name of the syslog server profile?\n")
    server_ip = input("What's IP address or FQDN of the server?\n")
    server_transport = input("What's the transport mechanism? Ex: UDP (default), TCP, or SSL are valid options \n")
    server_port = int(input("What's the port of the transport mechanism?\n"))
    server_format = input("What's the format of the syslog messages. Valid values are BSD (default (UDP)) or IETF (TCP or SSL/TLS)\n")
    server_facility = input("What's the syslog facility? Valid values are LOG_USER(default) or LOG_LOCAL0 through LOG_LOCAL7\n")
    
    syslog_server = SyslogServer(name=server_name, server=server_ip, transport=server_transport, port=server_port, format=server_format, facility=server_facility)
    firewall = Firewall(firewall_ip, api_username=username, api_password=password, vsys='vsys1')
    firewall.add(syslog_server)
    syslog_server.create()
    firewall.commit()

for fw in firewall_list:
    create_syslog_server(fw, username, password)
    
    
    