import re
def QuestionsMarks(strp):

  def an_int(s):
    try:
      s = int(s)
      return s
    except:
      return False
      
  h_map = [ an_int(i) for i in strp ]
  for i,_ in enumerate(h_map):

    if _:
      for j in range(i+1, len(h_map)):
        if h_map[j] and _ + h_map[j] == 10:
            _strp =  strp[i+1:j]
            # rgx = re.compile('(\?)')
            if re.search(r'([\?])', _strp):
              if len(re.findall(r'(\?)', _strp)) == 3 :
                return True
        else:
          pass
  return False
    