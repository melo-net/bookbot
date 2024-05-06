def word_count(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    print(word_count(file_contents))

path_to_file = "books/frankenstein.txt"
main()