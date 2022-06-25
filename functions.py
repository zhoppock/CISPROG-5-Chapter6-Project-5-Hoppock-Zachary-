def isSorted(l):
  if len(l) >= 0 and len(l) < 2:
      return True
  else:
    for i in range(len(l)-1):
      if l[i] > l[i+1]:
        return False
    return True

def main():
  print("Are the following lists sorted?  True or False?")

  l = []
  print("\n" + str(l) + ": ", end = "")
  print(isSorted(l))

  l = [2]
  print("\n" + str(l) + ": ", end = "")
  print(isSorted(l))

  l.append(1)
  print("\n" + str(l) + ": ", end = "")
  print(isSorted(l))
  
  l = list(range(5))
  print("\n" + str(l) + ": ", end = "")
  print(isSorted(l))

  l[4] = 2
  print("\n" + str(l) + ": ", end = "")
  print(isSorted(l))

  l.sort()
  print("\n" + str(l) + ": ", end = "")
  print(isSorted(l))