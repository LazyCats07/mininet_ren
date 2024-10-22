"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

def myNetwork():
    net = Mininet(controller=Controller, link=TCLink, switch=OVSKernelSwitch)

    print("*** Adding controller")
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    print("*** Adding switches")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')

    print("*** Adding hosts")
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')
    h4 = net.addHost('h4', ip='10.0.0.4')
    h5 = net.addHost('h5', ip='10.0.0.5')
    h6 = net.addHost('h6', ip='10.0.0.6')
    h7 = net.addHost('h7', ip='10.0.0.7')
    h8 = net.addHost('h8', ip='10.0.0.8')
    h9 = net.addHost('h9', ip='10.0.0.9')
    h10 = net.addHost('h10', ip='10.0.0.10')

    print("*** Creating links")
    # Hubungkan host ke switch
    net.addLink(h1, s2)
    net.addLink(h2, s2)
    net.addLink(h3, s3)
    net.addLink(h4, s3)
    
    net.addLink(h5, s5)
    net.addLink(h6, s5)

    net.addLink(h7, s6)
    net.addLink(h8, s6)
    net.addLink(h9, s1)
    net.addLink(h10, s4)

    # Hubungkan antar switch
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)
    net.addLink(s4, s5)
    net.addLink(s5, s6)
    net.addLink(s1, s6)

    # Hubungkan Controller ke switches
    net.addLink(c0,s1);
    net.addLink(c0,s2);
    net.addLink(c0,s3);
    net.addLink(c0,s4);
    net.addLink(c0,s5);
    net.addLink(c0,s6);



    print("*** Starting network")
    net.start()

    print("*** Running CLI")
    CLI(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()



# topos = { 'mytopo': ( lambda: MyTopo() ) }
