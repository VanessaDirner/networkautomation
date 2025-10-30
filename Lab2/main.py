import os
from ping3 import ping, verbose_ping
import ping3
import ifaddr
import ipaddress
from ipaddress import IPv4Network, ip_network
import time
import json
import scapy
import threading
import concurrent.futures
import subprocess
import nmap
import traceback
from netmiko import ConnectHandler
from getpass import getpass


import getadapters
import getdevices
import connecttodevice


ip_address_combined = getadapters.adapterdetails()

getdevices(ip_address_combined)