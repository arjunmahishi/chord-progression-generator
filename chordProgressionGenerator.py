import random
import time

chromatic_scale = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

def getMajorScale(key_note):
    formula = [2,2,1,2,2]
    scale = []
    scale.append(key_note)
    for i in range(len(chromatic_scale)):
        if chromatic_scale[i] == key_note:
            break
    j = 0
    while len(scale) < 6:
        if i + formula[j] < 12:
            i += formula[j]
            j += 1
        else:
            i = 12 - (i + formula[j])
            j += 1
        scale.append(chromatic_scale[i])
    return scale

def getMinorScale(key_note):
    formula = [2,1,2,2,1]
    scale = []
    scale.append(key_note)
    for i in range(len(chromatic_scale)):
        if chromatic_scale[i] == key_note:
            break
    j = 0
    while len(scale) < 6:
        if i + formula[j] < 12:
            i += formula[j]
            j += 1
        else:
            i = 12 - (i + formula[j])
            j += 1
        scale.append(chromatic_scale[i])
    return scale            

def compose():
    key_note = random.choice(chromatic_scale)

    toss = [0,1]
    j = random.choice(toss)
    if j == 1:
        scale = getMinorScale(key_note)
    else:
        scale = getMajorScale(key_note)

    no_of_chords = random.randrange(3,6)

    chords = ''
    picked = []
    while chords.count(' ') < no_of_chords:
        k = random.randrange(6)
        if k not in picked:
            picked.append(k)
            if k in [1,2,5]:
                chords += scale[k] + 'm'+ ' '
            else :
                chords += scale[k] + ' '

    return chords
