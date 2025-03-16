https://www.youtube.com/watch?v=aEf1nm_26JY

Task 1
Which TCP port is hosting a database server?
- 1433
![[Pasted image 20250307092745.png]]
![[Pasted image 20250314085900.png]]

Task 2
What is the name of the non-Administrative share available over SMB?
- backups
![[Pasted image 20250307093124.png]]
#SMB 
![[Pasted image 20250314090215.png]]

Task 3
What is the password identified in the file on the SMB share?
- M3g4c0rp123
![[Pasted image 20250307093336.png]]
![[Pasted image 20250307093423.png]]
![[Pasted image 20250307093441.png]]
(we also got an usernamr ID/username ARCHETYPE\sql_svc)
![[Pasted image 20250314090347.png]]
![[Pasted image 20250314090357.png]]



Task 4
What script from Impacket collection can be used in order to establish an authenticated connection to a Microsoft SQL Server?
- mssqlclient.py
![[Pasted image 20250307093800.png]]

Task 5
What extended stored procedure of Microsoft SQL Server can be used in order to spawn a Windows command shell?
- xp_cmdshell
![[Pasted image 20250307094119.png]]
![[Pasted image 20250307094102.png]]
![[Pasted image 20250307094152.png]]

![[Pasted image 20250314090620.png]]
![[Pasted image 20250314091055.png]]
![[Pasted image 20250314091119.png]]


Task 6
What script can be used in order to search possible paths to escalate privileges on Windows hosts?
- winPEAS
![[Pasted image 20250307094519.png]]
https://github.com/peass-ng/PEASS-ng/blob/master/winPEAS/winPEASexe/README.md
![[Pasted image 20250307094656.png]]

Task 7
What file contains the administrator's password?
- 
can use #msfvenom
![[Pasted image 20250307094952.png]]
![[Pasted image 20250314091351.png]]
![[Pasted image 20250307095056.png]]![[Pasted image 20250314091527.png]]

Then msfconsole
![[Pasted image 20250307095148.png]]
![[Pasted image 20250307095244.png]]

![[Pasted image 20250307095255.png]] + set LHOST \<our IP>
![[Pasted image 20250307095311.png]]
![[Pasted image 20250307095518.png]]
![[Pasted image 20250307095552.png]]
![[Pasted image 20250307095530.png]]
![[Pasted image 20250307095931.png]]
![[Pasted image 20250307095952.png]]
https://youtu.be/aEf1nm_26JY?si=yiDf0NMcOOAFDjr2&t=1447


Submit Flag
Submit user flag
- 

