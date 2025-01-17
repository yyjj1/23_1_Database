import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#EmployeeCount랑 EmployeeNumber ㅈ도 의미없는거 같음

df = pd.read_csv('HR Employee Attrition.csv')

sns.histplot(data=df, x=df['Age'], multiple="stack",
             binwidth=1, discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
#19,20살 histogram 정상적으로 출력 안됨
sns.histplot(data=df, x=df['BusinessTravel'], multiple="stack",
             binwidth=1, discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['DailyRate'], multiple="stack",
             bins=15, binwidth=100, binrange=(100,1500), hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['Department'], multiple="stack",
             hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['DistanceFromHome'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['Education'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['EducationField'], multiple="stack",
             hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['EnvironmentSatisfaction'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4])
plt.show()
sns.histplot(data=df, x=df['Gender'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['HourlyRate'], multiple="stack",
             binwidth=5, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['JobInvolvement'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4])
plt.show()
sns.histplot(data=df, x=df['JobLevel'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['JobRole'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['JobSatisfaction'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4,5])
plt.show()
sns.histplot(data=df, x=df['MaritalStatus'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['MonthlyIncome'], multiple="stack",
             binwidth=500, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['MonthlyRate'], multiple="stack",
             binwidth=1000, bins=27, binrange=(2000,27000), hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['NumCompaniesWorked'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['OverTime'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['PercentSalaryHike'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['PerformanceRating'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[3,4])
plt.show()
sns.histplot(data=df, x=df['RelationshipSatisfaction'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4])
plt.show()
sns.histplot(data=df, x=df['StockOptionLevel'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[0,1,2,3])
plt.show()
sns.histplot(data=df, x=df['TotalWorkingYears'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['TrainingTimesLastYear'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['WorkLifeBalance'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4])
plt.show()
sns.histplot(data=df, x=df['YearsAtCompany'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['YearsInCurrentRole'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=list(range(0,19)))
plt.show()
sns.histplot(data=df, x=df['YearsSinceLastPromotion'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['YearsWithCurrManager'], multiple="stack",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=list(range(0,18)))
plt.show()