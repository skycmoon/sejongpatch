import copy
import re

from sejongpatch.wrapper import ProcessedWord


def recover_english_cases(p_word: ProcessedWord) -> ProcessedWord:
    if p_word.has_error():
        return p_word

    try:
        word_letters = [_ for _ in p_word.word.raw if re.match(r'[a-zA-Z]', _)]
        letter_idx = -1
        is_recovered = False
        word_copy = copy.deepcopy(p_word.word)
        for morph in word_copy.morphs:
            for idx, char in enumerate(morph.lex):
                if not re.match(r'[a-zA-Z]', char):
                    continue
                letter_idx += 1
                if word_letters[letter_idx] == char:
                    continue
                morph.lex = morph.lex[:idx] + word_letters[letter_idx] + morph.lex[idx + 1:]
                is_recovered = True
        if is_recovered:
            p_word.word.morphs = word_copy.morphs
    except IndexError as idx_err:
        p_word.err = f"English recover failed: {p_word.word}, {idx_err}."

    return p_word
