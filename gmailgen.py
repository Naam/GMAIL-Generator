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

MAIL_MAX_LEN    =   64
PROVIDER        =   'gmail.com'
AT              =   '@'

parser = argparse.ArgumentParser(description=
        'G(en)mail generate numerous of valid email that lead directly' +
        '\ninto your inbox.',
        prog='G(en)mail')
parser.add_argument('-n', '--number',
        help    =   'Number of generated email, by default the all' +
                    ' combination will be generated',
        nargs   =   1,
        default =   0,
        metavar =   'nb',
        type    =   int,
        dest    =   'number')
parser.add_argument('-t', '--type',
        help    =   'Disposition preference (0:before|1:mixed|2:after)',
        nargs   =   1,
        default =   0,
        metavar =   'nb',
        type    =   int,
        choices =   range(0,3),
        dest    =   'type')
parser.add_argument('-s', '--size',
        help    =   'max size of the new email, max is 64. Default is the ' +
                    'length of the localpart + 3',
        nargs   =   1,
        default =   0,
        metavar =   'nb',
        type    =   int,
        choices =   range(0,65),
        dest    =   'size')
parser.add_argument('-o', '--output',
        help    =   'Specify output file, default is stdin',
        nargs   =   1,
        default =   'stdout',
        metavar =   'file.ext',
        dest    =   'output')
parser.add_argument('-f', '--format',
        help    =   'Output format, line by line (0) or CSV (1).' +
                    'Default is CSV',
        nargs   =   1,
        default =   1,
        metavar =   'nb',
        type    =   int,
        choices =   range(0,2),
        dest    =   'fmt')
parser.add_argument('email',
        help    =   'email template, since the script is wrote for GMAIL we' +
                    'just need the local part of the email (localpart@domain)',
        nargs   =   1,
        )

args = parser.parse_args()

def main():
    stdout = sys.stdout if args.output[0] is 'stdout' \
            else open(args.output[0], 'w')
    parsemail()
    maxdot = dotavlb()
    stdout.close()

def dotavlb():
    return MAIL_MAX_LEN - len(args.email[0])

def getmails():
    return mails()

def mails(current, coef, posmail, size):
    pass

def parsemail():
    posat = args.email[0].find('@')
    if posat is not -1:
        args.email[0] = args.email[0][:posat]

if __name__ == '__main__':
    main()
