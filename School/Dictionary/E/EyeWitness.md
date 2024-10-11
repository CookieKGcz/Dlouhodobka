#command 
`EyeWitness` can be used to take screenshots of target web applications, fingerprint them, and identify possible default credentials.


Supported - Kali Linux.
It will auto detect the file you give it with the ==-f flag== as either being a text file with URLs on each new line, nmap xml output, or nessus xml output. The --timeout flag is completely optional, and lets you provide the max time to wait when trying to render and screenshot a web page.


https://github.com/RedSiege/EyeWitness
A complete usage guide which documents `EyeWitness` features and its typical use cases is available here - [https://www.christophertruncer.com/eyewitness-2-0-release-and-user-guide/](https://www.christophertruncer.com/eyewitness-2-0-release-and-user-guide/)

# Usage:
```sh
./EyeWitness.py -f filename --timeout optionaltimeout
```
# Examples:
```shell
./EyeWitness -f urls.txt --web

./EyeWitness -x urls.xml --timeout 8 

./EyeWitness.py -f urls.txt --web --proxy-ip 127.0.0.1 --proxy-port 8080 --proxy-type socks5 --timeout 120
```