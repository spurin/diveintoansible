1. Note that the ip addresses for your own linux containers, or whatever container
system you are using may be different than mine! So, be aware of this when
configuring your own hosts inventory.

2. The bootstrap.yml playbook is for bootstrapping centos-based hosts

3. Since we're using privileged containers, we need to install yum on this ubuntu
box:
sudo apt install yum

then:
sudo lxc-create -n centos -t centos

Once you've done that, start the container os:
sudo lxc-start -n centos

then ssh into the box in order to change the password:
ssh root@<ip address>

Now you can bootstrap the centos box and follow along
