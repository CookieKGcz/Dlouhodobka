## Shared key established by pub. agreement
- DH key agreement - first published concept in public key cryptography (1976)

- Alice -> Bob
	- $g^a \ mod \ p$
- Alice <- Bob
	- $g^b \ mod \ p$

- both have $g^{ab} \ mod \ p$
## MitM attack
- ![[Pasted image 20260309100609.png | 400]]
## Some attacks on auth. protocols

| Attack         | Description |
| -------------- | ----------- |
| replay         | #todo       |
| reflection     |             |
| relay          |             |
| interleaving   |             |
| middle-person  |             |
| dictionary     |             |
| forward search |             |
| pre-capture    |             |
## Station-to-station (STS) protocol
- Turns unauth. DH into auth DH, using signatures.
- A -> B: $g^a$
- A <- B: $g^b, \{ S_{B}(g^b, g^a), cert_{B}\}_{K}$
- A -> B: $\{S_{A}(g^a, g^b), cert_{A}\}_{K}$

- K is derived as in DH, not shared before the protocol run.
## Key auth - properties
- ![[Pasted image 20260309101219.png|300]]
- Good session key:
	- fresh, suff. long, known whom it's shared with
- **Forward secrecy**: should not learn the keys from the past
- **Ephemeral** = key vanishes at the end of session.
- **Known-key security**: when attacker compromises session keys they should not be able to impersonate/compromise future sessions.
## Needham-Schroeder (symm) protocols
- S = server trusted by A and B

- A -> S: $A, B, N_{A}$
- S -> A: $\{N_{A}, K_{AB}, B, \{K_{AB }, A\}_{K_{BS}}\}_{K_{AS}}$

- A -> B: $\{K_{AB}, A\}_{K_{BS}}$
- B -> A: $\{N_{B}\}_{K_{AB}}$
- A -> B: $\{N_{B} - 1\}_{K_{AB}}$

- Replay attack with knowledge of old K_AB -> M replays old {K_AB, A}\_KBS -> B cannot tell unless logging all old values
## Fixed N-S (symm) protocols
- Timestamp deployed in Kerberos (later), also can be fixed by a nonce:

- #todo 
- ![[Pasted image 20260309102516.png| 300]]
- $N'_{B} \neq N_{B}$
## Needham-Schroeder public key protocol
- #todo 
- ![[Pasted image 20260309102711.png | 180]]

- MitM attack:
	- if Mallory being able to convince Alice to initiate the protocol with her,
	- then Bob believes that he communicates with Alice while he communicates with Mallory
### Lowe's attack
- #todo 
- ![[Pasted image 20260309102919.png|200]]
### Needham-Schroeder-Lowe protocol
- easy fix -> be explicit in protocol
- ![[Pasted image 20260309103147.png|200]]
## Kerberos
- Protocols suite for mutual auth.
	- communication of nodes in an insecure network
	- client-server applications
	- symm-key crypto
- Client: user provided username and password on client machine
- Client auth itself to AS
- AS forwards the client ID/name to Key Distrib. Center (KDC)
- KDC issues ticket-granting ticket (TGT)
	- time-stamped
	- encrypted with ticket-granting service (server) key
## Simplified version of auth. protocol
- #todo 

# TLS protocol family
- Transport layer sec. protocol
	- Handshake layer/protocol
		- Key exchange
		- Auth of server
		- Setting of server-selected params.
		- Design intent for handshake
	- Record layer/protocol
- TLS provides
	- Confidentiality of application data -> encrypted
	- Integrity of application data -> AEAD (MAC for TLS/SSL)
	- Entity authentication (server, mutual or none (rare))
## TLS info
- Above TCP layer and below appl. layer
- HTTPS = HTTP Secure most frequent
- Dating from 1995
## Key exchange and entity auth. in TLS
- Master key - shared secret between client and server
	- both client and server nonces contribute
	- Three options:
		- DH ephemeral, with RSA / elliptic curves
		- PSK - pre-shared key
		- PSK with DHE (PSK alone does not provide forward secrecy)
- Server authentication (to client) with several options
	- Proof of knowledge of private key
		- RSA sig
		- PSK - rare

- ![[Pasted image 20260309105502.png | 450]]
## Encryption and data auth. in TLS
- Block cipher - AES (GCM, CCM - AEAD-integrated MAC)
- Stream cipher - ChaCha20 (Poly1305 MAC)
## TLS attacks
- Problems with implementations - Heartbleed (OpenSSL) allowing the attacker to acquire private keys from a vuln. TLS server.
- Downgrade - forcing the server to use older crypto alg.
- Padding - exploiting padding oracle (Lucky Thirteen)

- TLS interception (MitM) - when a new certificate is not properly checked (exploit of CA services)
	- network operator gets the traffic unencrypted
## Secure Shell (SSH)
- provides secure channel over an unsecured network

- Transport layer protocol
	- server auth
	- negotiation of crypto params. and keys
	- encryption and integrity protection
- User auth protocol
- Connection protocol - enables usage of one SSH connection for multiple purposes.
## Auth - big picture
- #todo 



# Crypto in quantum computer era
- parallel computation is much much faster

- threat for asymm crypto -> 




# Midterm info
- 5 questions - 4 easier + 1 harder (4x2 + 4 points) = 12 points
- then divided by 4, so 3 points max