import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv("Data/DataSet.csv" , parse_dates=["DateOfBirth"], dayfirst=True)
df1["DateOfBirth"] = pd.to_datetime(df1["DateOfBirth"], format="%d-%m-%Y")
df1["TransactionDate"] = pd.to_datetime(df1["TransactionDate"])



print("\033[1mProject Goals\033[0m")
print("""    This project looks at credit card transactions to
    find strange or unusual patterns The goal is to learn what 
    makes a transaction more likely to be fraud The data will be 
    checked by looking at things like the type of store
    country or region, amount of money, how often the card is used,
    and the time of day\n\n"""
      )

print("\033[1mResearch Questions\033[0m")
print("""    What are the key differences between normal and fraudulent transactions
    Are there certain locations or store types where fraud is more common
    Does the amount of money in a transaction affect the chance of fraud
    Do some payment methods have more fraud
    Can we use past fraud cases to help spot new ones faster
    \n\n"""
      )
print("\033[1mTools We Will Use\033[0m")
print("""      Python - for cleaning analyzing and exploring the data
      Data Visualization - using matplotlib seaborn to create graphs and charts
      Statistical Analysis - to find important patterns and relationships in the data
    \n\n"""
      )



#--------------------------------------  2.1 Data Analysis  --------------------------------------

print(df1.info(),'\n\n')

print("\033[1mCustomerName\033[0m - Contains the name of the customer")
print("\033[1mTransactionMethod\033[0m - A number represents the type of payment method"
      " 1 - Online , 3 - Mobile , 5 - EMV , 7 - Contacless ")
print("\033[1mMerchantCategoryCode\033[0m - A code showing the type of business (grocery, gas station, clothing)")
print("\033[1mIsPremiumCustomer:\033[0m - true or False – shows whether the customer is considered a premium member")
print("\033[1mAmount\033[0m - The total value of the transaction")
print("\033[1mPhoneNumber\033[0m - The customers phone number")
print("\033[1mDateOfBirth\033[0m - The customers date of birth")
print("\033[1mTransactionDate\033[0m - The date when the transaction took place")
print("\033[1mMerchantName\033[0m - The name of the business where the purchase happened")
print("\033[1mMerchantID\033[0m - A unique code for each merchant.")
print("\033[1mIsFraud\033[0m - True/False column that shows whether the transaction was fraud")
print("\033[1mAIConfidenceScore\033[0m - A score (0 to 100) showing how sure an AI model is that the transaction is fraud\n\n\n")




#--------------------------------------  2.2 Data Processing  --------------------------------------


df1['DateOfBirth'] = pd.to_datetime(df1['DateOfBirth'])


# Age helps spot patternsnolder people falling more for scams
# or younger ones using risky stuff like crypto It makes fraud detection smarter.
df1['Age'] = (pd.to_datetime("today") - df1['DateOfBirth']).dt.days // 365


# Dropping NA values helps clean the data so we don’t get errors or wrong results when analyzing.
df1.dropna(inplace=True)

#This is good because it fixes wrong or weird ages (like under 16 or over 120)
# by replacing them with the average age. That way, the data stays realistic and doesn’t mess up the analysis.


AgeCheck = df1[(df1['Age'] < 16) | (df1['Age'] > 120)].index
mean_age = df1['Age'].mean()
df1.loc[(df1['Age'] < 16) | (df1['Age'] > 120), 'Age'] = int(mean_age)




#--------------------------------------  2.3 Descriptive Statistical Analysis  --------------------------------------


# mask that will help us  work only
# with the fraud cases later It saves time and keeps your code clean

Fraud =df1[df1["IsFraud"] == True]


print(df1[["Amount", "Age", "AIConfidenceScore"]].describe(),'\n\n\n')
print('The Max Age is:',max(df1['Age']))
print('The Min Age is:',min(df1['Age']))
print('The Highest Transaction amount is:',max(df1['Amount']))
print('The Lowest Transaction amount is:',min(df1['Amount']),'\n\n\n')

#helps compare how much premium vs regular customers spend
#premium users really make bigger transactions like we expect

print('the average spending of premium Customers\n',df1.groupby('IsPremiumCustomer')['Amount'].mean())


#This shows the top 10 countries where transactions happen.
#It helps understand where most of the activity is and spot high-volume regions.
print(df1['MerchantCountry'].value_counts().head(10),'\n\n\n')

#This shows the top 10 countries where fraud happens.
#It helps find which countries have more fraud cases
print(Fraud['MerchantCountry'].value_counts().head(10),'\n\n\n')
print(df1.groupby('Gender')['Amount'].mean(),'\n\n\n')

fraud_percent = (
    df1[df1["IsFraud"] == True]["TransactionMethod"]
    .value_counts(normalize=True)
    * 100
).round(1).astype(str) + '%'
print(fraud_percent)



print((df1.groupby("Gender")["IsFraud"].mean()* 100).round(2))

print(Fraud.groupby("MerchantCategoryCode")["Amount"].mean().sort_values(ascending=False).head(5).round(2))



#--------------------------------------  2.4 advanced analysis  --------------------------------------

print(df1.groupby("IsPremiumCustomer")[["Amount", "IsFraud"]].agg({
    "Amount": "mean",
    "IsFraud": "mean"
}) * [1, 100])




correlation = df1["AIConfidenceScore"].corr(df1["IsFraud"])
print("Correlation between AI score and fraud:", round(correlation, 2))


fraud_rates = df1.groupby("MerchantCountry")["IsFraud"].mean().sort_values(ascending=False) * 100
print(fraud_rates)



yearly_trend = df1.groupby(df1["TransactionDate"].dt.year)["IsFraud"].mean() * 100
print(yearly_trend)


df1["Year"] = df1["TransactionDate"].dt.year
fraud_per_year = df1.groupby("Year")["IsFraud"].mean() * 100
print(fraud_per_year.round(2))








df1["Year"] = df1["TransactionDate"].dt.year
df1["Month"] = df1["TransactionDate"].dt.month

pivot = df1.pivot_table(
    values="IsFraud",
    index="Month",
    columns="Year",
    aggfunc="mean"
) * 100
print(pivot.round(2))





top_mcc = df1["MerchantCategoryCode"].value_counts().head(5)

plt.figure(figsize=(8, 5))
ax = sns.barplot(x=top_mcc.index.astype(str), y=top_mcc.values, palette="Set2")

plt.title("Top 5 MCCs by Transaction Count", fontsize=14)
plt.xlabel("Merchant Category Code")
plt.ylabel("Transaction Count")

# Add count labels on top of each bar
for i, value in enumerate(top_mcc.values):
    plt.text(i, value + max(top_mcc.values)*0.01, f"{value:,}", ha='center', fontsize=10)

plt.tight_layout()
plt.show()




fraud_by_gender = df1[df1["IsFraud"] == True]["Gender"].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(fraud_by_gender, labels=fraud_by_gender.index, autopct='%1.1f%%',
        startangle=140, colors=sns.color_palette("Set2"))
plt.title("Fraud Distribution by Gender")
plt.tight_layout()
plt.show()


top_fraud_mcc = df1[df1["IsFraud"] == True]["MerchantCategoryCode"].value_counts().head(5)
plt.figure(figsize=(6, 4))
sns.barplot(x=top_fraud_mcc.index.astype(str), y=top_fraud_mcc.values, palette="Reds")
plt.title("Top 5 Fraud-Prone MCCs")
plt.xlabel("MCC")
plt.ylabel("Fraud Count")
plt.tight_layout()
plt.show()


fraud_method = df1.groupby("TransactionMethod")["IsFraud"].mean().sort_values() * 100
plt.figure(figsize=(6, 4))
plt.barh(fraud_method.index.astype(str), fraud_method.values, color='skyblue')
plt.title("Fraud Rate by Transaction Method")
plt.xlabel("Fraud Rate (%)")
plt.ylabel("Transaction Method")
plt.tight_layout()
plt.show()



df1.to_excel('output.xlsx', index=False)


plt.figure(figsize=(6, 4))
sns.histplot(df1["AIConfidenceScore"], bins=30, kde=True, color='purple', edgecolor='black')
plt.title("AI Confidence Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

