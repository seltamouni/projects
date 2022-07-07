# import string library function
import string
  
# Storing the value in variable result
result = string.ascii_letters
  


def generator (text):
    global result
    s = []
    for i in text:
        for j in range(len(result)):
            if i == result[j]:
                s.append(result[j+3])
                break
    gen = ''.join([str(elem) for elem in s])
    
    return (gen)        
                



def original (text):
    global result
    s = []
    for i in text:
        for j in range(len(result)):
            if i == result[j]:
                s.append(result[j-3])
                break
    gen = ' '.join([str(elem) for elem in s])
    
    return (gen)        
retenu = input("enter a text : ")                
r = generator(retenu)
print(f"message encoded is {r}")
print(f"the original message is {original(r)}")
