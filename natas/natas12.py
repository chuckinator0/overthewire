import base64 # for decoding
import requests # for requesting from website
from urllib.parse import unquote # decodes the %xx part of the cookie. See https://en.wikipedia.org/wiki/Percent-encoding
from requests.auth import HTTPBasicAuth # allows us to authenticate into the site

HOST = "http://natas11.natas.labs.overthewire.org/"

r = requests.get(HOST, params={'bgcolor':"#ffffff"}, auth=HTTPBasicAuth('natas11', 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'))

cookie = unquote(r.cookies['data']) # Here, unquote turns '%3D' into '='
default_json = '{"showpassword":"no","bgcolor":"#ffffff"}'


'''
Ok, so here's the idea. We know that taking the json string '{"showpassword":"no","bgcolor":"#ffffff"}'
followed by xor encryption with a key followed by base64 encryption produces the cookie
"ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=".

We want to find the cookie produced by the same process starting with the json string
'{"showpassword":"yes","bgcolor":"#ffffff"}'

To do this, we need to find the key that turns the json string into the cookie. We know that

secret ^ key = encrypted, and
encrypted ^ secret = key

This is true because with secret ^ key, we turn off all the 1s that are common to both, and when we ^ with secret again,
we turn off all the 1s in secret that are not in key and turn back on all the 1s in secret that are also in key. The 1s in key
that were not in secret remained on. So the 1s that remain are the 1s in key that were not in secret, and the ones in secret
that were also in key. This leaves us just with key.

We know secret (the json string) and encrypted (the cookie), so we just need to do cookie ^ json to get the key.
Once we have the key, we can apply it to '{"showpassword":"yes","bgcolor":"$ffffff"}' to get a new cookie. We will
then give this new cookie to the site to reveal the next password.
'''

def principal_period(s):
    '''This function finds the part that repeats in a repeating string.
    We'll need this when we compute the key later, since we are only interested
    in the non-repeating part.
    A string repeats if and only if it is a non-trivial rotation of itself.'''
    i = (s+s).find(s, 1, -1)
    return s[:i]

def get_key(secret,encrypted):
    key = ''
    for char1, char2 in zip(secret,encrypted):
        key += chr( ord(char1) ^ ord(char2) ) # We compare character by character, XORing the ordinals and then extracting the new character
    # At this point, key is a repeating string. We just want the part that repeats.
    nonrepeating_key = principal_period(key)
    return nonrepeating_key

def xor_encrypt(secret,key):
    encrypted = ''
    for i,char in enumerate(secret):
        encrypted += chr( ord(char) ^ ord( key[i % len(key)]) ) # the key might be shorter than the encryption, so we mod by its length
    return encrypted

'''
Ok, now we can get the cookie produced from {"showpassword":"yes","bgcolor":"#ffffff"}'
'''


# First, let's undo the base64 encryption on the cookie
b64decoded_cookie = base64.b64decode(cookie).decode() # the .decode() is to turn the bytes-like object into a string

# Let's get the xor_encryption key
key = get_key(default_json,b64decoded_cookie)

# Now let's use the key to find the cookie for the json that will let us see the password
hacked_json = '{"showpassword":"yes","bgcolor":"#ffffff"}'

# need .encode() in there so b64encode receives a byte-like object and then we need to .decode() at the end to end with a string
hacked_cookie = base64.b64encode( xor_encrypt(hacked_json,key).encode() ).decode()

# Sanity check
print(key) # should be 'qw8J' repeated
print(cookie) # should be "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
print(base64.b64encode( xor_encrypt(default_json,key).encode() ).decode()) # sanity check--should be the same as cookie
print(hacked_cookie) # should be ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK

r = requests.get(HOST, params={'bgcolor':"#ffffff"}, auth=HTTPBasicAuth('natas11', 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'),cookies={'data':hacked_cookie})

# print the password!
for line in r.text.split('\n'):
    if "password" in line:
        print(line)
        break





