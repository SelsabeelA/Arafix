# AraFix - Arabic Text Processing and Diacritization Evaluation

A Python package for preprocessing Arabic text and evaluating diacritization models.

## Installation

### Local Installation
```bash
pip install -e .
```

### Kaggle Notebook
1. Upload the package files to your Kaggle notebook
2. Install the required dependencies:
```python
!pip install transformers datasets pyarabic jiwer diacritization_evaluation
```
3. Add the package directory to Python path:
```python
import sys
sys.path.append('/kaggle/working/ara_fix')
```
4. Import the package:
```python
from ara_fix import preprocess, postprocessing, der, calculate_der
```

### Google Colab
1. Upload the package files to your Colab notebook
2. Install the required dependencies:
```python
!pip install transformers datasets pyarabic jiwer diacritization_evaluation
```
3. Add the package directory to Python path:
```python
import sys
sys.path.append('/content/ara_fix')
```
4. Import the package:
```python
from ara_fix import preprocess, postprocessing, der, calculate_der
```

## Usage

### Preprocessing
```python
from ara_fix import preprocess

text = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
processed = preprocess(text)
print(processed)  # Output: "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
```

### Postprocessing
```python
from ara_fix import postprocessing

model_output = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
original_input = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
postprocessed = postprocessing(model_output, original_input)
print(postprocessed)  # Output: "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
```

### Diacritic Error Rate (DER)
```python
from ara_fix import der, calculate_der

reference = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
prediction = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"

der_score = der(reference, prediction)
print(f"DER score: {der_score}%")  # Output: "DER score: 0.0%"
```

## Functions

### `preprocess(text, remove_last_diacritic=True)`
- Removes tatweel (ـ) characters
- Removes extra spaces
- Strips invalid characters
- Normalizes text to NFC
- Optionally removes last diacritic

### `postprocessing(model_output, original_input)`
- Aligns model output with original input
- Preserves correct diacritic placement
- Handles letter and diacritic combinations

### `der(reference, prediction)`
- Calculates Diacritic Error Rate
- Compares reference and prediction diacritics
- Returns error rate as percentage

### `calculate_der()`
- Wrapper function for diacritization_evaluation's DER calculation

## Dependencies
- transformers
- datasets
- pyarabic
- jiwer
- diacritization_evaluation
- torch
- tqdm

## License
MIT License
