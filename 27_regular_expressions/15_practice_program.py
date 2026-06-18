import re

password = "Govind123"

pattern = r"^(?=.*[A-Za-z])(?=.*\d).+$"

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")