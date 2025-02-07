import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.countplot(y='signature', data=df, order=df['signature'].value_counts().index)
plt.title('Распределение событий по типам')
plt.xlabel('Количество событий')
plt.ylabel('Тип события')
plt.show()