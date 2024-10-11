# Nmap
#Nmap #command 
- Options:
	- =="-sC"== = more detailed output
	- =="-sV"== = version scan (service protocol, application name, and version)
	- =="-p-"== = all 65,535 TCP ports

## Nmap scripts
```pug
nmap --script <script name> -p<port> <host>
```
https://nmap.org/nsedoc/scripts/
#Nmap_scripts
## Banner Grabbing
```pug
nc -nv 10.129.42.253 21
```
Alt: `nmap -sV --script=banner -p21 10.10.10.0/24`.

## Connecting to FTP (if dir is available)
```pug
ftp -p 10.129.42.253
```
==download files== using the ==`get` command==

## SMB (Server Message Block)
#Nmap #SMB
In Nmap some vulnerabilities can be exploited, because of SMB. (35 Scripts for SMB in Nmap scripts)(some SMB versions may be vulnerable to RCE exploits such as [[EternalBlue]])
Example:
### `smb-os-discovery.nse`
https://nmap.org/nsedoc/scripts/smb-os-discovery.html
```pug
nmap --script smb-os-discovery.nse -p445 127.0.0.1
sudo nmap -sU -sS --script smb-os-discovery.nse -p U:137,T:139 127.0.0.1
```
Attempts to determine the operating system, computer name, domain, workgroup, and current time over the SMB protocol (ports 445 or 139)

+A tool for interacting with SMB shares: [[smbclient]]

=================================



# End quiz

Perform a Nmap scan of the target. What is the version of the service from the Nmap scan running on port 8080?
```pug
nmap -A -p8080 10.129.42.254
```
![[Pasted image 20240423190915.png]]



Perform an Nmap scan of the target and identify the non-default port that the telnet service is running on.
```pug
nmap 10.129.42.254
```
![[Pasted image 20240423191610.png]]



List the ==SMB shares available== on the target host. Connect to the available share as the bob user. Once connected, access the folder called 'flag' and submit the contents of the flag.txt file.
```pug
dceece590f3284c3866305eb2473d099
```
![[Pasted image 20240423191751.png]]
![[Pasted image 20240423191806.png]]
![[Pasted image 20240423191819.png]]
