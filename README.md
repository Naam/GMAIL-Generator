G(en)mail
===============

```
Generate numerous of valid email that lead to your inbox.

usage: G(en)mail [-h] [-n nb] [-t nb] [-s nb] [-o file.ext] [-f nb] email

G(en)mail generate numerous of valid email that lead directly into your inbox.

positional arguments:
  email                 email template, since the script is wrote for GMAIL
                        wejust need the local part of the email
                        (localpart@domain)

optional arguments:
  -h, --help            show this help message and exit
  -n nb, --number nb    Number of generated email, by default the all
                        combination will be generated
  -t nb, --type nb      Disposition preference (0:before|1:mixed|2:after)
  -s nb, --size nb      max size of the new email, max is 64. Default is the
                        length of the localpart + 3
  -o file.ext, --output file.ext
                        Specify output file, default is stdin
  -f nb, --format nb    Output format, line by line (0) or CSV (1).Default is
                        CSV
```
