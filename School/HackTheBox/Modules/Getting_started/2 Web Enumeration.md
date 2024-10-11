# Gobuster
#Gobuster #Ffuf #command 
For discovery of any hidden files or directories on the webserver that are not intended for public access.
Similar command: [[Ffuf]]

## Directory/File Enumeration
(wordlist attack)
Example:
```pug
gobuster dir -u http://10.10.10.121/ -w /usr/share/dirb/wordlists/common.txt
```
Example of output:
```sh
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.121/
[+] Threads:        10
[+] Wordlist:       /usr/share/dirb/wordlists/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/12/11 21:47:25 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/index.php (Status: 200)
/server-status (Status: 403)
/wordpress (Status: 301)
===============================================================
2020/12/11 21:47:46 Finished
==============================================================
```
! ==Status codes== (what went right/wrong)


## DNS Subdomain Enumeration
Can enumerate available subdomains of a given domain using the `dns` flag to specify DNS mode.
```pug
git clone https://github.com/danielmiessler/SecLists

sudo apt install seclists -y
```
- add a DNS Server such as 1.1.1.1 to the `/etc/resolv.conf` file
```pug
gobuster dns -d inlanefreight.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```
Output:
```sh
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Domain:     inlanefreight.com
[+] Threads:    10
[+] Timeout:    1s
[+] Wordlist:   /usr/share/SecLists/Discovery/DNS/namelist.txt
===============================================================
2020/12/17 23:08:55 Starting gobuster
===============================================================
Found: blog.inlanefreight.com
Found: customer.inlanefreight.com
Found: my.inlanefreight.com
Found: ns1.inlanefreight.com
Found: ns2.inlanefreight.com
Found: ns3.inlanefreight.com
===============================================================
2020/12/17 23:10:34 Finished
===============================================================
```
Found 6 subdomains!



# Web Enumeration Tips
## Banner Grabbing / Web Server Headers
Command: [[cURL]], [[EyeWitness]]
- We can use `cURL` to retrieve server header information from the command line.
- `EyeWitness` can be used to take screenshots of target web applications, fingerprint them, and identify possible default credentials.
## Whatweb
We can extract the version of web servers, supporting frameworks, and applications.
Command: [[whatweb]]
## Robots.txt
Instructs search engine web crawlers such as Googlebot which resources can and cannot be accessed for indexing
 ![[Pasted image 20240423210853.png]]
 `robots.txt` file contains two disallowed entries





# End quiz
Try running some of the web enumeration techniques you learned in this section on the server above, and use the info you get to get the flag.
```pug
gobuster  dir -u http://94.237.57.59:40126/ -w /usr/share/dirb/wordlists/common.txt
```
```sh
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://94.237.57.59:40126/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2024/04/24 21:56:16 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/index.php            (Status: 200) [Size: 990]
/robots.txt           (Status: 200) [Size: 45] 
/server-status        (Status: 403) [Size: 280]
/wordpress            (Status: 301) [Size: 325] [--> http://94.237.57.59:40126/wordpress/]
                                                                                          
===============================================================
2024/04/24 21:56:20 Finished
===============================================================
```
! robots.txt
![[Pasted image 20240424230122.png]]
![[Pasted image 20240424230221.png]]
HTB{w3b_3num3r4710n_r3v34l5_53cr375}