#!/usr/bin/python

from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


CORES = {
  's1': {'dpid': '000000000000010%s'},
  's2': {'dpid': '000000000000020%s'},
  's3': {'dpid': '000000000000030%s'},
  's4': {'dpid': '000000000000040%s'},
 
  
}

class myTopo(Topo):
	def __init__(self, k=5, **opts):
	
	
		super(myTopo, self).__init__(**opts)
		self.k=k

		lastSwitch = None 
		for i in range(1 , k):
			#m = CORES[s%s,% i]['dpid'][4:]% i 
			host =self.addHost('h%s' %i)

			switch =self.addSwitch('s%s' %i,dpid=(CORES['s%s' %i]['dpid'] % '0'))
			self.addLink( host, switch)
			if lastSwitch:
				self.addLink( switch, lastSwitch)
			lastSwitch =switch

if __name__ == '__main__':
	topo = myTopo(k=5)
	ip = '192.168.241.140'
	port = 6633
	c = RemoteController('c', ip=ip, port=port)
	
	net = Mininet(topo=topo, autoSetMacs=True, xterms=False, controller=None)
	net.addController(c)
	net.start()
	print "Hosts configured with IPs, switches pointing to OpenVirteX at %s:%s" % (ip, port)
	CLI(net)
	net.stop()
