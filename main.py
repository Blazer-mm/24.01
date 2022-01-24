teksts = input("Ievadi tekstu: ")
def ReplaceO(teksts):
  if teksts.count("O")>0 or teksts.count("o")>0:
    teksts = teksts.replace("O","%")
    teksts = teksts.replace("o","%")
    print(teksts)
  else:
    teksts = "Nekas nav mainīts"
    print(teksts)
ReplaceO(teksts)