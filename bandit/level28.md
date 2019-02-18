
0ef186ac70e04ea33b4c1853d2526fa2

This one was weird. The idea was to `git clone` a repo over ssh and read the next password, but there were permission issues with doing `git clone ssh://bandit27-git@localhost/home/bandit27-git/repo`. After some googling of the problem, I found I had to create a temporary directory `/tmp/chuck` and run `git clone ssh://bandit27-git@localhost/home/bandit27-git/repo.git` from there. Notice the `.git` at the end. I was able to clone the repo without permission issues and get the password.
