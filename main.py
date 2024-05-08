def word_count(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def letter_count(file_contents):
    letter_stats_dic = {
        "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, 
        "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, 
        "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, 
        "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, 
        "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, 
        "z" : 0 
    }

    for l in letter_stats_dic:
        char_num = file_contents.count(l)
        letter_stats_dic[l] = char_num

    return letter_stats_dic 

def sort_dictionary(dictionary_result):
    sort_by_highest = sorted(dictionary_result.items(), reverse=True, key = lambda item: item[1])

    tuplelist_to_dict = {}
    for key, value in sort_by_highest:
        tuplelist_to_dict[key] = value

    return tuplelist_to_dict

def make_book_report(total_word_count,final_character_count):
    print (f"--- Begin report of {path_to_file} ---")
    print (f"{total_word_count} words found in document\n")
    for item in final_character_count:
        print(f"the '{item}' character was found {final_character_count[item]} times")

    print (f"--- End report ---")
    pass

def main():
    
    with open(path_to_file) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()

    final_character_count = sort_dictionary(letter_count(file_contents))
    make_book_report(word_count(file_contents),final_character_count) 

path_to_file = "books/frankenstein.txt"
main()