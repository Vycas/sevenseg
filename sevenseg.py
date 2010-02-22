#!/usr/bin/env python

from UserString import MutableString

class SevenSeg(int):
    """
    Class providing integer representation using seven digits display style.
    """

    segments = ( 
        (' ### ', '     ', ' ### ', ' ### ', '     ', ' ### ', ' ### ', ' ### ', ' ### ', ' ### '),
        ('#   #', '    #', '    #', '    #', '#   #', '#    ', '#    ', '    #', '#   #', '#   #'),
        ('#   #', '    #', '    #', '    #', '#   #', '#    ', '#    ', '    #', '#   #', '#   #'),
        ('#   #', '    #', '    #', '    #', '#   #', '#    ', '#    ', '    #', '#   #', '#   #'),
        ('     ', '     ', ' ### ', ' ### ', ' ### ', ' ### ', ' ### ', '     ', ' ### ', ' ### '),
        ('#   #', '    #', '#    ', '    #', '    #', '    #', '#   #', '    #', '#   #', '    #'),
        ('#   #', '    #', '#    ', '    #', '    #', '    #', '#   #', '    #', '#   #', '    #'),
        ('#   #', '    #', '#    ', '    #', '    #', '    #', '#   #', '    #', '#   #', '    #'),
        (' ### ', '     ', ' ### ', ' ### ', '     ', ' ### ', ' ### ', '     ', ' ### ', ' ### '))

    def __str__(self):
        num = self
        digits = []
        while num != 0:
            num, last = divmod(num, 10)
            digits.append(last)
        if len(digits) == 0:
            digits.append(0)
        digits.reverse()
        out = MutableString()
        for row in range(9):
            for d in digits:
                out += self.segments[row][d]
                out += '  '
            out += '\n'
        return str(out)

if __name__ == '__main__':
    import sys
    s = SevenSeg(sys.argv[1])
    print s
