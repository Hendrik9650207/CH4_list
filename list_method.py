'''
index()
append()
insert()
remove()
sort() #不可對有字串跟數字格式的list做排序

'''


spam = ['a', 'b', 'c', 'd', 'e']
spam.append('f')
print(spam)


spam.insert(0, '0')
print(spam)


for i in spam:
    print(i, '\n')


spam.remove('0')
print(spam)


del spam[5]
print(spam)


spam.sort(reverse=True)
print(spam)

spam.sort()
print(spam)


spam.reverse()
print(spam)


name = 'Hendrik'
print(name[3])

# 字串可用list來取用
print(name[-2])


name1 = 'Geralt of Rivia'
newname1 = name1[0:7] + 'aa' + name1[9:14]

print(newname1)
