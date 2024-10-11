# Nmap
fist ports
```pug
nmap -sV --open -oA nibbles_initial_scan <ip address>
```
`-oA` will output XML, greppable output, 

all ports
```pug
nmap -p- --open -oA nibbles_full_tcp_scan 10.129.182.11
```

# Banner grabbing
```pug
nc -nv 10.129.42.190 <port>
```

# Scripts
## Man-NSE
```pug
nmap -sC -p <ports> -oA nibbles_script_scan 10.129.42.190
```

## HTTP-enum
```pug
nmap -sV --script=http-enum -oA nibbles_nmap_http_enum 10.129.42.190 
```




# End Quiz
Run an nmap script scan on the target. What is the Apache version running on the server? (answer format: X.X.XX)
2.somthing XD forgot
