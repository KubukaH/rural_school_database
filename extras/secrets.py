from hashlib import blake2b
from hmac import compare_digest

# HASHLIB SIGNATURE MAKING
def hash_sign(cookie, secret):
    h = blake2b(digest_size=32, key=secret)
    h.update(cookie)
    return h.hexdigest().encode('utf-8')

# check the signature of the digest
def verify(cookie, sig, secret):
    good_sig = hash_sign(cookie, secret)
    return compare_digest(good_sig, sig)

# generate random ids using blake 2 b
def hashed_id(pid):
    h = blake2b(digest_size=32)
    h.update(pid)
    return h.hexdigest().encode('utf-8')
