bbc96594b4e001778eee9975372716b2

Interestingly, the solution to this level gives this output:

```
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
```

AHA! So it turns out the actual password can be found by looking at the version history of the file. Do `git log` to see the commits, and `git checkout <commit id>` to move to the state of the repo at that commit. That's where we get the password.
