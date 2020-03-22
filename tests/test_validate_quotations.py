import pytest

from sejongpatch.sejong_corpus import Word, Morph
from sejongpatch.validate_quotations import validate_quotations
from sejongpatch.wrapper import ProcessedWord


class TestValidateQuotations:
    @pytest.mark.parametrize("test_input,expected", [
        (
                Word(raw='"태극기"',
                     morphs=[Morph(lex='"', tag="SS"), Morph(lex="태극기", tag="NNG"), Morph(lex='"', tag="SS")]),
                False
        ),
        (
                Word(raw='"태극기"',
                     morphs=[Morph(lex="'", tag="SS"), Morph(lex="태극기", tag="NNG"), Morph(lex='"', tag="SS")]),
                True
        ),
        (
                Word(raw='"태극기""',
                     morphs=[Morph(lex='"', tag="SS"), Morph(lex="태극기", tag="NNG"), Morph(lex='"', tag="SS")]),
                True
        ),
        (
                Word(raw='"태극기"',
                     morphs=[Morph(lex='"', tag="SS"), Morph(lex="태극기", tag="NNG"), Morph(lex='"', tag="SS"),
                             Morph(lex='"', tag="SS")]),
                True
        ),
    ])
    def test_validate_quotations(self, test_input: Word, expected: bool):
        actual_pw = validate_quotations(ProcessedWord(test_input))
        assert actual_pw.has_error() == expected
