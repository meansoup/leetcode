class Solution:
    def calc_letters(self, letters):
        alphabet_count = [0] * 26
        for letter in letters:
            index = ord(letter) - ord('a')
            alphabet_count[index] += 1
        return alphabet_count

    def calc_words_alpha(self, words):
        return [self.calc_letters(word) for word in words]

    def minus_score(self, minuend, subtrahend):
        minuend[:] = [minuend[i] - subtrahend[i] for i in range(26)]

    def plus_score(self, augend, addend):
        augend[:] = [augend[i] + addend[i] for i in range(26)]

    def subtractable(self, minuend, subtrahend):
        return all(m >= s for m, s in zip(minuend, subtrahend))

    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        letter_count = self.calc_letters(letters)
        words_alpha_count = self.calc_words_alpha(words)
        words_score = [sum([words_alpha_count[word_idx][i] * score[i] for i in range(26)]) for word_idx in range(len(words))]

        def calc_score(word_idx, current_score):
            if word_idx == len(words):
                return current_score

            without = calc_score(word_idx + 1, current_score)

            if self.subtractable(letter_count, words_alpha_count[word_idx]):
                self.minus_score(letter_count, words_alpha_count[word_idx])
                with_word = calc_score(word_idx + 1, current_score + words_score[word_idx])
                self.plus_score(letter_count, words_alpha_count[word_idx])
                return max(with_word, without)
            else:
                return without

        return calc_score(0, 0)