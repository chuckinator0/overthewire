DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

Here, we have two pages: "Home" and "About". Viewing the source, there's a comment that says: `hint: password for webuser natas8 is in /etc/natas_webpass/natas8`. So, I checked if there was another page at that path:

```
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
```

And, indeed, the password was there!
