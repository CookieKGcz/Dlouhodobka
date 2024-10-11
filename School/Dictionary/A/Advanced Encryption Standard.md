#AES

 - specification for the [encryption](https://en.wikipedia.org/wiki/Encryption "Encryption") of electronic data established by the U.S. [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology "National Institute of Standards and Technology") (NIST) in 2001.
 - Jedná se o symetrickou ([[symmetric key]]) blokovou šifru ([[Block cipher]]) šifrující i dešifrující stejným [klíčem](https://cs.wikipedia.org/wiki/Kl%C3%AD%C4%8D_(kryptografie) "Klíč (kryptografie)") data rozdělená do bloků pevně dané délky.

 - based on a design principle known as a [[substitution–permutation network]], and is efficient in both software and hardware.

 - AES is a variant of [[Rijndael]], with a fixed [[block size]] of 128 [[bits]], and a [[key size]] of 128, 192, or 256 bits.
 - By contrast, [[Rijndael]] per se is specified with block and key sizes that may be any multiple of 32 bits, with a minimum of 128 and a maximum of 256 bits. Most AES calculations are done in a particular [[finite field]].

 - AES operates on a 4 × 4 [[column-major order]] array of 16 bytes b0, b1, ..., b15 termed the state: 
![[ce972adabe0f7c0a29829ced113db2bebca4204e.jpg | 300]]
### High-level description of the algorithm
- KeyExpansion – round keys are derived from the cipher key using the [[AES key schedule]]. AES requires a separate 128-bit round key block for each round plus one more.
- Initial round key addition:
    1. AddRoundKey – each byte of the state is combined with a byte of the round key using [[bitwise xor]].
- 9, 11 or 13 rounds:
    1. SubBytes – a non-linear substitution step where each byte is replaced with another according to a [[lookup table]].         
    2. ShiftRows – a transposition step where the last three rows of the state are shifted cyclically a certain number of steps.
    3. MixColumns – a linear mixing operation which operates on the columns of the state, combining the four bytes in each column.
    4. AddRoundKey
- Final round (making 10, 12 or 14 rounds in total):
    1. SubBytes
    2. ShiftRows
    3. AddRoundKey


https://en.wikipedia.org/wiki/Advanced_Encryption_Standard




![[AES_(Rijndael)_Round_Function.png]]