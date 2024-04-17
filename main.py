def main():
    def get_book_contents(path):
        with open(path) as f:
            return f.read()
    def word_count(text):
        count = 0
        words = text.split()
        #faster method is to use ' return len(words) '
        for word in words:
            count+=1
        return count

    def letter_count(text):
        letters_count = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,
        'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,
        'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        lower_case = text.lower()        
        for letter in lower_case:
            if letter in letters_count:
                letters_count[letter]+=1
        return letters_count

    
        chars = letter_count(text)
        list_dicts = [{key:value} for key, value in chars.items()]
        for dict in list_dicts:
            for key,value in dict.items():
                print(f'The {key} character was found {value} times')

    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    number_of_words = word_count(text)
    

    #Report
    print("---Begin report of books/frankenstein.txt---")
    print(number_of_words, "words found in this document")
    print()
    chars = letter_count(text)
    list_dicts = [{key:value} for key, value in chars.items()]
    for dict in list_dicts:
        for key,value in dict.items():
            print(f'The {key} character was found {value} times')
    print('---End of Report---')

    


main()