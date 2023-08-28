import seaborn as sns
import matplotlib.pyplot as plt

ex = sns.load_dataset("exercise")
print(ex)
print(ex.columns)

sns.barplot(x='time',y='pulse',hue="kind",data=ex)
plt.show()

fly = sns.load_dataset("flights")
print(fly)
print(fly.columns)

sns.barplot(x='year',y='passengers',data=fly)
plt.title("flights")
plt.show()