#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

from libcloud.types import Provider
from libcloud.providers import get_driver
from libcloud.deployment import ScriptDeployment, SSHKeyDeployment
import os, time
import paramiko, socket

port = 22
keypath = os.path.expanduser("~/.ssh/id_rsa.pub")
RACKSPACE_USER = 'user' 
RACKSPACE_KEY = 'key'

def run_on_node(host, user, cmd, password=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if password is not None:
        ssh.connect(host, port, user, password=password)
    else:
        ssh.connect(host, port, user)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for line in stdout.readlines(): print line
    ssh.close()

def upload_public_key(host, username, password):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    remotepath = './.ssh/authorized_keys'
    sftp.put(keypath, remotepath)
    print "Public key succesfully loaded"
    sftp.close()
    transport.close()

def _is_host_up(host, port):
    # Set the timeout
    original_timeout = socket.getdefaulttimeout()
    new_timeout = 3
    socket.setdefaulttimeout(new_timeout)
    host_status = False
    try:
        transport = paramiko.Transport((host, port))
        host_status = True
    except:
        pass
    socket.setdefaulttimeout(original_timeout)
    return host_status

if __name__ == "__main__":
    Driver = get_driver(Provider.RACKSPACE)
    print "Connecting to Rackspace..."
    conn = Driver(RACKSPACE_USER, RACKSPACE_KEY)
    images = conn.list_images()
    sizes = conn.list_sizes()
    
    # Some clouds can deploy keys using the following libcloud functionality
    # sd = SSHKeyDeployment(open(os.path.expanduser("~/.ssh/id_rsa.pub")).read())
    # node = conn.deploy_node(name='test', image=images[0], size=sizes[0], deploy=sd)
    
    ## CREATE NODE ##
    nodename = "test"
    print 'Creating new node "%s"...' % nodename
    node = conn.create_node(name=nodename, image=images[1], size=sizes[0])
    # print "Node parameters:"
    # d = node.__dict__
    # for field in d: print field + ": " + d[field]
    # print "Node features dict:"
    print conn.features
    
    ## Wait until node comes online ##
    pause = 20
    print "\nWaiting for %s seconds..." % pause
    time.sleep(pause)

    host   = node.public_ip[0]
    user = 'root'
    newpass = node.extra.get('password')
    print "Trying to connect to new node",
    timeout = 80
    host_up = False
    for i in range(timeout):
        if _is_host_up(host, int(port)) is True:
            print "\nSuccess!: System online"
            host_up = True
            break
        else:
            print ".",
            time.sleep(2)
    print
    if not host_up:
        print('***Warning*** Host {host} on port {port} is down.'.format(
            host=host, port=port)
        )
    
    ## CONNECT TO NEW NODE ##
    print "Conecting to new node on ip %s" % host
    
    print "\nExcecuting command 'uname -a' with root/password login"
    run_on_node(host, user, "uname -a", password=newpass)

    # Upload public key
    print "Uploading public key..."
    run_on_node(host, user, "mkdir -p ~/.ssh/", password=newpass)
    
    upload_public_key(host, user, newpass)
    
    print "\nExcecuting command 'uname -a' with root/public_key login"
    run_on_node(host, user, "uname -a")
