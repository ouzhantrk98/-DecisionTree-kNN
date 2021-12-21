# -*- coding: utf-8 -*-
"""
Created on Sun May 16 23:21:14 2021

@author: birir
"""

#gerekli kütüphaneleri yükleyelim.

from sklearn.tree import DecisionTreeClassifier
import numpy as np

#test eğitim verisi olarak ayırmak ve doğruluk değeri bulmak için aşağıdaki kütüphaneleri ekliyoruz. 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Hata matrisi bulmak için kullanacağımız kütüphane
from sklearn.metrics import confusion_matrix

#K-Katlı çapraz geçerleme için kullanılan kütüphane
from sklearn.model_selection import cross_val_score


from sklearn.neighbors import KNeighborsClassifier

#veri setini yükleyelim...
veri = open('tae_data.csv')

#tüm veriyi matris şeklinde aktardık şimdi target ve datayı ayıklayalım..

matris = np.loadtxt(veri,delimiter=",")

#Target ve data matrislerini tanımladık şimdi onları dolduralım...
target = [0]*len(matris)

rows,cols = len(matris),5
data = [[ 0 for x in range(cols)] for y in range(rows)]

#target ı doldurduk...
for i in range(len(target)):
    
    target[i] = int(matris[i][5])
    
#şimdi datayı i dolduralım..
for i in range(len(data)):
    
    for j in range(5):
        
        data[i][j] = int(matris[i][j])
        

#Doğruluk değeri bulmak için verilerin %70 ini eğitim % 30' unu test verisi olarak ayırıyoruz. 
Data_train,Data_test,target_train,target_test = train_test_split(data,target,train_size= 0.7,test_size=0.3,random_state=0,stratify=target)


#karar ağacı algoritmasını veri üzerinde uygulayan fonksiyon
def decisionTree():
    
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(data,target)
    

    print("Decision tree için sınıflandırma sonuçları...")
    print("\nHata Matrisi")
    #hata matrisi için test_sonuc' u yeniden tanımlayalım...
    test_sonuc = clf.predict(Data_test)
    
    cm = confusion_matrix(target_test,test_sonuc)
    
    print(cm)    
    
    print("\n cv= 10 için K-Fold Cross-validation\n")

    dogrulukDegeriBulDT()
    print('\n')


#cv = 10 için fold cross validation' ı bulan fonksiyon
def dogrulukDegeriBulDT():
    
    clf = DecisionTreeClassifier(random_state=0)
    
    print(cross_val_score(clf,data,target,cv=10))
    
    
#knn yöntemi ile veriseti üzerinde sınıflandırma yapalım...
#Bu fonksiyon aynı zamanda kNN algoritmasının hata matrisinide hesaplar
def knnYontemi():
    
    print("k: 1 için kNN yöntemi ile veriyi sınıflandırma...\n")
    
    knn= KNeighborsClassifier(n_neighbors=1)
    knn.fit(data,target)
    
    test_sonuc = knn.predict(Data_test)
    
    cm = confusion_matrix(target_test,test_sonuc)
    print(cm)    
    
    print("\n cv=10 için K-Fold Cross-validation")
    dogrulukDegeriBulKNN()
    
    
#kNN için doğruluk değerini bulur.
def dogrulukDegeriBulKNN():
    
    knn= KNeighborsClassifier(n_neighbors=1)
    print(cross_val_score(knn,data,target,cv=10))
    
    
decisionTree()
knnYontemi()


#Kullanıcıdan input alan ve inputa göre iki sınıflandırma algoritmasının nasıl sonuç verdiğini 
#gösteren fonksiyon
def kullanıcıdanInputAl():
    
    print("\n\n Her verinin arasında 1 boşluk olmalı")
    print("Gireceğiniz ilk değer öğretim asistanının ingilizce bilmesi")
    print("Biliyorsa: 1, Bilmiyorsa: 2 girin")
    print("Diğer değer yardımcı olduğu dersi veren öğretim üyesi kim ? ")
    print("0-25 arasında değer girebilirsiniz.")
    print("Öteki değer hangi dersi verdiği")
    print("0-26 arasında değer girilebilir")
    print("Dersin yaz döneminde mi yoksa normal dönemlerde mi verildiği"),
    print("1: yaz dönemi-2:normal dönem (güz-bahar)")
    print("Dersi alan öğrenci sayısı")
    print("Bu öznitelikler sonucunda öğretim asistanının performansı düşük-orta-iyi olarak değerlendirilecektir.")
    print("1-Düşük, 2-Orta, 3-İyi")

    secim = input("(Örnek: 1 18 11 1 23) Giriniz: ")    
    
    #Veriyi öncelikle integer' a dönüştürdük.
    test = map(int,secim.split())
    
    #sonra arraye dönüştürdük. 
    secim_array = list(test)
    
    
    
    #Decision tree ve knn algoritmasını yazalım...
    
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(data,target)
    
    #knn için 
    knn= KNeighborsClassifier(n_neighbors=1)
    knn.fit(data,target)
    
    test_sonuc1 = clf.predict([secim_array])
    test_sonuc2 = knn.predict([secim_array])
    
    print("\nDecision Tree Algoritmasının Bulduğu Sonuç")
    print("=> ",test_sonuc1[0])
    
    print("\n kNN Algoritmasının Bulduğu Sonuç (k=1)")
    print("=> ",test_sonuc2[0])    
    
    
kullanıcıdanInputAl()
    
    
    