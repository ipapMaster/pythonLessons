# res = ord(string[0])  # Код буквы P = 80 (код по символу)
# res = chr(189)  # Символ с кодом 80 - P (символ по коду)

# string = 'Python'  # UTF-8 (0 - 255)  -> UTF-16 (0 - 65535)
string = 'S|wkrq'
encrypted = []

for letter in string:
    code = ord(letter)
    code -= 3
    new_letter = chr(code)
    encrypted.append(new_letter)

print(*encrypted, sep='')
