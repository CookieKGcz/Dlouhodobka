#R1
en
conf t

ipv6 unicast

ip dhcp ex 172.16.10.1
ip dhcp ex 172.16.20.1
ip dhcp pool VLAN10
network 172.16.10.0 255.255.255.0
default-r 172.16.10.1
ip dhcp pool VLAN20
network 172.16.20.0 255.255.255.0
default-r 172.16.20.1

ipv6 dhcp pool VLAN10v6
ipv6 dhcp pool VLAN20v6

ip route 172.16.30.0 255.255.255.0 10.10.10.2
ip route 172.16.40.0 255.255.255.0 10.10.10.2
ipv6 route 2001:acad:0:30::/64 2001:acad::2
ipv6 route 2001:acad:0:40::/64 2001:acad::2

int g0/0
no shut

int g0/1
ip add 10.10.10.1 255.255.255.0
ipv6 add 2001:acad::1/64
ipv6 add fe80::1 link

int g0/0.10
enc d 10
ip add 172.16.10.1
ipv6 add 2001:acad:0:10::1/64
ipv6 add fe80::1 link
ipv6 dhcp server VLAN10v6
ipv6 nd other

int g0/0.20
enc d 20
ip add 172.16.20.1
ipv6 add 2001:acad:0:20::1/64
ipv6 add fe80::1 link
ipv6 dhcp server VLAN20v6
ipv6 nd other

#Switch
en
conf t
vlan 10
vlan 20
int vlan 10
int vlan 20

int f0/1
sw m ac
sw ac vl 10
int f0/2
sw m ac
sw ac vl 20
int g0/1
sw m t
sw t al vl 10,20

#R2

en
conf t

ipv6 unicast

ip dhcp ex 172.16.30.1
ip dhcp ex 172.16.40.1
ip dhcp pool VLAN30
network 172.16.30.0 255.255.255.0
default-r 172.16.30.1
ip dhcp pool VLAN40
network 172.16.40.0 255.255.255.0
default-r 172.16.40.1

ipv6 dhcp pool VLAN30v6
ipv6 dhcp pool VLAN40v6

ip route 172.16.20.0 255.255.255.0 10.10.10.1
ip route 172.16.10.0 255.255.255.0 10.10.10.1
ipv6 route 2001:acad:0:20::/64 2001:acad::1
ipv6 route 2001:acad:0:10::/64 2001:acad::1

int g0/0
no shut

int g0/1
no shut
ip add 10.10.10.2 255.255.255.0
ipv6 add 2001:acad::2/64
ipv6 add fe80::2 link

int g0/0.30
enc d 30
ip add 172.16.30.1 255.255.255.0
ipv6 add 2001:acad:0:30::1/64
ipv6 add fe80::1 link
ipv6 dhcp server VLAN30v6
ipv6 nd other

int g0/0.40
enc d 40
ip add 172.16.40.1 255.255.255.0
ipv6 add 2001:acad:0:40::1/64
ipv6 add fe80::1 link
ipv6 dhcp server VLAN40v6
ipv6 nd other