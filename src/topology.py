#!/usr/bin/python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


'''
My main function executing all the commands
'''
def main():
	#Initialise mininet with OVSController and TCLink
	net = Mininet(controller = OVSController,link=TCLink)
	#create hosts and networks
	c0 = net.addController('C0')
	h1 = net.addHost('h1')
	h2 = net.addHost('h2')
	h3 = net.addHost('h3')
	h4 = net.addHost('h4')
	h5 = net.addHost('h5')
	h6 = net.addHost('h6')
	h7 = net.addHost('h7')
	h8 = net.addHost('h8')
	h9 = net.addHost('h9')
	h10 = net.addHost('h10')
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')
	s4 = net.addSwitch('s4')
	s5 = net.addSwitch('s5')
	#create links with parameters(node1,node2,bw in Mbit,delay,loss in percentage)
	net.addLink(s5,s1,bw=40,delay='52us',loss=2)
	net.addLink(s4,s1,bw=38,delay='76us',loss=4)
	net.addLink(s3,s1,bw=35,delay='48us',loss=2)
	net.addLink(s2,s1,bw=30,delay='87us',loss=3)
	net.addLink(h5,s1,bw=22,delay='3ms',loss=9)
	net.addLink(h6,s1,bw=25,delay='1ms',loss=7)
	net.addLink(h7,s1,bw=18,delay='4ms',loss=6)
	net.addLink(h8,s1,bw=20,delay='2ms',loss=8)
	net.addLink(h1,s2,bw=14,delay='5ms',loss=13)
	net.addLink(h2,s2,bw=12,delay='4ms',loss=15)
	net.addLink(h3,s3,bw=15,delay='3ms',loss=8)
	net.addLink(h4,s3,bw=11,delay='2ms',loss=9)
	net.addLink(h9,s4,bw=30,delay='7ms',loss=12)
	net.addLink(h10,s5,bw=25,delay='5ms',loss=10)
	# Start the network
	net.start()
	# Test connectivity by trying to have all nodes ping each other
	print("Testing network connectivity")
	net.pingAll()
	# Dump Connections
	dumpNodeConnections(net.hosts)
	dumpNodeConnections(net.switches)
	# Enter Mininet's CLI mode
	CLI(net)

'''
Main (entry point)
'''
if __name__ == '__main__':
	# Tell mininet to print useful information
	setLogLevel('info')
	# Create and test a simple network
	main()
