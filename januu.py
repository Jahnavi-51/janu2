'''import requests
res = requests.get("https://reqres.in/api/users/2")
print(res)
print(res.content)
print(res.status_code)
import requests
d ={
    "name": "morpheus",
    "job": "zion resident"
}
a = requests.post(url="https://reqres.in/api/users", data = d)
print(a.status_code)
print(a.content)'''
import requests

a = requests.get("https://reqres.in/api/users?page=2")
print(a.status_code)
print(a.content)

b = requests.get("https://reqres.in/api/users/2")
print(b.status_code)
print(b.content)

c = requests.get("https://reqres.in/api/users/23")
print(c.status_code)
print(c.content)

d = requests.get("https://reqres.in/api/unknown")
print(d.status_code)
print(d.content)

e = requests.get("https://reqres.in/api/unknown/2")
print(e.status_code)
print(e.content)

f = requests.get("https://reqres.in/api/unknown/23")
print(f.status_code)
print(f.content)

g = requests.post("https://reqres.in/api/users?page=2")
print(g.status_code)
print(g.content)

ha = {
    "name": "morpheus",
    "job": "zion resident"
}
h = requests.put(url="https://reqres.in/api/users/2",data=ha)
print(h.status_code)
print(h.content)

ia ={
    "name": "morpheus",
    "job": "zion resident"
}
i = requests.patch(url="https://reqres.in/api/users/2",data=ia)
print(i.status_code)
print(i.content)

j = requests.delete("https://reqres.in/api/users/2")
print(j.status_code)
print(j.content)

