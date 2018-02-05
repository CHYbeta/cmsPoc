import os
import time
import base64
import hashlib


class AuthCode(object):

    @classmethod
    def encode(cls, string, key, expiry=0):
        return cls._auth_code(string, 'ENCODE', key, expiry)

    @classmethod
    def decode(cls, string, key, expiry=0):
        return cls._auth_code(string, 'DECODE', key, expiry)

    @staticmethod
    def _md5(source_string):
        return hashlib.md5(source_string).hexdigest()

    @classmethod
    def _auth_code(cls, input_string, operation='DECODE', key='', expiry=3600):
        rand_key_length = 8

        key = cls._md5(key)
        key_a = cls._md5(key[:16])
        key_b = cls._md5(key[16:])
        if rand_key_length:
            if operation == 'DECODE':
                key_c = input_string[:rand_key_length]
            else:
                key_c = cls._md5(str(time.time()))[-rand_key_length:]
        else:
            key_c = ''

        crypt_key = key_a + cls._md5(key_a + key_c)

        if operation == 'DECODE':
            handled_string = base64.b64decode(input_string[rand_key_length:])
        else:
            expiration_time = expiry + int(time.time) if expiry else 0
            handled_string = '%010d' % expiration_time + cls._md5(input_string + key_b)[:16] + input_string

        rand_key = list()
        for i in xrange(256):
            rand_key.append(ord(crypt_key[i % len(crypt_key)]))

        box = range(256)
        j = 0
        for i in xrange(256):
            j = (j + box[i] + rand_key[i]) % 256
            tmp = box[i]
            box[i] = box[j]
            box[j] = tmp

        result = ''
        a = 0
        j = 0
        for i in xrange(len(handled_string)):
            a = (a + 1) % 256
            j = (j + box[a]) % 256
            tmp = box[a]
            box[a] = box[j]
            box[j] = tmp
            result += chr(ord(handled_string[i]) ^ (box[(box[a] + box[j]) % 256]))

        if operation == 'DECODE':
            if (int(result[:10]) == 0 or (int(result[:10]) - time.time() > 0)) and \
                    (result[10:26] == cls._md5(result[26:] + key_b)[:16]):
                output_string = result[26:]
            else:
                output_string = ''
        else:
            output_string = key_c + base64.b64encode(result)

        return output_string
