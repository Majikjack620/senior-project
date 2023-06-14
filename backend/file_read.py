with open('dependent.txt', 'r') as file:
  for line in file:
    listings = list(line.split())
    length = len(listings)
    
    for i in range(length):
      if listings[i] == 'by':
        continue
      else:
        if i == length-1 or listings[i] == "Depended":
          print(f'| {listings[i]}', end=" | \n")
        else:
          print(f'| {listings[i]}', end=" ")
