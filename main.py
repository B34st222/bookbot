with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(book):
    book_split_words = book.split()
    return len(book_split_words)

def sort_on(dict):
    return dict["num"]

def count_char(book):
    book = book.lower()

    book_dict = {}
    for char in book:
        if char.isalpha() == True:

            if char in book_dict:
                book_dict[char] += 1
            else:
                book_dict[char] = 1
    
    bdl = []

    for key in book_dict:
        bdl.append({"char":key, "num":book_dict[key]})
    
    bdl.sort(reverse=True, key=sort_on)
    for i in bdl:
        letter = i["char"]
        use = i["num"]
        print(f"The \'{letter}' character was found {use} times")
  
    
    





def main(book):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(book)} words found in the document")
    print("")

    count_char(book)
    print("--- End report ---")


main(file_contents)