# classicrack
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Documentation Status](https://readthedocs.org/projects/classicrack/badge/?version=latest)](https://classicrack.readthedocs.io/en/latest/?badge=latest)

### [wip 🛠️] A Python library for implementing and cracking classical ciphers (Atbash, Caesar, ROT13, etc.)

**This library is still a work-in-progress and is open for contributions. Some ciphers are not yet implemented, and cryptanalysis modules are still unstable.**

## Supported Ciphers
* [Affine](https://github.com/starkfire/classicrack#affine)
* [Atbash](https://github.com/starkfire/classicrack#atbash)
* [Caesar](https://github.com/starkfire/classicrack#caesar)
* [ROT13](https://github.com/starkfire/classicrack#rot13)

## Installation
```
pip install -r requirements.txt
```

# Ciphers
## Affine
### Example
```py
from classicrack.ciphers import Affine

af = Affine()

# encode (plaintext, a, b)
af.encode('cheemsburger', 5, 8)
# decode (ciphertext, a, b)
af.decode('srccqunepmcp', 5, 8)
```

`encode (pt, a, b)`: encrypts the input plaintext using Affine
  * `pt`: the input plaintext
  * `a`: a slope value, which must be a positive integer coprime with 26
  * `b`: an intercept value, which can take any positive integer

`decode (ct, a, b)`: decrypts an input ciphertext using Affine
  * `ct`: the input ciphertext
  * `a`: a slope value, which must be a positive integer coprime with 26
  * `b`: an intercept value, which can take any positive integer

## Atbash
### Example
```py
from classicrack.ciphers import Atbash

ab = Atbash()

# encode
ab.encode('zebras')
# decode
ab.decode('avyizh')
```

`encode (pt)`: encrypts the input plaintext using Atbash
  * `pt`: the input plaintext

`decode (ct)`: decrypts a ciphertext using Atbash
  * `ct`: the input ciphertext

## Caesar
### Example
```py
from classicrack.ciphers import Caesar

cs = Caesar()

# encode
cs.encode('cheemsburger', 13)
# decode
cs.decode('purrzfohetre', 13)
# crack: bruteforce
cs.crack_bruteforce('purrzfohetre')
# crack: frequency analysis (ciphertext, n)
cs.crack_ngram('purrzfohetre', 1)
```

`encode (pt, shift)`: encrypts the input plaintext with Caesar's Cipher
  * `pt`: the input plaintext
  * `shift`: a shift value, which can be any positive integer

`decode (ct, a, b)`: decrypts a ciphertext encrypted with Caesar's Cipher
  * `ct`: the input ciphertext
  * `shift`: a shift value, which can be any positive integer

`crack_bruteforce (ct)`: returns all possible plaintext values for an input ciphertext using Caesar
  * `ct`: the input ciphertext

`crack_ngram (ct, n)`: uses frequency analysis (via [n-grams](https://en.wikipedia.org/wiki/N-gram)) to crack a ciphertext
  * `ct`: the input ciphertext
  * `n`: number of items for each n-gram (default: 1)

## ROT13
### Example
```py
from classicrack.ciphers import ROT13

rot = ROT13()

# encode
rot.encode('cheemsburger')
# decode
rot.decode('purrzfohetre')
```
`encode (pt)`: encrypts the input plaintext with ROT-13
  * `pt`: the input plaintext

`decode (ct)`: decrypts a ciphertext encrypted with ROT-13
  * `ct`: the input ciphertext

<hr>

## Notes
[classicrack](https://github.com/starkfire/classicrack) is part of my learning process in crypto, and was made as a tool I can use in CTF challenges. It is not meant to be a replacement for similar existing libraries out there (but it kinda works though, so...).

However, as long as it can be maintained, I might add support for other ciphers and improve its cryptanalysis implementation. The API is not (yet) stable, and plenty of optimizations must still be made.

<hr>

## License

[MIT License]()