#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Controller, OVSSwitch,OVSController
from mininet.cli import CLI

def phase1():
	"Create an empty network and add nodes to it."

	net = Mininet(controller=ovsc,switch=OVSSwitch )
	info('*** Adding controller\n' )
	  
	c0 = net.addController( 'c0', port=6633 )
	
	info('*** Adding hosts\n' )
	h1 = net.addHost( 'h1', ip='10.0.0.1')
	h2 = net.addHost( 'h2', ip='10.0.0.2')
	h3 = net.addHost( 'h3', ip='10.0.0.3')
	h4 = net.addHost( 'h4', ip='10.0.0.4')
	
	info('*** Adding Switches\n')
	s5=net.addSwitch("s5")
	s6=net.addSwitch("s6")
	
	
	info("*** Creating links")
	net.addLink(h1,s5)
	net.addLink(h2,s5)
	net.addLink(h3,s6)
	net.addLink(h4,s6)
	net.addLink(s5,s6)
	
	info('*** Starting network\n')
	net.build()
    c0.start()
    s5.start([c0])
	s6.start([c0])

	net.start()

	info('*** Running CLI\n' )
	CLI(net)
	
	info('*** Testing network\n')
	net.pingAll()
	
	info( '*** Stopping network' )
	net.stop()
	


if __name__ == '__main__':
	setLogLevel( 'info' )
	phase1()
	
