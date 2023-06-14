with open('dependent.txt', 'r') as file:
  for line in file:
    sep = list(line.split())
    length = len(sep)
    
    for i in range(length):
      if i == length-1:
        print(sep[i], end=" | \n")
      else:
        print(sep[i], end=" | ")

    print("| - | - | - | - | - | - |")
