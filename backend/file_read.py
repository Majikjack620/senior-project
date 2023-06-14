with open('dependent.txt', 'r') as file:
  for line in file:
    sep = list(line.split())
    length = len(sep)
    
    for i in range(length):
      if sep[i] == "by":
        continue
      else:
        if i == length-1:
          print(sep[i], end=" | \n")
        else:
          print(sep[i], end=" | ")

    print("| - | - | - | - | - | - |")
