# -*- coding: utf-8 -*-

""" The module provides convenient access to the cryptography module.
    Author: Myshko E.V.
"""

try:
    from cryptography.fernet import Fernet
except ImportError as exception:
    print('Missing "cryptography" module. More about the module: https://cryptography.io/en/latest/ \n'
          'Try installing the module with the command: "pip install cryptography"')

import base64

def generate_key():
    """
    Method generates key
    :return: generated key
    """
    return Fernet.generate_key()

def encrypt(data, key):
    """
    Method encrypts data
    :param data: encrypted data
    :param key: encryption key
    :return: encrypted data
    """
    if not data:
        raise ValueError('missing parameter "data"')
    if not key:
        raise ValueError('missing parameter "key"')

    encoder = Fernet(key)
    return encoder.encrypt(data)

def decrypt(data, key):
    """
    Method decrypts data
    :param data: encrypted data
    :param key: encryption key
    :return: decrypted data
    """
    if not data:
        raise ValueError('missing parameter "data"')
    if not key:
        raise ValueError('missing parameter "key"')

    encoder = Fernet(key)
    return encoder.decrypt(data)

