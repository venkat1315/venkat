import re

text = "Python is Easy To Learn and Fun"
words = re.findall(r'\b[A-Z][a-z]*\b', text)
print("Capitalized words:", words)
