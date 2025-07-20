import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv("Data/DataSet.csv")
df1["DateOfBirth"] = pd.to_datetime(df1["DateOfBirth"])
df1["TransactionDate"] = pd.to_datetime(df1["TransactionDate"])



print("\033[1mProject goals\033[0m")
print("""    this project looks at credit card transactions to
    find strange or unusual patterns The goal is to learn what 
    makes a transaction more likely to be fraud The data will be 
    checked by looking at things like the type of store
    country or region  amount of money  how often the card is used 
    and the time of day\n\n"""
      )

print("\033[1mResearch Questions\033[0m")
print("""    What are the differences between normal and fraudulent transactions
    Are there certain locations or store types where fraud is more common
    Does the amount of money in a transaction affect the chance of fraud
    Do some payment methods have more fraud
    Can we use past fraud cases to help spot new ones
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
df1['Age'] = (pd.to_datetime("today") - df1['DateOfBirth']).dt.days // 365 # הוספת עמודת גיל מחושבת לפי תאריך הלידה
df1.dropna(inplace=True)                                                   # הפלת ערכים חסרים מהדאטא סט שלנו
AgeCheck = df1[(df1['Age'] < 16) | (df1['Age'] > 120)].index               # ביצוע בדיקה של האם יש לנו גילאים אשר לא הגיונים במידע
mean_age = df1['Age'].mean()                                               # מציאת הגיל ממוצע
df1.loc[(df1['Age'] < 16) | (df1['Age'] > 120), 'Age'] = int(mean_age)     # החלפת אותם גילאים לא הגיונים בגיל הממוצע של המידע

#--------------------------------------  2.3 Descriptive Statistical Analysis  --------------------------------------

Fraud =df1[df1["IsFraud"] == True]                                         # יצירת סט שהוא רק כאשר עסקת הונאה יעזור לנו בע
print(df1[["Amount", "Age", "AIConfidenceScore"]].describe(),'\n\n\n')
print('The Max Age is:',max(df1['Age']))
print('The Min Age is:',min(df1['Age']))
print('The highest transaction amount is:',max(df1['Amount']))
print('The lowest transaction amount is:',min(df1['Amount']),'\n\n\n')
print('the average spending of premium Customers\n',df1.groupby('IsPremiumCustomer')['Amount'].mean())     # סכום עסקה ממוצע של לקוח פרימיום
print(df1['MerchantCountry'].value_counts().head(10),'\n\n\n')                                             # טופ 10 מדינות לפי עסקאות
print(Fraud['MerchantCountry'].value_counts().head(10),'\n\n\n')                                           # טופ 10 מדינות שיש בהם הכי הרבה עסקאות הונאה
print(df1.groupby('Gender')['Amount'].mean(),'\n\n\n')                                                     # ממוצע עסקה לפי מגדר
print((df1.groupby("Gender")["IsFraud"].mean()* 100).round(2))                                             # מ לפי מגדר
print(Fraud.groupby("MerchantCategoryCode")["Amount"].mean().sort_values(ascending=False).head(5).round(2))# ממוצע עסקה בטופ 10 ענפים שהיו הונאה
#--------------------------------------  2.4 advanced analysis  --------------------------------------

print(df1.groupby("IsPremiumCustomer")[["Amount", "IsFraud"]].agg({                                     # ממוצע עסקה ואחוז הונאה ללקוחות פרימיום ורגילים
    "Amount": "mean",
    "IsFraud": "mean"
}) * [1, 100])




correlation = df1["AIConfidenceScore"].corr(df1["IsFraud"])
print("Correlation between AI score and fraud:", round(correlation, 2))                                # קורולאציה בין ציון הונאה לעסקאות הונאה


fraud_percent = df1.groupby("MerchantCountry")["IsFraud"].mean().sort_values(ascending=False) * 100    # אחוזי ההונאה עבור מדינות
print(fraud_percent.round(2))



yearly_trend = df1.groupby(df1["TransactionDate"].dt.year)["IsFraud"].mean() * 100                     # אחוזי ההונאה עבור כל שנה
print(yearly_trend)




df1["Year"] = df1["TransactionDate"].dt.year
df1["Month"] = df1["TransactionDate"].dt.month

pivot = df1.pivot_table(
values="IsFraud", index="Month", columns="Year", aggfunc="mean") * 100                                 # טבלת פיוט אשר מראה עבור כל שנה וחודש את אחוזי ההונאה
print(pivot.round(2))
top_mcc = df1["MerchantCategoryCode"].value_counts().head(5)

plt.figure(figsize=(7, 3))
ax = sns.barplot(x=top_mcc.index.astype(str), y=top_mcc.values)

plt.title("Top 5 MCCs by Transaction Count", fontsize=14)
plt.xlabel("Merchant Category Code")
plt.ylabel("Transaction Count")
plt.show()


fraud_by_gender = df1[df1["IsFraud"] == True]["Gender"].value_counts()
plt.figure(figsize=(7, 4))
plt.pie(fraud_by_gender, labels=fraud_by_gender.index, autopct='%1.1f%%')
plt.title("Fraud distribution by gender")
plt.tight_layout()
plt.show()


top_fraud_mcc = df1[df1["IsFraud"] == True]["MerchantCategoryCode"].value_counts().head(5)
plt.figure(figsize=(7, 3))
sns.barplot(x=top_fraud_mcc.index.astype(str), y=top_fraud_mcc.values)
plt.title("Top 5 Fraud Prone MCCs")
plt.xlabel("MCC")
plt.ylabel("Fraud count")
plt.show()


fraud_method = df1.groupby("TransactionMethod")["IsFraud"].mean().sort_values() * 100
plt.figure(figsize=(7, 4))
plt.barh(fraud_method.index.astype(str), fraud_method.values)
plt.title("Fraud Rate by Transaction Method")
plt.xlabel("Fraud Rate (%)")
plt.ylabel("Transaction Method")
plt.show()



plt.figure(figsize=(7, 3))
sns.histplot(df1["AIConfidenceScore"])
plt.title("AI Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

heatmap_data = df1.groupby(['MerchantCategoryCode', 'IsFraud'])['AIConfidenceScore'].mean().unstack()
plt.figure(figsize=(7, 4))
sns.heatmap(heatmap_data, annot=True)
plt.xlabel("Fraud")
plt.ylabel("Merchant Category")
plt.show()
print(""" 
סיכום ממצאים מהניתוח 
•	אחוז ההונאה בין 14% ל 15%
•	לקוחות פרימיום מבצעים עסקאות יקרות יותר אך אחוז ההונאה אצלם דומה ללקוחות רגילים
•	ציון AI  נמצא בקורלציה חיובית חזקה (0.67) עם העסקאות שסומנו כהונאה
•	מדינות כמו מצרים מלזיה וספרד מובילות באחוזי ההונאה
•	קטגוריות כמו 7299 ו6011 נפוצות בקרב ההונאות
•	הבדל קטן בין גברים לנשים בשיעורי ההונאה (נשים 15% גברים 14%)



מסקנות מבוססות על הנתונים
•	ניתן לסמוך על ציון   AI ככלי חיזוי ראשוני מאחר ומתאם ההונאה חיובי 
•	יש מדינות וקטגוריות בהם הסיכוי להונאה גבוה יותר מה שיכול לעזור ביצירת פרופיל סיכון
•	אין השפעה משמעותית למגדר או לסוג לקוח (פרימיום או לא) על הסיכון להונאה
•	שיטות תשלום מסוימות מציגות סיכוי גבוה יותר להונאה ויש מקום לשימוש אמצעים בטוחים יותר

תובנות עסקיות
•	חברות אשראי יכולות להשתמש בציון ה  AI יחד עם מידע על מדינה וקטגוריית כדי לתעדף בדיקות נוספות
•	כדאי להפעיל אמצעי אימות במדינות ובקטגוריות שנמצאו בסיכון גבוה
•	שיפור ההסברה ללקוחות במדינות מועדות להונאה יכול להקטין את הנזק


כיון מחקר עתידי
•	לבצע ניתוח עומק לפי שעות ביום וימי האם יש דפוסי זמן להונאה
•	לנתח את התפלגות ההונאות לפי מכשיר
•	לשפר את אלגוריתם זיהוי ההונאות על ידי שילוב תכונות נוספות כמו מיקום GPS היסטוריית רכישות




""")