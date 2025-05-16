import pandas as pd
import numpy as np

# read csv
dataset = pd.read_csv("Titanic_dataset.csv")
dataset.head()

# 1. Kazada ölenlerin yaş ortalamasını bulunuz
result = dataset[dataset['Survived'] == 0]['Age'].mean()
print(result)

# 2. Kazada ölenlerin bilet fiyatlarının ortalamasını ve medyanını bulunuz
mean = dataset[dataset['Survived'] == 0]['Fare'].mean()
median = dataset[dataset['Survived'] == 0]['Fare'].median()

print(mean)
print(median)

# 3. Kazada ölen erkeklerin yaş ortalamasını bulunuz
result = dataset[(dataset['Survived'] == 0) & (dataset['Sex'] == 'male')]['Age'].mean()
print(result)

# 4. Kazada ölen Kadınların yaş ortalamasını bulunuz
result = dataset[(dataset['Survived'] == 0) & (dataset['Sex'] == 'female')]['Age'].mean()
print(result)

# 5. Kazadan kurtulanların yaş ortalamasını bulunuz
result = dataset[dataset['Survived'] == 1]['Age'].mean()
print(result)

# 6. Kazadan kurtulanların bilet fiyatlarının ortalamasını bulunuz
result = dataset[dataset['Survived'] == 1]['Fare'].mean()
print(result)

# 7. Kazadan kurtulan toplam kişi sayısını bulunuz… 
result = len(dataset[dataset['Survived'] == 1])
print(result)

# 8. 10 yaşından küçüklerin bilet fiyatlarının medyan değerini bulunuz
result = dataset[dataset['Age'] < 10]['Fare'].median()
print(result)

# 9. 1.sınıf, 2.sınıf ve 3.sınıf bilet fiyatlarının ortalama ve medyanlarını karşılaştırınız. (Pclass değişkeni sınıfları barındırmaktadır.)
dataset.groupby("Pclass")["Fare"].agg(["mean", "median"])

# 10. Kazada ölen kadınların oranı ile erkeklerin oranını karşılaştırınız. 
#(Örnek: erkekler için; ölen erkeklerin, erkek sayısına bölümü bu oranı vermektedir.

numberOfMale = len(dataset[dataset['Sex'] == 'male'])
numberOfDeadMale = len(dataset[(dataset['Survived'] == 0) & (dataset['Sex'] == 'male')])
ratioMale = numberOfDeadMale / numberOfMale

numberOfFemale = len(dataset[dataset['Sex'] == 'female'])
numberOfDeadFemale = len(dataset[(dataset['Survived'] == 0) & (dataset['Sex'] == 'female')])
ratioFemale = numberOfDeadFemale / numberOfFemale

print("Ratio male:", ratioMale * 100)
print("Ratio female:", ratioFemale * 100)
