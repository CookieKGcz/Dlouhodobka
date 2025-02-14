Task 1
When visiting the web service using the IP address, what is the domain that we are being redirected to?
- unika.htb 
- ![[Pasted image 20250214093623.png]]![[Pasted image 20250214093550.png]]
Task 2 
Which scripting language is being used on the server to generate webpages? 
- php
- ![[Pasted image 20250214093704.png]]

Task 3 
What is the name of the URL parameter which is used to load different language versions of the webpage? 
- page
- ![[Pasted image 20250214093815.png]]

Task 4 
Which of the following values for the `page` parameter would be an example of exploiting a Local File Include (LFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe" 
- ../../../../../../../../windows/system32/drivers/etc/hosts ![[Pasted image 20250214094216.png]]

Task 5 
Which of the following values for the `page` parameter would be an example of exploiting a Remote File Include (RFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe" 
- //10.10.14.6/somefile ![[Pasted image 20250214094248.png]]

Task 6 
What does NTLM stand for? 
- New Technology Lan Manager 

Task 7 
Which flag do we use in the Responder utility to specify the network interface? 
- -I

Task 8
There are several tools that take a NetNTLMv2 challenge/response and try millions of passwords to see if any of them generate the same response. One such tool is often referred to as `john`, but the full name is what?. 
- John The Ripper 

Task 9 
What is the password for the administrator user?
- ![[Pasted image 20250214094632.png]]![[Pasted image 20250214094644.png]]
- Try to get some file?![[Pasted image 20250214100004.png]]
- 526915e2d91206f232cc7152582c135a![[Pasted image 20250214160452.png]]

- now John ![[Pasted image 20250214160802.png]]
- -- badminton

Task 10
We'll use a Windows service (i.e. running on the box) to remotely access the Responder machine using the password we recovered. What port TCP does it listen on?
- 
![[Pasted image 20250214161951.png]]

https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management

https://www.kali.org/tools/evil-winrm/
![[Pasted image 20250214164203.png]]
![[Pasted image 20250214164411.png]]
![[Pasted image 20250214165154.png]]
![[Pasted image 20250214165327.png]]
- ea81b7afddd03efaa0945333ed147fac