import pandas as pd

file_name = 'RocketLeagueSkillshotsData.xlsx'
df = pd.read_excel(file_name)

# Boş değerleri içeren satırları sil
df = df.dropna()
#df.dropna(subset=df.columns, how='all', inplace=True)

# 'Time' sütununu numeric veri tipine dönüştür (veri tipi object)
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')

# 'DistanceCeil' sütunundaki değerleri sayısal bir formata çevir (veri tipi object)
df['DistanceCeil'] = pd.to_numeric(df['DistanceCeil'], errors='coerce')

# Her bir sütun için aykırı değerleri düzelt
attributes = ['BallAcceleration', 'Time', 'DistanceWall', 'DistanceCeil', 'DistanceBall',
              'PlayerSpeed', 'BallSpeed']

'''
BallSpeed'den sonrası dahil edilmedi her değeri 1 yapıyor.
attributes = ['BallAcceleration', 'Time', 'DistanceWall', 'DistanceCeil', 'DistanceBall',
              'PlayerSpeed', 'BallSpeed', 'up', 'accelerate', 'slow', 'goal', 'left', 'boost',
              'camera', 'down', 'right', 'slide', 'jump']
'''

for attribute in attributes:
    # -1 ve 0.0 değerlerini NaN olarak işaretle
    df[attribute] = df[attribute].replace([-1, 0.0], pd.NA)

    # NaN değerleri sütunun ortalaması ile doldur
    df[attribute] = df[attribute].fillna(df[attribute].mean())

# Sonuçları yeni bir Excel dosyasına yaz
output_file_name = 'ModifiedDataSet.xlsx'
df.to_excel(output_file_name, index=False)

# DataFrame'deki sütunları ve veri tiplerini göster
#print(df.dtypes)

# DataFrame'deki her sütundaki boş olmayan değer sayısını göster
#print(df.count())


'''
https://www.youtube.com/watch?v=gxBhnRTGdZU
https://www.youtube.com/watch?v=j-uHsi-KjOs
https://neptune.ai/blog/knn-algorithm-explanation-opportunities-limitations
https://arize.com/blog-course/knn-algorithm-k-nearest-neighbor/
https://www.ibm.com/topics/knn
https://www.datacamp.com/tutorial/k-nearest-neighbor-classification-scikit-learn

Codes for knn
score_list = []
for k in range(1,15):
    knn_model1 = KNeighborsClassifier(n_neighbors=k)
    knn_model1.fit(X_train, y_train)
    score_list.append(knn_model1.score(X_test, y_test))

plt.title("En uygun k değerine göre score")
plt.plot(range(1,15), score_list)
plt.xlabel("K Değeri")
plt.ylabel("Doğruluk Oranı")
plt.show()
'''
'''
# Boş listeler oluşturarak k değerleri ve doğruluk oranlarını saklama
k_values_list = []
accuracy_list = []

for k in range(1,21):
    knn_model1 = KNeighborsClassifier(n_neighbors=k)
    knn_model1.fit(X_train, y_train)
    y_pred = knn_model1.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    k_values_list.append(k)
    accuracy_list.append(accuracy)
'''