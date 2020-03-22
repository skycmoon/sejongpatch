from sejongpatch.sejong_corpus import Morph
from sejongpatch.wrapper import ProcessedWord


def attach_missing_symbols(p_word: ProcessedWord) -> ProcessedWord:
    if p_word.has_error():
        return p_word

    raw_word = p_word.word.raw
    raw_morph = ''.join([_.lex for _ in p_word.word.morphs])
    if not raw_word.startswith(raw_morph) or len(raw_word) != len(raw_morph) + 1:
        return p_word
    last_symbol = raw_word[-1]
    if last_symbol == '.' and p_word.word.morphs[-1].tag == 'EC':
        p_word.word.morphs.append(Morph('.', 'SF'))
    elif last_symbol == ',':
        p_word.word.morphs.append(Morph(',', 'SP'))
    elif last_symbol == '"':
        p_word.word.morphs.append(Morph('"', 'SS'))
