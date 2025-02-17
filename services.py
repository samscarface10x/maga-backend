import random

def load_words_from_file(filename):
    """Reads a list of words from a text file and returns them as a list."""
    with open(filename, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words

def find_matching_words(word_list, word, n):
    """Finds words that have the same first n letters as the input word."""
    matching_words = []
    while len(matching_words) < 1:
        prefix = word[:n].title()
        matching_words = [w for w in word_list if w.title().startswith(prefix)]
        n -= 1
    return matching_words

def get_random_word(word_list):
    """Returns a random word from the given list."""
    if not word_list:
        return None
    return random.choice(word_list)

def generate_alias_with_last_name(last_name:str|None):
    """Generates an alias by concatenating a random matching word with the given last name."""
    words = last_name_aliases
    n = random.randint(1,4)
    matching_words = find_matching_words(words, last_name, n)
    random_word = get_random_word(matching_words)
    if random_word:
        return random_word.title()
    return None

def generate_alias_with_first_name(first_name:str|None):
    """Generates an alias by concatenating the first name with a random matching word."""
    words = first_name_aliases
    n = random.randint(1,4)
    matching_words = find_matching_words(words, first_name, n)
    random_word = get_random_word(matching_words)
    if random_word:
        return random_word.title()
    return None
    
def generate_random_alias(first_name, last_name):
    alias_option = random.randint(1,7)
    alias = None
    if alias_option % 2 == 0:
        alias = generate_alias_with_first_name(first_name)
    else:
        alias = generate_alias_with_last_name(last_name)        
    return alias
    
def generate_alias_with_association():
    pass

f_name_aliases_file = 'last_name_aliases.txt'
l_name_aliases_file = 'last_name_aliases.txt'

first_name_aliases = load_words_from_file(f_name_aliases_file)
last_name_aliases = load_words_from_file(l_name_aliases_file)

first_name = "Dwarkesh"
last_name = "Patel"
print(generate_alias_with_last_name(last_name))
print(generate_alias_with_first_name(first_name))
