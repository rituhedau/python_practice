d = {"simple_key" : "Hello"}
print(d['simple_key'])

e = {'k1':{'k2':'hello'}}
print(e['k1']['k2'])

f = {'k1':[{'nest_key':['this is deep',['hello']]}]}
h = (f['k1'])
print(h[0])



g = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}