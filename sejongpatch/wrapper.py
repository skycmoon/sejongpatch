from sejongpatch.sejong_corpus import Word


class ProcessedWord:
    def __init__(self, word: Word) -> None:
        self.word = word
        self.err = ""

    def has_error(self) -> bool:
        return not not self.err  # if error is not None or empty
