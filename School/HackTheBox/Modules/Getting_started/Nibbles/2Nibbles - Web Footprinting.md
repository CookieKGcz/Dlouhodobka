We can use `whatweb` to try to identify the ==web application in use==.
#tool #webapps #whatweb
```pug
whatweb 10.129.42.190
```

Checking source code
```pug
curl http://10.129.42.190
```


# Directory Enumeration
#tool #Gobuster 
```pug
gobuster dir -u http://10.129.42.190/nibbleblog/ --wordlist /usr/share/dirb/wordlists/common.txt
```
```shell-session
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/admin (Status: 301)
/admin.php (Status: 200)
/content (Status: 301)
/index.php (Status: 200)
/languages (Status: 301)
/plugins (Status: 301)
/README (Status: 200)
/themes (Status: 301)
```

[[Status codes]]

#tool #xmllint #cURL
```pug
curl -s http://10.129.42.190/nibbleblog/content/private/users.xml | xmllint  --format -
```


#tool #CeWL #Hashcat
[CeWL](https://github.com/digininja/CeWL)
Can create a wordlist generated by crawling through a website.
