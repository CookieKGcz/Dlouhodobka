where exactly we are with `pwd`
```pug
cry0l1t3@htb[~]$ pwd

/home/cry0l1t3
```

## `ls -l` description
```pug
cry0l1t3@htb[~]$ ls -l

total 32
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 Desktop
```
total is how much is used in blocks (1024-byte blocks)

| **Column Content** | **Description**                                                                  |
| ------------------ | -------------------------------------------------------------------------------- |
| `drwxr-xr-x`       | Type and permissions                                                             |
| `2`                | Number of hard links to the file/directory                                       |
| `cry0l1t3`         | Owner of the file/directory                                                      |
| `htbacademy`       | Group owner of the file/directory                                                |
| `4096`             | Size of the file or the number of blocks used to store the directory information |
| `Nov 13 17:37`     | Date and time                                                                    |
| `Desktop`          | Directory name                                                                   |
|                    |                                                                                  |

# Questions

What is the name of the hidden "history" file in the htb-user's home directory?
![[Pasted image 20240812190451.png]]

What is the index number of the "sudoers" file in the "/etc" directory?
![[Pasted image 20240812190437.png]]
## index num is
the index number, or inode, is a number that is unique to a file in the Unix filesystem. It is an identifying number the OS will use when storing and retrieving the data. Data has two pieces to it - the metadata (permissions, file size, etc) along with the actual data itself.
```pug
ls -i <name-of-the-file>
```
