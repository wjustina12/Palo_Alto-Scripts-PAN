import requests
import os
from panos.firewall import Firewall
from panos.network import ManagementProfile
from rich import print as rprint 

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
ip_firewall = "192.168.1.4" #This can be a single firewall or multiple firewalls contained within a list

def get_int_management(uri, username, password):
    management_int = requests.get(uri, auth=(username,password), verify=False)
    management_response = management_int.json()
    return management_response

def true_convert(string):
    bool_value = bool(string)
    return bool_value

def false_convert(string):
    string = ""
    bool_value = bool(string)
    return bool_value

def create_interface_management(firewall_ip, username, password):
    firewall = Firewall(ip_firewall, api_username=username, api_password=password) 
    
    management_interface = input("What's the name of the management profile that you want to create?\n")
    http_bool = input("Do you want http enabled?\n")
    https_bool = input("Do you want https enabled?\n")
    ping_bool = input("Do you want ping enabled?\n")
    response_pages_bool = input("Do you want response pages enabled?\n")
    userid_service_bool = input("Do you want Userid_service enabled?\n")
    syslog_ssl_bool = input("Do you want userid-syslog-listener-ssl enabled?\n")
    syslog_udp_bool = input("Do you want userid-syslog-listener-udp enabled?\n")
    ssh_bool = input("Do you want ssh enabled?\n")
    telnet_bool = input("Do you want telnet enabled?\n")
    snmp_bool = input("Do you want snmp enabled?\n")
    http_ocsp_bool = input("Do you want ocsp enabled?\n")
    ip_permit = input("What ip range or IP address do you wanted admitted?\n")
    ip_list = ip_permit.split(', ')
        
    bool_dictionary = {'http':http_bool, 'https':https_bool, 'ping':ping_bool, 'response_pages':response_pages_bool, 'userid_service':userid_service_bool,
                       'userid_syslog_listener_ssl':syslog_ssl_bool, 'userid_syslog_listener_udp':syslog_udp_bool, 'ssh':ssh_bool, 'telnet':telnet_bool, 'snmp':snmp_bool,
                       'http_ocsp': http_ocsp_bool}
    
    
    for key,value in bool_dictionary.items():
        if value == 'yes':
            truth_value = true_convert(value)
            value = truth_value
            bool_dictionary[key] = value
            
        elif value == 'no':
            false_value = false_convert(value)
            value = false_value
            bool_dictionary[key] = value   

    named_interface = ManagementProfile(name=management_interface, ping=bool_dictionary['ping'], telnet=bool_dictionary['telnet'], ssh=bool_dictionary['ssh'], http=bool_dictionary['http'], http_ocsp=bool_dictionary['http_ocsp'], https=bool_dictionary['https'], snmp=bool_dictionary['snmp'], 
                                        response_pages=bool_dictionary['response_pages'], userid_service=bool_dictionary['userid_service'], userid_syslog_listener_ssl=bool_dictionary['userid_syslog_listener_ssl'], userid_syslog_listener_udp=bool_dictionary['userid_syslog_listener_udp'],
                                        permitted_ip=ip_list)

    locate_profile = firewall.find(named_interface, ManagementProfile)
    if locate_profile == None:
        firewall.add(named_interface)
        named_interface.create()
        firewall.commit()
        rprint(f"[green]{named_interface}[/green] has been successfully created!")
    if locate_profile != None:
        print(f"{named_interface} already exists")
    
    
create_interface_management(ip_firewall, username, password)
    
