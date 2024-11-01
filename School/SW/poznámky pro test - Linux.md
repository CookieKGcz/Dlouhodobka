## **Základy:**

### Opakovaní
nápovědy => `man`, `--help`, dokumentace, `info`

Distribuce  = rozšířeno o další software
Unix -> dvě rodiny -> RedHat (centos) / Debian (ubuntu)

### Správa sys. Linuxu
`df -h` => disk free -> zobrazí využití disku
`tap` => využití paměti
`ps` => běžící procesy
`kill` => pošle signál procesu (jeho PID)
### Správa disku
MBR `fdisk` / GPT `gdisk` => vytvoření oddílů
`mkfs` => formátování
	ntfs / ext2,3,4 / FAT32,64, swap (při nedostatku operační paměti)
`mount` => připojení filesys

### Zálohování dat
`dd` k zálohování disků a oddílů
	`dd if=/dev/sda of=/sys.img`
`tar` jen pro skupinu souborů

### LVM
`pvcreate`
`vgcreate`
`lvcreate`

fyzické svazky (PV) -> celé disky
skupina svazků (VG) -> z x fyz svaz
logický svazek (LV)

### RAID
`mdadm` prostě pro raid

### Správa uživatelů
`adduser` lepší
`useradd` jen user
`usermod` modifikace

v etc/passwd o uživateli
==v etc/shadow== jsou uloženy hesla

### Oprávnění
`ls -l` pro vypsání (- soubor, -d adresář..)
`chmod` chmod a+rwx, g-wx, o-wx file.txt

### DNS
spouštění `systemctl`
pro test `host web1.com` -> vypíše IP
pro test `host 192.168.0.24` -> vypíše doménu

locálně v /etc/hosts
daemon - ==bin==
zony
- mapuje název domény s IP adresou
- /var/named/dsdsdsd.firma.com
dělení
- dopředná - název na IP
- Zpětná - IP na název
- PTR pro zpětné vyhledávání

### DHCP
config v `/etc/dhcp/dhcpd.conf`
automaticky přiděluje IP

dvě hlavní části
- globální parametry (síťové parametry)
- deklarativní část (optiony pro individuální subnety)

### LDAP (něco jako Active dir)
daemon -> `slapd`
Soubory `LDIF`
config `/etc/ladp.conf`

light weight directory access protocol
pro správu objektů -> skupin, userů, počítačů, řadičů

--> Záznamy -> DN (distinguished name) -> s atributy jako "cn" common name nebo "mail"

### FTP
daemon `vsftpd` (very secure ftp daemon)
config `/etc/vsftpd/vsftpd.conf`
- povolení přístupu pro uživatele
- omezení šířky pásma
- omezení na porty v rozsahu
==na straně klienta jen ftp==

file transfer protocol
pro komunikaci a přenos souborů mezi vzdáleným serverem a klientem

### Webový server Apache
spouštění `systemctl`
config v `/etc/apache2/apache2.conf` nebo v `/etc/httpd/conf/httpd.conf`
DocumentRoot v `/var/www/html`
==direktivy = configurační parametry== web serveru (další třeba Listen)
hesla v `/var/www/html/secret`
SSL v /etc/httpd/ssl-certs
- vygenerování `openssl req -x 509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/httpd/ssl-certs/apache.key -out /etc/httpd/ssl-certs/apache.crt`

podporuje vícero webů
server pro http -> 80 443
daemon `squid`

### Virtualizace a Kontejnery
`qemu` nástroj pro virtualizaci
pro práci `virsh`

kontejnerizace = bare OS a aplikace
+ + lehký

### Bootvání
1. POST test - zíkladní test hardware
2. vyhledání zavaděče
	1. BIOS - MBR
	2. UEFI - EFI
	3. GRUB (boot manager)
3. načte kernel a obraz initrd nebo initramfs
4. detekuje hardware důkladně
5. mountne disky (root složku)
6. první proces PID 1 -> soupští daemony

init runlevely
systemd targety
- Runlevel 0 - poweroff.target - rychlé vypnutí
- Runlevel 1 - rescue.target - režim údržby 
- Runlevel 2 - multi-user.target - grafické rozhraní
- Runlevel 3 - graphical.target - bez graf rozh
- Runlevel 5 - reboot.target
- Runlevel 6 - emergency.target - restart


Sure! Here's a breakdown of the solutions for each of the questions:

---

**1. Charakterizujte komerční software. Kdo definuuje způsob používání takového software a kde jsou stanovena pravidla pro jeho používání?**

- **Komerční software** je placený software, který je vytvořen pro prodej a využití firmami nebo jednotlivci. Způsob jeho používání je definován licenční smlouvou, kterou stanovuje vývojář nebo firma. Pravidla pro jeho používání jsou obvykle stanovena v dokumentu zvaném **EULA (End User License Agreement)**.

---

**2. Vysvětlete rozdíl mezi pojmy Linux a distribuce. Vyjmenujte dvě nejběžnější rodiny linuxových distribucí.**

- **Linux** je jádro operačního systému (kernel), které poskytuje základní funkcionalitu OS.
- **Distribuce** je kompletní balík, který zahrnuje jádro Linuxu a další aplikace, knihovny a nástroje, které spolu tvoří plnohodnotný OS.
- Dvě hlavní rodiny distribucí: 
  - **Debian-based (např. Ubuntu)**
  - **Red Hat-based (např. Fedora)**

---

**3. Jaký je rozdíl mezi low-level tools a high-level tools nástroji pro práci s balíčky? Uveďte jeden příklad pro každý typ nástroje.**

- **Low-level tools** jsou základní nástroje, které přímo manipulují s balíčky a závislostmi. Příklad: **dpkg** (pro Debian-based systémy).
- **High-level tools** jsou uživatelsky přívětivější a automatizují proces správy balíčků. Příklad: **apt** (Debian-based systémy) nebo **yum** (Red Hat-based systémy).

---

**4. Které operace je třeba v Linuxu provést, abychom mohli číst a zapisovat data na úplně nový a dosud nepoužitý disk? Ke každé operaci napište vhodný příkaz.**

1. **Vytvoření oddílů:** `fdisk /dev/sdX` (kde X je označení disku)
2. **Formátování:** `mkfs.ext4 /dev/sdX1` (formátování oddílu)
3. **Připojení disku:** `mount /dev/sdX1 /mnt`

---

**5. Vysvětlete princip funkce LVM.**

- **LVM (Logical Volume Manager)** umožňuje flexibilní správu disků. Pomocí LVM lze spojit několik fyzických disků do jednoho logického disku, který lze snadno rozšiřovat nebo zmenšovat podle potřeby, aniž by bylo nutné zastavovat systém.

---

**6. Uveďte příkaz pro přidělení oprávnění pro provoz vlastníka, oprávnění pro skupinu vlastníka a oprávnění pro ostatní uživatele. Předpokládejme, že k souboru zatím nemá nikdo nastavená žádná oprávnění.**

- Použijte příkaz `chmod`. Například:
  - `chmod 755 file.txt`
  - To znamená: vlastník má plná práva (7), skupina a ostatní mohou číst a spouštět (5).

---

**7. Charakterizujte službu DHCP. Jak se jmenuje konfigurační soubor služby DHCP?**

- **DHCP (Dynamic Host Configuration Protocol)** je služba, která automaticky přiřazuje IP adresy klientům v síti.
- Konfigurační soubor pro DHCP službu v Linuxu je obvykle **/etc/dhcp/dhcpd.conf**.

---

**8. Jaký je účel služby FTP? Uveďte název balíčku zajišťujícího v Linuxu funkci služby FTP.**

- **FTP (File Transfer Protocol)** slouží k přenosu souborů mezi počítači v síti.
- Balíček zajišťující funkci FTP v Linuxu může být například **vsftpd**.

---

**9. Vysvětlete pojem virtuální PC a uveďte příklad nástroje pro virtualizaci v UNIX-like OS.**

- **Virtuální PC** je emulovaný počítač běžící uvnitř jiného počítače pomocí virtualizačního softwaru.
- Příklad nástroje pro virtualizaci v UNIX-like systémech: **KVM** (Kernel-based Virtual Machine) nebo **VirtualBox**.

---

**10. Uveďte důvody, kdy je vhodné mít vlastní síťový repozitář.**

- Vlastní síťový repozitář může být vhodný, pokud potřebujete:
  - Zajistit rychlejší a spolehlivější přístup k balíčkům.
  - Udržovat vlastní verze softwaru nebo specifické konfigurace.
  - Udržet kontrolu nad verzemi softwaru používaného v síti.

---

**11. Doplňte pojmy do následujícího textu:**

"Po stisku tlačítka pro zapnutí počítače spustí firmware uložený v paměti EEPROM test **POST (Power-On Self Test)**, který zkontroluje funkčnost hardwaru počítače. Následně vyhledá **boot loader**, který se nachází v **MBR (Master Boot Record)** nebo diskovém oddílu **/boot** na prvním disku a předá mu řízení. V dalším kroku se načte a spustí **kernel**. V Linuxu se obvykle jedná o GRUB. Ten načítá **init** a obraz, které jsou **kernel image**."

---

**12. Vysvětlete účel archivace. Kromě archivace lze vytvořený archiv i komprimovat. Uveďte metody komprese používané při archivaci a stručně je charakterizujte.**

- **Archivace** slouží k ukládání souborů do jednoho balíčku pro snazší správu a přenos.
- Při archivaci lze použít kompresní metody, jako je:
  - **gzip**: Rychlá komprese s dobrou úrovní zmenšení.
  - **bzip2**: Pomalejší, ale s lepším kompresním poměrem než gzip.
  - **xz**: Nabízí vysoký kompresní poměr, ale je pomalejší.

---

Let me know if you'd like any further clarification!