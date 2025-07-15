def get_num_words(bookText: str):
    return len(bookText.split())

def get_num_chars(bookText: str):
    result: dict = dict()
    for char in bookText:
        lowerCaseChar = char.lower()
        currentValue = result[lowerCaseChar] if lowerCaseChar in result else 0
        result[lowerCaseChar] = currentValue + 1
    return result

def sort_on(item: dict):
    return item["num"]

def format_num_chars(charDict: dict):
    dictList: list = []
    for charKey in charDict:
        print(charKey)
        dictList.append({
            "char": charKey,
            "num": charDict[charKey]
        })
    dictList.sort(reverse=True, key=sort_on)
    return dictList