
# coding: utf-8

# In[42]:

#scrap data from websites


# In[43]:

import requests
from bs4 import BeautifulSoup


# In[135]:

r=requests.get('http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
c=r.content
c


# In[136]:

soup=BeautifulSoup(c,'html.parser')
print(soup.prettify())


# In[145]:

all=soup.find_all('div',{'class':'propertyRow'})


# In[146]:

type(all)


# In[147]:

len(all)


# In[148]:

all[0]


# In[62]:

all[0].find_all('h4',{'class':'propPrice'})


# In[64]:

all[0].find('h4',{'class':'propPrice'}).text


# In[65]:

type(all[0].find('h4',{'class':'propPrice'}).text)


# In[66]:

all[0].find('h4',{'class':'propPrice'}).text.replace('\n','')


# In[67]:

all[0].find('h4',{'class':'propPrice'}).text.replace('\n','').replace(' ','')


# In[73]:

all


# In[149]:

for item in all:
    print(item.find('h4',{'class':'propPrice'}).text.replace('\n','').replace(' ',''))
    print(item.find_all('span',{'class','propAddressCollapse'})[0].text)
    print(item.find_all('span',{'class','propAddressCollapse'})[1].text)
    try:
        print(item.find('span',{'class','infoBed'}).text)
    except:
        pass
    print(' ')


# In[101]:

for item in all:
    print(item.find('h4',{'class':'propPrice'}).text.replace('\n','').replace(' ',''))
    print(item.find_all('span',{'class','propAddressCollapse'})[0].text)
    print(item.find_all('span',{'class','propAddressCollapse'})[1].text)
    
    try:
        print(item.find('span',{'class','infoBed'}).find('b').text)
    except:
        print(None)
    
    try:
        print(item.find('span',{'class','infoSqFt'}).find('b').text)
    except:
        print(None)
    try:
        print(item.find('span',{'class','infoValueFullBath'}).find('b').text)
    except:
        print(None)
    
    try:
        print(item.find('span',{'class','infoValueHalfBath'}).find('b').text)
    except:
        print(None)
        
    for column_group in item.find_all('div',{'class':'columnGroup'}):
        #print(column_group)
        for feature_group,feature_name in zip(column_group.find_all('span',{'class':'featureGroup'}),column_group.find_all('span',{'class':'featureName'})):
            #print(feature_group.text, feature_name.text)
            if 'Lot Size' in feature_group.text:
                print(feature_name.text)
    print(' ')


# In[111]:

l=[]
for item in all:
    d={}
    d['Address']=item.find_all('span',{'class','propAddressCollapse'})[0].text
    d['Locality']=item.find_all('span',{'class','propAddressCollapse'})[1].text
    d['Price']=item.find('h4',{'class','propPrice'}).text.replace('\n','').replace(' ','')
    try:
        d['Beds']=item.find('span',{'class','infoBed'}).find('b').text
    except:
        d['Beds']=None
    
    try:
        d['Area']=item.find('span',{'class','infoSqFt'}).find('b').text
    except:
        d['Area']=None
    try:
        d['Full Baths']=item.find('span',{'class','infoValueFullBath'}).find('b').text
    except:
        d['Full Baths']=None
    
    try:
        d['Half Baths']=item.find('span',{'class','infoValueHalfBath'}).find('b').text
    except:
        d['Half Baths']=None
        
    for column_group in item.find_all('div',{'class','columnGroup'}):
        #print(column_group)
        for feature_group,feature_name in zip(column_group.find_all('span',{'class':'featureGroup'}),column_group.find_all('span',{'class':'featureName'})):
            #print(feature_group.text, feature_name.text)
            if 'Lot Size' in feature_group.text:
                d['Lot Size']=feature_name.text
    l.append(d)


# In[112]:

l


# In[113]:

len(l)


# In[115]:

import pandas
df=pandas.DataFrame(l)


# In[116]:

df


# In[118]:

df.to_csv('Output.csv')


# In[122]:

pwd()


# In[152]:

base_url='http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='
for page in range(0,30,10):
    print (base_url+str(page)+'.html')


# In[153]:

base_url='http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='
for page in range(0,30,10):
    print (base_url+str(page)+'.html')
    r=requests.get(base_url+str(page)+'.html')
    c=r.content
    soup=BeautifulSoup(c,'html.parser')
    print(soup.prettify())


# In[156]:

base_url='http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='
for page in range(0,30,10):
    print (base_url+str(page)+'.html')
    r=requests.get(base_url+str(page)+'.html')
    c=r.content
    soup=BeautifulSoup(c,'html.parser')
    all=soup.find_all('div',{'class':'propertyRow'})


# In[161]:

l=[]
base_url='http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='
for page in range(0,30,10):
    print (base_url+str(page)+'.html')
    r=requests.get(base_url+str(page)+'.html')
    c=r.content
    soup=BeautifulSoup(c,'html.parser')
    all=soup.find_all('div',{'class':'propertyRow'})
    for item in all:
        d={}
        d['Address']=item.find_all('span',{'class','propAddressCollapse'})[0].text
        try:
            d['Locality']=item.find_all('span',{'class','propAddressCollapse'})[1].text
        except:
            d['Locality']=None
        d['Price']=item.find('h4',{'class','propPrice'}).text.replace('\n','').replace(' ','')
        try:
            d['Beds']=item.find('span',{'class','infoBed'}).find('b').text
        except:
            d['Beds']=None

        try:
            d['Area']=item.find('span',{'class','infoSqFt'}).find('b').text
        except:
            d['Area']=None
        try:
            d['Full Baths']=item.find('span',{'class','infoValueFullBath'}).find('b').text
        except:
            d['Full Baths']=None

        try:
            d['Half Baths']=item.find('span',{'class','infoValueHalfBath'}).find('b').text
        except:
            d['Half Baths']=None

        for column_group in item.find_all('div',{'class','columnGroup'}):
            #print(column_group)
            for feature_group,feature_name in zip(column_group.find_all('span',{'class':'featureGroup'}),column_group.find_all('span',{'class':'featureName'})):
                #print(feature_group.text, feature_name.text)
                if 'Lot Size' in feature_group.text:
                    d['Lot Size']=feature_name.text
        l.append(d)


# In[162]:

import pandas
df=pandas.DataFrame(l)


# In[163]:

df


# In[169]:

r=requests.get('http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
c=r.content
soup=BeautifulSoup(c,'html.parser')
all=soup.find_all('div',{'class':'propertyRow'})
all[0].find('h4',{'class':'propPrice'}).text.replace('\n','').replace(' ','')
page_nr=soup.find_all('a',{'class':'Page'})[-1].text
print(page_nr)
print(type(page_nr))


# In[170]:

l=[]
base_url='http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='
for page in range(0, int(page_nr)*10,10):
    print (base_url+str(page)+'.html')
    r=requests.get(base_url+str(page)+'.html')
    c=r.content
    soup=BeautifulSoup(c,'html.parser')
    all=soup.find_all('div',{'class':'propertyRow'})
    for item in all:
        d={}
        d['Address']=item.find_all('span',{'class','propAddressCollapse'})[0].text
        try:
            d['Locality']=item.find_all('span',{'class','propAddressCollapse'})[1].text
        except:
            d['Locality']=None
        d['Price']=item.find('h4',{'class','propPrice'}).text.replace('\n','').replace(' ','')
        try:
            d['Beds']=item.find('span',{'class','infoBed'}).find('b').text
        except:
            d['Beds']=None

        try:
            d['Area']=item.find('span',{'class','infoSqFt'}).find('b').text
        except:
            d['Area']=None
        try:
            d['Full Baths']=item.find('span',{'class','infoValueFullBath'}).find('b').text
        except:
            d['Full Baths']=None

        try:
            d['Half Baths']=item.find('span',{'class','infoValueHalfBath'}).find('b').text
        except:
            d['Half Baths']=None

        for column_group in item.find_all('div',{'class','columnGroup'}):
            #print(column_group)
            for feature_group,feature_name in zip(column_group.find_all('span',{'class':'featureGroup'}),column_group.find_all('span',{'class':'featureName'})):
                #print(feature_group.text, feature_name.text)
                if 'Lot Size' in feature_group.text:
                    d['Lot Size']=feature_name.text
        l.append(d)


# In[171]:

df=pandas.DataFrame(l)


# In[172]:

df


# In[173]:

df.to_csv('Output.csv')


# In[ ]:



