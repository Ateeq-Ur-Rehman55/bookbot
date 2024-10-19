def main():
    file = "books/frankenstein.txt"
    text = get_content(file)
    number = count_word(text)
    dic = get_chars_dict(text)
    
    chars_sorted_list = chars_dict_to_sorted_list(dic)

    print(f"--- Begin report of {file} ---")
    print(f"{number} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_content(file):
    with open(file) as f:
        return f.read()

def count_word(text):
    number = text.split()
    return len(number)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
main()