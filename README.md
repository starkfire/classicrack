# classicrack
### [wip 🛠️] A Python library for implementing and cracking classical ciphers (Atbash, Caesar, ROT13, etc.)

## Supported Ciphers
* Atbash
* Caesar
* ROT13

**This library is still a work-in-progress. Some ciphers are not yet implemented, and cryptanalysis modules are still unstable.**

## Install
```
pip install -r requirements.txt
```

## Ciphers
### Caesar
```py
from classicrack.ciphers import Caesar

cs = Caesar()

# encode
cs.encode('cheemsburger', 13)
# decode
cs.decode('purrzfohetre', 13)
# crack (bruteforce)
cs.crack_bruteforce('purrzfohetre')
# crack (frequency analysis: n-grams)
cs.crack_ngram('purrzfohetre', 1)
```
### Atbash
```py
from classicrack.ciphers import Atbash

ab = Atbash()

# encode
ab.encode('zebras')
# decode
ab.decode('avyizh')
```
### ROT13
```py
from classicrack.ciphers import ROT13

rot = ROT13()

# encode
rot.encode('cheemsburger')
# decode
rot.decode('purrzfohetre')
```