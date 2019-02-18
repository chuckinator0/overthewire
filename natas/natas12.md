EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

Our cookie has the value `ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFlopFRJeaAw%3D`. Looking at the source code, this value is the result of `base64_encode(xor_encrypt(json_encode($d)))`, where `$d` is the default data `array( "showpassword"=>"no", "bgcolor"=>"#ffffff")`. Decoding with `base64` gives an error due to the `%3D`, and consulting another person's solution, they just have an `=` instead of `%3D` so I went with that.

See `natas12.py`. Here's some commentary:

Ok, so here's the idea. We know that taking the json string `'{"showpassword":"no","bgcolor":"#ffffff"}'` followed by xor encryption with a key followed by base64 encryption produces the cookie `"ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="`.

We want to find the cookie produced by the same process starting with the json string
`'{"showpassword":"yes","bgcolor":"#ffffff"}'`

To do this, we need to find the key that turns the json string into the cookie. We know that

`secret ^ key = encrypted`, and
`encrypted ^ secret = key`

This is true because with `secret ^ key`, we turn off all the 1s that are common to both, and when we `^` with `secret` again, we turn off all the 1s in `secret` that are not in `key` and turn back on all the 1s in `secret` that are also in `key`. The 1s in `key` that were not in `secret` remained on. So the 1s that remain are the 1s in `key` that were not in `secret`, and the ones in `secret` that were also in `key`. This leaves us just with `key`.

We know secret (the json string) and encrypted (the cookie), so we just need to do cookie ^ json to get the key. Once we have the key, we can apply it to '{"showpassword":"yes","bgcolor":"$ffffff"}' to get a new cookie. We will then give this new cookie to the site to reveal the next password.
