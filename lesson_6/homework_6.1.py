text = input("Write the text:")
unique = set(text)
if len(unique) > 10:
    print(True)
else:
    print(False)
