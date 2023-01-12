from collections import deque

def encode(strs):
    res = ''
    for i in strs:
        res =  res + str(len(i)) + '*' + i
    return res

def decode(str):
    stack = deque(str[0])
    res = []
    while stack:
        length = int(stack.pop()) + 2
        slice = str[2:length]
        res.append(slice)
        str = str[length: len(str)]
        if str: stack.append(str[0])
    print(res)
    return res

if __name__ == '__main__':
    r = encode(["li*nt", "*", "code","love","you"])
    print(r)
    d = decode('5*li*nt1**4*code4*love3*you')

    
   
