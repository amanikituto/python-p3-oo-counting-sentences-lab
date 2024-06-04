#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace all punctuation with periods
        temp = self.value.replace('!', '.').replace('?', '.')
        # Split the string into sentences
        sentences = temp.split('.')
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence.strip() != '']
        return len(sentences)