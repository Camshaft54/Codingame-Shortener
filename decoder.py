encoded_text = input("Paste Encoded Text: ")
print(bytes(encoded_text, "u16")[2:].decode("ascii"))
