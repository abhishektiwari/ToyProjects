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
from libcloud.deployment import MultiStepDeployment, ScriptDeployment, SSHKeyDeployment 
import os 

RACKSPACE_USER = 'user' 
RACKSPACE_KEY = 'key' 
 
print "Getting connection"
Driver = get_driver(Provider.RACKSPACE) 
conn = Driver(RACKSPACE_USER, RACKSPACE_KEY) 
print "Now connected"
# read your public key in 
print "Reading ssh key"
sd = SSHKeyDeployment(open(os.path.expanduser("~/.ssh/id_rsa.pub")).read()) 
print "Public key succesfully loaded"
# a simple script to install puppet post boot, use - y option
script = ScriptDeployment("apt-get -y install puppet") 
# a task that first installs the ssh key, and then runs the script Yes to all queries
print "Preparing multi-step deployment"
msd = MultiStepDeployment([sd, script]) 
 
images = conn.list_images() 
sizes = conn.list_sizes() 
print "Images: ", images
print "Sizes : ", sizes
print "Selected size and image", sizes[0], images[1]
# deploy_node takes the same base keyword arguments as create_node. 
node = conn.deploy_node(name='MyDeploument2', image=images[1], size=sizes[0], deploy=msd) 
# <Node: uuid=..., name=test, state=3, public_ip=['1.1.1.1'], provider=Rackspace ...> 
# the node is now booted, with your ssh key and puppet installed. 		
# If you get error like ''connect not implemented for this ssh client'
# then install Paramiko (apt-get install python-paramiko) which is required in ssh.py	
