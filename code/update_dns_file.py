#!/usr/bin/python
# Python 2.7.10

# update dns zone file serial number when add or update record

import re

try:
    with open('zone.file.2', 'r') as file:
        with open('zone.file.22','w') as new_file:
            for line in file:
                if "serial" in line: 
                    # \s+(\d+)\s+;\sserial,\s
                    the_line = re.match(r'(\s+)(\d+)(\s+;\sserial,\s.*)', line, re.M|re.I)
                    if the_line:
                        serial_number = "{0}".format(the_line.group(2))
                        print serial_number
                        print line.rstrip()
                        new_serial_number = int(serial_number) + 1
                        print "new serial number=%s" % new_serial_number
                        new_line = "{0}{1}{2}".format(the_line.group(1), new_serial_number, the_line.group(3))
                        print new_line                        
                        # write to new file
                        new_file.write(str(new_line + '\n'))
                else:
                    new_file.write(str(line))
except IOError:
    print("can not open")
