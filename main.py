def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(count_words(file_contents))
    #print(count_chars(file_contents))
    chars_dict = count_chars(file_contents)
    chars_list = [{x: y} for x,y in chars_dict.items()]
    chars_list.sort(key=lambda x: list(x.values())[0], reverse=True)
    for char_dict in chars_list:
        for char_key, char_value in char_dict.items():
            if char_key.isalpha():
                print(f"The '{char_key}' character was found {char_value} times")



def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] +=1
        else:
            chars[char] = 1
    return chars

if __name__ == "__main__":
    main()