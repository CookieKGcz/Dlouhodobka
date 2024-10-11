The command `mkdir` has an option marked `-p` to add parent directories.
```pug
CCCCQQQQE@htb[/htb]$ mkdir -p Storage/local/user/documents
```

tree output
```pug
CCCCQQQQE@htb[/htb]$ tree .

.
├── info.txt
└── Storage
    └── local
        └── user
            └── documents

4 directories, 1 file
```


# Questions

What is the name of the last modified file in the "/var/backups" directory?
![[Pasted image 20240812192005.png]]

What is the inode number of the "shadow.bak" file in the "/var/backups" directory?
![[Pasted image 20240812192015.png]]
