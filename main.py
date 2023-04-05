import string


def contador(text):
    d = dict()
    for line in text:
        line = line.strip()
        line = line.upper()
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = ''.join(i for i in line if not i.isdigit())
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print(d)
    for k, v in d.items():
        if v > 0:
            print(k, ':', v)
    print('-----------------------------------')

contador(open("BeatlesDadosporAlbumCOPIA.txt", "r"))



'''contador(open("PleasePleaseMeLyrics.txt", "r"))
contador(open("WithTheBeatles.txt", "r"))
contador(open("AHardDaysNightLyrics.txt", "r"))
contador(open("BeatlesForSaleLyrics.txt", "r"))
contador(open("HelpLyrics.txt", "r"))
contador(open("RubberSoulLyrics.txt", "r"))
contador(open("RevolverLyrics.txt", "r"))
contador(open("SgtPeppersLyrics.txt", "r"))
contador(open("MagicalMysteryTourLyrics.txt", "r"))
contador(open("WhiteAlbumLyrics.txt", "r"))
contador(open("YellowSubmarineLyrics.txt", "r"))
contador(open("AbbeyRoadLyrics.txt", "r"))
contador(open("LetItBeLyrics.txt", "r"))'''
