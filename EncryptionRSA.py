"""

Title: RSA Encryption Program with predefined integer values as inputs.
Author: Garrett Timberlake

# Test Variables
# p = 123456791
# q = 987654323
# e = 127
# m = 14152019010605

"""


def egcd(a, b):
    s = 0
    s2 = 1
    t = 1
    t2 = 0
    r = b
    r2 = a

    while r != 0:
        quotient = r2 // r
        r2, r = r, r2 - quotient * r
        s2, s = s, s2 - quotient * s
        t2, t = t, t2 - quotient * t
    return r2, s2, t2


def modularinverse(a, b):
    gcd, x, y = egcd(a, b)
    if x < 0:
        x += b
    return x


def encrypt(e, n, message):
    cipher = pow(message, e, n)
    return cipher


def decrypt(d, n, cipher):
    decipher = pow(cipher, d, n)
    return decipher


def encryptRSA():
    # Input Given Variables
    p = int(input('p = '))
    q = int(input('q = '))
    e = int(input('e = '))
    m = int(input('m = '))

    print('######################################\n'
          'Given Variables: ',
          '\n p = ', p,
          '\n q = ', q,
          '\n e = ', e,
          '\n m = ', m)

    # Calculations
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modularinverse(e, phi)

    print('######################################\n'
          'Calculated Variables: ',
          '\n n = p * q = ', n,
          '\n phi = (p - 1) * (q - 1) = ', phi,
          '\n d = ', d)

    cipher = encrypt(e, n, m)
    print('Cipher Message = ', cipher)

    decrypted = decrypt(d, n, cipher)
    print('Decrypted Message = ', decrypted)
    # NOTE: decrypted should be equal to m (original message)


encryptRSA()
