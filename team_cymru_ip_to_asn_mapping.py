#!/usr/bin/python3

import os
import sys
import time
import subprocess
import ipaddress

# Team Cymru IP to ASN Mapping through 'netcat' (bulk use - few thousand per bulk use to minimize overall load as noted by the team cymru doc page).
# Set output filename to include date+time
date = time.strftime("%m-%d-%Y_%H:%M:%S")
output_file = date + "_output_ip_list.txt"
error_file = "NOT_EXPECTED_COLUMN_COUNT_" + date

# Place output into list
tc_output_list = subprocess.getoutput("netcat whois.cymru.com 43 < " + sys.argv[1]).splitlines()
# Skip first line of netcat output which is the following: 'Bulk mode; whois.cymru.com [2020-05-13 21:08:56 +0000]'
for tc_record in tc_output_list[1:]:
    # Format of Output: ASN, IP, CIDR, CC, Registry, Allocated, AS Name
    tc_record = " ".join(tc_record.split()).replace(' | ','#~#')
    # Verify there's an expected amount of columns (6).
    counted_columns = tc_record.count("#~#")
    if counted_columns == 6:
        asn = tc_record.split('#~#')[0]
        ip = tc_record.split('#~#')[1]
        cidr = tc_record.split('#~#')[2]
        cc = tc_record.split('#~#')[3]
        registry = tc_record.split('#~#')[4]
        allocated = tc_record.split('#~#')[5]
        as_name = tc_record.split('#~#')[6]

        # Requested to convert CIDR into IP Range - from '68.22.187.0/24' to the following format: '68.22.187.0#~#24#~#68.22.187.255'
        cidr_tail = cidr.split('/')[1]
        cidr = ipaddress.ip_network(cidr)
        cidr = '%s#~#%s#~#%s' % (cidr[0], cidr_tail, cidr[-1])

        # Test prints
        '''
        print ("ASN: " + asn)
        print ("IP: " + ip)
        print ("CIDR: " + cidr)
        print ("CC: " + cc)
        print ("Registry: " + registry)
        print ("Allocated: " + allocated)
        print ("AS Name: " + as_name)
        print ('%s#~#%s#~#%s#~#%s#~#%s#~#%s#~#%s' % (asn, ip, cidr, cc, registry, allocated, as_name) + '\n')
        '''
        #Append to Output File
        with open(output_file, 'a') as f:
            f.write('%s#~#%s#~#%s#~#%s#~#%s#~#%s#~#%s' % (asn, ip, cidr, cc, registry, allocated, as_name) + '\n')
    else:
        # If there's for some reason an unexpected number of columns (greater/lower than 6), the above parser would be inaccurate and need to analyze the given IP's output and update the script accordingly.
        with open(error_file, 'a') as error_f:
            error_f.write(tc_record + '\n')
