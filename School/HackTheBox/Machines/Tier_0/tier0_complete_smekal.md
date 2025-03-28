# Meow
TASK 1
What does the acronym VM stand for?
- Virtual Machine

TASK 2
What tool do we use to interact with the operating system in order to issue commands via the command line, such as the one to start our VPN connection? It's also known as a console or shell.
- terminal

TASK 3
What service do we use to form our VPN connection into HTB labs?
- openvpn

TASK 4
What tool do we use to test our connection to the target with an ICMP echo request?
- ping

TASK 5
What is the name of the most common tool for finding open ports on a target?
- nmap

TASK 6
What service do we identify on port 23/tcp during our scans?
- telnet
```pug
namp -sC -sV -Pn <ip>
```

TASK 7
What username is able to log into the target over telnet with a blank password?
- root

SUBMIT FLAG
Submit root flag
- b40abdfe23665f766f9c61ecba8a4c19

# Fawn
TASK 1
What does the 3-letter acronym FTP stand for?
- File Transfer Protocol

TASK 2
Which port does the FTP service listen on usually?
- 21

TASK 3
What acronym is used for the secure version of FTP?
- SFTP

TASK 4
What is the command we can use to send an ICMP echo request to test our connection to the target?
- ping

TASK 5
From your scans, what version is FTP running on the target?
- vsftpd 3.0.3
![[Pasted image 20240505190459.png]]
TASK 6
From your scans, what OS type is running on the target?
- Unix

TASK 7
What is the command we need to run in order to display the 'ftp' client help menu?
- ftp -h

TASK 8
What is username that is used over FTP when you want to log in without having an account?
- anonymous

TASK 9
What is the response code we get for the FTP message 'Login successful'?
- 230
![[Pasted image 20240505190744.png]]
TASK 10
There are a couple of commands we can use to list the files and directories available on the FTP server. One is dir. What is the other that is a common way to list files on a Linux system.
- ls

TASK 11
What is the command used to download the file we found on the FTP server?
- get
![[Pasted image 20240505190932.png]]

SUBMIT FLAG
Submit root flag
- 035db21c881520061c53e0536e44f815

# Dancing
TASK 1
What does the 3-letter acronym SMB stand for?
- Server Message Block

TASK 2
What port does SMB use to operate at?
- 445

TASK 3
What is the service name for port 445 that came up in our Nmap scan?
- microsoft-ds
![[Pasted image 20240505192114.png]]

TASK 4
What is the 'flag' or 'switch' that we can use with the smbclient utility to 'list' the available shares on Dancing?
- -L

How many shares are there on Dancing?
- 4
![[Pasted image 20240505192123.png]]

TASK 6
What is the name of the share we are able to access in the end with a blank password?
- WorkShares

TASK 7
What is the command we can use within the SMB shell to download the files we find?
- get

SUBMIT FLAG
Submit root flag
![[Pasted image 20240505192652.png]]
![[Pasted image 20240505192708.png]]
- 5f61c10dffbc77a704d76016a22f1664


# Redeemer
TASK 1
Which TCP port is open on the machine?
- 6379
![[Pasted image 20240505222733.png]]

TASK 2
Which service is running on the port that is open on the machine?
- redis

TASK 3
What type of database is Redis? Choose from the following options: (i) In-memory Database, (ii) Traditional Database
- In-memory Database

TASK 4
Which command-line utility is used to interact with the Redis server? Enter the program name you would enter into the terminal without any arguments.
- redis-cli

TASK 5
Which flag is used with the Redis command-line utility to specify the hostname?
- -h

TASK 6
Once connected to a Redis server, which command is used to obtain the information and statistics about the Redis server?
- info
![[Pasted image 20240505222944.png]]

TASK 7
What is the version of the Redis server being used on the target machine?
- 5.0.7
![[Pasted image 20240505223137.png]]
TASK 8
Which command is used to select the desired database in Redis?
- select

TASK 9
How many keys are present inside the database with index 0?
- 4
![[Pasted image 20240505223154.png]]

TASK 10
Which command is used to obtain all the keys in a database?
- `keys *`
![[Pasted image 20240505223247.png]]

SUBMIT FLAG
Submit root flag
- 03e1d2b376c37ab3f5319922053953eb
![[Pasted image 20240505222913.png]]
![[Pasted image 20240505223322.png]]