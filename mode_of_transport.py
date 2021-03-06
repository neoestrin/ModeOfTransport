# -*- coding: utf-8 -*-
"""Mode of Transport.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lghk6_T54Ql_owzspNddzvQl5mjwpcBg

# Mode of Transport

This project needs us to understand what mode of transport employees prefer to commute to their office. This can prove to be a very informative study, especially in the world of Olas and Ubers where a huge chunk of the public has switched to the cab services from personal/public transport systems. Even new services for carpooling like Quickride, Sride, etc have come up nowadays which provides even more affordable commute options for office employees.

The dataset provided to us contains the following attributes:
- **Age:** Employees current age
- **Gender:** Gender of the employees
- **Engineer:** Tells us whether the employee is an Engineer or not. 1 being yes and 0 being not an engineer
- **MBA:** Similar to the above attribute this tells us whether the employee is a Management Graduate or not
- **Work Experience:** This tells us the work experience of the concerned candidate (assuming it is in years)
- **Salary:** Salary of the Employee
- **Distance:** Distance of the Employee from his residence to office
- **License:** Whether the employee has any license to drive/ride or not
- **Transport:** Finally, which mode of transport the employee uses for his/her commute

We are required to do the following:
- Perform **Exploratory Data Analysis (EDA)** on the dataset.
- Illustrate the **Insights** based on the EDA done.
- **Multicollinearity check** and summarization of problem statement for business stakeholders.
- **Prepare data for analysis**.
- Create **multiple models** (like KNN, Naive Bayes, Logistic Regression) and explore how each model performs using appropriate model performance metrics.
- Apply both bagging and boosting modelling procedures to create 2 models and compare its accuracy with the best model of the above step. (**Actionable Insights and Recommendations**)
- **Summarize** our findings.

# Importing and Reading the Dataset
"""

import pandas as pd

data = pd.read_csv("/content/drive/My Drive/Data/Misc/Cars.csv")
data

"""After reading the data we find that it has 444 records consisting of 9 attributes.

Checking dropping null values (if any):
"""

colL = data.columns

for col in colL:
    print (col,data[col].unique())

"""Here, we can see that MBA attribute has Nan/Null values. Hence, to remove it, we first replace the null value with "-1" and then remove the value from the data frame altogether."""

data["MBA"].fillna(value = -1, inplace = True)
data["MBA"].unique()

data = data[data["MBA"]!=-1]
data

"""After treating the null values, we can now move forward to our Exploratory Data Analysis (EDA)

# Exploratory Data Analysis

Before individually analyzing each attribute, let us first see what kind of information the complete data provides us.
"""

data.describe()

"""With that out of the way, let us start with plotting graphs for these attributes and see what kind of data we are dealing with. We will be using **Plotly's** advanced graphs for doing the same.

# EDA: Univariate Analysis:
"""

import plotly.express as px

"""Let's start with the **Age**

This can be a very important parameter while classifying which employees prefer what mode of transport. For eg. employees who are elder or in their midlife would like to prefer a comfortable way to commute. They will be using more of Cars/Two Wheelers than public transport. Again with the young employees, most of them would want to own their two-wheelers and ride that to work.
"""

px.box(data, y="Age")

"""This tells us that the majority of the employees are aged between 18 to 37 years, with a few employees aged between 38 & 43. This can be also noticed in the histogram of below."""

px.histogram(data, x="Age")

"""The histogram again shows us with a proper count that majority of the employees are between 20 to 34 age group.

**Gender:**

Again Gender can also be a good parameter. While Men like to ride/drive to work, Women prefer a more comfortable commute and resort to cab/carpooling services if not for their own car.
"""

px.histogram(data, x="Gender")

"""This plot tells us that there are 316 counts of male employees in the organisation as compared to 128 female employees.

**Engineer:**

Now, this attribute, in general, will not be so effective for our model. As an engineer, doesn't have a different preference for a commute than an accountant or a manager.
"""

px.histogram(data, x="Engineer")

"""This tells us that 335 engineers are working in this company and 109 non-engineers

**MBA:**

Again, as discussed in the case above, this attribute also doesn't help us much.
"""

px.histogram(data, x="MBA")

"""Similar to the plot above this shows us that there are 331 management graduates employed as compared to 112 Non-MBA graduates

**Work Exp:**

Generally, people with more work experience get more of a workload in their senior position. They do not like to waste time while driving and like to work on the go to save time. Hence, this category must be resorting to either cab services or hiring drivers for their cars to commute to their offices.
"""

px.box(data, y="Work Exp")

"""This shows us that the majority of people working have experience ranging between 0-15 years with a few outliers ranging from 16-24 years of experience."""

px.histogram(data, x="Work Exp")

"""The same can be seen on the histogram plot above as well. It shows that the majority of people working have experienced below 15 years. More specifically around 10 years.

**Salary:**

Also, employees with higher salaries tend to buy their own vehicles. Hence, there is a higher chance that employees with higher salaries will be commuting in their own car.
"""

px.box(data, y="Salary")

"""Prima facie it looks like there a lot of outliers present in this attribute with salaries of the employees ranging from 6.5L to 23.9L, with few employees drawing a salary between 24.9L to 57L.

Let's plot the histogram of the same and check the results:
"""

px.histogram(data, x="Salary")

"""Well, the histogram also shows us a similar result. Let's take this attribute to our Bivariate Analysis and then decide what to do with it.

**Distance:**

Distance is also a very important parameter, due to which people with their residence nearby generally go for public means of transport, whereas people who live far off the location of their offices tend to use their personal transport options.
"""

px.box(data, y="Distance")

"""This shows us that employees generally are located around 3.2 km to 19.8 km from their office. With some people choosing to stay even farther ranging from 20.8 km to 23.4 km.

The same can be seen from the plot below.
"""

px.histogram(data, x="Distance")

"""**License:**

This gives a clear picture that the license holders only get to choose whether they want to come via their vehicles or public transport. But the employees who do not have their licenses altogether would be struck to the public mode of transport.
"""

px.histogram(data, x="license")

"""This plot shows us how many employees have a license with them. As it turns out the majority of the employees (around 340) have licenses and around 104 employees don't have it.

We can plot this with which mode of transport the license holders use to see some good insights.

**Transport:**

Finally our the attribute which says whether the employee takes public transport, two-wheeler or cars to their office.
"""

px.histogram(data, x="Transport")

"""This plot shows us that the majority of the people (around 300) are using Pubic Transport with around 83 of them using two-wheelers and 61 using car

# EDA: Bivariate Analysis

Coming to the Bivariate Analysis, we will analyze more than one attribute together and see what insights come up when two factors are put in with each other.

Now since we have to work around the mode of transport which the employees take to their commute, let us first see how other factors react with Transport.

**Transport vs Salary:**
"""

px.scatter(data, x = "Transport", y = "Salary")

"""As discussed above, we can see that people with more salary tend to use their vehicles (cars) to commute to the office.

**Transport vs Distance:**
"""

px.scatter(data, x="Transport", y="Distance")

"""With the above plot, we can see that the more the distance grows people tend to use their vehicles more often than using the public mode of transportation."""

px.scatter(data, x="Transport", y="Work Exp")

"""This plot seems very similar to the **Transport vs Salary** plot. It shows the same thing, people with more work experience generally do not like to waste time and like to be on the move. But again, since the plot is quite similar to the one with salary. We can also conclude that since, people with more work experience are drawing more salary from the company, they might have bought their vehicle to come to the office.

**Transport vs Gender:**
"""

px.histogram(data, x="Transport", y = "Gender", color="Gender")

"""We can see that there are a very few ladies who use their mode of transport, they either use public transport more, like cab services or come on two wheelers like scooties or with their colleagues or their husbands, who might be dropping them.

**Transport vs Age:**
"""

px.scatter(data, x="Transport", y="Age")

"""As discussed before as well, this plot shows very well that with age, people start looking for comfort. As a result they shift from public transport to their vehicles.

**Transport vs License:**

Now let's see how many people who have license, choose which mode of transport.
"""

px.histogram(data, x= "Transport", y="license", color = "license")

"""Here, we can see that out of 300 people using public transport, around 11% of the employees hold their license. Again, for people using car for their commute, around 21% employees do not hold a license (they might be hiring a driver).

As for the Two wheeler section, we found that interestingly around 72% of employees riding down to the office do not have a license.

Now, since we have done plots with transportation, let us just plot different attributes to see if we can find any interesting insights.

**Gender vs Salary:**
"""

px.scatter(data, x="Gender", y="Salary", size= "Work Exp")

"""Male counter-parts are getting more salary for the same work experience than their female counterparts.

**Gender vs Distance:**
"""

px.scatter(data, x = "Gender", y = "Distance")

"""We can see apart from one outlier, generally, female employees live closer to their workplace as compared to male employees.

# Data Preparation

Now that we are done with the data analysis, let's jump right into preparing our data for training and testing.
"""

data

"""**Outlier Treatment:**

First, we have to remove the outliers, which we have found in our Univariate Analysis. An outlier, in general, is an extreme (unusually different) data point which differs from other data points in our data. Treating this skewed data is very important especially while running a model with these kinds of points poses a risk of having a biased model.

Hence, we first remove all the outliers from each of our attributes.

Let us first start with **Age:**

From the boxplot we can see that anything above the age of 37 is an outlier, again while confirming with the histogram plot, we can say that anything above 40 years is for sure an outlier, others can still be considered normal. Thus, let's remove those two data points above the age of 40.
"""

data = data[data["Age"]<41]
data["Age"].unique()

"""Coming to our second attribute with outliers, **Work Experience:**

From the boxplot, we can see people with more than 15 years of experience are unusually high than other data points in our dataset. Coming to the Histogram, we can see that up to 24 years of work experience, there are still 2-3 or sometimes even 10 persons available in groups with more than 15 years of work experience. However, there's just one person with 24 years of experience. So let's just get rid of that single data point.
"""

data = data[data["Work Exp"]<24]
data["Work Exp"].unique()

"""Now let's take a look at the dataset which has the most dramatic boxplot in our dataset, **Salary:**

From the boxplot, we can see that any value above 23.9 Lakhs is an outlier. But let's take a look at the Histogram just be sure as well.

From the histogram plot, we can see that there are still a good amount of people in each salary groups till 46 Lakhs, above which, all the salary groups have just one or two people which we can say are extreme data points and hence, we can choose to remove them.
"""

data = data[data["Salary"]<46]
data["Salary"].unique()

"""Coming to the final attribute which has outliers **Distance:**

The boxplot shows us that employees are staying up to at max 19.8 km away from home.
And if we look at the histogram plot of the same, people are staying up to 21.9km beyond which there are only a few persons staying even further away from the office. Hence, we remove them from the equation as well.

Now, we cannot have any string variables going into our training model. The machine can understand only numbers. Hence, we import **Label Encoding** for the job.
"""

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

data["Transport"] = le.fit_transform(data["Transport"])
data

"""Alternatively, we can also encode the values manually instead of running a Label Encoder by simply using a **Lambda Function** or a loop.

Let us encode "Gender" by using the lambda function:
"""

data["Gender"] = data["Gender"].apply(lambda x: 0 if "Male" in str(x) else 1)
data

"""**EDA: Correlation Map:**"""

import plotly.figure_factory as ff
corr = data.corr()
fig = ff.create_annotated_heatmap(
    x = list(corr.columns),
    y = list(corr.index),
    z = corr.values,
    annotation_text = corr.round(2).values,
    showscale = True)

fig

"""Now, we have seen above that Engineer and MBA columns are not required for our training purpose as it doesn't affect in any way which public transport employees choose."""

data.drop(["Engineer", "MBA"], axis = 1, inplace = True)
data

"""# Training & Testing the dataset

Now that our data is prepared, Let us split our data into training and testing sets
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn import metrics
from sklearn import preprocessing

y = data["Transport"]
x = data
x.pop("Transport")

"""The problem statement which we have in our hand requires us to predict which mode of transport will be preferred by what kind of employee. Hence, our target variable is "Transport", which we save in y and we have our independent variables which we save in x.

Now, splitting our dataset into two parts. 80% of the dataset at random for Training purposes and keeping 20% of the dataset at random for Testing purposes.
"""

trainx, testx, trainy, testy = train_test_split(x, y, test_size = 0.2, stratify = y)

"""Since the problem statement is to predict which mode of transport is preferred by which kind of employee. This is a classification problem and hence, let us run some classification model for the same.

**Logistic Regression:**

Logistic Regression is another technique of machine learning which is borrowed from the field of statistics. It is used to describe data and to explain the relationship between one dependent binary variable and one or more nominal, ordinal, interval or ratio-level independent variables.
"""

logreg = LogisticRegression()
logreg.fit(trainx, trainy)

y_pred = logreg.predict(testx)
score = logreg.score(testx, testy)
print(score)

cm = metrics.confusion_matrix(testy, y_pred)
print(cm)

"""Hence, for the logistic regression model, we get, 86.04% accuracy.

Also if we interpret the confusion matrix that is printed, we get:

Total number of all correct predictions: (7+7+60) = 74
Total number of the dataset: (7+1+6) + (0+7+2) + (3+0+60) = 86

Total Accuracy = 74/86 = 0.860465

**K Nearest Neighbour:**

Coming to the next model we do here is K Nearest Neighbour. It is one of the most basic yet essential classification algorithms from the supervised learning domain of machine learning and finds intense application in pattern recognition, data mining and intrusion detection.
"""

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 7, metric= "euclidean")
knn.fit(trainx, trainy)

y_pred = knn.predict(testx)
score = knn.score(testx, testy)
print(score)

cm = metrics.confusion_matrix(testy, y_pred)
print(cm)

"""Hence, for the KNN model, we get, 81.39% accuracy.

Also if we interpret the confusion matrix that is printed, we get:

Total number of all correct predictions: (5+8+57) = 70
Total number of the dataset: (5+0+9) + (0+8+1) + (5+1+57) = 86

Total Accuracy = 70/86 = 0.8139534

**Naive Bayes:**

Coming to our 3rd model, Naive bayes is a collection of algorithms based on Bayes Theorem. But the family of algorithms where all of them share a common "naive" assumption that every pair of features being classified is independent of each other.
"""

from sklearn.naive_bayes import MultinomialNB

nb = MultinomialNB()
nb.fit(trainx, trainy)

y_pred = nb.predict(testx)
score = nb.score(testx, testy)
print(score)

cm = metrics.confusion_matrix(testy, y_pred)
print(cm)

"""Hence, for the Naive Bayes model, we get, 84.88% accuracy.

Also if we interpret the confusion matrix that is printed, we get:

Total number of all correct predictions: (6+8+59) = 73
Total number of the dataset: (6+0+8) + (0+8+1) + (3+1+59) = 86

Total Accuracy = 73/86 = 0.8488

# Ensemble Techniques

Now that our problem statement also wants us to try Bagging and Boosting techniques. Let us add two more models.

**Random Forest (Bagging):**

This is a kind of ensemble model (uses multiple learning algorithms to obtain better predictive performance) which consists of a large number of decision trees that spits out a class prediction. The class with the most votes becomes our model's prediction.
"""

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 1000, random_state = 42)
rf.fit(trainx, trainy)

y_pred = rf.predict(testx)
score = rf.score(testx, testy)
print(score)

cm = metrics.confusion_matrix(testy, y_pred)
print(cm)

"""Hence, for the Random Forest model, we get, 87.20% accuracy, which is much better than the models before.

Also if we interpret the confusion matrix that is printed, we get:

Total number of all correct predictions: (9+8+58) = 75 Total number of the dataset: (9+0+5) + (0+8+1) + (4+1+58) = 86

Total Accuracy = 75/86 = 0.87209

**eXtreme Gradient Boost - XG Boost (Boosting):**

XG Boost, as the name suggests is another kind of decision tree-based ensemble model, based on its predecessor gradient boosting algorithm. In prediction problems involving unstructured data (images, text, etc.) artificial neural networks tend to outperform all other algorithms or frameworks. However, when it comes to small-medium structures/tabular data, decision tree-based algorithms are considered best-in-class right now.
"""

from xgboost import XGBClassifier

xg = XGBClassifier()
xg.fit(trainx, trainy)

y_pred = xg.predict(testx)
score = xg.score(testx, testy)
print(score)

cm = metrics.confusion_matrix(testy, y_pred)
print(cm)

"""Hence, for the XG Boost model, we again get, 87.20% accuracy, which is similar to the Random Forest Model.

Also if we interpret the confusion matrix that is printed, we get:

Total number of all correct predictions: (9+8+58) = 75 Total number of the dataset: (9+0+5) + (0+8+1) + (4+1+58) = 86

Total Accuracy = 75/86 = 0.87209

# Conclusion:

To conclude we can say since we have a very small dataset with us. It is best to run an Ensemble model like **Random Forest or XG Boost**, which gave us good accuracy.

Again, we think if we did remove all the outliers from our dataset according to the boxplot the accuracy could've been even better. But considering that our dataset is too small and our histogram plot showed a good number of count under the group, hence, we chose to remove the outliers on need basis.

For now, we think these models are the best anyone can find on this dataset.
"""