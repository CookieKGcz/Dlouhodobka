# VPN Issues
## Still Connected to VPN?
```pug
sudo openvpn ./htb.ovpn
```
```shell-session
Initialization Sequence Completed
```
= OK
## Getting VPN Address
```pug
ip -4 a show tun0
```
## Checking Routing Table
```pug
sudo netstat -rn
```
```shell-session
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0      192.168.195.2   0.0.0.0         UG        0 0          0 eth0
10.10.14.0   0.0.0.0         255.255.254.0   U         0 0          0 tun0
10.129.0.0   10.10.14.1      255.255.0.0     UG        0 0          0 tun0
192.168.1.0  0.0.0.0         255.255.255.0   U         0 0          0 eth0
```
## Pinging Gateway
```pug
ping -c 4 10.10.14.1
```
## Working on Two Devices
X -> is not possible.
"HTB VPN cannot be connected to more than one device simultaneously"
## Checking Region
Correct VPN server
## VPN Troubleshooting
[HackTheBox Help page](https://help.hackthebox.eu/troubleshooting/v2-vpn-connection-troubleshooting)

# Burp Suite Proxy Issues
[Burp Suite](https://portswigger.net/burp/communitydownload)
# Changing SSH Key and Password
```pug
ssh-keygen
```
