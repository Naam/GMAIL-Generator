"""
G(en)mail generate numerous of valid email that lead directly into
your inbox.
Copyright (C) 2014 Naam

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.
"""

import argparse
import sys
import os
import random

MAIL_MAX_LEN    =   64
AT              =   '@'
PROVIDER        =   'gmail.com'
ml              =   []
random.seed(os.urandom(42))

parser = argparse.ArgumentParser(description=
        'G(en)mail generate numerous of valid email that lead directly' +
        'into your inbox.',
        prog='G(en)mail')
parser.add_argument('-t', '--type',
        help    =   'Disposition preference (0:before|1:mixed|2:after)',
        default =   1,
        metavar =   'nb',
        type    =   int,
        choices =   range(0,3),
        dest    =   'type')
parser.add_argument('-s', '--size',
        help    =   'size of the new email, default is max length allowed.',
        default =   64,
        metavar =   'nb',
        type    =   int,
        choices =   range(0,65),
        dest    =   'size')
parser.add_argument('-o', '--output',
        help    =   'Specify output file, default is stdout',
        default =   'stdout',
        metavar =   'file.ext',
        dest    =   'output')
parser.add_argument('-f', '--format',
        help    =   'Output format, line by line (0) or CSV (1).' +
                    'Default is CSV',
        default =   1,
        metavar =   'nb',
        type    =   int,
        choices =   range(0,2),
        dest    =   'fmt')
parser.add_argument('email',
        help    =   'email template, since the script is wrote for GMAIL we ' +
                    'just need the local part of the email (localpart@domain)')

args = parser.parse_args()

def main():
    stdout      = sys.stdout if args.output is 'stdout' \
                    else open(args.output, 'w')
    parsemail()
    getmails(dotavlb())
    if args.fmt == 1:
        stdout.write(",".join(ml))
    else:
        stdout.writelines("\n".join(ml))
        if stdout == sys.stdout:
            stdout.write('\n')
    stdout.close()

def dotavlb():
    res = MAIL_MAX_LEN
    if args.size is 64:
        res     -= len(args.email)
    else:
        res     = min(MAIL_MAX_LEN, args.size - len(args.email))
    return res

def getmails(dotavlb):
    ml = []
    for i in range(0, dotavlb):
        mails("", args.type * 0.5, 0, i)

def mails(current, coef, posmail, dot):
    if dot < 1:
        if posmail < len(args.email) - 1:
            ml.append(current + args.email[posmail:] + AT + PROVIDER)
        else:
            ml.append(current + AT + PROVIDER)
        return
    if dot > 0:
        if posmail == len(args.email) - 1:
            ml.append(current + args.email[posmail] + '.'*dot + AT + PROVIDER)
            return
        if coef <= 0.5:
            mails(current + '.', coef, posmail, dot - 1)
        if coef >= 0.5:
            mails(current + args.email[posmail], coef, posmail + 1, dot)

def parsemail():
    try:
        posat = args.email.find('@')
        if posat is not -1:
            mail            = args.email[:posat]
            assert len(mail) < MAIL_MAX_LEN
            args.email   = mail
        else:
            assert len(args.email) < MAIL_MAX_LEN
    except:
        print ('localpart too long, max size is ' + str(MAIL_MAX_LEN))
        sys.exit(2)
    args.email = args.email.replace('.', '')

if __name__ == '__main__':
    main()
