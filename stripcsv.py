import os


def stripdoc():
    os.system("head -n 1 results.csv > new.csv")
    os.system("tail -n 1 results.csv >> new.csv")

