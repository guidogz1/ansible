from jnpr.junos import Device
from lxml import etree

with Device(host='10.1.99.9') as dev:   
    #invoke the RPC equivalent to "show version"
    sw = dev.rpc.get_software_information()
    print(etree.tostring(sw, encoding='unicode'))
