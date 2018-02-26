#!/usr/bin/python
# Python 2.7.10 & 2.7.5

# update dns zone file serial number when add or update record

import re
import sys

def update_dns_zone(org_file, new_file):
    print "org_file=%s" % org_file
    print "new_file=%s" % new_file
    try:
        with open(org_file, 'r') as file:
            with open(new_file,'w') as new_file:
                for line in file:
                    if "serial" in line:
                        # \s+(\d+)(\s+)?;\sserial\s
                        the_line = re.match(r'(\s+)(\d+)(\s+)?(;\sserial\s.*)', line, re.M|re.I)
                        if the_line:
                            serial_number = "{0}".format(the_line.group(2))
                            print "original serial number=%s" % serial_number
                            print "original line=%s" % line.rstrip()
                            new_serial_number = int(serial_number) + 1
                            print "     new serial number=%s" % new_serial_number
                            if the_line.group(3) is None:
                                new_line = "{0}{1}{2}".format(the_line.group(1), new_serial_number, the_line.group(4))
                            else:
                                new_line = "{0}{1}{2}{3}".format(the_line.group(1), new_serial_number, the_line.group(3), the_line.group(4))
                                print "     new line=%s" % new_line
                            # write to new file
                            new_file.write(str(new_line))
                        else:
                            print "no serial line match!"
                    else:
                        new_file.write(str(line))
    except IOError:
        print "can not open file!"

def append_new_vm_in_dns_zone(hostname, zone_file):
    print "Check hostname %s in zone file %s" % (hostname,zone_file)

if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print "Need 3 parameters!. Quit!"
        quit()

    domain_name=""
    domain_surfix=""
    domain_prefix=""
    #org_file=str(sys.argv[1])
    #new_file=str(sys.argv[2])
    #update_dns_zone(org_file, new_file)
    append_new_vm_in_dns_zone(str(sys.argv[1]), str(sys.argv[2]))
