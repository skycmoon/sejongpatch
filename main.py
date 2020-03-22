import logging
import os
import sys
from argparse import ArgumentParser

from sejongpatch.fix_final_symbol_error import attach_missing_symbols
from sejongpatch.normalize_line import normalize_line
from sejongpatch.recover_english_cases import recover_english_cases
from sejongpatch.recover_raw_morph_mismatch import recover_raw_morph_mismatch
from sejongpatch.sejong_corpus import WORD_ID_PTN, Word, ParseError
from sejongpatch.validate_quotations import validate_quotations
from sejongpatch.wrapper import ProcessedWord


def run():
    file_name = os.path.basename(sys.stdin.name)
    for line_num, line in enumerate(sys.stdin, start=1):
        line = normalize_line(line)
        if not WORD_ID_PTN.match(line):
            print(line)
            continue

        try:
            p_word = ProcessedWord(Word.parse(line, file_name, line_num))
        except ParseError as par_err:
            if 'raw-morph mismatch' in str(par_err):
                line = recover_raw_morph_mismatch(line)
                p_word = ProcessedWord(Word.parse(line, file_name, line_num))
            else:
                logging.error('Morpheme mismatch recover failed, %s(%d): %s', file_name, line_num, line)
                continue
        recover_english_cases(p_word)
        attach_missing_symbols(p_word)
        validate_quotations(p_word)
        print('{}\t{}\t{}'.format(p_word.word.wid, p_word.word.raw, p_word.word.morph_str()))


def main():
    """
    main function processes only argument parsing
    """
    parser = ArgumentParser(description='Patch errors in Sejong Corpus')
    parser.add_argument('--input', help='input file <default: stdin>', metavar='FILE')
    parser.add_argument('--output', help='output file <default: stdout>', metavar='FILE')
    parser.add_argument('--debug', help='enable debug', action='store_true')
    args = parser.parse_args()

    if args.input:
        sys.stdin = open(args.input, 'r', encoding='UTF-8')
    if args.output:
        sys.stdout = open(args.output, 'w', encoding='UTF-8')
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    run()


if __name__ == '__main__':
    main()
