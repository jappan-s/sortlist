#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tuple1=input("Enter a list of tuples:")

List2 =[]
List3 =[]

for t in tuple1:
    List2.append(t[1],)

List2.sort()
print(List2)

for l in List2:
    for q in tuple1:
        if l == int(q[1],):
            List3.append(q)

print(List3)


# In[ ]:





# In[ ]:




