G(en)mail
===============

```
usage: G(en)mail [-h] [-t nb] [-s nb] [-o file.ext] [-f nb] email

G(en)mail generate numerous of valid email that lead directlyinto your inbox.

positional arguments:
  email                 email template, since the script is wrote for GMAIL we
                        just need the local part of the email
                        (localpart@domain)

optional arguments:
  -h, --help            show this help message and exit
  -t nb, --type nb      Disposition preference (0:before|1:mixed|2:after)
  -s nb, --size nb      size of the new email, default is max length allowed.
  -o file.ext, --output file.ext
                        Specify output file, default is stdout
  -f nb, --format nb    Output format, line by line (0) or CSV (1).Default is
                        CSV
```
