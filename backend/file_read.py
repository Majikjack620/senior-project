divider = "              |              "

with open('dependent.txt', 'r') as file:
  for line in file:
    for word in line.split():
      print(word, end=divider)

    print("\n")
file.close()
