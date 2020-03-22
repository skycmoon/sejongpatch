from sejongpatch.sejong_corpus import Word


def assert_eq(actual: Word, expected: Word):
    assert actual.wid == expected.wid
    assert actual.raw == expected.raw
    assert len(actual.morphs) == len(expected.morphs)
    for i, actual_morph in enumerate(actual.morphs):
        assert actual_morph.lex == expected.morphs[i].lex
        assert actual_morph.tag == expected.morphs[i].tag
