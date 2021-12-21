## Veri Setinin İncelenmesi
Veri setinde öğretim üyesi asistanları, aldıkları öznitelik değerlerine göre performans bakımından iyi-orta-düşük şeklinde sınıflandırılıyor. 5 farklı öznitelik var. Birincisi öğretim üyesinin dil bilip bilmemesi. İkincisi Asistanı olduğu öğretim üyesi, Üçüncüsü verdiği ders, Dördüncüsü ders yaz döneminde mi veriliyor yoksa normal dönemde mi (güz veya bahar) döneminde mi veriliyor. Beşincisi ise dersi alan öğrenci sayısı. 151 adet örnek var veri setinde.
Bizden bu veri setini ve 2 farklı sınıflandırma algoritması kullanarak veri setini sınıflandırmamız ve her sınıflandırma algoritmasının performansını ölçmek için veri seti üzerindeki hata matrisini ve k-fold cross validation’ ı bulmamız isteniyor. Ayrıca kullanıcın girdiği değerler için öğretim üyesinin nasıl bir performansa sahip olduğunun bulunup konsolda yazdırılması da isteniyor.

## Hata matrisi ve Doğruluk Değeri Çıktıları…
Doğruluk değerini bulmak için bizden cv=10 olacak şekilde k-Fold Cross Validation isteniyordu. İlk sınıflandırma algoritması Decision Tree.. Veri seti üzerindeki değerleri şu şekilde: 

![Hata Matrisi DT](https://i.hizliresim.com/e1vg0xk.jpg)

Diğer sınıflandırma algoritması için k-NN, k=1 değeri için sınıflandırma yapıldığında değerler şu şekilde:

![Hata Matrisi kNN](https://i.hizliresim.com/hyoweze.jpg)

## Kullanıcı Girdisi için sonuçlar…

![Çıktı](https://i.hizliresim.com/kd8ezi1.jpg)