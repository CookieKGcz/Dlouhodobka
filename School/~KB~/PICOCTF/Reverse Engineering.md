## vault-door-training

dostali jsem hint že by něco mohlo být v source codu -> tam je zanechané heslo v public boolean které stačí jen wrapnout do picoCTF{}

Reverse Engineering

vault-door-training

dostali jsem hint že by něco mohlo být v source codu -> tam je zanechané heslo v public boolean které stačí jen wrapnout do picoCTF{}
obsidian://open?vault=ObsNotes&file=School%2F~KB~%2FPICOCTF%2FAttachments%2FPicture1.png

![](School/~KB~/PICOCTF/Attachments/picture1.png)

## Transformation
První začneme od konce a tak for loopem si budeme odstřihávat zanaky -> first = ord(flag\[i])
pak si proměníme chr za ord a dáme do proměnné first
to je celkem tedy soucet dvou ordů v původím kodu

jelikož v jednom posouváme flagu o 8 bitů doleva tak soucet v binárce bude vypadat třeba takto
0100 0000 0010
(vlastně víme co se přičetlo protože ta menší část je ta neposunutá)

takže stačí vydělit 256 s !mod! aby jsme dostali zbytek to je tedy ta druhá část součtu ![[Pasted image 20240927160408.png]]

pro první (tu posunutou) musíme první odečíst druhou od součtu
pak "posunem" zpět na předchozí číslo s "/ 256"

pak obě čísla dáme zpět do charakterové podoby (UTF)



nedokončená verze s join
![](School/~KB~/PICOCTF/Attachments/picture2.png)

## vault-door-1
ze zadání jsme dostali další zdroják kde je vlastně heslo napsané ale trochu porozházené
![[Pasted image 20240927161003.png]]
stačí si tedy napsat script v pythonu který mi je vypíše popořadě za pomocí globals() a f'a{}'
![[Pasted image 20240927160841.png]]![[Pasted image 20240927161202.png]]

## vault-door-3
zadání
![[Pasted image 20240927161812.png]]
![[Pasted image 20240927213658.png]]
![[Pasted image 20240927213740.png]]
První si nadefinujeme buffer a password (to bude to co nakonci source porovnává)
Pak stačí jen obrátit for loopy
POZOR poslední for (který bude první v našem scriptu) se musí zachovat increment -2 protože pak by to odstřihlo kus passwordu

## vault-door-4
![[Pasted image 20240927223408.png]]
![[Pasted image 20240927224157.png]]
![[Pasted image 20240927224212.png]]
Stačí prostě chr nout všechny kolonky v my_bytes
+ můžeme si ordnout charaktery v arrayi aby se to preložilo v jednom kuse

## vault-door-5
![[Pasted image 20240927224635.png]]
můžeme použít cyberchef
3 stringy dáme do sebe a decodujeme první s base64
pak URL decode a máme flag
![[Pasted image 20240927225449.png]]
![[Pasted image 20240927225554.png]]
![[Pasted image 20240927225604.png]]
![[Pasted image 20240927225619.png]]



## vault-door-6
![[Pasted image 20240927225842.png]]
:)
![[Pasted image 20240927230012.png]]
0x55 je z hex přeložeeno jako U a pak ord("U") = 85

![[Pasted image 20240927232906.png]]
dá se tedy přeložit jako 
( passw[1]  XOR 85 ) - 59    != false
tím pádem se to musí rovnat a jde tedy použít 59 XOR 85 = password[1]

![[Pasted image 20240927233359.png]]
![[Pasted image 20240927233421.png]]

## vault-door-7 ==WIP==
![[Pasted image 20240927233613.png]]


## WinAntiDbg0x100
### Ve x64dbg
Ze začátku nám bylo řečeno že program nám bude bránit ve debuggování takže prostě začnem debuggovat
![[Pasted image 20240928180102.png]]
(ve VS nejde (nebo aspoň nevím jakl) debuggovat .exe, takže jsem si stáhl random opensource debugger)

debugování skončí po tomto řádku
![[Pasted image 20240928180241.png]]

takže asi něco musíme udělat s "==IsDebuggerPresent=="
 po několika malích skipech jsme tady
 ![[Pasted image 20240928180535.png]]
 ![[Pasted image 20240928180601.png]]
 ![[Pasted image 20240928180616.png]]
 musíme bypassnout jelikož tento kus to pak shodí
 
pokud to tedy nevidí žádný debugger tak se posune sem na push b
![[Pasted image 20240928181724.png]]
takže zkusíme setnout EIP / to kde jsem na push b a jet dál
![[Pasted image 20240928181916.png]]

po pár kroků vpřed máme flagu
![[Pasted image 20240928181659.png]]
00921634 | A1 08549200              | mov eax,dword ptr ds:[925408]           | 00925408:&"picoCTF{d3bug_f0r_th3_Win_0x100_cc0ff664}"

### V IDA
Postup
vyhledáme se searchem string "debugg"
tam si naklikneme na graf který obsahuje IsDebuggPresent
Dáme brakepoint na začátek a F8 postupujeme dál
U rozdvojky (jumpu) buď přepíšeme EAX, nebo setneme EIP tam kam chceme jít
![[Pasted image 20241012225344.png]]
## WinAntiDbg0x200
### Ve x64dbg
ze začátku nejde najít začátek ale po pár skipech už můžeme najít
![[Pasted image 20240928184831.png]]
![[Pasted image 20240928184856.png]]

stačilo znovu jen skipnout přes isdebuggerpresent
![[Pasted image 20240928185946.png]]
0019185F | 8B0D A0501900            | mov ecx,dword ptr ds:[1950A0]           | 001950A0:&"picoCTF{0x200_debug_f0r_Win_c6db2768}"
### V IDA
Zase s search „debugg“
![[Pasted image 20241012230920.png]]
Najdeme kus kde nám to kontroluje pro debugg s IsDebuggPresent

Dáme breakpoint
![[Pasted image 20241012231001.png]]
Spandne to dříve takže dáme další breakpoint na začátku grafu

Zasekne se nám to tady

**Vyřešení s SET EIP**
![[Pasted image 20241012231015.png]]
Setneme EIP doprava
![[Pasted image 20241012231030.png]]

Znova setneme doprava protože by to šlo doleva (IsDebugPresent by to detekoval)
![[Pasted image 20241012231055.png]]

flag
![[Pasted image 20241012231124.png]]

**Vyřešení s přepisováním**
![[Pasted image 20241012231151.png]]
Jumb if NOT zero

![[Pasted image 20241012231201.png]]
Přepsali jsme EAX na 1
![[Pasted image 20241012231211.png]]
Pozor musíme na testu, né na jumpu
![[Pasted image 20241012231218.png]]
Správně nám to skočí doprava

Zde nám to zase půjde nesprávně
![[Pasted image 20241012231234.png]]
Máme Jz = Jump if zero
Přepíšeme EAX na 0

![[Pasted image 20241012231244.png]]
A máme flagu.
## WinAntiDbg0x300 ==WIP==
vyzkoušet pak na vm

## Classic CrackMe 0x100
musel jsem si najít jak přesně se dokáže decompilovat bin -> dá se pomocí IDA
pro pseudocode F5
![[Pasted image 20240928193852.png]]




z chatgpt
![[Pasted image 20240928194236.png]]
![[Pasted image 20240928194220.png]]


## Asm1
Assembly
Source:

asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x3a2
	<+10>:	jg     0x512 <asm1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x358
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0x12
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0x12
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x6fa
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0x12
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0x12
	<+60>:	pop    ebp
	<+61>:	ret    

### Function Prologue:

1. `<+0>: push ebp` — Pushes the base pointer (EBP) onto the stack to save the caller's stack frame.
2. `<+1>: mov ebp, esp` — Sets EBP to the current stack pointer (ESP), establishing a new stack frame for this function.

### First Comparison:

3. `<+3>: cmp DWORD PTR [ebp+0x8], 0x3a2` — Compares the first argument (which is likely at `[ebp+0x8]`) with `0x3a2` (decimal 930).
4. `<+10>: jg 0x512 <asm1+37>` — If the argument is **greater than** `0x3a2`, jump to address `<+37>`, bypassing the following instructions.

### Second Comparison (if not greater than 930):

5. `<+12>: cmp DWORD PTR [ebp+0x8], 0x358` — Compares the argument with `0x358` (decimal 856).
6. `<+19>: jne 0x50a <asm1+29>` — If the argument is **not equal** to `0x358`, jump to `<+29>`.
7. `<+21>: mov eax, DWORD PTR [ebp+0x8]` — If the argument is equal to `0x358`, move its value into the `eax` register.
8. `<+24>: add eax, 0x12` — Add `0x12` (decimal 18) to the value in `eax`.
9. `<+27>: jmp 0x529 <asm1+60>` — Jump to `<+60>` to complete the function.

### Branch if Not Equal to 856:

10. `<+29>: mov eax, DWORD PTR [ebp+0x8]` — If the argument is not equal to `0x358`, move its value into `eax`.
11. `<+32>: sub eax, 0x12` — Subtract `0x12` (decimal 18) from the value in `eax`.
12. `<+35>: jmp 0x529 <asm1+60>` — Jump to `<+60>` to complete the function.

### Third Comparison (if greater than 930):

13. `<+37>: cmp DWORD PTR [ebp+0x8], 0x6fa` — Compare the argument with `0x6fa` (decimal 1786).
14. `<+44>: jne 0x523 <asm1+54>` — If the argument is **not equal** to `0x6fa`, jump to `<+54>`.
15. `<+46>: mov eax, DWORD PTR [ebp+0x8]` — If the argument is equal to `0x6fa`, move its value into `eax`.
16. `<+49>: sub eax, 0x12` — Subtract `0x12` (decimal 18) from `eax`.
17. `<+52>: jmp 0x529 <asm1+60>` — Jump to `<+60>` to complete the function.

### Branch if Not Equal to 1786:

18. `<+54>: mov eax, DWORD PTR [ebp+0x8]` — If the argument is not equal to `0x6fa`, move its value into `eax`.
19. `<+57>: add eax, 0x12` — Add `0x12` (decimal 18) to the value in `eax`.

### Function Epilogue:

20. `<+60>: pop ebp` — Restores the caller's base pointer by popping the old `ebp` value from the stack.
21. `<+61>: ret` — Returns from the function, transferring control back to the caller.

### Summary:

- If the argument is **equal to 856**, the function adds 18 to it.
- If the argument is **not equal to 856**, it subtracts 18 from it.
- If the argument is **greater than 930**, and **equal to 1786**, the function subtracts 18 from it.
- If the argument is **greater than 930** but **not equal to 1786**, it adds 18.
- The function always modifies the argument by either adding or subtracting 18, based on the conditions.

For `asm1` equal to `0x6fa` (1786 in decimal), the result of the calculation is **1768** 0x6e8

## Bit-O-Asm-1
![[Pasted image 20241012231503.png]]
![[Pasted image 20241012231507.png]]
![[Pasted image 20241012231511.png]]
![[Pasted image 20241012231515.png]]
Podle mého se jen přiřadí 0x30 do eax

Což je 48 v decimal

Ano, picoCTF{48}
## Bit-O-Asm-2
![[Pasted image 20241012231626.png]]
![[Pasted image 20241012231630.png]]
Podle mě eax se rovná DWORD PTR \[rbp-ox4]

Tak když se DWORD … rovná 0x9fe1a tak eax se rovná taky 0x9fe1a
![[Pasted image 20241012231705.png]]

## Packer
Dostali jsme Binary file. První ověříme, co je to vůbec za file s „file“
![[Pasted image 20241005173056.png]]
Executable. Zkusíme strings co nám vyjde (většinou jen nepoužitelný text, ale!)
![[Pasted image 20241005173114.png]]
![[Pasted image 20241005173118.png]]
Má UPX command na dekompresi?
Ano
![[Pasted image 20241005173130.png]]
![[Pasted image 20241005173135.png]]
Stačí tedy „upx -d -o out2 out“

Vyzkoušel jsem grep na "pico", "CTF" a "password". Password něco vyběhlo, takže zase stringneme.
![[Pasted image 20241005173211.png]]
Už jen stačí dát do cyberchefu
![[Pasted image 20241005173223.png]]

## Picker I
![[Pasted image 20241005173839.png]]
Po lounchi nám to dá 'Try entering "getRandomNumber" without the double quotes...'

když to dáme tak nám to vyhodí 4..
koukneme do sourcu :)
![[Pasted image 20241005174011.png]]
náš dice roll
![[Pasted image 20241005174040.png]]
zajímavá funkce win
vyzkoušíme
![[Pasted image 20241005174117.png]]
hex
takže stačí přeložit
![[Pasted image 20241005174141.png]]

## Picker II
od předchozího máme problém
![[Pasted image 20241005174353.png]]
![[Pasted image 20241005174430.png]]

něco budeme muset udělat s eval()
eval funguje že executne jestli může
![[Pasted image 20241005175710.png]]
teoreticky by jsme mohli dát do user_input něco co nám printne flagu
![[Pasted image 20241005180035.png]]
Můžeme rovnou printnout flagu?
ANO
![[Pasted image 20241005180126.png]]

## Picker III ==WIP==
![[Pasted image 20241005181144.png]]

## 
