## Digital sig irl
- functionality - ==data integrity + data origin authentication + non-repudiation of data origin==
	- MAC - gives first two, but NO repudiation of origin
- Actual signing -> hash of data!

- Public key must be authentic and available
- Key steps
	- Key generation
	- Public-key cert/signing
	- Sig generation
	- Sig verification
## Public key ownership
- creating public-key certificate for X, will req:
	- public key of X,
	- evidence of being identified as 'X',
	- sometimes online challenge for private key ownership
- Public-key cert - issued y a trusted authority:
	- can be used with this authority being offline!
	- The cert authority must be trusted by those who should rely on the public key (relying party)
- Relying party - trusts (some) values in the certificate to make decisions:
	- TOFU - trust on first use (blacklisting)
	- COFU - check on first
## X.509v3
- ![[Pasted image 20260302101500.png | 400]]
### X.509b3 cert extension fields
- Critical / non-critical - encounter an extension field it doesn't know
	- critical = reject whole cert
- Example fields:
	- key-usage -> allowed key usage -> for sig, encryption, key agreement, CRL sigs
	- Extended-key-usage -> TLS server authentication
	- Subject-alternate-name -> email address, domain name, IP address, URI
	- Name-constraints -> CA controls of Subject names in subsequent cert when using hierarchical name spaces
## Public-key cert generation
- Public key - submitted typically by subject
- Certification authority checks:
	1. Evidence of corresponding private key control/knowledge
		1. logistics complicated
	2. Evidence of computer-addressable identity control/ownership
		1. easy
	3. Evidence of real-world identity/name ownership
		1. Complicated across borders/cultures, happens within a country/federation
- Public key + subject info + data set by policy -> ==all signed by CA private key==
	- CA public key must be available to relying parties

## Certificate chain validation
- ![[Pasted image 20260302102627.png | 450]]
## Public-key certificate revocation
- key compromised
- compromised detecred
- reported to CA
- report received, being processed
- revocation effected at CA
- revocation publicly available
- relying party sees revocation information
## Revoked cert
- != revoked public-key
	- recertification
- X.509 - Cert revocation list (CRL)
	- blacklist
	- not a list but pointers
- Online cert status protocol (OCSP)
	- Inquiring the CA whether a cert is (still) valid
	- Status = "good", "revoked", "unknown"
## PKI trust models
- cross cert
- ![[Pasted image 20260302103414.png | 450]]
- hierarchical
- ![[Pasted image 20260302103614.png | 400]]
## Timestamping
- timestamp - guarantee of data existence at the specified time
- typically a combination of digital sig with reliable clock info
- first of so-called digital notary services

# Legislation
## Relevant legislation
- eIDAS
- Regulation (EU) 2024/1183 of the European Parliament and of the Council of 11 April 2024 amending Regulation (EU) No 910/2014 as regards establishing the European Digital Identity Framework
## What does the regulation cover?
- Area of electronic identification (cooperation, identification, eID)
	- ID cards -> effort to build the so-called digital single market to enable mutual recognition if eID
- Area of trust services (alignment of regulation)
	- electronic:
		- sig, seal, timestamp
		- registered delivery
		- document
	- website auth
## eIDAS assurance levels
1. Low
2. Substantial
3. High
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:JOL_2015_235_R_0002
## Electronic sig - types (by eIDAS)
- Electronic signature
	- anything that the person uses to sign data
- Advanced elec. sig.
	- based on a certificate, but there are no requirements for it - it can be any certificate
- Qualified elec. sig.
	- must be based on a qualified cert for electronic signatures and must be created using a qualified means for creating electronic sign. (chip cards - eID or tokens)
### (Simple) electronic signature
- pdf signing
- email signature
- bank electronic signature
# Cryptographic protocols I
## Basic unilateral auth protocol
- ![[Pasted image 20260302110644.png | 500]]
## Crypto protocol
- algorithm specifying exchange of messages and actions taken between parties (entities)
- Goal/type
	- Entity auth protocol
	- Key established protocols
## Naive solution
1. A sends B the secret itself - S
	- B can impersonate A
2. A sends B hash of the secret - H(S)
	- B does not learn the secret, but can replay H(S) and thus impersonate A
3. Challenge-response (2-step) protocol proving password knowledge -> B challenges A with a random value e, A responds with H(r, P)
	- low entropy secret like a password the attacker can recover P
## Simple protocol example
- Challenge - response with symmetric cryptography
	- $A <- B: r_{B}$
	- $A \to B: E_{k}(r_{B}, \text{"B"})$
		- $r_{B}$ random num
	- Goal - unilateral auth. of A (= claimant) to B (= verifier)
- Proof of knowledge (of a secret)
	- instead of sending the secret as such,
	- Attacks obviously possible - TBD next week
	- Critical arbiter/3rd party issue
## Simple protocol examples II
- Proving the ability to use the private key
- In both cases below: A =claimant, B =verifier

- Through signing
	- $A <- B: r_{B}$
	- $A \to B: r_{A}, \text{"B"}, Sign_{A}(r_{A},r_{B},\text{"B"})$
		- B must have a trusted cert_A

- Through decryption
- $A <- B: h(r), \text{"B"}, Pub_{A}(r,\text{"B"})$
- $A \to B: r$
	- B must have Pub_A (from a trusted cert_A)
## Challenge-response with symm. crypto
- #todo 
## Authentication and key establishment I
- Typical combination - authenticated key establishment
- Session key
	- short-term purpose
	- typically symmetric key
	- Ephemeral key - destroyed at the session end, unrecoverable
## Key establishment
- simple public-key encrypted session key (K) examples:

- $A \to B: P_{B}(S_{A}(\text{"B"}, K, t_{A}))$
	- for sig schemes with message recovery
- $A \to B: P_{B}(K, t_{A}), S_{A}(\text{"B"}, K, t_{A})$
	- typically for sig schemes with appendix
## Authentication and key establishment II
- #todo 
## Key transport
- ![[Pasted image 20260302113951.png | 500]]
## Time variant parameters (TVPs)
- provide protocol message uniqueness or freshness (timeliness)
	- random number
	- timestamp
	- sequence number