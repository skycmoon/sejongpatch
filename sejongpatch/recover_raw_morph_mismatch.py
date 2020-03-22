import logging
import os
import sys

from sejongpatch.sejong_corpus import Morph, ParseError, Word, WORD_ID_PTN


def recover_raw_morph_mismatch(line: str) -> str:
    """
    어절의 원문과 형태소 분석 결과의 문자가 정규화하면 같지만 코드가 다른 경우 원문의 문자로 복원
    """
    wid, raw, morphs_str = line.split('\t')
    raw_idx = 0
    morphs = []
    for token_str in morphs_str.split(' + '):
        morph = Morph.parse(token_str)
        lex = []
        for _ in range(len(morph.lex)):
            try:
                lex.append(raw[raw_idx])
                raw_idx += 1
            except IndexError as idx_err:
                logging.error(line)
                raise idx_err
        morph.lex = ''.join(lex)
        morphs.append(morph)
    morphs_new = ' + '.join([str(m) for m in morphs])
    logging.debug('%s\t%s\t%s  =>  %s', wid, raw, morphs_str, morphs_new)
    return '{}\t{}\t{}'.format(wid, raw, morphs_new)


def run():
    """
    run function which is the start point of program
    """
    file_name = os.path.basename(sys.stdin.name)
    for line_num, line in enumerate(sys.stdin, start=1):
        line = line.rstrip('\r\n')
        if not WORD_ID_PTN.match(line):
            print(line)
            continue
        try:
            Word.parse(line, file_name, line_num)
        except ParseError as par_err:
            if 'raw-morph mismatch' in str(par_err):
                line = recover_raw_morph_mismatch(line)
            else:
                raise par_err
        print(line)
