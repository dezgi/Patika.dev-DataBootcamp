Bitirme Projesi

- Seçilen Veri Seti: Airline Passenger Satisfaction Dataset
- Kullanılan kütüphaneler: pandas,numpy, matpilot, seaborn

1. İstatiksel Özet
     - Sayısal değişkenler için ortalama, medyan, standard sapma, minimum ve maksimum değeler hesaplandı.
2. Eksik Değer Analizi
     - Null olan değerler hesaplandı.
     - Sadece Arrival Delay in Minutes değişkeninde eksik veri tespit edildi.
     - Bu eksik değerlerin medyan değerlerinin hesaplanarak doldurulmadı en uygun yöntemdir.
3. Aykırı Değer Analizi
   - Age, Flight Distance, Departure Delay in Minutes, Arrival Delay in Minutes sütunlarında IQR yöntemine göre aykırı değerler belirlendi.
   - Özellikle Departure Delay in Minutes ve Arrival Delay değerlerinde yüksek oranda aykırı değer tespit edildi.
4. Görselleştirme
    - Sayısal değişkenler kısmında Histogram ile dağılım grafikleri çizildi.
    - Kategorik değişkenler kısmında ise Countplot ile dağılımlar gösterildi.



