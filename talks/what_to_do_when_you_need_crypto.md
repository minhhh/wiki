# SUMMARY

    Title: What to do when you need crypto
    Date: 2015-04-11
    Speaker: Jarret Raim, Paul Kehrer
    Conference: Pycon2015
    Tags: crypto

Url: https://www.youtube.com/watch?v=0m2ZUS9OH4k

The cryptographic world doesn't lend itself to the typical developer flow of learning while doing. Add that to the massive amount of bad or outdated information on the web and many developers are lost or worse, build insecure systems. This tutorial will introduce developers to modern cryptography with an eye towards practical scenarios around password management, encryption and key management.


# WHAT TO DO WHEN YOU NEED CRYPTO

## Outline
* Take good programmers and give you some intuition about how to use complex crypto systems to good effect.
    * Password and authentication
    * Key management : all encryption schemes are only as secure as their keys. We'll review various types of key management for applications and review which type will be appropriate in different scenarios.
    * Data at rest: Data in applications comes in a huge variety of forms. We will review options for encrypting data and the pros and cons of each method.
    * Signing & verification

## Passwords
* Passwords are just subtype of encryption key. It should be hard to guess
* Passwords are easy to guess. We need to make our passwords better keys
* Key derivation functions
    * PBKDF2
    * BCRYPT
    * SCRYPT
    * HKDF

## Key derivation
* A key derivation function is a function that derives one or more secret values from one secret value.
* Key strengthening: Passwords and other user chosen secrets generally do not have enough entropy to prevent them from being easily guessed.
* Multiple keys: when starting with one single secret, but the protocol needs multiple secrets, e.g. an encryption and MAC key.

## Bcrypt and Scrypt
* bcrypt
    * based on blowfish symmetric cipher
    * used as default password storage for many systems such as BSD
    * 128-bit salt combined with 192-bit key
* scrypt
    * designed to be resistant to large-scale, customer customer hardware attacks
    * raises resource demand of algorithm to make it more expensive to implement in hardware, e.g. more memory

## pbkdf2 and hkdf
* pbkdf2
    * part of Public Cryptography Standard
    * Use a pseudorandom function and a salt value and repeat a hash process for a number of iterations
* HKDF
    * HMAC based 'extract and expand'
    * Not for use with password

## Randomness
* Generating keys
    * Ensure that you're using cryptographically secure random number generator that has been correctly seeded to generate random data.
* Virtual machines
    * It's vanishingly unlikely that using a virtual machine will cause randomness exhaustion.
* /dev/urandom
    * Just use it.

## Data at rest
* There are 3 general ways to protect data at rest
    * Hashing
    * Symmetric encryption
    * Asymmetric encryption

## To hash or not to hash
* A hash function is any function that can be used to map digital data of arbitrary size to digital data of fixed size
* One way
    * Hashes are only useful for recognizing a known value as they can not be reversed. The data that is hashed cannot be reconsitituted from the hash itself.
* Uses
    * Most common use is authenticating sensitive data like password, social security number

## Symmetric encryption
* A function that uses the same keying material for both encryption and decryption
* Single key
    * A single key is used for all encryption operations. This key is enforced secrt, disclosure renders encryption data viewable
* Uses
    * Protecting sensitive data that must be retrieved, but isn't exposed to outside systems.

## Asymmetric encryption
* Also known as public-key cryptography, asymmetric cryptography requires two separate key (public and private), one of which is sharable.
* Multiple keys
    * A public key can be shared, allowing another party to encrypt a secret that can only be decrypted by the corresponding private key.
* Uses
    * Data and connections that must be shared outside a trust boundary

## Signing and verification
* Signing data allows for user to verify its authenticity and integrity
* Key generation algorithm
    * Signature algorithms can be built from other encryption algorithms, most usually a cryptographic hash function.
* Signature generation algorithm
    * Signatures use asymmetric cryptography (since they need to be shared with third parties). In this case the private key is used to create the message so that it can be verified by anyone with the public key.
* Signature verification algorithm
    * Any user with access to the public key can hash the signed data and verify that the hash was encrypted with the corresponding private key
* A storage mechanism
    * It's usually useful to combine the signed data and signature into a single message. This can be small data (TLS) or for larger data where something like Fernet is more usefu.
