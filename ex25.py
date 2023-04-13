def break_words(stuff):
    """Эта функций рабирает текст на слове."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Сортирует слова."""
    return sorted(words)

def print_first_word(words):
    """Выводит первое слово после извлечения."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Выводит последнее слово после извечления."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Приминает целое предложение и возращает отсорированные слова."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Выводит первое и последнее слова предложения."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Сортирует слова, а затем выводит первое и последнее."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
