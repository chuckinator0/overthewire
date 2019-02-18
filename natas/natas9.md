W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

Interestingly, viewing the page source doesn't give us the hint--we have to actually follow the "view source link" link. There, we see a function for encoding a secret:

```javascript
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
```

So we need to reverse the order of the encoding. First, we take `3d3d516343746d4d6d6c315669563362` and convert it from hex to binary, then reverse the result, and then base64 decode that. In bash:

```bash
echo 3d3d516343746d4d6d6c315669563362 | xxd -r -p | rev | base64 -D
```

We pipe the string with `echo` into `xxd`, which is a program that makes or decodes hexadecimal dumps. The `-r` option reverses the hexdump, and the `-p` gives us "plain hexdump" style. Then `rev` reverses that string, and then the `-D` option of `base64` decodes the string. The result is the secret we input to get the password to the next level.
