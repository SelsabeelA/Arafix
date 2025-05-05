LETTERS = [
    'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ',
    'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي', 'ا', 'ى', 'أ', 'إ', 'ؤ', 'ئ', 'ة', 'ء' , 'آ'
]

DIACRITICS = [
    "", # No Diacritic
    "َ", # Fatha
    "ً", # Fathatah
    "ُ", # Damma
    "ٌ", # Dammatan
    "ِ", # Kasra
    "ٍ", # Kasratan
    "ْ", # Sukun
    "ّ", # Shaddah
    "َّ", # Shaddah + Fatha
    "ًّ", # Shaddah + Fathatah
    "ُّ", # Shaddah + Damma
    "ٌّ", # Shaddah + Dammatan
    "ِّ", # Shaddah + Kasra
    "ٍّ", # Shaddah + Kasratan
]

# Arabic diacritics range (Tashkeel)
DIACRITICS_PATTERN = r'[\u0617-\u061A\u064B-\u0652]'

# Arabic letters (common range)
LETTERS_PATTERN = r'[\u0621-\u064A]'

