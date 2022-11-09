import ast
def TreeConstructor(stra):

  strt = [ast.literal_eval(i) for i in stra]

  c = 0
  c_list = [i[0] for i in strt]
  p_list = [i[1] for i in strt]

  for i in strt:
    if c_list.count(i[0]) > 2:
      return False

    if p_list.count(i[1]) > 2:
      return False
      
  return True

# keep this function call here 
print(TreeConstructor(input()))