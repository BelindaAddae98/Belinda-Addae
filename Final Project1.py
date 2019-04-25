
# coding: utf-8

# # Final 241

# ## Introduction
# 
# Reagan and Belinda hope to use this project to learn more information about jobs listed within their potential career fields as well as learn how to somehow simplify the search for themselves and others.

# Data used in this project: <a href='new.xlsx'>data</a>

# # 2.1 Common Job Titles

# In[105]:


import pandas 
df=pandas.read_excel('new.xlsx')
df[:20]


# In[88]:


import xlrd


# In[17]:


import xlrd

book=xlrd.open_workbook('new.xlsx')

sheet=book.sheet_by_name('Sheet1')
job_title_list=[]
company_name_list=[]
posted_date_list=[]
job_location_list=[]
minimal_salary_list=[]
job_duties_list=[]
required_skills_list=[]
min_years_exp_list=[]
min_education_list=[]
url_list=[]

for i in range(sheet.nrows):
    job_title,company_name,posted_date,job_location,minimal_salary,job_duties,required_skills,min_years_exp,min_education,url=sheet.row_values(i)
    if i !=0:
        
        job_title_list.append(job_title)
        company_name_list.append(company_name)
        posted_date_list.append(posted_date)
        job_location_list.append(job_location)
        minimal_salary_list.append(minimal_salary)
        job_duties_list.append(job_duties)
        required_skills_list.append(required_skills)
        min_years_exp_list.append(min_years_exp)
        min_education_list.append(min_education)
        url_list.append(url)
print(job_title_list)
print(company_name_list)
print(posted_date_list)
print(job_location_list)
print(minimal_salary_list)
print(job_duties_list)
print(required_skills_list)
print(min_years_exp_list)
print(min_education_list)
print(url_list)


# In[90]:


import xlwt
from collections import Counter
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

count_result=Counter(job_title_list)


print(count_result)


# The most common job title is "Intelligence Analyst"

# # 2.2 Which company posted the most number of jobs

# In[93]:


from collections import Counter
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

count_result=Counter(company_name_list)
print(count_result)
word_list = []
count_list = []
for word,count in count_result.most_common(20):
    word_list.append(word)
    count_list.append(count)
print(word_list)
print(count_list)


# In[94]:


plt.barh(list(count_result.keys()),list(count_result.values()))


# Each company posted the same number of jobs throughout the data

# # 2.3 How do the number of job posts vary by days?

# In[95]:


import pandas
df=pandas.read_excel("new.xlsx")
df['posted date']


# In[96]:


from collections import Counter
result1=Counter(df['posted date'])
print(result1.keys())


# In[97]:


plt.plot(result1.keys(),result1.values())
plt.show()


# There is a almost an immediate hike in february but then there is a shift between drops nad hikes between March 3, 2019 and April 4, 2019. Then an immediate stable drop afterwards. 

# # 2.4 Where are the location of the jobs?

# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[136]:


from collections import Counter

result = Counter(df['job location'])

plt.barh(list(result.keys()),list(result.values()))
plt.show()


# Although the locations vary primarily along the east coast of the United States, a majority of the job locations are located within Washington,D.C.

# # 2.5 What is the average minimum salary?

# In[19]:


import numpy as np
print('mean minimal salary is {}'.format(np.mean(minimal_salary_list)))


# The average minimal salary from the jobs within the data set is $73,647.45.

# # 2.6 What is the average minimal years of experience?

# In[108]:


print('mean minimal years is {}'.format(np.mean(min_years_exp_list)))


#  The average minimal years of experience from the jobs within the data set is 4.2 years.

# # 2.7 How are the years of experience related to the salaries?

# In[22]:


print("the cor minimum number of years and salaries is {}".format(np.corrcoef(min_years_exp_list,minimal_salary_list)[0][1]))


# In[27]:


plt.scatter(min_years_exp_list,minimal_salary_list)
plt.show()


# There seems to be a positive correlation between the years of experience and the minimal salry recieved according to the chart.

# # 2.8 What are the common job duties?

# In[112]:


for duty in df['job duties']:
    print (duty)


# In[117]:


duties =''
for duty in df['job duties']:
    duties = duty + duties
print (duties)


# In[118]:


import xlwt        

from collections import Counter        

from nltk.corpus import stopwords

stop = set(stopwords.words('english'))

  

book = xlwt.Workbook() # create a new excel file

sheet_test = book.add_sheet('word_count') # add a new sheet

i = 0

sheet_test.write(i,0,'word') # write the header of the first column

sheet_test.write(i,1,'count') # write the header of the second column

sheet_test.write(i,2,'ratio') # write the header of the third column


# In[122]:


word_list = [i for i in duties.lower().split() if i not in stop]

word_total = word_list.__len__()



count_result =  Counter(word_list)

for result in count_result.most_common(20):

    i = i+1 

    sheet_test.write(i,0,result[0])

    sheet_test.write(i,1,result[1])

    sheet_test.write(i,2,(result[1]/word_total))

    

book.save('duties.xls')# define the location of your excel file


# <img src="finalduties.png">

# The common job duties include producing repots,analyzing, an being responsible

# # 2.9

# In[124]:


skills =''
for skill in df['required skills']:
    skills = skill + skills
print (skills)


# In[127]:


import xlwt        

from collections import Counter        

from nltk.corpus import stopwords

stop = set(stopwords.words('english'))

  

book = xlwt.Workbook() # create a new excel file

sheet_test = book.add_sheet('word_count') # add a new sheet

i = 0

sheet_test.write(i,0,'word') # write the header of the first column

sheet_test.write(i,1,'count') # write the header of the second column

sheet_test.write(i,2,'ratio') # write the header of the third column


# In[128]:


word_list = [i for i in skills.lower().split() if i not in stop]

word_total = word_list.__len__()



count_result =  Counter(word_list)

for result in count_result.most_common(20):

    i = i+1 

    sheet_test.write(i,0,result[0])

    sheet_test.write(i,1,result[1])

    sheet_test.write(i,2,(result[1]/word_total))

    

book.save('skills.xls')# define the location of your excel file


# <img src="finalskills.png">

# Some common skills require being able to use tools, being able to research and have background knowledge of the job as well as inoformation.

# # Conclusion

# In conclusion, Reagan and Belinda believe this knowledge can aid future analysts to hone in their job searches and to be more effective and efficient throughout the search. This project has the ability to let an aspiring analyst know the common job titles within a search, which company seems to be hiring the most, the primary location of the jobs, the average minimal salaries and minimal years of experience,as well as common job duties nad skills required.There is hope that with the aid of this project, you too can simplfy your job searches in the future. Thank you.
