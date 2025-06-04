""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. """

from text import cmudict, pinyin

_pad = "_"
_punctuation = "!'(),.:;? "
_special = "-"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_silences = ["@sp", "@spn", "@sil"]
_twlj = ["pad", "sil", "sp","a", "a˥", "a˥˩", "a˧˥", "a˨˩˦", "AA0", "AA1", "AA2", "AE0", "AE1", "AE2", "AH0", "AH1",
 "AH2", "aj˥", "aj˥˩", "aj˧˥", "aj˨˩˦", "AO0", "AO1", "AO2", "aw˥", "aw˥˩", "aw˧˥", "aw˨˩˦", "AW0", "AW1", "AW2", "AY0",
  "AY1", "AY2", "B", "CH", "ɕ", "ɕʷ", "D", "DH", "e˥", "e˥˩", "e˧˥", "e˨˩˦", "EH0", "EH1", "EH2", "ej˥", "ej˥˩", "ej˧˥",
   "ej˨˩˦", "ER0", "ER1", "ER2", "EY0", "EY1", "EY2", "ə", "ə˥", "ə˥˩", "ə˧˥", "ə˨˩˦", "f", "F", "G", "HH", "i", "i˥", "i˥˩",
    "i˧˥", "i˨˩˦", "IH0", "IH1", "IH2", "IY0", "IY1", "IY2", "j", "JH", "k", "K", "kʰ", "kʷ", "l", "L", "ʎ", "m", "M",
     "mʲ", "n", "N", "NG", "ɲ", "ŋ", "o˥", "o˥˩", "o˧˥", "o˨˩˦", "ow˥", "ow˥˩", "ow˧˥", "ow˨˩˦", "OW0", "OW1", "OW2", "OY0",
      "OY1", "OY2", "p", "P", "pʰ", "pʲ", "pʷ", "R", "ɻ", "s", "S", "SH", "sil", "sp", "spn", "ʂ", "t", "T", "tɕ",
       "tɕʰ", "tɕʷ", "tʰ", "TH", "tʲ", "ts", "tsʰ", "tʷ", "ʈʂ", "ʈʂʰ", "u˥", "u˥˩", "u˧", "u˧˥", "u˨˩˦", "UH0", "UH1",
        "UH2", "UW0", "UW1", "UW2", "ɥ", "V", "w", "W", "x", "xʷ", "y˥", "y˥˩", "y˧˥", "y˨˩˦", "Y", "Z", "z̩˥", "z̩˥˩", "z̩˧˥",
         "z̩˨˩˦", "ZH", "ʐ", "ʐ̩˥", "ʐ̩˥˩", "ʐ̩˧˥", "ʐ̩˨˩˦", "ʔ"]

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ["@" + s for s in cmudict.valid_symbols]
_pinyin = ["@" + s for s in pinyin.valid_symbols]
_twlj = ["@" + s for s in _twlj]

# Export all symbols:
symbols = (
    [_pad]
    + list(_special)
    + list(_punctuation)
    + list(_letters)
    + _arpabet
    + _pinyin
    + _silences
    + _twlj
)
