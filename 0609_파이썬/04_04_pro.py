import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)

print(tips.columns) # 컬럼명
##
## 앞의 데이터만 살펴보기
print( tips.head() )

## 뒤의 데이터 살펴보기 - tail()
print( tips.tail() )

### 요일별 식사 금액은 얼마나 될까?
plt.figure(figsize=(8,6))
sns.barplot(x="day", y="total_bill", data=tips) # 막대 그래프
plt.show()

# 요일별 tip은 남성과 여성은 어떠할까?
plt.figure(figsize=(8,6))
sns.barplot(x="day", y="tip", hue="sex", data=tips)
plt.title("Tips by day")
plt.show()