import argparse
from os import popen
import subprocess

parser = argparse.ArgumentParser(description="Transfer and update MongoDB")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("-db", dest='db', default=False, help="Database name")
parser.add_argument("-c", dest='collection', default=False, help="Collection name")
parser.add_argument("-d", dest='dest_ip', default=False, help="Destination IP")
parser.add_argument("-u", dest='username', default=False, help="Username")
args = parser.parse_args()

username = str(args.username)
dest_ip = str(args.dest_ip)
db = str(args.db)
collection = str(args.collection)


# Export db
source = "/tmp/temp.json"
cmd = 'mongoexport --db=' + db + " --collection=" + collection + " --out=" + source
print(popen(cmd).read())
print("Successfully exported DB")

# Copying the file
cmd = "sudo scp " + source + " " + username + "@" + dest_ip + ":" + source
print(popen(cmd).read())
print("Successfully copied to remote OVX")

# Run import database in remote OVX
import_script = '/home/ubuntu/import_db.py'

cmd = ['ssh', username + '@' + dest_ip, 'sudo', 'python', import_script, source]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

for line in iter(proc.stdout.readline, ''):
    print(line)

print("Successfully imported DB")












