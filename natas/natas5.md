iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

For this one, we needed to trick the server into thinking we were referred from "http://natas5.natas.labs.overthewire.org/". To do this, we can use `curl`!

```bash
curl -H 'Referer: http://natas5.natas.labs.overthewire.org/' --user natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ http://natas4.natas.labs.overthewire.org
```

Note that the "Referer" header is spelled incorrectly--apparently this is a famous misspelling. The `-H` or `--header` option allows us to pretend we were referred from a different site. The `--user` option allows us to log in with our credentials. 
