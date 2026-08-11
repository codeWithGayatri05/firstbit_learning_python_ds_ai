var=10
print(type(var))
var=3.14
print(type(var))
var=10+5j
print(type(var))
var='firstbit solutions'
print(type(var))
var="firstbit's solution"
print(type(var))
var=""""firstbit solution's"""
print(type(var))
var='(''firstbit"s "solution"'''
print(type(var))
####3.sequential
#1.list
var=[10,20,30,40]
print(type(var))
#2.tuple
var=(10,20,30,40)
print(type(var))
#3.range
var= range(1, 11)
print(type(var))
###4.set type
#1.set
var={10,20,30}
print(type(var))
#2.frozenset
var=frozenset({10,20,30})
print(type(var))
#3.mapping 
#1.dict
var={'id':101,'name':'xyz'}
print(type(var))
###6.others
#1.boolean
var=True
print(type(var))

