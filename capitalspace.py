# sample = input('Enter your sentence: ')

def put_space(s:str)->str:
    s = s.replace(' ','')
    index = 0
    for char in s :
        if char.isupper():
            s = s[:index] + ' ' + s[index:]
            index +=1
        index +=1
    return s[1:]

print(put_space('  This IsThe TTest'))
    