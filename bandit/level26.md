
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

This one was very sneaky, and I needed some help from google. When we enter the bandit25 prompt, the current directory gives an ssh key to bandit26. When we use `ssh -i bandit26.sshkey bandit26@localhost`, we see a shell login and then it immediately exits. Upon doing `cat /etc/passwd | grep bandit26`, we see that this user's shell is defined in `/usr/bin/showtext` rather than `/bin/bash` like all the others. Looking at this file, we see that it does a `more` command on a text file and then `exit 0` to immediately exit the shell.

To overcome this, as I learned, we need to "escape the shell." What we can do is `ssh` into bandit26 like before, but with our terminal size very squished vertically in order to activate the `more` command. While `more` is running, we can press `v` to activate the `vi` editor within `more`. Vi allows us to run commands to spawn a new shell:

```
:set shell=/bin/bash
:shell
```

Viola, we have escaped the shell. From there, we can retrieve the next password from `/etc/bandit_pass/bandit26`.

We also retrieve the bandit 27 password by using the executable in the current directory `./bandit27-do /etc/bandit_pass/bandit27` which yields:

3ba3118a22e93127a4ed485be72ef5ea
