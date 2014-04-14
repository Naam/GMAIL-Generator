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

MAIL_MAX_LEN    =   64
PROVIDER        =   'gmail.com'
AT              =   '@'

parser = argparse.ArgumentParser(description=
        'G(en)mail generate numerous of valid email that lead directly' +
        '\ninto your inbox.',
        prog='G(en)mail')
parser.add_argument('-n', '--number',
        help    =   'Number of generated email',
        nargs   =   1,
        default =   0,
        type    =   int,
        dest    =   'number')
parser.add_argument('-t', '--type',
        help    =   'Disposition preference (0:before|1:mixed|2:after)',
        nargs   =   1,
        default =   0,
        type    =   int,
        choices =   range(0,3),
        dest    =   'type')
parser.add_argument('-o', '--output',
        help    =   'Specify output file, default is stdin',
        nargs   =   1,
        default =   'stdin',
        metavar =   'file.ext',
        dest    =   'output')
parser.add_argument('email',
        help    =   'email template, since the script is wrote for GMAIL we' +
                    'just need the local part of the email (localpart@domain)',
        nargs   =   1,
        )

args = parser.parse_args()

def main():
    pass

def getmail(current, disp, pos, nb):
    """current is the constructing string, start with \"\"
    disp is the type of disposition chosen in args
    pos is the current position in the localpart
    nb is the remaining address to build"""
    if nb < 0:
        pass


if __name__ == '__main__':
    main()
