print(type("hello"))
print("\n Happy Day \t Good moring")  #\t for new tap

print("hey hellow"[8])

name = "andrei neagoie"
print(name[5])
print(name[:])
print(name[5:])
print(name[-1])
print(name[ : :1])
print(name[ : : -1])

#Basic fucntion 

print(len('muthudeiva'))

word = 'I am alone'
print(word.strip())
cler = word.strip('e')
print(cler)

# word split and mini max word 
word_split = 'life is good b happyondfi'.split()
print(word_split)
min_word = word_split[0]
max_word = word_split[0]

for w in word_split:
    # print(w)
    if len(w) < len(min_word):
        min_word = w
    elif len(w) > len(max_word):
        max_word = w 
print(min_word)
print(max_word)

word_replce = 'Help me '.replace('Help' , 'you', )
print(word_replce)  

new_word = "i am hAppy with my JOp"
print(new_word.startswith('i'))
print(new_word.endswith("me"))
print(new_word.lower())
print(new_word.index("O"))
print(new_word.capitalize())
print(new_word.find('c'))
print(new_word.count('y'))

# String Fromating 

name1 = 'Muthu'
name2 = 'priya'

print(f'Hello there {name1} and {name2}')
print('Happy to see you {} and {}'.format(name1,name2))
print('Hello there %s and %s' %(name2,name1))


#Palindrome check 

wo = 'madam'
p = bool(wo.find(wo[::-1]) +1)
print(p)


print(bool(True))

print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))
