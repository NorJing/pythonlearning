# python2.7

import pycurl
from StringIO import StringIO

def extract_vm_info(source, destination):
    try:
        with open(source, 'r') as file:
            with open(destination, 'w') as new_file:
                for line in file:
                    if "," in line:
                        vm_name = line.split(",")[0]
                        status = line.split(",")[2]
                        print "%s;%s" % (vm_name,status)
                        new_line = "{0};{1}{2}".format(vm_name,status,"\n")
                        new_file.write(new_line)
    except IOError:
        print "can not open file 2"
    
if __name__ == '__main__':
    source = "vmrapport.csv"
    source1 = "vmrapport1.csv"
    destination = "short_vm_info.csv"
    
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://somewhere.com/diskrapport/vmrapport.csv')
    c.setopt(pycurl.USERPWD, "username:password")
    c.setopt(c.WRITEDATA, buffer)
    try:
        c.perform()
    except pycurl.error:
        print pycurl.error
    body = buffer.getvalue()
    c.close()
    print(body)
    try:
        with open(source1, 'w') as file:
            file.write(body)
    except IOError:
        print "can not open file 1"
    extract_vm_info(source1, destination)
