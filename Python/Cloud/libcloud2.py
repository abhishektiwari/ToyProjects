>>> from libcloud.types import Provider
>>> from libcloud.providers import get_driver 
>>> from libcloud.deployment import MultiStepDeployment, ScriptDeployment, SSHKeyDeployment
>>> import os 
>>> RACKSPACE_USER = 'username'
>>> RACKSPACE_KEY  = 'key'
>>> Driver = get_driver(Provider.RACKSPACE)
>>> conn = Driver(RACKSPACE_USER, RACKSPACE_KEY)
>>> sd = SSHKeyDeployment(open(os.path.expanduser("~/.ssh/id_rsa.pub")).read())  
>>> script = ScriptDeployment("apt-get install puppet")
>>> msd = MultiStepDeployment([sd, script])
>>> images = conn.list_images()
>>> images
[<NodeImage: id=29, name=Windows Server 2003 R2 SP2 x86, driver=Rackspace  ...>, <NodeImage: id=69, name=Ubuntu 10.10 (maverick), driver=Rackspace  ...>, <NodeImage: id=41, name=Oracle EL JeOS Release 5 Update 3, driver=Rackspace  ...>, <NodeImage: id=53, name=Fedora 13 (Goddard), driver=Rackspace  ...>, <NodeImage: id=187811, name=CentOS 5.4, driver=Rackspace  ...>, <NodeImage: id=4, name=Debian 5.0 (lenny), driver=Rackspace  ...>, <NodeImage: id=10, name=Ubuntu 8.04.2 LTS (hardy), driver=Rackspace  ...>, <NodeImage: id=62, name=Red Hat Enterprise Linux 5.5, driver=Rackspace  ...>, <NodeImage: id=17, name=Fedora 12 (Constantine), driver=Rackspace  ...>, <NodeImage: id=23, name=Windows Server 2003 R2 SP2 x64, driver=Rackspace  ...>, <NodeImage: id=24, name=Windows Server 2008 SP2 x64, driver=Rackspace  ...>, <NodeImage: id=49, name=Ubuntu 10.04 LTS (lucid), driver=Rackspace  ...>, <NodeImage: id=14362, name=Ubuntu 9.10 (karmic), driver=Rackspace  ...>, <NodeImage: id=31, name=Windows Server 2008 SP2 x86, driver=Rackspace  ...>, <NodeImage: id=51, name=CentOS 5.5, driver=Rackspace  ...>, <NodeImage: id=14, name=Red Hat Enterprise Linux 5.4, driver=Rackspace  ...>, <NodeImage: id=19, name=Gentoo 10.1, driver=Rackspace  ...>, <NodeImage: id=28, name=Windows Server 2008 R2 x64, driver=Rackspace  ...>, <NodeImage: id=55, name=Arch 2010.05, driver=Rackspace  ...>, <NodeImage: id=40, name=Oracle EL Server Release 5 Update 4, driver=Rackspace  ...>]
>>> sizes = conn.list_sizes()
siz>>> 
>>> sizes
[<NodeSize: id=1, name=256 server, ram=256 disk=10 bandwidth=None price=None driver=Rackspace ...>, <NodeSize: id=2, name=512 server, ram=512 disk=20 bandwidth=None price=None driver=Rackspace ...>, <NodeSize: id=3, name=1GB server, ram=1024 disk=40 bandwidth=None price=None driver=Rackspace ...>, <NodeSize: id=4, name=2GB server, ram=2048 disk=80 bandwidth=None price=None driver=Rackspace ...>, <NodeSize: id=5, name=4GB server, ram=4096 disk=160 bandwidth=None price=None driver=Rackspace ...>, <NodeSize: id=6, name=8GB server, ram=8192 disk=320 bandwidth=None price=None driver=Rackspace ...>, <NodeSize: id=7, name=15.5GB server, ram=15872 disk=620 bandwidth=None price=None driver=Rackspace ...>]
>>> node = conn.deploy_node(name='test_deploy_libcloud', image=images[1], size=size[0], deploy=msd)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'size' is not defined
>>> node = conn.deploy_node(name='test_deploy_libcloud', image=images[1], size=sizes[0], deploy=msd)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.6/dist-packages/apache_libcloud-0.3.1-py2.6.egg/libcloud/base.py", line 714, in deploy_node
    raise DeploymentException(node, e)
libcloud.types.DeploymentException: NotImplementedError('connect not implemented for this ssh client',)
>>> sd
<libcloud.deployment.SSHKeyDeployment object at 0x2060f90>
>>> msd
<libcloud.deployment.MultiStepDeployment object at 0x2069090>
>>> list = conn.list_nodes()
>>> list
[<Node: uuid=12c2767dc66b82d79f2078a46f859b3d1e2c8bd8, name=testdeploylibcloud, state=0, public_ip=['184.106.132.177'], provider=Rackspace ...>]
>>> conn.destroy_node(list[0])
True

