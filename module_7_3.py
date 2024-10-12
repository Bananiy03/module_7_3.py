import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation_to_remove = [',', '.', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()

                for punctuation in punctuation_to_remove:
                    text = text.replace(punctuation, '')

                self.words = text.split()
                all_words[file_name] = self.words

        return all_words

    def find(self, word):
        search_word = word.lower()
        word_positions = {}

        for name, words in self.get_all_words().items():
            if search_word in words:
                word_positions[name] = words.index(search_word)

        return word_positions

    def count(self, word):
        search_word = word.lower()
        word_counts = {}

        for name, words in self.get_all_words().items():
            word_counts[name] = words.count(search_word)

        return word_counts


# Пример использования
finder2 = WordsFinder('test_file.txt')

# Все слова
print(finder2.get_all_words())

# Позиция первого появления слова 'TEXT'
print(finder2.find('TEXT'))

# Количество вхождений слова 'teXT'
print(finder2.count('teXT'))
