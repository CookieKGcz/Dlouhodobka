## Standardization in security
- compatibility of components
- reduction of mistakes
- interchangeability
- reduce costs of both system and also of user training

- ! mare existence of a standard does not oblige anybody
	- application must be specifically req.
- Standards already mention: Common Criteria, ISO27000, standardized algs like AES, DES, SHA-3...

- International/European/National
	- ***BS***
## Cryptographic algorithms
- national interest
- some scheming things with US and Russia
## Standards in security
- ISO (International Organization of Standardization)
	- 1947, HQ in Geneva
	- many relevant standards with international electrotechnical commission (ISO/IEC)
		- takes long (3+ y, but reduces mistakes)
	- standards valid for 5 y, must be reviewed and then revised or reissued
- Internet Engineering Task Force (IETF) - open standards organization
	- RFC
## NIST standards
- National Institute of Standards and Technology
	- under the US Department of Commerce
	- FIPS PUB = *Federal Information Processing Standards PUBlication*
	- SP - *Special Publication*

- FIPS 140             - Security Requirements for Cryptographic Modules
- FIPS PUB 180-4  - Secure Hash Standard (SHS) = SHA-2
- FIPS PUB 186-4  - Digital Signature Standard (DSS)
- ...
## Security evaluation criteria
- USA - 60/70's
- need to minimize costs of gov. institutions when requesting, comparing and selection secure computing systems individually
	- 1985 - Trusted Computer System Evaluation Criteria - "Orange Book"
		- D-A grading
- Europe - ITSEC - split of functionality and assurance
- Canada - CTCPEC - functionality split to confidentiality, integrity, accountability, availability
- US - Federal Criteria - development halted
- Common criteria - worldwide standard - ISO/IEC 15408
## Common Criteria
- Common Criteria for Information Technology Security Evaluation
	- latest - v 3.1, 2017
- Evaluation is requested (and paid for) by application (vendor/manufacturer) with a security *claim* - this is verified and either certified or debunked
- Functionality - what security functions does the evaluated system/product have
- Assurance - ground for confidence that it meets its security objectives
## Common Criteria concepts
- Target of evaluation (TOE) - what is evaluated
- Protection profile (PP) (smartcards, biometrics, ...)
- Security target (ST) - theoretical concept/aim
- Security Functional Requirements (SFRs) - individual sec. functions provided by the TOE

- Evaluation of TOE - is the reality corresponding to the claim (ST)?

### Assurance
- grounds for confidence that a TOE meets the SRFs
- 7 levels
- Hierarchical system
## CC - going for eval
1. Define the product/system for eval
2. Specify functionality
3. Specify the assurance level claimed
4. See details of eval with a certification body
5. Prepare evidence
## Common Criteria model
- ![[Pasted image 20260511103358.png|300]]
- [[6 260323 - Privacy]]
