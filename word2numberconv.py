def text2int(textnum, numwords={}):
    if not numwords:
        units = ["eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf"]

        for index in range(1, len(units) + 1):
            numwords[units[index-1]] = index
    
    return numwords.get(textnum, "NO NUMBER")