import re
#Question 1
def check_string(s):
    pattern = r'^[a-zA-Z0-9]+$'
    if re.fullmatch(pattern, s):
        return "Valid"
    else:
        return "Invalid"

print("Q1", check_string("ABCDEFabcdef123450"))
print("Q1", check_string("*&%@#!}{"))

#Question 2
def match_ab(s):
    pattern = r'^ab*$'
    if re.fullmatch(pattern, s):
        return "Match"
    else:
        return "No Match"

tests = ["ab", "abc", "a", "ab", "abb"]

for t in tests:
    print("Q2", t, "->", match_ab(t))

#Question 3
def match_ab_plus(s):
    pattern = r'^ab+$'

    if re.fullmatch(pattern, s):
        return "Match"
    else:
        return "No Match"

tests = ["ab", "abc", "a", "ab", "abb"]

for t in tests:
    print("Q3", t, "->", match_ab_plus(t))

#Question 4
def lowercase_underscore(s):
    pattern = r'^[a-z]+_[a-z]+$'

    if re.fullmatch(pattern, s):
        return "Match"
    else:
        return "No Match"

tests = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]

for t in tests:
    print("Q4", t, "->", lowercase_underscore(t))

#Question 5
def first_word(s):
    pattern = r'^\w+'
    match = re.match(pattern, s)
    if match:
        return match.group()
    else:
        return "No Match"

tests = [
    "The quick brown fox jumps over the lazy dog.",
    " The quick brown fox jumps over the lazy dog."
]

for t in tests:
    print("Q5", t, "->", first_word(t))

#Question 6
def word_with_z(s):
    pattern = r'\b\w*z\w*\b'
    matches = re.findall(pattern, s)
    if matches:
        return matches
    else:
        return "No Match"

tests = [
    "The quick brown fox jumps over the lazy dog.",
    "Python Exercises."
]

for t in tests:
    print("Q6", t, "->", word_with_z(t))

#Question 7
def remove_leading_zeros(ip):
    pattern = r'\b0+(\d+)\b'
    return re.sub(pattern, r'\1', ip)

test_ip = "216.08.094.196"
print("Q7", test_ip, "->", remove_leading_zeros(test_ip))

#Question 8
def search_words(text, words):
    pattern = '|'.join(words)  # join words with OR operator
    matches = re.findall(pattern, text)
    if matches:
        return matches
    else:
        return "No Match"

sample_text = 'The quick brown fox jumps over the lazy dog.'
search_list = ['fox', 'dog', 'horse']

print("Q8", search_words(sample_text, search_list))

#Question 9
def find_word_location(text, word):
    pattern = word
    match = re.search(pattern, text)
    if match:
        return f"'{word}' found at position {match.start()}"
    else:
        return f"'{word}' not found"

sample_text = 'The quick brown fox jumps over the lazy dog.'
search_word = 'fox'

print("Q9", find_word_location(sample_text, search_word))

#Question 10
def replace_spaces_underscores(text, to_underscore=True):
    if to_underscore:
        # Replace spaces with underscores
        return re.sub(r'\s', '_', text)
    else:
        # Replace underscores with spaces
        return re.sub(r'_', ' ', text)

text1 = "Regular Expressions"
text2 = "Code_Examples"

print("Q10", replace_spaces_underscores(text1))          # spaces -> underscores
print("Q10", replace_spaces_underscores(text2, False))  # underscores -> spaces

#Question 11
def extract_date_from_url(url):
    pattern = r'/(\d{4})/(\d{2})/(\d{2})/'
    match = re.search(pattern, url)
    if match:
        year, month, day = match.groups()
        return year, month, day
    else:
        return "No date found"

url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

print("Q11", extract_date_from_url(url))

#Question 12
def words_starting_a_e(text):
    pattern = r'\b[aeAE]\w*\b'
    matches = re.findall(pattern, text)
    if matches:
        return matches
    else:
        return "No Match"

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

print("Q12", words_starting_a_e(sample_text))

#Question 13
def replace_space_comma_dot(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

sample_text = 'Python Exercises, PHP exercises.'
print("Q13", replace_space_comma_dot(sample_text))

#Question 14
def words_starting_a_e(text):
    pattern = r'\b[aeAE]\w*\b'
    matches = re.findall(pattern, text)
    if matches:
        return matches
    else:
        return "No Match"

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

print("Q14", words_starting_a_e(sample_text))

#Question 15
def remove_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text)

sample_text = 'Python      Exercises'
print("Q15", remove_multiple_spaces(sample_text))
