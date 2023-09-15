"""
Welcome to the Nmap optimizer!
The main goal of this script is to run two separate scans and make it simpler for the user.
The first scan gets all the open port numbers.
The second scan runs a more thorough scan against each port individually.
If you want to change either scan, modify either command in the second or third function.
"""


import subprocess
import re
import multiprocessing
import time

def extract_ports(result):
    return re.findall(r'(\d{1,5})/tcp\s+open', result)

def nmap_scan_ports(ip):
    command = f'nmap -T5 -p- {ip}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    return result.stdout

def nmap_scan_port(args):
    ip, port = args
    command = f'nmap -T5 -sV -sC -O -p {port} {ip}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    return result.stdout

# Ask the user for an IP address
ip_address = input("Enter the IP address to scan: ")

# Record start time
start_time = time.time()

# Run initial scan to get open ports
print("Running initial scan...")
result_ports = nmap_scan_ports(ip_address)
print(result_ports)

# Extract port numbers using regular expression
open_ports = extract_ports(result_ports)

# Perform detailed scan for each open port in parallel
print("Scanning open ports...")
with multiprocessing.Pool() as pool:
    results = pool.map(nmap_scan_port, [(ip_address, port) for port in open_ports])

# Print the results
for result in results:
    print(result)

# Calculate and print elapsed time
end_time = time.time()
