#!/usr/bin/env python

# Run in python 2.6, 2.7
import os

old_ftp_volume = "prod-ecom-d0075:/vol/fnr_pointcarbonproddtc_snap/ftpdata /data/ftp nfs rw,bg,hard,intr,tcp,nfsvers=3,rsize=32768,wsize=32768"
old_ftp_volume_short = "prod-ecom-d0075:/vol/fnr_pointcarbonproddtc_snap/ftpdata"
new_ftp_volume = "cpsprod-d0010:/cb0628_fnr_pointcarbonproddtc_snap/ftpdata /data/ftp nfs rw,bg,hard,intr,tcp,nfsvers=3,rsize=32768,wsize=32768"

old_raw_volume="prod-ecom-d0075:/vol/fnr_pointcarbonproddtc_snap/dsdata /data/raw nfs rw,bg,hard,intr,tcp,nfsvers=3,rsize=32768,wsize=32768"
old_raw_volume_short = "prod-ecom-d0075:/vol/fnr_pointcarbonproddtc_snap/dsdata"
new_raw_volume="cpsprod-d0010:/cb0628_fnr_pointcarbonproddtc_snap/dsdata /data/raw nfs rw,bg,hard,intr,tcp,nfsvers=3,rsize=32768,wsize=32768"

def comment_and_append_volume(old_volume, new_volume):
    if os.path.exists("/data/ftp") or os.path.exists("/data/raw"):
        print "/data/ftp or /data/raw exists"

        with open("/etc/fstab", 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if line.rstrip("\n").startswith(old_volume):
                    # comment the old volume
                    f.write(line.replace(line, "#" + line))
                    # add new volume
                    if not lines.__contains__(new_volume + "\n"):
                        f.write(new_volume + "\n")
                else:
                    f.write(line)

if __name__ == '__main__':
    comment_and_append_volume(old_ftp_volume_short, new_ftp_volume)
    comment_and_append_volume(old_raw_volume_short, new_raw_volume)
