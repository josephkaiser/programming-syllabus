# title case, all caps, all lower
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# concatenation and title case
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())

# right strip (rstrip), left strip (lstrip) and full strip (strip) examples to remove extra spaces from strings
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language + "!")
favorite_language = ' python'
favorite_language = favorite_language.lstrip()
print(favorite_language + "!")
favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language + "!")

