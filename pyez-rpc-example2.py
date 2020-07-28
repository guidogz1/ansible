from jnpr.junos import Device
from lxml import etree
from getpass import getpass
import sys

hostname = raw_input("Hostname: ")
junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS password: ")

with Device(hostname) as dev:   
    #invoke the RPC equivalent to "show version"
    sw = dev.rpc.get_software_information()
    print(etree.tostring(sw, encoding='unicode'))
