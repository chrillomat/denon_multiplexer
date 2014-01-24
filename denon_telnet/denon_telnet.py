#!/usr/bin/python2

import sys, time
from telnet import MyDebugServerFactory, MyProxyClientFactory, MyProxyServerFactory
from twisted.internet import reactor

class TelnetMultiplexer():
       
    #-----------------------------------------------------------#
    # Read in command line arguments
    def run(self):
        remote_ip        = "192.168.192.128"
        remote_port      = 23
        local_port       = 8823
        local_debug_port = 1357
        my_client = MyProxyClientFactory()
        my_server = MyProxyServerFactory()
        my_debug  = MyDebugServerFactory()
        my_server.local_server  = my_client
        my_server.debug_clients = my_debug
        my_client.local_clients = my_server
        my_client.debug_clients = my_debug
        reactor.connectTCP(remote_ip, remote_port, my_client)
        reactor.listenTCP(local_port, my_server)
        reactor.listenTCP(local_debug_port, my_debug)
        reactor.run()

if __name__ == "__main__":
    daemon = TelnetMultiplexer()
    daemon.run()
