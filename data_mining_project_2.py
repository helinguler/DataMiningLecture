#Information gain hesabı yapıldıktan sonraki şablon
#ÇIKTILARI NOT ETMEYİ UNUTMA!

'''ÖNEMLİ NOT!
Algoritmayı yazıp bir kez çalıştırdıktan sonra çıktıları yani başarı kriterlerini not ediyoruz. 
Bu çıktı feature sayısı=150 olan hesaplamanın çıktısı olacak.
Sonra 150 yazan yere sırasıyla 125, 100, 75, 50 yazıyoruz ve bunları da sırasıyla çalıştırarak çıktıları not ediyoruz.
Burada amacımız her algoritma için en optimum feature sayısını bulabilmek.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


veriler = pd.read_csv("TUANDROMD.csv")
veriler = veriler.dropna()
x = veriler.iloc[:,0:-1].values
y = veriler.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)


from sklearn.feature_selection import mutual_info_classif
information_gain = mutual_info_classif(x, y)

information_gain_with_index = list(enumerate(information_gain))
sorted_information_gain = sorted(information_gain_with_index, key=lambda x: x[1], reverse=True)

for i in range(len(sorted_information_gain)):
    print("Information Gain values of all features\n")
    print(f"Feature {i+1}: {sorted_information_gain[i]}")



selected_features = sorted_information_gain[:50]
for i, (index, information_gain) in enumerate(selected_features):
    print("Selected Features\n")
    print(f"Feature {i+1} - Index: {index}, Information Gain: {information_gain}")

selected_feature_indices = [index for index, _ in selected_features]
x_selected = x[:, selected_feature_indices]



from sklearn.model_selection import cross_val_score, train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_selected, y, test_size=0.33, random_state=0)





#Algoritma

# K-Nearest Neighbors (KNN) Algorithm
from sklearn.neighbors import KNeighborsClassifier

# Modeli oluşturma
knn_model = KNeighborsClassifier(n_neighbors=3, metric='euclidean')

# Modeli eğitme
knn_model.fit(x_train, y_train)

# Test verilerini kullanarak tahmin yapma
y_pred = knn_model.predict(x_test)


# Optimum k değerini bulmak için
k_values = [i for i in range (1,31)]
acc_scores = []

for k in k_values:
    knn_model1 = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    cv_scores = cross_val_score(knn_model1, x_train, y_train, cv = 5, scoring='accuracy')
    acc_scores.append(cv_scores.mean())


# Doğruluk oranlarını görselleştirme
plt.plot(k_values, acc_scores, marker='o', linestyle='-', color='b')
plt.title('Optimum K Değerinin Bulunması')
plt.xlabel('K Değeri')
plt.ylabel('Doğruluk Oranı')
plt.show()

# En iyi k değerini bulma
best_k = k_values[acc_scores.index(max(acc_scores))]
print(f"En iyi k değeri: {best_k}")





#Başarı Kriterleri
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, mean_squared_error

cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix")
print(cm)

accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2f}")

precision = precision_score(y_test, y_pred, average='weighted')
print(f"Precision: {precision:.2f}")

recall = recall_score(y_test, y_pred, average='weighted')
print(f"Recall: {recall:.2f}")

f1 = f1_score(y_test, y_pred, average='weighted')
print(f"F1-Score: {f1:.2f}")

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.2f}")

