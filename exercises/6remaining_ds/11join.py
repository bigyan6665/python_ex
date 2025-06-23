string = "bigyan"
ls = ['67','34','89','55']
tup = ('67','34','89','55')
st = {'67','34','89','55'}
fst = frozenset(st)
dt = {"rol_no":23,"name":"Bigyan"}

sep = "-"
print(sep.join(string))
print(sep.join(ls))
print(sep.join(tup))
print(sep.join(st))
print(sep.join(fst))
print(sep.join(dt))