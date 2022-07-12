#!/usr/bin/env python
# coding: utf-8

# In[10]:


def locate_card(cards, query):
    pass


# In[11]:


cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3


# In[12]:


result = locate_card(cards, query)
print(result)


# In[13]:


result == output


# In[14]:


test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}


# In[15]:


locate_card(**test['input']) == test['output']


# In[16]:


tests = []


# In[17]:


# query occurs in the middle
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})


# In[18]:


# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})


# In[19]:


# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})


# In[20]:


# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})


# In[21]:


# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})


# In[22]:


# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})


# In[23]:


# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})


# In[24]:


# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


# In[25]:


tests


# In[26]:


def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0
    
    # Set up a loop for repetition
    while True:
        
        # Check if element at the current position matche the query
        if cards[position] == query:
            
            # Answer found! Return and exit..
            return position
        
        # Increment the position
        position += 1
        
        # Check if we have reached the end of the array
        if position == len(cards):
            
            # Number not found, return -1
            return -1


# In[27]:


test


# In[28]:


result = locate_card(test['input']['cards'], test['input']['query'])
result


# In[29]:


result == output


# In[30]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[31]:


from jovian.pythondsa import evaluate_test_case


# In[32]:


evaluate_test_case(locate_card, test)


# In[33]:


from jovian.pythondsa import evaluate_test_cases


# In[34]:


evaluate_test_cases(locate_card, tests)


# In[35]:


def locate_card(cards, query):
    position = 0
    
    print('cards:', cards)
    print('query:', query)
    
    while True:
        print('position:', position)
        
        if cards[position] == query:
            return position
        
        position += 1
        if position == len(cards):
            return -1


# In[36]:


cards6 = tests[6]['input']['cards']
query6 = tests[6]['input']['query']

locate_card(cards6, query6)


# In[37]:


def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


# In[38]:


tests[6]


# In[39]:


locate_card(cards6, query6)


# In[40]:


evaluate_test_cases(locate_card, tests)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




