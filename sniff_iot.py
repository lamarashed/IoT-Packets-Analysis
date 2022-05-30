'''
authors: Lama, Lin

 1- Capture specific device traffic ( by mac address or ip address )
 2- Save pcap file
 3- Convert pcap file into flow file using tranalyzer
 4- Import trained ml learning with the specicifc features 
 5- Predict the flow file using the ml learning
 
'''
from scapy.all import *
import sys
import argparse
from t2py import T2Utils
import tranalyzer
import dhcp_dns
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
 # plug : dc:4f:22:8d:b5:07 and 192.168.2.3
 # camera e4:26:86:f2:ef:b7  and  192.168.2.7
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--devname", help="Enter the name of the device", default="example")
    parser.add_argument("--devid", help="Enter MAC address of the device", default="example")
    args = parser.parse_args()
    args = vars(parser.parse_args())
    dev_name = args["devname"]
    dev_id = args["devid"]


    try: 
        filter = "ip src "+dev_id+""
        capture = sniff(filter=filter, timeout=1800,  iface="en0")
        name = dev_id + ".pcap"
        wrpcap(name,capture)
        dhcp_dns.DHCP_profile(name)
        dhcp_dns.domain_name(name)
        tranalyzer.convert_pcap(name)
    except Exception as e:
        print("[ERROR] Sniffer File: " + e)
