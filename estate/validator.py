import re


# This variable is for regular validation of English letters and number with a limit of more than 5 characters and less than 50 characters
english_regex = re.compile(r'^[a-zA-Z0-9 ]{5,50}$')
