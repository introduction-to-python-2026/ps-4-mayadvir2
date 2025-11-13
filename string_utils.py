def split_before_each_uppercases(formula):
  lst = []
  i=0
  while i < len(formula):
    str = formula[i]
    i+=1
    while i < len(formula) and not formula[i].isupper():
      str += formula[i]
      i+=1
    lst.append(str)
  return lst

def split_at_first_digit(formula):
  string = ""
  num = 1
  index = 0
  for i in range(len(formula)):
    if not formula[i].isdigit():
        string += formula[i]
        index += 1
    else:
        break
  if index < len(formula):
      num = int(formula[index:])
  return (string , num)

