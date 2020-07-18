# classicrack
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/starkfire/classicrack/blob/master/LICENSE.md)
[![Documentation Status](https://readthedocs.org/projects/classicrack/badge/?version=latest)](https://classicrack.readthedocs.io/en/latest/?badge=latest)

### [wip 🛠️] A Python library for implementing and cracking classical ciphers (Atbash, Caesar, ROT13, etc.)

## Supported Ciphers
* [Affine](https://github.com/starkfire/classicrack#affine)
* [Atbash](https://github.com/starkfire/classicrack#atbash)
* [Caesar](https://github.com/starkfire/classicrack#caesar)
* [ROT13](https://github.com/starkfire/classicrack#rot13)

## Installation
```
pip install -r requirements.txt
```

# Cryptanalysis

For cracking, cipher implementations have a `crack()` method. Implementations of some ciphers, such as ROT-13 and Atbash do not have it, since the `decode()` method already performs the same task.

So far, classicrack can only perform cryptanalysis on ciphers with keyspace weaknesses (e.g. Affine, Caesar). Implementations for other ciphers such as Vigenere might be added soon.

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
# crack (ciphertext)
af.crack('srccqunepmcp')
```

`encode (pt, a, b)`: encrypts the input plaintext using Affine
  * `pt`: the input plaintext
  * `a`: a slope value, which must be a positive integer coprime with 26
  * `b`: an intercept value, which can take any positive integer

`decode (ct, a, b)`: decrypts an input ciphertext using Affine
  * `ct`: the input ciphertext
  * `a`: a slope value, which must be a positive integer coprime with 26
  * `b`: an intercept value, which can take any positive integer

`crack (ct)`: cracks an input Affine ciphertext
  * `ct`: the input ciphertext

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
# crack
cs.crack('purrzfohetre')
```

`encode (pt, shift)`: encrypts the input plaintext with Caesar's Cipher
  * `pt`: the input plaintext
  * `shift`: a shift value, which can be any positive integer

`decode (ct, a, b)`: decrypts a ciphertext encrypted with Caesar's Cipher
  * `ct`: the input ciphertext
  * `shift`: a shift value, which can be any positive integer

`crack (ct)`: cracks an input Caesar ciphertext
  * `ct`: the input ciphertext

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

## License

[MIT License](https://github.com/starkfire/classicrack/blob/master/LICENSE.md)