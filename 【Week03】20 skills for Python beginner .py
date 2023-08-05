#!/usr/bin/env python
# coding: utf-8

# ##### !!! please DO NOT rename this file !!!

# ### 20 skills for Python beginner (2) 12~17
# - student id:111524019
# - name：陳品蓁

# ##### 12 List

# In[2]:


# A list is a collection which is ordered and changeable. Allows duplicate members.
# lists are written with square brackets.
# You access the list items by referring to the index number

LL = [1,3,5,"7",11,13,True,False,"hello"]


# In[3]:


len(LL)


# In[4]:


# Remember that the first item has index 0
print(LL[0])
print(LL[6])
print(LL[-1])
print(LL[2:5]) # Range of Indexes


# In[6]:


print(len(LL)) #To determine how many items a list has
print("7" in LL)  # Check if item exists true or false
print(LL.index("7")) # Returns the index of the first element with the specified value


# In[25]:


# list
LL = [1,3,5,"7",11,13,True,False,"hello"]

 # to add an item
LL.append("hoho")
LL.insert(2,"D")
LL.extend("Huert")
LL.extend(["Huert","Rex","Daisy"])
print(LL)
# to edit an item in a list
LL[4]=7
print(LL)
 # remove items from a list
del LL[8]
LL.remove(13)
print(LL)


# In[18]:


# sorts the list ascending


# In[31]:


nn=[22,9,28,6,123,456,111]
nn.sort()
print(nn)
nn.sort(reverse=True)
print(nn)
nn[::-1]
print(nn)


# ##### 13 List VS String

# In[33]:


# string ==> list
S = "Python"
L = list(S)
print(S)
print(L)


# In[34]:


print(S[-2:])
print(L[-2:])
print(len(S))
print(len(L))


# In[42]:


# string ==> list ===> str.split()
# Split a string into a list where each word is a list item
S = "Life is Short We need Python"
list(S)
S.split()
S.split("o")


# In[46]:


# list　＝＞　string ==>str.join()
# takes all items in an iterable and joins them into one string.
L=S.split()
L.reverse()
L


# In[104]:


L.reverse()
' '.join(L)


# ##### 14 list in list

# In[105]:


a = [1,2,3,4,5,6,7,8,9] # 1D
B = [[1,2,3],
     [4,5,6],
     [7,8,9]]  #2D


# In[108]:


len(B)
B[2][1] #B[row][colum]


# ##### 15 tuple

# In[ ]:


# () tuple ....................... ordered and unchangeable.
# [] List is a collection which is ordered and changeable. Allows duplicate members.
# {} dict/set..................... unordered and changeable unique.


# In[109]:


### tuple
# A tuple is a collection which is ordered and unchangeable. 
# Written with round brackets裡面的值可以呼叫不能修改
t = (3,6,9)
t
t.count(3)


# In[110]:


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


# In[113]:


# print "Hi~, I am XX years old XXX"
# Basic formatting
# Method 1
age = 34
pro = "teacher"
print("hi, I am "+ str(age)+ "years old"+pro)


# In[59]:


# Simple positional formatting is probably the most common use-case. 
# Use it if the order of your arguments is not likely to change and 
# you only have very few elements you want to concatenate.
# Method 2
age = 34
pro = "teacher"
format_A = "Hi ,I am %s year old %s" # bland Q IN str 
values_B =(age , pro) #A IN tuple
format_A % values_B


# ##### 16 dictionary

# In[ ]:


# () tuple ....................... ordered and unchangeable.
# [] List is a collection which is ordered and changeable. Allows duplicate members.
# {} dict/set..................... unordered and changeable unique.


# In[ ]:


# A dictionary is a collection which is unordered, changeable and indexed. 
# dictionaries are written with curly brackets{}, and they have keys and values.


# In[82]:


# Method 1： { }
week = {"Mon":"senin" , 
        "Tue":"An-kan", 
        "Wed":"週三" }


# In[60]:


week["Mon"]


# In[84]:


# Method 2： { } creat from nothing 無中生有
W = {}
W["Mon"]="星期一" 
print(W)
type(W)
W["Tue"]="An-kan"
print(W)
W["Mon"]="SENIN" 
print(W)


# In[74]:


# keyd, values, key-value pairs(items)
print(W.keys())
print(W.values())
print(W.items())


# In[85]:


# Add
W["Thu"]="星期四"

# Edit
W["Mon"]="3"
# remove
del W["Tue"]
W


# In[86]:


# Check if Key Exists 確認

"Fir" in W


# In[88]:


# You can loop through a dictionary by using for loop
# When looping through a dictionary, the return value are the keys of the dictionary, 
# but there are methods to return the values as well.

for i in W:
    print(i,W[i])


# In[89]:


for i in W.items():
    print(i)


# In[94]:


for i in W.items():
    print(i[1],i[0])


# In[95]:


for k,v in W.items():
    print(v)


# In[96]:


for i in W.items():
    print(i)


# In[99]:


[i for i in W.items()]
dict(i for i in W.items())


# In[100]:


dict((k,v) for (k,v) in W.items() )


# In[102]:


dict((v,k) for (k,v) in W.items() ) #switch key and value


# In[103]:


dict((k,v) for (k,v) in W.items() if len(v)>3) 


# In[114]:


# diffetent data type in the dict

inv = {
    "coin":168,
    "wallet": ["ID","Credit Card"],
    "backpack":{
                "phone":1,
                "NB":1,
                "apple":3
               }
}


# In[116]:


inv["backpack"]
inv["wallet"]


# In[124]:


# revise
#add "stu ID" in awllet
inv["wallet"].append("stu id")
                     
# revise the apple from 3 > 2 
inv["backpack"]["apple"]=2
inv


# In[126]:


# clear
W.clear()
W={}
W


# In[129]:


# update() 
# updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs. 
# adds element(s) to the dictionary if the key is not in the dictionary.
# If the key is in the dictionary, it updates the key with the new value.

W1 = {'Mon': '星期一', 'Tue': '星期二', 'Wed': '星期三'}
W2 = {'Mon': '周一', 'Tue': '周二', 'Thu': '週四'}
W1.update(W2)
W1


# ##### 17 set

# In[137]:


# set {}
# A set is a collection which is unordered and unindexed. 
# sets are written with curly brackets.

set1 =  {2 , 4 , 6, 4, 6, 6, 8 ,12}
print(set1)
2 in set1


# In[138]:


# Add
set1.add(10)
print(set1)
# Remove
set1.remove(4)
print(set1)


# In[146]:


setA = {2,4,6,8,10}
setB = {1,2,3,4,5,6}

# Join Two Sets

print(setA & setB) # intersetion
print(setA | setB) # union
print(setA - setB) # difference


# In[147]:


# subset
setC = {2,4,6,8,10}
setD = {2,4,6}
print(setD <= setC) # Returns whether another set contains this set or not
print(setD.issubset(setC)) #Returns whether another set contains this set or not
print(setD.isdisjoint(setC)) #Returns whether two sets have a intersection or not


# In[151]:


#practice : try to find the common words in two poems
p1="春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。"
p2="紅豆生南國，春來發幾枝。願君多采擷，此物最相思。"
p3="。，?" 
set(p1) & set(p2)-set(p3)

