alph = "abcdefghijklmnopqrstuvwxyz"
message = "hello your computer has virus, to fix it, you must paypall me $72,000 in order for me to fix it and give me money"
enc = ""
shift = 13

for c in message:
  try:
    index = alph.index(c) + shift;
    if index > len(message):
      index = index-26
    if index < 1:
      index = index+26
    enc = enc + alph[index]
  except:
    enc = enc + c
print(enc)
