# -*- coding: utf-8 -*-

""" Unit testing module for module crypto_wrapper.
    Author: Myshko E.V.
"""

import unittest
import crypto_wrapper

# Constant with data to encrypt
DATA = b'test data'

class KeyTest(unittest.TestCase):
    """
    Class testing methods for working with encryption keys.
    """
    def test_key_is_not_empty(self):
        """
        The method checks the presence of a value in the generated key.
        """
        key = crypto_wrapper.generate_key()
        self.assertTrue(key)

    def test_key_type(self):
        """
        The method checks the type of encryption key
        """
        key = crypto_wrapper.generate_key()
        self.assertEquals(type(key), type(b''))

class EncryptTest(unittest.TestCase):
    """
    Class testing methods for working with encryption.
    """
    def test_encrypt_is_not_empty(self):
        """
        The method checks the presence of encrypted data.
        """
        key = crypto_wrapper.generate_key()
        encrypted_data = crypto_wrapper.encrypt(DATA, key)
        self.assertTrue(encrypted_data)

    def test_encrypted_data_type(self):
        """
        The method checks the type of encrypted data
        """
        key = crypto_wrapper.generate_key()
        encrypted_data = crypto_wrapper.encrypt(DATA, key)
        self.assertEquals(type(encrypted_data), type(b''))

    def test_invalid_first_parameter(self):
        """
        The method checks the generation of an exception when
        the first parameter is incorrect.
        """
        key = crypto_wrapper.generate_key()
        with self.assertRaises(ValueError):
            crypto_wrapper.encrypt(None, key)

    def test_invalid_second_parameter(self):
        """
        The method checks the generation of an exception when
        the second parameter is incorrect.
        """
        with self.assertRaises(ValueError):
            crypto_wrapper.encrypt(DATA, None)

class DecryptTest(unittest.TestCase):
    """
    Class testing methods for working with decrypt.
    """
    def test_decrypt_is_not_empty(self):
        """
        The method checks the presence of decrypted data.
        """
        key = crypto_wrapper.generate_key()
        encrypted_data = crypto_wrapper.encrypt(DATA, key)
        decrypted_data = crypto_wrapper.decrypt(encrypted_data, key)
        self.assertTrue(decrypted_data)

    def test_decrypted_data_type(self):
        """
        The method checks the type of decrypted data
        """
        key = crypto_wrapper.generate_key()
        encrypted_data = crypto_wrapper.encrypt(DATA, key)
        decrypted_data = crypto_wrapper.decrypt(encrypted_data, key)
        self.assertEquals(type(decrypted_data), type(b''))

    def test_invalid_first_parameter(self):
        """
        The method checks the generation of an exception when
        the first parameter is incorrect.
        """
        key = crypto_wrapper.generate_key()
        with self.assertRaises(ValueError):
            crypto_wrapper.decrypt(None, key)

    def test_invalid_second_parameter(self):
        """
        The method checks the generation of an exception when
        the second parameter is incorrect.
        """
        key = crypto_wrapper.generate_key()
        encrypted_data = crypto_wrapper.encrypt(DATA, key)
        with self.assertRaises(ValueError):
            crypto_wrapper.decrypt(encrypted_data, None)

    def test_correct_decryption(self):
        """
        The method checks the correctness of the decryption.
        """
        key = crypto_wrapper.generate_key()
        encrypted_data = crypto_wrapper.encrypt(DATA, key)
        decrypted_data = crypto_wrapper.decrypt(encrypted_data, key)
        self.assertEquals(DATA, decrypted_data)

if __name__ == '__main__':
    unittest.main()