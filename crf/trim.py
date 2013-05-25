# -*- coding:utf-8 -*-

import codecs
import sys

def trim(train, newtrain):
    f = codecs.open(train, 'r', 'utf-8')
    contents = f.read()
    f.close

    words = contents.split(u'\n')
    newfile = []
    count = 0

    for word in words:
        count = count + 1
        newfile.append(word + u'\n')
        if count == 1000:
            break

    f = codecs.open(newtrain, 'w', 'utf-8')
    f.write(''.join(newfile))
    f.close

def main():
    args = sys.argv[1:]

    trim(args[0], args[0]+'.trim')

if __name__ == '__main__':
    main()

        