#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[71]:


text_file=open('gSpeech.txt', 'rb')


# In[72]:


all_text=text_file.read()


# In[73]:


all_text=all_text.lower()
all_str=str(all_text)


# In[74]:


sentence_count=all_str.count('.')+all_str.count('!')+all_str.count('?')
sentence_count


# In[75]:


all_str=all_str.replace('\\xa1\\xaa','').replace('\\r\\n\\r\\n','').replace('\\r\\n','')
all_str=all_str.replace('.','').replace('?','').replace('!','').replace(',','').replace(';','').replace("b'",'').replace("'",'')




# In[ ]:





# In[ ]:





# In[78]:


w_list=all_str.split()


# In[80]:


word_count=len(w_list)
word_count


# In[86]:


char_count=len(all_str)-all_str.count(' ')
char_count


# In[141]:


w_dict={}
w_greater5_dict={}
longest_word_list=[]
longest_word=''
for item in w_list:
    if len(item)>len(longest_word):
        longest_word=item
        longest_word_list=[]
        longest_word_list.append(item)
    elif len(item)==len(longest_word):
        longest_word_list.append(item)
        
    if w_dict.get(item)==None:
        w_dict[item]=1
    else:
        w_dict[item]=w_dict.get(item)+1
    
    if len(item)>5:
        if w_greater5_dict.get(item)==None:
            w_greater5_dict[item]=1
        else:
            w_greater5_dict[item]=w_greater5_dict.get(item)+1
        


# In[117]:


unique_word_count=len(w_dict.keys())
unique_word_percent=str(float(len(w_dict.keys())/word_count)*100)[:6]+'%'

unique_word_percent
unique_word_count


# In[143]:


longest_word_list


# In[108]:





# In[137]:


alpha_list=[]

for item in w_dict.keys():
    alpha_list.append(item)


# In[138]:


alpha_file = 'alpha.txt'
alpha_txt = open(alpha_file,'w')
while len(alpha_list)>0:
    temp_w=min(alpha_list)
    temp_w_count=w_dict.get(temp_w)
    if temp_w_count>1:
        print(temp_w+': '+str(temp_w_count)+" times ",file=alpha_txt)
    else:
        print(temp_w+': '+str(temp_w_count)+" time ",file=alpha_txt)
    alpha_list.remove(temp_w)


alpha_txt.close()

print("finished")


# In[ ]:





# In[181]:





# In[190]:


w_greater5_dict.keys()


# In[191]:


greater5_key=[]
greater5_value=[]
for item in w_greater5_dict.keys():
    greater5_key.append(item)
    greater5_value.append(w_greater5_dict.get(item))


# In[192]:


top10_list=[]

while len(top10_list)<10:
    temp_index=greater5_value.index(max(greater5_value))
    top10_list.append(greater5_key[temp_index])
    print (greater5_key[temp_index]+': '+str(max(greater5_value))+' times')
    greater5_value=greater5_value[:temp_index]+greater5_value[temp_index+1:]
    greater5_key=greater5_key[:temp_index]+greater5_key[temp_index+1:]


# In[ ]:





# In[ ]:





# In[ ]:





# In[172]:





# In[ ]:





# In[ ]:




