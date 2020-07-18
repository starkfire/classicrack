.. classicrack documentation master file, created by
   sphinx-quickstart on Fri Jul 10 23:56:05 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to classicrack's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

GitHub: https://github.com/starkfire/classicrack/

Current Version: v0.1.0

Python library for implementing and performing cryptanalysis on classical ciphers.

Supported Ciphers
-----------------
* Affine
* Atbash
* Caesar
* ROT13

Cryptanalysis
-------------
For cracking, cipher implementations have a ``crack()`` method. Implementations of some ciphers, such as ROT-13 and Atbash do not have it, since the ``decode()`` method already performs the same task.

So far, classicrack can only perform cryptanalysis on ciphers with keyspace weaknesses (e.g. Affine, Caesar). Implementations for other ciphers such as Vigenere might be added soon.

Install
-------
Clone the project on GitHub and install with pip:

.. code-block:: bash

   git clone https://github.com/starkfire/classicrack/
   cd classicrack/
   pip install -r requirements.txt

Ciphers
=======

Affine
------

.. autoclass:: classicrack.ciphers.Affine
   :members:

Caesar
------

.. autoclass:: classicrack.ciphers.Caesar
   :members:

Atbash
------

.. autoclass:: classicrack.ciphers.Atbash
   :members:

ROT13
-----

.. autoclass:: classicrack.ciphers.ROT13
   :members: