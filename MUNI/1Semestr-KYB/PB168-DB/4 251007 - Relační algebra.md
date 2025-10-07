## Relational Model - Revision
- Given attribute names A1, A2... An
	- Schema R is an ordered tuple R=(A1, A2, ... An)
- Given attributes domains D1, D2, ... Dn corresponding to A1, A2, ... An
	- Relation r on the chema R is
		- r ⊆ D1 x D2 x … x Dn
- r = set of n-tuples (a1, a2, .. an) where ai in Di
![[Pasted image 20251007161507.png | 400]]
## Query Lan. examples
- Given a relation 
	- loan (loan_number, branch_name, amount)
- Query:
	- Return all loans having amount greater than $ 1,200

- Relation algebra
	- sigma_(amount > 1200) (Loan)$$\sigma_{amount \ > \ 1200 } (loan)$$
- Tuple relational calculus $$\{ t |t \in loan \střížka \ t[amount] > 1200\}$$
- Doamin relation calculus
	- ![[Pasted image 20251007162159.png]]
- SQL
	- SELECT loan_number, branch_name, amount FROM loan WHERE amount > 1200
- Apache Pig Latin
	- A = LOAD ‘loan’ as (loan_number, branch_name, amount)
	- B = FILTER A BY amount > 1200
	- DUMP B;
## Relational Algebra
- Procedural language
- Six operations
	- Select: ![[Pasted image 20251007162423.png]] (unární, jako fce)
	- Project: ![[Pasted image 20251007162433.png]]
	- Union: ![[Pasted image 20251007162443.png]] (binární , napsaná mezi)
	- Set difference: ![[Pasted image 20251007162501.png]]
	- Cartesian product: ![[Pasted image 20251007162518.png]]
	- Rename: ![[Pasted image 20251007162530.png]]
- Principle:
	- An operation takes one or two relations as input and produce a new realtion as a result.
		- So, another operation can be applied to this result.
## Select
![[Pasted image 20251007162725.png | 300]]
## Project
![[Pasted image 20251007162858.png | 300]]
## Union
![[Pasted image 20251007162958.png | 350]]
(Kdyby s bylo ABC tak se C nepřidá !) (musí být kompatibilní)
## Set Difference
![[Pasted image 20251007163245.png | 350]]
## Cartesian-Product
![[Pasted image 20251007163313.png | 350]]
## Composition of Operations
![[Pasted image 20251007163507.png | 400]]
## Rename and Cartesian-Product
- r (A,B,C)
- s (C, D, E)
- pro evaluaci r x s, potřebujeme přejmenovat atributy$$r × p_{ s(sC,D,E)} (s)$$
- plus existuje tečková notace![[Pasted image 20251007164218.png]]
## Constant Relation
- A relation that is “manually” written as an expression.
- {('A-973', 'Perryridge', 1200)}
- Rename operation is usually applied to name the attributes.
- Pro vkládání do tabulky
## Příklad Banking
![[Pasted image 20251007165035.png | 500]]
## Příklad Queries
- Vztahy:
	- loan (loan_number, branch_name, amount)
	- depositor (customer_name, account_number)
	- borrower (customer_name, loan_number)
- Find all lones of over 1200
	- ![[Pasted image 20251007165440.png]]
- Find the loan number for each loan of an amount greater than $1,200
	- ![[Pasted image 20251007165459.png]]
- Find the names of all customers who have a loan, an account, or both, from the bank
	- ![[Pasted image 20251007165524.png]]

- Vztahy:
	- customer (customer_name, customer_street, customer_city)
	- loan (loan_number, branch_name, amount)
	- borrower (customer_name, loan_number)
- Find the names of all customers who have a loan at the Perryridge branch
	1. ![[Pasted image 20251007170945.png]]
	2. ![[Pasted image 20251007170956.png]]

- Vztahy:
	- loan (loan_number, branch_name, amount)
	- depositor (customer_name, account_number)
	- borrower (customer_name, loan_number)
- Find the names of all customers who have a loan at the Perryridge branch but do not have an account at any branch of the bank.
	1. ![[Pasted image 20251007172251.png]]

- account (account_number, branch_name, balance)
- Find the largest account balance
	- Strategy:
		- Find those balances that are not the largest
			- Rename account relation as d so that we can compare each account balance with all others
		- Use set difference to find those account balances that were not found in the earlier step
	- query is: ![[Pasted image 20251007172719.png]]
## Natural-Join
- přirozené spojení
![[Pasted image 20251007173236.png | 350]]
## Outer Join
- extention of the natural join operation
	- avoids loss of information
- Missing rows in result of natural joins
![[Pasted image 20251007173824.png | 500]]
### Left Outer Join
![[Pasted image 20251007173909.png | 500]]
### Right Outer Join
![[Pasted image 20251007173934.png | 500]]
### Full Outer Join
![[Pasted image 20251007174001.png | 500]]
## Aggregate Functions
- avg
- min
- max
- sum
- count
![[Pasted image 20251007174233.png | 300]]
![[Pasted image 20251007174250.png | 400]]
![[Pasted image 20251007174302.png | 400]]
![[Pasted image 20251007174322.png | 450]]
## Modifikace tabulek
- Deletion
- Insertion
- Updating

- Značení:
	- r <- E
	- It can be used to store intermediate results
		- ![[Pasted image 20251007174543.png]]


## Cvičení - After notes
### 2
- Uvažujte tři atributy jméno, příjmení a platová_třída.

- Mějme následující relační schémata
- R1=(jméno, příjmení, platová_třída)
- R2=(jméno, příjmení)
- R3=(příjmení, jméno, platová_třída)
- Liší se? Jak?
### 3
### 4
- Mějme relaci
![[Pasted image 20251007180348.png | 400]]
- Formulujte výraz v relační algebře pro dotazy:
	- Předměty s názvem "Paralelní výpočty"
	- Předměty s více jak dvěma kredity.
$$T_{kód}(G_{název='Par.Vý'} (předmět))$$
### 6
![[Pasted image 20251007180754.png | 400]]
- Napište výraz v relační algebře, který vrací
	- ❑ kódy předmětů s názvem ‘Paralelní výpočty’;
	- ❑ názvy předmětů, které mají alespoň tři kredity;
	- ❑ kódy a ukončení předmětů, které mají ukončení vyšší než zápočet
		- možná ukončení jsou {‘z’, ‘k’, ‘zk’}
$$T_{kód, ukončení}({ G_{ukončení = 'k' \ \text{v} \ ukončení = 'zk'} (předmět) })$$
### 11
- Mějme relace:
	- předmět ( kód, název, kredity )
	-  skupina ( kód, číslo, kapacita )
	- zápis ( učo, kód )
	- student ( učo, jméno )
- Sestavte výrazy relační algebry, které vrací:
	-  jména studentů, kteří mají zapsaný předmět ‘PB168’;
$$ T_{jméno}(student \bowtie T_{učo} (G_{kód = 'PB168'}(Zápis)))$$

- čísla skupin předmětu s názvem ‘UNIX’, které mají kapacitu menší než 10;
$$T_{číslo}(G_{název='UNIX'}(G_{kapacita<10 \ \  \cap \ předmět.kód = skupina.kód }(skupina \ \times \ předmět)))$$
nebo místo x bude natural join |><|


- názvy a počty kreditů předmětů, které má zapsaný student ‘Tomáš’.
$$G_{jméno = 'Tomáš'}(student \bowtie zápis \bowtie předmět)$$

- Napište výraz vracející učo studentů, kteří mají zapsané předměty ‘PB154’ a ‘MA102’ současně
$$T_{učo}(G_{kód='PB154'}(zápis)) \bowtie T_{učo}(G_{kód='MA102'}(zápis))$$
### 13
- Mějme relace:
	- předmět ( kód, název, kredity )
	-  skupina ( kód, číslo, kapacita )
	- zápis ( učo, kód )
	- student ( učo, jméno )
- kódy a názvy předmětů, které nemá zapsaný žádný student;
$$T_{kód, název}(G_{učo \ is \ NULL}(předmšt \ left\bowtie zápis))$$
- jména studentů, kteří nemají zapsaný žádný předmět; ???????
$$G_{count = 0}(_{kód, název}Q_{count(učo)}(předmět \ ⟕ zápis))$$
- názvy všech předmětů, které mají alespoň dvě skupiny. ???????????

### 19? SQL
select kod, count()





cheat sheet
- σ (selekce)
    
- π (projekce)
    
- × (kartézský součin)
    
- ∪ (sjednocení)
    
- − (rozdíl)
    
- ρ (přejmenování)
    
- ∩ (průnik) – lze odvodit
    
- ⨝ (přirozené spojení) – lze odvodit