'''#list and its default functions

lst=[30,1175,65.97,[2,3,4],11.007,548892,476]
lst.append("aplle")
print(lst)
lst.pop(2)
print(lst)

print(lst.index(1175))
lst.extend([67,99.7,3.8])
print(lst)
lst.remove(11.007)
print(lst)
lst.insert(3,33779)
print(lst)

#tuple and its default functions

tup=("real",34.9,55,12345,7890,55,65)
print(tup.count(55))
print(tup.index(12345))

#sets and its default functions

st={66,547,90,214,78.8,59.3,4.123,64}
st1={5,975,33,214,59.3,200,6002}
print(st|st1)
print(st&st1)
print(st-st1)
st.add(7.341)
print(st)
print(st1.issubset(st))


#string and its default functins

st=input('enter your string:')
pre=input('enter the string you want to change:')
rep=input('enter replace string:')
new=st.replace(pre,rep)
print('new string:',new)

st1=input('enter your string:')
print('length of the string is:',len(st1))'''

#dictionaries and its functions

dit={'name':'xyz','age':45,'address':'abcd'}
print(dit)

print(dit.get('name'))
print(dit.keys())
print(dit.values())
print(dit.items())
dit.update(occupation='XYZ')
print(dit)
