A tool that can enumerate and interact with SMB shares.

Example of use:
```pug
smbclient -N -L \\\\10.129.42.253
```
`-L` flag specifies that we want to retrieve a list of available shares on the remote host
`-N` suppresses the password prompt

normal connection / with username
```pug
smbclient \\\\10.129.42.253\\users
```
```pug
smbclient -U bob \\\\10.129.42.253\\users
```
