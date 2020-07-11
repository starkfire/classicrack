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
* Affine (no stable cracking implementation yet)
* Atbash
* Caesar
* ROT13

Cryptanalysis
-------------
So far, the project can only perform cryptanalysis on supported ciphers, and only works when the cipher used is known. It does not yet include modules for discerning what cipher is used in a text.

Install
-------
Clone the project on GitHub and install with pip:

.. code-block:: bash

   git clone https://github.com/starkfire/classicrack/
   cd classicrack/
   pip install -r requirements.txt