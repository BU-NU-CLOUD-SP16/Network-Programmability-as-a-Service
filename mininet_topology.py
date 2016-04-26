from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
import sys
"""
Instructions to run the topo:
    1. Go to directory where this fil is.
    2. run: sudo -E python <file name>
       In this case it is: sudo -E python Tree_Generic_Topo.py     
"""

CORES = {
  's1': {'dpid': '000000000000010%s'},
  's2': {'dpid': '000000000000020%s'},
  's3': {'dpid': '000000000000030%s'},
  's4': {'dpid': '000000000000040%s'},
  's5': {'dpid': '000000000000050%s'},
  's6': {'dpid': '000000000000060%s'},
  's7': {'dpid': '000000000000070%s'},
}

class GenericTree(Topo):
    """Simple topology example."""

    def build( self, depth=1, fanout=2 ):
        # Numbering:  h1..N, s1..M
        self.hostNum = 1
        self.switchNum = 1

    def __init__( self, depth=1, fanout=2 ):
	super(GenericTree, self).__init__()
        # Numbering:  h1..N, s1..M
        self.hostNum = 1
        self.switchNum = 1
        # Build topology
        self.addTree(depth, fanout)

    def addTree( self, depth, fanout ):
        """Add a subtree starting with node n.
           returns: last node added"""
        isSwitch = depth > 0
        if isSwitch:
            node = self.addSwitch( 's%s' % self.switchNum,dpid=(CORES['s%s' %self.switchNum]['dpid'] % '0') )
            self.switchNum += 1
            for _ in range( fanout ):
                child = self.addTree( depth - 1, fanout )
                self.addLink( node, child )
        else:
           
            node = self.addHost( 'h%s' % self.hostNum )
            self.hostNum += 1
        return node


def run(a, b):
    c1 = RemoteController('c1', a, 6633)
    c2 = RemoteController('c2', b, 6633)
    c3 = RemoteController('c3', b, 6633)
    # Change the args of GenericTree() to your desired values. You could even get them from command line.
    net = Mininet(topo=GenericTree(depth=3, fanout=2),autoSetMacs=True,controller=None)
    net.addController(c1)
    net.addController(c2)
    net.addController(c3)
    net.start()

    # installStaticFlows( net )
    CLI(net)
    net.stop()

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    try:
        run(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        print "Please enter IP addresses of 2 OVX instances as CLI"
