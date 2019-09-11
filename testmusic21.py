from music21 import *

def parseChorales():
    file = open("romandata.txt", "w+")
    paths = corpus.getComposer('bach')
    for chorale in paths:
        chorale = corpus.parse(chorale)

        # chorale.show('text')
        try:
            key = chorale.recurse(classFilter='Key')[0]
            print(key)
        except Exception as e:
            continue


        for thing in chorale.getElementsByClass(stream.Part):
            if thing.partName not in ['Soprano', 'Alto', 'Tenor', 'Bass']:
                chorale.remove(thing)
        # chorale.show('text')

        chordList = chorale.chordify(addPartIdAsGroup=True)
        chordList.show()
        # firstChords = harmony.realizeChordSymbolDurations(firstChords)

        # chordList.show("text")
        # firstChords.show()

        # access chords
        length = 0
        choraleNumerals = []
        for el in chordList.recurse(classFilter='Chord'):
            # print(el.offset, el, el.activeSite)
            rn = roman.romanNumeralFromChord(el, key)
            choraleNumerals.append(rn.figure)
            file.write(rn.figure + " ")
            # print(rn.figure)
            length += 1
        file.write('\n')
        print(length)
        print(choraleNumerals)
    file.close()

# firstkey = first.keySignature()
# print(first.classes)

parseChorales()


# print roman numerals
def romanToChord(numerals, key):
    for number in numerals:
        roman = roman.RomanNumeral(number, key)


# myStream = stream.Stream()
#
# m1 = stream.Measure()
# m1.timeSignature = meter.TimeSignature('4/4')
# m1.keySignature = key.KeySignature(3)
# m1.append([note.Note('A'), note.Note('A'), note.Note('E5'), note.Note('E5')])
# m2 = stream.Measure()
# m2.append([note.Note('F#5'), note.Note('F#5'), note.Note('E5')])
# m2[-1].quarterLength = 2
# m3 = stream.Measure()
# m3.append([note.Note('D5'), note.Note('D5'), note.Note('C#5'), note.Note('C#5')])
# m4 = stream.Measure()
# m4.append([note.Note('B'), note.Note('B'), note.Note('A')])
# m4[-1].quarterLength = 2
#
# p = stream.Part()
# p.append([m1, m2, m3, m4])
# # p.show()
#
#
# twinkle = converter.parse("tinyNotation: 4/4 a4 a e' e' f'# f'# e'2 d'4 d' c'# c'#")
# twinkle.keySignature = key.KeySignature(3)
# twinkle.show()
#
#
# #Open a score:
# s = corpus.parse("bach/bwv846")
# s.show()
# # s = converter.parse('~/Desktop/1.xml')
# p = graph.plot.HistogramPitchClass(s)
# p.run()
# s.plot(
