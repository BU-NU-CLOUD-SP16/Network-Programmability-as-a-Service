#!/usr/bin/python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import lg, setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

CORES = {
  'sw1': {'dpid': '000000000000010%s'},
  'sw2': {'dpid': '000000000000020%s'},
  'sw3': {'dpid': '000000000000030%s'},
  }

FANOUT = 4
    
class I2Topo(Topo):

  def __init__(self, enable_all = True):
    "Create Internet2 topology."

    # Add default members to class.
    super(I2Topo, self).__init__()

    # Add core switches
    self.cores = {}
    for switch in CORES:
      self.cores[switch] = self.addSwitch(switch, dpid=(CORES[switch]['dpid'] % '0'))

    # Add hosts and connect them to their core switch
    for switch in CORES:
      for count in xrange(1, FANOUT + 1):
        # Add hosts
        host = 'h_%s_%s' % (switch, count)
        ip = '10.0.0.%s' % count
        mac = CORES[switch]['dpid'][4:] % count
        h = self.addHost(host, ip=ip, mac=mac)
        # Connect hosts to core switches
        self.addLink(h, self.cores[switch])

    # Connect core switches
    self.addLink(self.cores['sw2'], self.cores['sw1'])
    #self.addLink(self.cores['SEA'], self.cores['SLC'])
    self.addLink(self.cores['sw2'], self.cores['sw3'])
    #self.addLink(self.cores['LAX'], self.cores['SLC'])
    #self.addLink(self.cores['LAX'], self.cores['IAH'])
    #self.addLink(self.cores['SLC'], self.cores['MCI'])
    #self.addLink(self.cores['MCI'], self.cores['IAH'])
    #self.addLink(self.cores['MCI'], self.cores['ORD'])
    #self.addLink(self.cores['IAH'], self.cores['ATL'])
    #self.addLink(self.cores['ORD'], self.cores['ATL'])
    #self.addLink(self.cores['ORD'], self.cores['CLE'])
    #self.addLink(self.cores['ATL'], self.cores['IAD'])
    #self.addLink(self.cores['CLE'], self.cores['IAD'])
    #self.addLink(self.cores['CLE'], self.cores['EWR'])
    #self.addLink(self.cores['EWR'], self.cores['IAD'])

if __name__ == '__main__':
   topo = I2Topo()
   ip = '127.0.0.1'
   port = 6633
   c = RemoteController('c', ip=ip, port=port)
   net = Mininet(topo=topo, autoSetMacs=True, xterms=False, controller=None)
   net.addController(c)
   net.start()
   print "Hosts configured with IPs, switches pointing to OpenVirteX at %s:%s" % (ip, port)
   CLI(net)
   net.stop()

