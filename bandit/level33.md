c9c3199ddf4121b10cf581a98d51caee

This one was interesting. So we are taken to a shell that capitilizes all input, so you can't run any commands. It just says command <uppercase version of command> doesn't exist. In order to escape the shell, we do `$0` to bring up a new shell. We can then run the `bash` command to get a born again shell that we are used to. From there, we just `cat /etc/bandit_pass/bandit33`.
