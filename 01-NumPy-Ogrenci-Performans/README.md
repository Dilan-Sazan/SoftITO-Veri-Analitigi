# NumPy Pratik: Öğrenci Performans Analizi 🎯

Bu klasör, **NumPy Temelleri** dersinde öğrenilen kavramların gerçek bir veri seti üzerinde uygulandığı **kişisel pratik çalışmamı** içerir.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `numpy_pratik_ogrenci_performans.ipynb` | Ders konularının veri seti üzerinde uygulandığı pratik notebook (çıktılarıyla birlikte) |
| `Student_Performance_Dataset.csv` | 5.000 öğrencilik performans veri seti |

## 📊 Veri Seti Hakkında

Veri seti 5.000 öğrenciye ait 16 sütun içerir:

- **Demografik:** yaş, cinsiyet, sınıf, veli eğitim durumu
- **Alışkanlıklar:** günlük çalışma saati, devam yüzdesi, internet erişimi, sosyal aktivite
- **Başarı:** matematik / fen / İngilizce notları, geçen yıl notu, final yüzdesi, geçme-kalma durumu

## 🛠️ Uygulanan Konular

1. CSV verisini NumPy array'lerine dönüştürme
2. Array özellikleri (`shape`, `dtype`, `ndim`) inceleme
3. İndeksleme ve dilimleme ile belirli öğrenci/ders seçme
4. **Boolean indeksleme** ile filtreleme (80+ alanlar, çok çalışanlar, kalan öğrenciler)
5. **Aggregate fonksiyonlarla** istatistikler (ortalama, medyan, standart sapma, `argmax` ile en başarılı öğrenciyi bulma)
6. **Broadcasting** ile kaynak puanı ekleme ve ağırlıklı ortalama hesaplama
7. `reshape` ve `np.random.choice` ile rastgele örneklem alma

## 📌 Öne Çıkan Bulgular

- Günde **4+ saat çalışan** öğrencilerin başarı ortalaması, 2 saatten az çalışanlardan belirgin şekilde yüksek
- **Kalan öğrencilerin** devam yüzdesi, geçen öğrencilere göre daha düşük
- `argmax` ile en yüksek final yüzdesine sahip öğrenci tespit edildi

---

## 📓 Notebook Adım Adım — `numpy_pratik_ogrenci_performans.ipynb`

Notebook'un kendisinde yalnızca kod bulunur; her adımın açıklaması burada.

#### 1. Veriyi Yükleme

Önce CSV dosyasını okuyup sayısal sütunları NumPy array'ine dönüştürüyoruz.

#### 2. Array Özellikleri

Derste gördüğümüz `shape`, `dtype`, `ndim`, `size` özniteliklerini kendi verimizde inceliyoruz.

#### 3. İndeksleme ve Dilimleme (Slicing)

Derste `a[0]`, `a[1:4]`, `m[satır, sütun]` gibi kullanımları görmüştük. Şimdi gerçek veride uyguluyoruz.

#### 4. Boolean İndeksleme ile Filtreleme

Derste `a[a > 3]` şeklinde koşula uyan elemanları seçmeyi öğrenmiştik. Bu, veri analizinde en çok kullanılan tekniklerden biridir.

#### 5. Toplulaştırma (Aggregate) Fonksiyonları

Derste `sum`, `mean`, `min`, `max`, `std`, `argmax` fonksiyonlarını görmüştük. Şimdi veri setimizin genel istatistiklerini çıkarıyoruz.

#### 6. Broadcasting ile Hesaplamalar

Derste skaler ile array arasındaki işlemlerin tüm elemanlara otomatik uygulandığını görmüştük.

#### 7. Reshape ve Rastgele Örneklem

Son olarak derste gördüğümüz `reshape` ve `np.random` modülünü uyguluyoruz.

#### Özet

Bu pratikte, NumPy Temelleri dersinde öğrendiklerimizi 5.000 kişilik gerçek bir öğrenci veri setine uyguladık:

- CSV verisini **NumPy array'lerine** dönüştürdük
- `shape`, `dtype` gibi **array özelliklerini** inceledik
- **İndeksleme ve dilimleme** ile belirli öğrencilere/derslere ulaştık
- **Boolean indeksleme** ile filtreler kurduk (80+ alanlar, çok çalışanlar, kalanlar...)
- **Aggregate fonksiyonlarla** (mean, min, max, std, argmax) istatistik çıkardık
- **Broadcasting** ile kaynak puanı ve ağırlıklı ortalama hesapladık
- **Reshape** ve **rastgele örneklem** uyguladık

📌 Öne çıkan bulgular:
- Günde 4+ saat çalışan öğrencilerin başarı ortalaması, 2 saatten az çalışanlardan belirgin şekilde yüksek
- Kalan öğrencilerin devam yüzdesi, geçenlere göre daha düşük
