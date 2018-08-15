# textutil
utility functions regarding text and language such as

language of alphabet, language of word, length of specified language alphabet in a word, ..


* alphabet.py has functions as follows
  * is_hanja() check whether a character is Chinese or not. (unihan)
  * is_hangul() check whether a character is Korean or not.
  * is_alpha() check whether a character is English or not.
  * is_num() check whether a character is number or not.
  * is_punctuation() check whether a character is punctuation mark of not.
  * is_extended_punctuation() check whether a character is a symbol that can be used in article including puntuation mark.

Han character is originated from China but adopted and changed in neighbor countries like Japan and Korea.
In Unicode, multiple character sets of the so-called CJK languages are mapped into a single set of unified characters, unihan.
(https://en.wikipedia.org/wiki/Han_unification)
  
* unihan.py has functions as follows
  * is_chinese_unihan() check whether a han character is used in China or not
  * is_japanese_unihan() check whether a han character is used in Japan or not
  * is_korean_unihan() check whether a han character is used in Korea or not
