from ara_fix import preprocess, postprocessing, der, calculate_der

# Test preprocessing
text = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
print("Testing preprocessing:")
processed = preprocess(text)
print(f"Original: {text}")
print(f"Processed: {processed}")

# Test postprocessing
model_output = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
original_input = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
print("\nTesting postprocessing:")
postprocessed = postprocessing(model_output, original_input)
print(f"Model output: {model_output}")
print(f"Original input: {original_input}")
print(f"Postprocessed: {postprocessed}")

# Test DER calculation
reference = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
prediction = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
print("\nTesting DER calculation:")
der_score = der(reference, prediction)
print(f"Reference: {reference}")
print(f"Prediction: {prediction}")
print(f"DER score: {der_score}%")
