from sklearn import preprocessing
le = preprocessing.LabelEncoder()
print le.fit([1, 2, 2, 6])
print le.classes_
#le.transform([1, 1, 2, 6]) 
#le.inverse_transform([0, 0, 1, 2])
#array([1, 1, 2, 6])
