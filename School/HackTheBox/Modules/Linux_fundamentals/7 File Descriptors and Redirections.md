1. Data Stream for Input
    - `STDIN – 0`
2. Data Stream for Output
    - `STDOUT – 1`
3. Data Stream for Output that relates to an error occurring.
    - `STDERR – 2`
## YEEEES redirect Permission denied
```pug
CCCCQQQQE@htb[/htb]$ find /etc/ -name shadow 2>/dev/null
```

## Redirect STDOUT to a File
```pug
CCCCQQQQE@htb[/htb]$ find /etc/ -name shadow 2>/dev/null > results.txt
```
basically saves output to a file

## Combine >
```pug
CCCCQQQQE@htb[/htb]$ find /etc/ -name shadow 2> stderr.txt 1> stdout.txt
```

## Redirect STDOUT and Append to a File
Append with >>
```pug
CCCCQQQQE@htb[/htb]$ find /etc/ -name passwd >> stdout.txt 2>/dev/null
```

# pipes

```pug
CCCCQQQQE@htb[/htb]$ find /etc/ -name *.conf 2>/dev/null | grep systemd
```
![[Pasted image 20240812214011.png]]



## Q

How many files exist on the system that have the ".log" file extension?
![[Pasted image 20240812215030.png]]

How many total packages are installed on the target system?
![[Pasted image 20240812215041.png]]
