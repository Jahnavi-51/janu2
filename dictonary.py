d = {'vamsi': 'wastefellow', 'likki': 'good girl', 'Nandu': 'intelligent', 'jagru': 'innocent'}
print(d)
d1 = d.copy()
print("copy :", d1)
d2 = d.items()
print(d2)
print(d.values())
print(d.keys())
new = {'gayi':'stupid'}
d.update(new)
print(d)
d.update([('vamsi', 'pichi'), ('likki', 'bad girl')])
print(d)
print(d.popitem())
print()
d.setdefault("jahnavi", "bejawada")

