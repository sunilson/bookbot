from stats import get_num_words, get_num_chars, format_num_chars
import sys

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookPath = sys.argv[1]
    bookText = get_book_text(bookPath)
    numWords = get_num_words(bookText)
    formattedNumChars = format_num_chars(get_num_chars(bookText))
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}".format(path=bookPath))
    print("----------- Word Count ----------")
    print("Found {numWords} total words".format(numWords = numWords))
    print("--------- Character Count -------")
    for entry in formattedNumChars:
        if(entry["char"].isalpha()):
            print("{char}: {num}".format(char=entry["char"], num=entry["num"]))
    print("============= END ===============")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()   

main()