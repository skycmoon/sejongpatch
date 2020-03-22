import pytest

from sejongpatch.normalize_line import normalize_line


class TestNormalizeLine:
    @pytest.mark.parametrize("test_input,expected", [
        ("", ""),
        ('"””', '"""'),
        ("'‘’`", "''''"),
        ("ㄱㄴㄷ", "ㄱㄴㄷ"),
        (" abc \r\n", "abc"),
        ("ᄀᆯ", "ㄱㄹ"),
        ("ᄀᆯ", "ㄱㄹ"),
        ("\u1100\u1105", "ㄱㄹ")

    ])
    def test_validate_quotations(self, test_input: str, expected: str):
        actual = normalize_line(test_input)
        assert actual == expected
