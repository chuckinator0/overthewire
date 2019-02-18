U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

Same as last time, but the characters that allowed the last exploit were restricted. So instead, we used the `grep` function to our advantage:

```bash
.* /etc/natas_webpass/natas11 #
```

This is inserted into a `grep`, so we see the contents of that directory that matches the regular expression `.*`, and the `#` comments out the subsequent code.
