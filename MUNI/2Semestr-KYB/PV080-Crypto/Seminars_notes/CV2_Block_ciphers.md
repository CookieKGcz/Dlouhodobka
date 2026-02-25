## AES basics
- Permutation on 16B blocks
	- Mathematically $AES_{K}:\{0,1\}^{128}\to\{0,1\}^{128}$
	- Different keys correspond to different permutations
	- Key has to be hard to guess -> random
- AES keys - 128, 192, 256 bits
- **16 byte blocks**
- last block is padded
- Avalanche effect: [[2 260223 - Crypto building block II]]
- Several modes of operation: ECB, CBC, CTR, CFB, OFB
	- some modes need IVs/nonces [[CV1_encoding_and_stream-ciphers]]



# notes
## PKCS7
- padding by "blocks" of 16 hex char?
- if we have msg of 3 hex chars -> we then have padding of 13 chars
	- if there is more then 16 chars it pads to n // 16 (we have 19 chars, padding is 13 chars)
- 