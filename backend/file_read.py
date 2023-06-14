with open('dependent.txt', 'r') as file:
  for line in file:
    for word in line.split():
      print(word, end="\t")
file.close()
