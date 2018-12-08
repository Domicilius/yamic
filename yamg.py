'''
Implements the tables and generators found in The Nameless Grimoire.
Textfiles found in the accompanying directory are all credits to Johnstone
Metzger with minor alterations made for ease of use.
'''

import argparse
import io
from random import randrange


def magicitemgen():
    switcher = randrange(1, 11)
    if switcher == 1:
        return aspectgen() + ' ' + elementgen() + ' ' + itemgen()
    elif switcher == 2:
        return aspectgen() + ' ' + formgen() + ' ' + itemgen()
    elif switcher == 3:
        return aspectgen() + ' ' + itemgen()
    elif switcher == 4:
        return creaturegen() + ' ' + itemgen()
    elif switcher == 5:
        return elementgen() + ' ' + creaturegen() + ' ' + itemgen()
    elif switcher == 6:
        return elementgen() + ' ' + itemgen()
    elif switcher == 7:
        return formgen() + ' ' + itemgen()
    elif switcher == 8:
        return itemgen() + ' of the ' + aspectgen() + ' ' + creaturegen()
    elif switcher == 9:
        return itemgen() + ' of the ' + aspectgen() + ' ' + elementgen()
    elif switcher == 10:
        return itemgen() + ' of ' + elementgen()


def monstergen():
    switcher = randrange(1, 9)
    if switcher == 1:
        return aspectgen() + ' ' + creaturegen()
    elif switcher == 2:
        return aspectgen() + ' ' + creaturegen() + ' ' + creaturegen()
    elif switcher == 3:
        return aspectgen() + ' ' + elementgen() + ' ' + creaturegen()
    elif switcher == 4:
        return aspectgen() + ' ' + formgen() + ' ' + creaturegen()
    elif switcher == 5:
        return creaturegen() + ' ' + creaturegen()
    elif switcher == 6:
        return elementgen() + ' ' + creaturegen()
    elif switcher == 7:
        return elementgen() + ' ' + creaturegen() + ' ' + creaturegen()
    elif switcher == 8:
        return formgen() + ' ' + creaturegen()


def firstspellhalfgen():
    switcher = randrange(1, 13)
    firsthalf = ""
    if switcher == 1:
        firsthalf = aspectgen()
    elif switcher == 2:
        firsthalf = aspectgen()
    elif switcher == 3:
        firsthalf = aspectgen() + ' ' + creaturegen()
    elif switcher == 4:
        firsthalf = aspectgen() + ' ' + elementgen()
    elif switcher == 5:
        firsthalf = aspectgen() + ' ' + formgen()
    elif switcher == 6:
        firsthalf = aspectgen() + ' ' + itemgen()
    elif switcher == 7:
        firsthalf = creaturegen()
    elif switcher == 8:
        firsthalf = elementgen()
    elif switcher == 9:
        firsthalf = elementgen()
    elif switcher == 10:
        firsthalf = formgen()
    elif switcher == 11:
        firsthalf = formgen()
    elif switcher == 12:
        firsthalf = itemgen()
    return firsthalf


def secondspellhalfgen():
    switcher = randrange(1, 21)
    secondhalf = ""
    if switcher == 1:
        secondhalf = creaturegen()
    elif switcher == 2:
        secondhalf = creaturegen()
    elif switcher == 3:
        secondhalf = elementgen()
    elif switcher == 4:
        secondhalf = elementgen()
    elif switcher == 5:
        secondhalf = elementgen()
    elif switcher == 6:
        secondhalf = formgen()
    elif switcher == 7:
        secondhalf = formgen()
    elif switcher == 8:
        secondhalf = formgen()
    elif switcher == 9:
        secondhalf = formgen()
    elif switcher == 10:
        secondhalf = itemgen()
    elif switcher == 11:
        secondhalf = aspectgen() + ' ' + creaturegen()
    elif switcher == 12:
        secondhalf = aspectgen() + ' ' + elementgen()
    elif switcher == 13:
        secondhalf = aspectgen() + ' ' + elementgen()
    elif switcher == 14:
        secondhalf = aspectgen() + ' ' + formgen()
    elif switcher == 15:
        secondhalf = aspectgen() + ' ' + formgen()
    elif switcher == 16:
        secondhalf = aspectgen() + ' ' + itemgen()
    elif switcher == 17:
        secondhalf = elementgen() + ' ' + creaturegen()
    elif switcher == 18:
        secondhalf = elementgen() + ' ' + formgen()
    elif switcher == 19:
        secondhalf = elementgen() + ' ' + formgen()
    elif switcher == 20:
        secondhalf = elementgen() + ' ' + itemgen()
    return secondhalf


def complexspellgen():
    return firstspellhalfgen() + ' ' + secondspellhalfgen()


def simplespellgen():
    switcher = randrange(1, 9)
    if switcher == 1:
        return aspectgen() + ' Curse'
    elif switcher == 2:
        return 'Summon ' + creaturegen()
    elif switcher == 3:
        return 'Calling the ' + secondspellhalfgen()
    elif switcher == 4:
        return 'Create ' + elementgen()
    elif switcher == 5:
        return 'Summon ' + elementgen()
    elif switcher == 6:
        return elementgen() + ' Control'
    elif switcher == 7:
        return elementgen() + ' Summoning'
    elif switcher == 8:
        return firstspellhalfgen() + ' Spell'


def aspectgen():
    with open('aspects.txt', 'r') as f:
        read_data = list(f.readlines())
        filelen = len(read_data)
        return read_data[randrange(0, filelen)].rstrip()


def elementgen():
    with open('elements.txt', 'r') as f:
        read_data = list(f.readlines())
        filelen = len(read_data)
        return read_data[randrange(0, filelen)].rstrip()


def itemgen():
    with open('items.txt', 'r') as f:
        read_data = list(f.readlines())
        filelen = len(read_data)
        return read_data[randrange(0, filelen)].rstrip()


def creaturegen():
    with open('creatures.txt', 'r') as f:
        read_data = list(f.readlines())
        filelen = len(read_data)
        return read_data[randrange(0, filelen)].rstrip()


def formgen():
    with open('forms.txt', 'r') as f:
        read_data = list(f.readlines())
        filelen = len(read_data)
        return read_data[randrange(0, filelen)].rstrip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-g',
        '--generator',
        help='set generator to ITEM, MONSTER or SPELL',
        type=str,
        choices=['item', 'monster', 'spell'])
    args = parser.parse_args()

    if args.generator == 'item':
        print(magicitemgen())
    if args.generator == 'monster':
        print(monstergen())
    if args.generator == 'spell':
        print(simplespellgen())
