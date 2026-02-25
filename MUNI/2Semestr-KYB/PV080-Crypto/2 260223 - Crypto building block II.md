## ECB x CBC modes of operation
- ECB
	- $c_{i} = E_{k}(m_{i})$
	- $m_{i} = D_{k}(c_{i})$
	- - repetitions in message can reflect in ciphertext
	- main use: sanding few block of data
- CBC (cipher block chaining (with the previous block))
	- $c_{i} = E_{k}(m_{i}\oplus c_{i-1})$
	- $m_{i} = D_{k}(c_{i})\oplus c_{i-1}$
	- each ciphertext block is dependent on all message blocks before it
		- initial value (IV) must be known by both sender and receiver
			- IV cannot be sent in clear
		- at end of message have to handle padding problem
- ![[Pasted image 20260223101359.png | 400]]
### CTR mode
- counter mode
- $c_{i} = m_{i}\oplus E_{k}(N_{i})$
- ![[Pasted image 20260223101556.png | 400]]
- + instead of CBC, we can increase the counter so that we can decrypt the only parts we want to decrypt (saves time, processing..) (the CBC would have to decrypt every previous data that is "closer" to us)
- + Ad hoc access to encrypted data blocks and parallel processing

- must ensure to never reuse key/counter values
## Cryptographic alg. and/vs key
- Kerckhoffs' principle - a system security should not rely on the secrecy of its design details
	- cannot hardcode basically
- Algorithms:
	- with keys: ciphers, MAC, etc
	- without keys: hash functions, RNG.
# Hash functions - integrity
- property of data remains unaltered, except by authorized parties
## Cryptographic hash fce
- fixed-length output (hash value, message, digital fingerprint)
- "one way" - the decrypt one is so costly its basically impossible for now
## Cryptographic hash fce - properties
- Speed, avalanche effect
	- (any change of input results in completely different)(Single bit =  50% of output change)
- One-wayness
- Second preimage resistance (weak collision resistance)
	- given any first m1, it should be (computationally) infeasible to find any distinct second m2 such that H(m1) = H(m2). (**m1 is fixed**)
- Collison resistance (string collision resistance)
	- (computationally) infeasible to find any pair of distinct inputs m1, m2 such that H(m1) = H(m2). (**nothing is fixed**, "challenging" the attacker)
## Hash functions in use, deprecated
- ![[Pasted image 20260223104857.png | 500]]
## Hash function security - attack aspects
- Birthday paradox - generic method to find collisions
	- Complexity: O($2^{s/2}$) for hash size s
	- Collision $H(m_{i}) = H(m_{i})$ among $H(m_{i}), \dots, H(m_{2^{s/2}})$ for random messages
- MD5 (128 bit hash)
	- complexity ($2^{64}$) - 3 weeks of Super X computer
	- 1996 weakness found
- SHA1 - collision found in 2017
# Authentication
## Authentication with symmetric crypto
- entity authentication = proof of a shared key possession
- Data authentication:
	- based again on proof of shared key possession and
	- all (auth) data must be represented/processed
- Small tag added to protected data:
	- Two approaches: tag computed using block cipher or hash fce. (both use two inputs: key and message)
	- Verification: Tag computed same way (using shared key) compared with received tag.
## Message authentication code (MAC)
- ![[Pasted image 20260223110244.png | 500]]
### CBC-MAC
- Recall for CBC mode of block ciphers:
	- Each ciphertext block is dependent on all message blocks before it
- c_t is dependent on all previous blocks
	- And obviously also the key k
- c_t is the MAC value!
- ![[Pasted image 20260223110445.png | 400]]
## Keyed hash functions as MACs
- Original proposals like:
	- KeyedHash = Hash (Key|Massage),
		- weakness were found with this
- Eventually led to the development of HMAC.
### HMAC
- RFC2104
- $$HMAC_{K} = Hash[(K^+ \oplus opad) \ || \ Hash[(K^+ \oplus ipad)] \ || \ M]$$
- Where $K^+$ is the key:
	- opad, ipad are specific padding constants
## Authenticated encryption
1. Generic composition
	- MAC-plaintext-then-encrypt: encrypt both MAC PT and MAC tag together
		- Good sec., tricky padding, used in TLS
	- MAC-ciphertext-after-encrypt: PT encrypted without MAC, CT and both sent/stored together
		- Highest sec., 2 diff keys must be used for encryption and MAC!
	- Encrypt-and_MAC-plaintext: PT - input both fce, MAC tag appended to ciphertext and both sent/stored together
		- Good sec, Used in SSH
2. Authenticated encryption with associated data (AEAD)
### AEAD
- #todo 
# Public-key cryptography
## GCHQ "non-secret encryption"
- **Key distribution** motivation - primary desire that lead governments to research the topic:
	- Public keys don't have to be confidential
	- Decryption done with a private key that the sending party doesn't possess.
- Data auth. (digital signatures) - came as a aside effect:
	- Purpose (probably) not discovered by government
	- Allows for proofs to 3rd parties, unlike MAC
	- Due to speed relying on hash fce.
## Public-key cryptography
- Key pair:
	- public key - encr
	- private key - decr
- Key distribution - symmetric/shared and public-key
- Public key - integrity and ownership/affiliation critical
- Private key - confidential critical
- One directional communication Bob -> Alice, Alice generates key-pair
## RSA
- For Bob -> Alice communication, Alice generates :
	1. Secret primes p, q and public:   n = p . q
	2. Public exponent $e_{A}$:                   $gcd(e_{A}, \phi(n)) = 1$
	3. Private exponent $d_{A}$ from $e_{A}$:    $d_{A} = e_{A}^{-1}mod \phi(n)$

	- Encryption - public key (n, eA):    $E_{A}(m) = m^{e_{A}} mod (n) = c$
	- Decryption - private key (n, dA):  $D_{A} (c)= c^{d_{A}} mod(n) = m$
### RSA - toy example
- ![[Pasted image 20260223113403.png | 500]]
## Shared-key and public-key encryption
- ![[Pasted image 20260223113501.png | 400]]
- #todo 
## Hybrid encryption
- ![[Pasted image 20260223113532.png | 450]]
- main data encrypted using symmetric key k, while k is made available by public-key methods
## Digital signature
- Non-repudiation of origin (cf. symmetric/shared key crypto!)
## Public-key operations
- ![[Pasted image 20260223113801.png | 450]]
- #todo 
## Using the same key for two purposes
- possible for some algorithms - RSA.
- sometimes created for this purpose - DSA
	- So that they don't allow encryption to hide information from spying
- Even if possible, it is strongly not recommended using the same key for two purposes!
## Requirements - public-key
- Recovering private key from public key and ciphertexts (any amount) not possible.
- Recovering plaintext from ciphertext and public key not possible (computational infeasibility)
## Digital signature in reality
- #todo 
# Security requirements and key sizes
## Speed of algorithms
- ![[Pasted image 20260223114452.png | 500]]
## Brute-force attacks (symmetric crypto)
- #todo 
## Algebraic attacks (asymm.)
- RSA modulo factorization:
	- 2020 RSA-250 829 bits (2700 core years)
- DLP in Zp:
	- 2019 795bit prime (3100 core years)
- DLP in EC:
	- 2020 114 bit interval (13 days, 256x GPU)
## Comparable strengths
- #todo 
