text=input("Ievadi tekstu: ")
x = len(text)
if x>1:
  text=text.upper()
  text="".join(list(reversed(text)))
  print(text)
else:
  print("Teksts ir pārāk mazs")