#!/usr/bin/env python3
# coding: utf-8

TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""


"""Translate hungarian accented characters into non-accented
characters and return as a translated string"""


def translator(s):
    d = dict(zip([c for c in 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'],
                 [c for c in 'aeiooouuuAEIOOOUUU']))
    return ''.join([d[c] if c in d.keys() else c for c in s])


def main():
    print(translator(TEXT))


if __name__ == '__main__':
    main()
