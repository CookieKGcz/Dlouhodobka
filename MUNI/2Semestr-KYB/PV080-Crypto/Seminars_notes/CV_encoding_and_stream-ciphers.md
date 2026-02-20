## En/De-crypt as permutations
- Ciphers user the same $X, Y$ alphabet $X = Y$ and $PT.CT$ are represented by the same symbols.
- Since ciphers use same $X = Y$ and encryptions are one-to-one they form permutations.
- Hance encr/decr mappings $E, D : X \to X$ can be composed freely and the result mapping is still permutation of $X$.
	- whatever order
	- can be chained
```
CT1 = apply_mapping(Caesar_E, PT)
CT2 = apply_mapping(Caesar_E, CT1)

CT2 == 'migynyrn' # obtained from unknown PT

CPT = apply_mapping(Ceasar_D, CT2)
PT = apply_mapping(Caesar_D, CPT)
```
## Ways to define perm. based on secret key $k$.
- Caesar $E(K.x) = (K + x)(mod 26)$
- Atbash $E(K.x) = (K - x)(mod 26)$
- Noname $E(K.x) = (a*K + b*x)(mod 26)$

- RSA $E(K.x) = (x^K)(mod 26)$

- $E(K.x) = K \oplus x$
### Problematic - do not define 1-to-1 mapping
- $E(K.x) = (2k+ 4x)(mod 26)$
- $E(K.x) = x^6$
### Inverse perm.
- $D(K.ct) = a^{-1}(y - bK)(mod \ 26)$ (norm Noname)
- $D(K'.ct) = (y^{K'})(mod \ 26)$ (norm RSA)
## Statistical attacks
- Issue: $E$ just permute symbols in the text $\implies$ same letter frequencies in $PT, CT \implies$ statistical attack possible.
- Solution: encryption should produce randomly-looking $CT$.

1. Use different key (use different E) for each positions - **stream ciphers**.
2. Use very large alphabet so analysis is computationally impossible (e.g. $2^{128}$) - **block ciphers**.
## Stream ciphers
- To make graph flat it suffices to randomly change the encryption mapping $E$ for each position.
- That means to use stream of key (called **keystream**) $K_{0}, K_{1} \dots$ one for each position.

- Issues:
	- Practical: Keystream can be large - _keystream, PT, CT_ are all of the same size - GBs of data isn't possible.
	- Security: Keystream can be used only once
### Vernam
- bits
- XOR
- $CT = K \oplus PT$
	- => all same size
#### XOR properties
- $c = a \oplus b$
- $a = b \oplus c$
- $b = a \oplus c$
- $(A \oplus X) \oplus (B \oplus X) = A \oplus B$
#### Key reuse attack:
- When same $K$ was used to encrypt two plaintexts $PT_{1}, PT_{2}$ to corresponding plaintexts $CT_{1}, CT_{2}$. Two scenarios:
	- $CT_{1}, CT_{2}$ and $PT_{1}$ are known, then $K$ can be computed by
$$K = Vernam(CT_{1}, PT_{1}) = PT_{1} \oplus CT_{1}$$
$$PT_{2}=Vernam(K,CT_{2}) = (PT_{1} \oplus CT_{1}) \oplus CT_{2}$$
	- $CT_{1}, CT_{2}$ known then we will see the patterns when ciphertext are xored
$$CT_{1} \oplus CT_{2} = PT_{1} \oplus PT_{2}$$
- Issues:
	- $PT, CT$ pair reveals key $K = PT \oplus CT$
	- $CT_{1} \oplus CT_{2}$ cancel $K$ if reused for both ciphertexts
- Sol:
	- Key $K$ (Keystream) must be different (unique) for each massage.
### Chacha20
- encrypts plaintext by XORing it with a "Keystream" generated from a small key $K$.
$$CT = keystream \oplus PT = F(K) \oplus PT$$
- Issue: Keystream _keystream_ is as long as the message $(PT, CT)$ - imagine data in GBs.
- Sol: Generate it deterministically from small key $keystream = F(K)$ using some deterministic function

- Steps diff from vernam:
	1. keystream is generated from $K$ first,
	2. then XOR-ed with $PT$ for encryption.
```
PT = b"Whatever"
CT_XOR = XOR(keystream, PT)
CT_vernam = Vernam(keystream, PT)
CT_chacha = chacha20(PT, key, nonce)

CT obtained using XOR    = 21d081d9c58758e2405d
CT obtained using vernam = 21d081d9c58758e2405d
CT obtained using chacha = 21d081d9c58758e2
```
#### nonce
- Nonce (number once) is used together with $K$ to generate the keystream hence
$$CT = keystream \oplus PT = Stream_{cipher(PT, K, nonce)}$$
- nonce is not a secret, can be sent together with CT

- Issue: _keystream_ must be unique for each message
- Sol: _keystream_ generated as $keystream = F(nonce, K)$. It suffices to change nonce and send it with ciphertext, hence fixed $K$ can be used still.
- 