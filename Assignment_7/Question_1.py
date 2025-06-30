import re

email = "test@example.com"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
print(bool(re.match(pattern, email)))  

# Explanation...
# ^ – Start of the string

# [\w\.-]+ – Match one or more word characters (a-z, A-Z, 0-9, _) or . or -

# @ – Must include the @ symbol

# [\w\.-]+ – Match domain name (e.g., gmail, outlook)

# \. – Match the dot (.) before domain extension

# \w{2,4} – Match 2 to 4 characters (e.g., com, net, org)

# $ – End of the string

mobile_no = "9898965923"
pattern = r'^[6-9]\d{9}$'
print(bool(re.match(pattern,mobile_no)))

# Explanation..

# ^ – Start

# [6-9] – First digit must be from 6 to 9 (valid starting digit in India)

# \d{9} – Followed by 9 digits (\d = digit)

# $ – End

string = "abc859"
pattern = r'^.+$'
print(bool(re.match(pattern,string)))

# Explanation...
# ^ – Start of the string

# .+ – One or more of any character (except newline)

# $ – End of the string

Strong_pass = "Hello@System96"
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
print(bool(re.match(pattern,Strong_pass)))

# Explanation...

# ^ – Start

# (?=.*[a-z]) – Lookahead for at least one lowercase letter

# (?=.*[A-Z]) – Lookahead for at least one uppercase letter

# (?=.*\d) – Lookahead for at least one digit

# .{8,} – Minimum of 8 characters (any kind)

# $ – End

#    Alphabetic String With Spaces

Alpha_string_space = "Hello humans"
pattern = r'^[A-Za-z ]+$'
print(bool(re.match(pattern,Alpha_string_space)))

# Explanation...
# ^ – Anchors the start of the string

# [A-Za-z ]+ – Matches one or more:

# A-Z → uppercase letters

# a-z → lowercase letters

# space character ( )

# $ – Anchors the end of the string