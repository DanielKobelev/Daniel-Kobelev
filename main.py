import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


# -- -- -- -- --    Input 1 data prints -- -- -- -- --


data_df1 = pd.read_csv('DB/input1_df.csv', encoding='latin1')
print("\033[1mThis is our Raw Data:\033[0m\n")
print(data_df1.info())
print("\n\033[1mThis is a Sum of our null values:\033[0m\n\n", data_df1.isnull().sum())
print("\n\033[1mThis are Our First 5 rows :\033[0m\n\n", data_df1.head(5))
print("\n\033[1mThis are Our Last 5 rows :\033[0m\n\n", data_df1.tail(5))
middle1 = data_df1.iloc[500:505]
print("\n\033[1mThis are Our Middle rows :\033[0m\n\n", middle1)
print("\n\033[1mThis is the describe function on our data set :\033[0m\n\n", data_df1.describe(include='all'))


# -- -- -- -- --    Input 2 data prints -- -- -- -- --


print("\n -- -- -- -- --  -- -- -- -- --   -- -- -- -- --   -- -- -- -- --     Input data 2  prints   -- -- -- -- --   -- -- -- -- --   -- -- -- -- --   -- -- -- -- --\n")

data_df2 = pd.read_csv('DB/input2_df.csv', encoding='latin1')
print("\033[1mThis is our Raw Data:\033[0m\n")
print(data_df2.info())
print("\n\033[1mThis is a Sum of our null values:\033[0m\n\n", data_df2.isnull().sum())
print("\n\033[1mThis are Our First 5 rows :\033[0m\n\n", data_df2.head(5))
print("\n\033[1mThis are Our Last 5 rows :\033[0m\n\n", data_df2.tail(5))
middle2 = data_df2.iloc[500:505]
print("\n\033[1mThis are Our Middle rows :\033[0m\n\n", middle2)
print("\n\033[1mThis is the describe function on our data set :\033[0m\n\n", data_df2.describe(include='all'))



# -- -- -- -- --    Merged prints -- -- -- -- --


print("\n -- -- -- -- --  -- -- -- -- --   -- -- -- -- --   -- -- -- -- --     Merged prints   -- -- -- -- --   -- -- -- -- --   -- -- -- -- --   -- -- -- -- --\n")

df_join_outer = data_df1.merge(data_df2, on='id', how='outer')
print("\n\033[1mThis is a Sum of our null values in the new Merged data:\033[0m\n\n", df_join_outer.isnull().sum())
df1= df_join_outer.loc[:, ['id','ParentEduc', 'LunchType', 'TestPrep', 'MathScore', 'ReadingScore', 'WritingScore']]
df2= df_join_outer.loc[:, ['id','age', 'gender', 'year_in_school', 'major', 'monthly_income', 'financial_aid', 'tuition', 'housing', 'food','books_supplies','technology','health_wellness','preferred_payment_method']]



# -- -- -- -- --    Cleaning and organizing -- -- -- -- --


print("\n -- -- -- -- --  -- -- -- -- --   -- -- -- -- --   -- -- -- -- --     Cleaning and organizing   -- -- -- -- --   -- -- -- -- --   -- -- -- -- --   -- -- -- -- --\n")

def char_fixer(data_frame, series_name):
    cnt = 0
    for row in data_frame[series_name]:
        try:
            float(row)
        except ValueError:

            data_frame.drop([cnt], inplace=True)
        cnt += 1
    data_frame[series_name] = data_frame[series_name].astype('float64', errors='raise')
    data_frame.reset_index(drop=True, inplace=True)

def num_fixer(data_frame, series_name):
    cnt = 0
    for row in data_frame[series_name]:
        try:
            int(float(row))  # if no error, drop it in
        except ValueError:
            # drop if would-be boolean
            if row == 'True' or row == 'False':
                data_frame.drop([cnt], inplace=True)
            elif row == 'nan':
                # turn the string 'nan' into NaN
                data_frame.loc[cnt, series_name] = np.nan
            else:  # Chars or NaNs
                pass
        else:
            data_frame.drop([cnt], inplace=True)
        cnt += 1
    data_frame[series_name] = data_frame[series_name].astype('object', errors='raise')
    data_frame.reset_index(drop=True, inplace=True)

num_fixer(df1, 'ParentEduc')
num_fixer(df1,'LunchType')
num_fixer(df1,'TestPrep')
char_fixer(df1,'MathScore')
char_fixer(df1,'ReadingScore')
char_fixer(df1,'WritingScore')
char_fixer(df2,'age')
char_fixer(df2,'monthly_income')
char_fixer(df2,'financial_aid')
char_fixer(df2,'tuition')
char_fixer(df2,'housing')
char_fixer(df2,'food')
char_fixer(df2,'books_supplies')
char_fixer(df2,'technology')
char_fixer(df2,'health_wellness')
num_fixer(df2,'preferred_payment_method')
num_fixer(df2,'gender')
num_fixer(df2,'year_in_school')
num_fixer(df2,'major')

print("\n\033[1mChecking the Data types in the first Data frame :\033[0m\n\n", df1.dtypes)
print("\n\033[1mChecking the Data types in the second data frame :\033[0m\n\n", df2.dtypes)

df1['MathScore'] = df1['MathScore'].interpolate().bfill().ffill()
df1['ReadingScore'] = df1['ReadingScore'].interpolate().bfill().ffill()
df1['WritingScore'] = df1['WritingScore'].interpolate().bfill().ffill()
df1['ParentEduc'] = df1['ParentEduc'].interpolate().bfill().ffill()
df1['LunchType'] = df1['LunchType'].interpolate().bfill().ffill()
df1['TestPrep'] = df1['TestPrep'].interpolate().bfill().ffill()
df2['tuition'] = df2['tuition'].interpolate().bfill().ffill()
df2['monthly_income'] = df2['monthly_income'].interpolate().bfill().ffill()
df2['financial_aid'] = df2['financial_aid'].interpolate().bfill().ffill()
df2['housing'] = df2['housing'].interpolate().bfill().ffill()
df2['food'] = df2['food'].interpolate().bfill().ffill()
df2['age'] = df2['age'].interpolate().bfill().ffill()
df2['gender'] = df2['gender'].interpolate().bfill().ffill()
df2['books_supplies'] = df2['books_supplies'].interpolate().bfill().ffill()
df2['technology'] = df2['technology'].interpolate().bfill().ffill()
df2['health_wellness'] = df2['health_wellness'].interpolate().bfill().ffill()
df2['preferred_payment_method'] = df2['preferred_payment_method'].interpolate().bfill().ffill()
df2['year_in_school'] = df2['year_in_school'].interpolate().bfill().ffill()
df2['major'] = df2['major'].interpolate().bfill().ffill()



# -- -- -- -- --    normalizing data set -- -- -- -- --


for index, row in df1.iterrows():
    df1.at[index, 'WritingScore_norm'] = row['WritingScore'] / df1['WritingScore'].max()

sorted_duplicates = df1[df1.duplicated('WritingScore_norm')].sort_values('WritingScore_norm')
print("\n\033[1mDuplicate float values :\033[0m\n\n", sorted_duplicates)
df1.drop_duplicates(subset=['WritingScore_norm'] ,inplace = True)
df1.reset_index(drop=True, inplace=True)

#df1.to_csv("Test1.csv",index= False)
#df2.to_csv("Test2.csv",index= False)


# -- -- -- -- --    Data Visualization -- -- -- -- --


df1.plot.scatter(x='ReadingScore', y='WritingScore')
plt.title(' Correlation between ReadingScore and WritingScore')
plt.show()

income_by_gender = df2.groupby('gender')['monthly_income'].mean()
income_by_gender.plot(kind='bar', color=['pink', 'blue','grey'])
plt.title('Average Monthly Income by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Monthly Income($)')
plt.xticks(rotation=0)
plt.show()

avg_scores_lunch = df1.groupby('LunchType')[['MathScore', 'ReadingScore', 'WritingScore']].mean()
avg_scores_lunch.plot(kind='bar', ax=plt.gca())
plt.title('Average Scores by Lunch Type')
plt.xlabel('Lunch Type')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.show()

df2['preferred_payment_method'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Preferred Payment Method')
plt.show()

corr = df2[['monthly_income', 'food', 'housing',"health_wellness"]].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()

sns.countplot(y='major', data=df2)
plt.title('Major Distribution')
plt.show()

plt.figure(figsize=(16, 6))
sns.boxplot(x='major', y='monthly_income', data=df2)
plt.title('Monthly Income($) by major')
plt.show()


df_long = pd.melt(df1, id_vars=['TestPrep'], value_vars=['MathScore', 'ReadingScore', 'WritingScore'],
                  var_name='ScoreType', value_name='Score')
plt.figure(figsize=(12, 6))
sns.stripplot(x='TestPrep', y='Score', data=df_long, jitter=True, hue='ScoreType', dodge=True)
plt.title('Scores by Test Preparation Course')
plt.legend(title='Score Type')
plt.show()

plt.figure(figsize=(10, 6))
avg_scores_by_education = df1.groupby('ParentEduc')[['MathScore', 'ReadingScore', 'WritingScore']].mean().reset_index()
avg_scores_by_education_melted = avg_scores_by_education.melt(id_vars='ParentEduc', var_name='ScoreType', value_name='AverageScore')
sns.lineplot(x='ParentEduc', y='AverageScore', hue='ScoreType', marker='o', data=avg_scores_by_education_melted)
plt.title('Average Scores by Parents Education Level')
plt.show()


plt.figure(figsize=(12, 6))
sns.violinplot(x='major', y='tuition', data=df2)
plt.title('Tuition spending by Major ')
plt.ylabel('tuition($)')
plt.show()



# -- -- -- -- --    clustering  -- -- -- -- --


X = df1.iloc[:,[5,4]].values
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters = 4, random_state = 42)
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=100, c='pink', label='Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', label='Centroids')

plt.title('Clusters and Centroids')
plt.xlabel('Reading Score')
plt.ylabel('Math Score')
plt.legend()
plt.show()

# -- -- -- -- --    Regression   -- -- -- -- --

from sklearn.linear_model import LinearRegression
g = df1['ReadingScore'].values.reshape(-1, 1)
f = df1['WritingScore']
model = LinearRegression().fit(g, f)
print(f'y = {model.coef_}x + {model.intercept_}')


x_regression = df1["ReadingScore"]
y_regression = df1["WritingScore"]
a , b = np.polyfit(x_regression,y_regression ,deg = 1)
y_est = a * x_regression + b
y_err = x_regression.std() * np.sqrt(1/len(x_regression) + (x_regression - x_regression.mean())** 2 / np.sum ((x_regression - x_regression.mean())** 2))
fig, ax = plt.subplots()
ax.plot(x_regression , y_est,'-')
ax.fill_between(x_regression , y_est - y_err , y_est + y_err , alpha = 0.2 )
ax.plot(x_regression, y_regression,'o', color = 'tab:brown')
plt.xlabel('ReadingScore')
plt.ylabel('WritingScore')
plt.title('Liner Regression')
fig.show()
plt.waitforbuttonpress()