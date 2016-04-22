import nmap
from sender import MessageSender
from receiver import Client,Receiver

class NMAPUtil:
	def get_active_ips(self):
		nm = nmap.PortScanner()

		nm.scan(hosts='10.0.0.0/24', arguments='-n -sP')

		hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

		active_ips = set()
		for host, status in hosts_list:
			if str(status).lower() == "up":
				active_ips.add(host)

		return active_ips
