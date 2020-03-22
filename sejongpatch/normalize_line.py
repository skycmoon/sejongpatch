from typing import Dict

_QUOT_NORM_MAP = {
    '"': '"',
    '“': '"',
    '”': '"',
    "'": "'",
    "‘": "'",
    "’": "'",
    "`": "'",
}

_COMPATIBILITY_PHONEME_NORM_MAP: Dict[str, str] = {
    "\u1100": "\u3131",  # Choseong      ㄱ
    "\u1101": "\u3132",  # Choseong      ㄲ
    "\u1102": "\u3134",  # Choseong      ㄴ
    "\u1103": "\u3137",  # Choseong      ㄷ
    "\u1104": "\u3138",  # Choseong      ㄸ
    "\u1105": "\u3139",  # Choseong      ㄹ
    "\u1106": "\u3141",  # Choseong      ㅁ
    "\u1107": "\u3142",  # Choseong      ㅂ
    "\u1108": "\u3143",  # Choseong      ㅃ
    "\u1109": "\u3145",  # Choseong      ㅅ
    "\u110a": "\u3146",  # Choseong      ㅆ
    "\u110b": "\u3147",  # Choseong      ㅇ
    "\u110c": "\u3148",  # Choseong      ㅈ
    "\u110d": "\u3149",  # Choseong      ㅉ
    "\u110e": "\u314a",  # Choseong      ㅊ
    "\u110f": "\u314b",  # Choseong      ㅋ
    "\u1110": "\u314c",  # Choseong      ㅌ
    "\u1111": "\u314d",  # Choseong      ㅍ
    "\u1112": "\u314e",  # Choseong      ㅎ
    "\u1161": "\u314f",  # Jungseong     ㅏ
    "\u1162": "\u3150",  # Jungseong     ㅐ
    "\u1163": "\u3151",  # Jungseong     ㅑ
    "\u1164": "\u3152",  # Jungseong     ㅒ
    "\u1165": "\u3153",  # Jungseong     ㅓ
    "\u1166": "\u3154",  # Jungseong     ㅔ
    "\u1167": "\u3155",  # Jungseong     ㅕ
    "\u1168": "\u3156",  # Jungseong     ㅖ
    "\u1169": "\u3157",  # Jungseong     ㅗ
    "\u116a": "\u3158",  # Jungseong     ㅘ
    "\u116b": "\u3159",  # Jungseong     ㅙ
    "\u116c": "\u315a",  # Jungseong     ㅚ
    "\u116d": "\u315b",  # Jungseong     ㅛ
    "\u116e": "\u315c",  # Jungseong     ㅜ
    "\u116f": "\u315d",  # Jungseong     ㅝ
    "\u1170": "\u315e",  # Jungseong     ㅞ
    "\u1171": "\u315f",  # Jungseong     ㅟ
    "\u1172": "\u3160",  # Jungseong     ㅠ
    "\u1173": "\u3161",  # Jungseong     ㅡ
    "\u1174": "\u3162",  # Jungseong     ㅢ
    "\u1175": "\u3163",  # Jungseong     ㅣ
    "\u11a8": "\u3131",  # Jongseong     ㄱ
    "\u11a9": "\u3132",  # Jongseong     ㄲ
    "\u11aa": "\u3133",  # Jongseong     ㄳ
    "\u11ab": "\u3134",  # Jongseong     ㄴ
    "\u11ac": "\u3135",  # Jongseong     ㄵ
    "\u11ad": "\u3136",  # Jongseong     ㄶ
    "\u11ae": "\u3137",  # Jongseong     ㄷ
    "\u11af": "\u3139",  # Jongseong     ㄹ
    "\u11b0": "\u313a",  # Jongseong     ㄺ
    "\u11b1": "\u313b",  # Jongseong     ㄻ
    "\u11b2": "\u313c",  # Jongseong     ㄼ
    "\u11b3": "\u313d",  # Jongseong     ㄽ
    "\u11b4": "\u313e",  # Jongseong     ㄾ
    "\u11b5": "\u313f",  # Jongseong     ㄿ
    "\u11b6": "\u3140",  # Jongseong     ㅀ
    "\u11b7": "\u3141",  # Jongseong     ㅁ
    "\u11b8": "\u3142",  # Jongseong     ㅂ
    "\u11b9": "\u3144",  # Jongseong     ㅄ
    "\u11ba": "\u3145",  # Jongseong     ㅅ
    "\u11bb": "\u3146",  # Jongseong     ㅆ
    "\u11bc": "\u3147",  # Jongseong     ㅇ
    "\u11bd": "\u3148",  # Jongseong     ㅈ
    "\u11be": "\u314a",  # Jongseong     ㅊ
    "\u11bf": "\u314b",  # Jongseong     ㅋ
    "\u11c0": "\u314c",  # Jongseong     ㅌ
    "\u11c1": "\u314d",  # Jongseong     ㅍ
    "\u11c2": "\u314e",  # Jongseong     ㅎ
    "\u119e": "\u318d",  # ᆞ
    "\u111d": "\u3171",  # ㅱ
}


def normalize_line(line: str) -> str:
    line_arr = list(line)
    for i, c in enumerate(line_arr):
        if c in _COMPATIBILITY_PHONEME_NORM_MAP:
            line_arr[i] = _COMPATIBILITY_PHONEME_NORM_MAP[c]
        if c in _QUOT_NORM_MAP:
            line_arr[i] = _QUOT_NORM_MAP[c]
    return "".join(line_arr).strip()
