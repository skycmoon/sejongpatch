import pytest

from sejongpatch.recover_english_cases import recover_english_cases
from sejongpatch.sejong_corpus import Word, Morph
from sejongpatch.wrapper import ProcessedWord
from tests.test_helper import assert_eq


class TestNormalizeLine:
    @pytest.mark.parametrize("test_input,expected", [
        (
                Word(raw="ABC",
                     morphs=[Morph(lex="A", tag="SS"), Morph(lex="b", tag="SS"), Morph(lex="c", tag="SS")]),
                (False, Word(raw="ABC",
                             morphs=[Morph(lex="A", tag="SS"), Morph(lex="B", tag="SS"), Morph(lex="C", tag="SS")]))
        ),
        (
                Word(raw="abc",
                     morphs=[Morph(lex="A", tag="SS"), Morph(lex="b", tag="SS"), Morph(lex="C", tag="SS")]),
                (False, Word(raw="abc",
                             morphs=[Morph(lex="a", tag="SS"), Morph(lex="b", tag="SS"), Morph(lex="c", tag="SS")])),
        ),
        (
                Word(raw="abc",
                     morphs=[Morph(lex="A", tag="SS"), Morph(lex="b", tag="SS"), Morph(lex="C", tag="SS"),
                             Morph(lex="C", tag="SS")]),
                (True, Word()),
        ),
    ])
    def test_validate_quotations(self, test_input: Word, expected: (bool, Word)):
        actual = recover_english_cases(ProcessedWord(test_input))
        assert actual.has_error() == expected[0]
        if not actual.has_error():
            assert_eq(actual.word, expected[1])
