from difflib import SequenceMatcher;
with open("Python projects\demoFile1.txt") as firstFile, open("Python projects\demoFile2") as secondFile:
    dataFirst = firstFile.read()
    dataSecond = secondFile.read()
    matches = SequenceMatcher(None,dataFirst,dataSecond).ratio()
    print(f"The plagirized content is {matches*100}%")