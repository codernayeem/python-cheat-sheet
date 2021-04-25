import re

# findall, search, spilt, sub, finditer

# findall() : Returns a list containing all matches
# search()  : Returns a Match object if there is a match anywhere in the string
# split()   : Returns a list where the string has been split at each match
# sub()     : Replaces one or many matches with a string


# **** Metacharacters ****
# []           A set of characters                                                            "[a-m]"
# \            Signals a special sequence (can also be used to escape special characters)     "\d"
# .            Any character (except newline character)                                       "he..o"
# ^            Starts with                                                                    "^hello"
# $            Ends with                                                                      "world$"
# *            Zero or more occurrences                                                       "aix*"
# +            One or more occurrences                                                        "aix+"
# ?            Zero or One occurrence                                                         "aix+"
# +?, *?, .?   As few characters as possible will be matched                                  "aix+?"
# {m}          exactly m copies of the previous RE                                            "al{2}"
# {m, n}       match from m to n repetitions of the preceding RE, (match as many repetitions as possible)     "al{2, 4}"
# {m, n}?      match from m to n repetitions of the preceding RE, (match as few repetitions as possible)      "al{2}"
# |            Either or                                                                      "falls|stays"
# (...)        Capture and group                                                              "a(ix)+"
# (?#...)      A comment                                                                      "(?#This is a comment)"
# (?=...)      "Isaac (?=Asimov)" will match 'Isaac ' only if it’s followed by 'Asimov'       "Isaac (?=Asimov)"
# (?!...)      "Isaac (?=Asimov)" will match 'Isaac ' only if it’s not followed by 'Asimov'   "Isaac (?!Asimov)"
# (?<=...)     "(?<=abc)def" for 'abcdef' will match 'def'                                     r"(?<=-)\w+"
# (?<!...)     "(?<!abc)def" for 'anydef' will match 'def'                                     r"(?<!\d)\w+"


# **** Special Sequence ****
# \A   Returns a match if the specified characters are at the beginning of the string                 r"\AThe"
# \b   Returns a match where the specified characters are at the beginning or at the end of a word    r"\bain", r"ain\b"
# \B   Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word     r"\Bain" , r"ain\B"
# \d   Returns a match where the string contains digits (numbers from 0-9)                            r"\d"
# \D   Returns a match where the string DOES NOT contain digits                                       r"\D"
# \s   Returns a match where the string contains a white space character                              r"\s"
# \S   Returns a match where the string DOES NOT contain a white space character                      r"\S"
# \w   Returns a match where the string contains any 'word' characters ([a-zA-Z0-9_])                 r"\w"
# \W   Returns a match where the string DOES NOT contain any 'word' characters                        r"\W"
# \Z   Returns a match if the specified characters are at the end of the string                       r"Spain\Z"


# **** Sets ****
# [arn]       Returns a match where one of the specified characters (a, r, or n) are present    
# [a-n]       Returns a match for any lower case character, alphabetically between a and n    
# [^arn]      Returns a match for any character EXCEPT a, r, and n    
# [0123]      Returns a match where any of the specified digits (0, 1, 2, or 3) are present    
# [0-9]       Returns a match for any digit between 0 and 9    
# [0-5][0-9]  Returns a match for any two-digit numbers from 00 and 59    
# [a-zA-Z]    Returns a match for any character alphabetically between a and z, lower case OR upper case    
# [+]         In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string


s1 = '''
Man1 : 01813-456789
Man2 : 01818-646787
Man3 : 01812-846782
'''

print('Findall : ', re.findall(r'\d{5}-\d{6}', s1))      # return list of matched strings
print('Search : ', re.search(r'\d{5}-\d{6}', s1))        # return a match object
print('Sub : ', re.sub(r'\d{5}-\d{6}', '00000000', s1))  # replace all matched strings
print('Split : ', re.split(r'\d{5}-\d{6}', s1))            # returns a list where the string has been split at each match
print('Filditer : ')
matches = re.finditer(r'\d{5}-\d{6}', s1)  # return a iterable of match objects
for i in matches:
    print(i)

# using complie() & finditer()
print('Using compile and finditer : ')
patt = re.compile(r'\d{5}-\d{6}') # use compile, when this is going to be used many times (compile use function caching)
matches = patt.finditer(s1)
for i in matches:
    print(i)

print('-----------------------------')
match = re.search(r'\d{5}-\d{6}', s1)
print(match.string)  # returns the string passed into the function
print(match.re)      # returns the regular expression object passed into the function
print(match.group()) # returns the part of the string where there was a match
print(match.span())  # returns matched part's index (start, end)
print(match.start()) # returns the index of the start of the matched substring
print(match.end())   # returns the index of the end of the matched substring
print('-----------------------------')


s2 = '''
abcd67@gmail.com
123.babu_hi@hotmail.com
tata#@gmail.com
'''

# email ...
patt = re.compile(r'[\w\.-]+@[\w\-]+.[\w\-]+')
matches = patt.finditer(s2)
for i in matches:
    print(i)

