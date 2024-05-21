import gzip
import os
import csv

# Function to load IP addresses from a CSV file
def load_ip_addresses_from_csv(csv_file):
    ip_addresses = set()
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) >= 1:  # Check if the row is not empty and contains at least one element
                    ip_addresses.add(row[0])
    except FileNotFoundError:
        print("CSV file not found:", csv_file)
    return ip_addresses

# Function to extract IP addresses from CloudWatch logs- Expecting VPC-flowlogs file names are prefixed with 'eni' and ends with -all and with .gz extension as standrad export from cloudwatch to S3.
def extract_ip_addresses_from_logs(log_dir):
    ip_addresses = set()
    for subdir in os.listdir(log_dir):
        subdir_path = os.path.join(log_dir, subdir)
        if os.path.isdir(subdir_path):
            for filename in os.listdir(subdir_path):
                if filename.endswith(".gz"):
                    with gzip.open(os.path.join(subdir_path, filename), 'rt') as file:
                        for line in file:
                            elements = line.strip().split()
                            if len(elements) >= 6:
                                src_ip = elements[4]
                                packet_status = elements[13]
                                # dest_ip = elements[5]
                                if packet_status == "ACCEPT":
                                    if src_ip:
                                       ip_addresses.add(src_ip)
                                  
    return ip_addresses


csv_file = 'ip_addresses_test.csv' 
log_dir = './data1/'
csv_ip_addresses = load_ip_addresses_from_csv(csv_file)
log_ip_addresses = extract_ip_addresses_from_logs(log_dir)
unmatched_ip_addresses = log_ip_addresses - csv_ip_addresses

# Function to export IP addresses to a file
def export_ip_addresses(ip_addresses, output_file):
    with open(output_file, 'w') as file:
        for ip_address in ip_addresses:
            file.write(ip_address + '\n')
    print("IP addresses exported to:", output_file)

# getting unmatched_ip list 
output_file_unmatched = 'unmatched_ip_addresses.txt'
export_ip_addresses(unmatched_ip_addresses, output_file_unmatched)

# getting logged_ip list
log_output_file = 'logged_ip_addresses.txt'
export_ip_addresses(log_ip_addresses, log_output_file)

#print("Logged IP addresses:", log_ip_addresses)
