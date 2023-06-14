wordList = []

with open('dependent.txt', 'r') as file:
  for line in file:
    for word in line.split():
      if word == 'by':
        continue
      else:
        wordList.append(word)
file.close()

for i in range(len(wordList)):
  if i % 5 == 0:
    print(f'\n{wordList[i]}', end='\t\t\t\t')
  else:
    print(f'{wordList[i]}', end='\t\t\t\t')
