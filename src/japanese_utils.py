import re

# Sources:
# Hiragana Unicode Table - Wikipedia: https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode/U3040
# Regular Expression for Japanese Characters: http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/

HIRAGANA_FULL = r'[ぁ-ゟ]'
KATAKANA_FULL = r'[゠-ヿ]'
KANJI = r'[㐀-䶵一-鿋豈-頻]'
RADICALS = r'[⺀-⿕]'
KATAKANA_HALF = r'[｟-ﾟ]'
ALPHANUM_FULL = r'[！-～]'
symbols_punct = r'[、-〿]'
misc_symbols = r'[ㇰ-ㇿ㈠-㉃㊀-㋾㌀-㍿]'
ascii_char = r'[ -~]'


def extract_unicode_block(unicode_block, string):
    ''' extracts and returns all texts from a unicode block from string argument.
            Note that you must use the unicode blocks defined above, or patterns of similar form '''
    return re.findall(unicode_block, string)


def remove_unicode_block(unicode_block, string):
    ''' removes all chaacters from a unicode block and returns all remaining texts from string argument.
            Note that you must use the unicode blocks defined above, or patterns of similar form '''
    return re.sub(unicode_block, '', string)


def is_hiragana_full(char) -> bool:
    return re.match(HIRAGANA_FULL, char) != None


def is_katakana_full(char) -> bool:
    return re.match(KATAKANA_FULL, char) != None


def is_kanji(char) -> bool:
    return re.match(KANJI, char) != None

# Examples of use

#text = '初めての駅 自由が丘の駅で、大井町線から降りると、ママは、トットちゃんの手を引っ張って、改札口を出ようとした。ぁゟ゠ヿ㐀䶵一鿋豈頻⺀⿕｟ﾟabc！～、〿ㇰㇿ㈠㉃㊀㋾㌀㍿'
#print('Original text string:', text, '\n')
#print('All kanji removed:', jp_utils.remove_unicode_block(jp_utils.KANJI, text))
#print('All hiragana in text:', ''.join(jp_utils.extract_unicode_block(jp_utils.HIRAGANA_FULL, text)))
