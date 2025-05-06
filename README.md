# AraFix - Arabic Text Correction (Pro and Post Processing and Diacritization Evaluation)

A Python package for preprocessing Arabic text and evaluating diacritization models.

## Contributors:

[Roaa Fathi Nada](https://github.com/rFathi03) 

[Basma Mahmoud Hashem](https://github.com/Basma2423/) 
## Installation

### Local Installation
```bash
pip install -e .
```

### Kaggle Notebook
1. Upload the package files to your Kaggle notebook
2. Install the required dependencies:
```python
!pip install transformers datasets pyarabic jiwer
```
3. Add the package directory to Python path:
```python
import sys
sys.path.append('/kaggle/working/ara_fix')
```
4. Import the package:
```python
from ara_fix import AraFix
```

### Google Colab
1. Upload the package files to your Colab notebook
2. Install the required dependencies:
```python
!pip install transformers datasets pyarabic jiwer
```
3. Add the package directory to Python path:
```python
import sys
sys.path.append('/content/ara_fix')
```
4. Import the package:
```python
from ara_fix import AraFix
```

## Usage

### Preprocessing
```python
from ara_fix import AraFix

corrector = AraFix()

text = "فِي يَوْمِنَا هَذَا وَاصَرَ الشَّعْبُ الْيَابَانِيُّ إِلٌى يَوْمِنَا هَذَا عَلَى تَقِّلِيدِ الْهَانَامِي، الْآلٍّافُ مِنَ الْأَشْخَاصِ تَمْلَأُ علْحَدَائِقَ لِعَغْدِ حَفْرِ الْهَانَامِي"
corrected_text = corrector.correct(text)
print(f"Corrected Text: {corrected_text}")
# Output: "فِي يَوْمِنَا هَذَا وَاصَلَ الشَّعْبُ الْيَابَانِيُّ إِلَى يَوْمِنَا هَذَا عَلَى تَقْلِيدِ الْهَانَامِي الْآلَافُ مِنَ الْأَشْخَاصِ تَمْلَأُ الْحَدَائِقَ لِعَقْدِ حَفْرِ الْهَانَامِي"
```


## AraFix Methods

### `correct(text)`
- text: **str** or a **list** of str
- corrects phonetic and diacritic mistakes

### `evaluate(reference, text)`
- reference: **str** or a **list** of str
- text: **str** or a **list** of str
- computes character, word, and diacritic error rates (CER, WER, and DER)

## Dependencies
- transformers
- datasets
- pyarabic
- jiwer
- torch
- tqdm

## License
MIT License
