import re
from .config import DIACRITICS, DIACRITICS_PATTERN, LETTERS_PATTERN

def is_diacritic(c):
    return re.match(DIACRITICS_PATTERN, c)

def is_letter(c):
    return re.match(LETTERS_PATTERN, c)

def remove_last_diacritic(text):
  while text and text[-1] in DIACRITICS:
    text = text[:-1]
  return text

def postprocess(model_output, original_input):

    result = []
    i, j = 0, 0

    while i < len(model_output) and j < len(original_input):
        out_char = model_output[i]
        in_char = original_input[j]
        # print(f"i {i} j {j}")
        # print(f"out {out_char} and {in_char}")
        

        # Cases we increase both indecies
        CASE_1 = out_char == in_char
        CASE_2 = is_diacritic(out_char) and is_diacritic(in_char)
        CASE_3 = out_char == ' ' and in_char == ' '
        CASE_4 = is_letter(out_char) and is_letter(in_char)

        # Cases we increase input index
        CASE_5 = is_letter(out_char) and is_diacritic(in_char)
        CASE_6 = out_char == ' ' and is_diacritic(in_char)
        CASE_7 = is_letter(out_char) and in_char == ' ' 

        # Cases we increase output index
        CASE_8 = out_char == ' ' and is_letter(in_char)
        CASE_9 = is_diacritic(out_char) and in_char == ' '
        CASE_10 = is_diacritic(out_char) and is_letter(in_char)

        if CASE_1 or CASE_2 or CASE_3 or CASE_4:
            # print("Cases 1-4")
            result.append(out_char)
            i += 1
            j += 1
        elif CASE_5 or CASE_6:
            # print("Cases 5-6")
            # result.append(out_char)
            j += 1
        elif CASE_7:
            # print("Case 7: Letter out Space in")
            result.append(out_char)
            j += 1
        elif CASE_8 or CASE_9 or CASE_10:
            # print("Cases 8-10")
            # result.append(in_char)
            i += 1
        else:
            # print("Not in the 10 cases")
            result.append(out_char)
            i += 1
            j += 1
        # print("+"*10)

    while i < len(model_output):
        if model_output[i] != ' ':
            result.append(model_output[i])
        i += 1
    
    return remove_last_diacritic(''.join(result))
