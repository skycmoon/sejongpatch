from sejongpatch.wrapper import ProcessedWord

_QUOT_NORM = {
    '"': '"',
    '“': '"',
    '”': '"',
    "'": "'",
    "‘": "'",
    "’": "'",
    "`": "'",
}

_SUPPORTED_QUOTS = {'"', "'"}


def validate_quotations(p_word: ProcessedWord) -> ProcessedWord:
    if p_word.has_error():
        return p_word

    word = p_word.word
    word_quots = [_ for _ in word.raw if _ in _SUPPORTED_QUOTS]
    morph_quots = []
    for idx, morph in enumerate(word.morphs):
        if morph.tag != 'SS' or morph.lex not in _QUOT_NORM:
            continue
        morph_quots.append((idx, morph))
        quot_idx = len(morph_quots) - 1
        if len(word_quots) <= quot_idx or word_quots[quot_idx] != morph.lex:
            p_word.err = f"{quot_idx + 1}-th quots are different: {word}"
            return p_word
    if len(word_quots) != len(morph_quots):
        morph_quots = [_ for _ in word.morph_str() if _ in _QUOT_NORM]
        if word_quots != morph_quots:
            p_word.err = f"Number of quots are different: {word}"
        return p_word
    return p_word
