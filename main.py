import pyperclip
import python_minifier

text = "".join(open("input.txt").readlines())
print(bytearray(text, "ascii"))
# encoded_text = str(b'1', "u16")
# print("exec(bytes(\"{}\",\"u16\")[2:])".format(encoded_text))
# pyperclip.copy("exec(bytes(\"{}\",\"u16\")[2:])".format(encoded_text))
print(b's=open(\'i\').readlines();print(sum([1if int(s[i-1])<int(a)else 0for i,a in enumerate(s)])) '.decode('utf-16'))