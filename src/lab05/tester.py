from pathlib import Path


def cat(filey: str|Path, kol):
    if filey is Path:
        a = open(filey).readlines(int(kol))
        print(a)
    else:
        print(filey)

