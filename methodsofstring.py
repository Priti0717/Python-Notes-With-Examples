
# 1) upper()= Return a copy of the string converted to uppercase.

name="the kiran academy"
print(name.upper())
name1=name.upper()
print(name1)

# 2) lower()= Return a copy of the string converted to lowercase.

name="THE KIRAN ACADEMY"
print(name.lower())
name1=name.lower()
print(name1)

"""3) title() = Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case."""

name="the kiran academy"
print(name.title())
name1=name.title()
print(name1)


""" 4) capitalize ()= Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case"""


name="the kiran academy"
print(name.capitalize())
name1=name.capitalize()
print(name1)

# 5) isalpha()=Return True if the string is an alphabetic string, False otherwise.
name="pritipatil"
print(name.isalpha())

name1="1234priti"
print(name1.isalpha())

# 6) isnumeric()= Return True if the string is a numeric string, False otherwise
name="1234567890"
print(name.isnumeric())

name1="priti"
print(name1.isnumeric())

# 7) isalnum()=Return True if the string is an alpha-numeric string, False otherwise.
name="1234567890pritu"
print(name.isalnum())

name1="priti"
print(name1.isalnum())

name2="12345"
print(name2.isalnum())

name3="123 ravi"
print(name3.isalnum())


# 8) index()= gives us index value
name="sidhant"
print(name.index('h'))

# 9) count()= gives us how much time letter came
name="sidhant"
print(name.count('h'))

# 10) istitle()=Return True if the string is a title-cased string, False otherwise.
name="sidhant"
print(name.istitle())

name="Sidhant"
print(name.istitle())

# 11)isspace()=Return True if the string is a whitespace string, False otherwise.
name="sidhant"
print(name.isspace())

name1="  "
print(name1.isspace())

# 12)replace()=Return a copy with all occurrences of substring old replaced by new.
name="sidhant"
print(name.replace("sidhant","priti"))
