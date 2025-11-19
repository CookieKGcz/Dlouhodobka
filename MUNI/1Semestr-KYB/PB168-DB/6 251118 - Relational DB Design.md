## Combine smaller schemas
- Suppose we combine instructor(ID, name, salary, dept_name) and department(dept_name, building, budget) into inst_dept
- Suppose we had started with
	- inst_dept (ID, name, salary, dept_name, building, budget)
- How would we know to split up decompose into instructor and department tables?
	- Denote as a functional dependency:
		- dept_name → building, budget
- In inst_dept, because dept_name is not a candidate key, the building and budget of a department may have to be repeated.
	- This indicates the need to decompose inst_dept
## Lossy decomposition
![[Pasted image 20251118161459.png | 500]]
### example:
![[Pasted image 20251118161532.png | 500]]
## Functional Dependencies
 - A → B
	 - holds on R if and only if for any legal relation r(R), whenever any two tuples t1 and t2 of r agree on the atributes A, they also agree on the attributes B. That is:
$$t_{1}[\alpha] = t_{2}[\alpha] \implies t_{1}[\beta] = t_{2}[\beta]$$
- read A -> B as "B depends on A"
- exaple:
	- ![[Pasted image 20251118164112.png | 400]]
- K is a superkey for a relation schema R if and only if K → R
- K is a candidate key for R if and only if:
	- ![[Pasted image 20251118164215.png | 200]]
- Meaning: there is only one value for each value of K
- Functional dependencies allow us to express constraints that cannot be expressed using superkeys.:
	- Consider the schema: inst_dept (ID, name, salary, dept_name, building, budget)
	- We expect these functional dependencies to hold:
		- ![[Pasted image 20251118164310.png | 200]]
		- only one building for each department
	- but would not expect the following to hold:
		- dept_name -> salary

- We use functional dependencies to:
	- test realtions to se if they are legal under a given set of funct. depend.
	- specify constraints on the set of legal relations

## Closure of a Set of Functional Dependencies
- Given a set F of functional dependencies, there are certain other functional dependencies that are logically implied by F.
	- If A → B and B → C, then we can infer that A → C
- The set of all functional dependencies logically implied by F is the closure of F.
	- We denote the closure of F by F+
	- F+ is a superset of F.
## Boyce-Codd Normal Form
- A relation schema R is in BCNF with respect to a set F of functional dependencies if for all functional dependencies in F+ of the form A -> B
- where A <= R and B <= R, at least one of the following holds:
	- A -> B is trivial (B <= A)
	- A is a superkey for R (A -> R)

- example schema not in BCNF
	- instr_dept (ID, name, salary, dept_name, building, budget )
	- because dept_name → building, budget holds on instr_dept, but dept_name is not a superkey.
### Decomposing a Schema into BCNF
![[Pasted image 20251118170158.png | 500]]

## Third Normal Form
- A relation schema R is in third normal form (3NF) if for all: A → B in F+
- where A <= R and B <= R, at least one of the followeing holds:
	- A -> B is trivial (B in A)
	- A is a superkey for R
	- Rach attribute A in B - A is contained in a candidate key for R
		- each attribute may be in a different candidate key

- If a relation is in BCNF, it is in 3NF Since in BCNF one of the first two conditions above must hold
- Third condition is the minimal relaxation of BCNF to ensure dependency preservation (will see why later).

## Closure of a Set of Functional Dependencies
- Given a set F of functional dependencies, there are certain other functional dependencies that are logically implied by F.
	- If A -> B and B -> C, then we can infer that A -> C
- The set of all functional dependencies logically implied by F is the closure of F.
- We denote the closure of F by F +

- We can find F+, the closure of F, by repeatedly applying Armstrong’s Axioms:
	- if B <= A, then A -> B    (reflexivity)
	- if A -> B, then y A -> y B  (augmentation)
	- if A -> B, and B -> y, then A -> y  (transitivity)
### example:
![[Pasted image 20251118172248.png | 400]]

## Shrnutí
BCND <= 3NF <= 2NF <= 1NF


# Cvičení Funkční závislosti
## Tvorba fun. závislosti a jejich platnost
- Uvažujte evidenci zapsaných předmětů s následujícími požadavky
	- Student má jméno a své jedinečné UČO; 
		- učo -> jméno
	- Předmět má název, počet kreditů a svůj jedinečný kód; 
		- kód -> název, počet kreditů
	- Student si zapisuje více předmětů;
		- učo, kód -> ukončení (z vytvoření tabulky učo, kód)
	- Předmět si může zapsat více studentů;
		- učo, kód -> ukončení (z vytvoření tabulky učo, kód)
	- Student má pro zapsaný předmět zvolené určité ukončení.
		- učo, kód -> ukončení
- Formulujte funkční závislosti

## Třetí normální forma
- ![[Pasted image 20251118184851.png | 450]]
- ![[Pasted image 20251118184910.png | 500]]
- vedoucí -> vedoucí_katedra VADÍ

- 