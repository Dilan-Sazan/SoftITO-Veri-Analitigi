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

## 🔗 İlgili Ders

Bu pratiğin dayandığı ders notebook'u için:
👉 [`01-NumPy-Temelleri-Ders`](../01-NumPy-Temelleri-Ders) klasörüne bakabilirsiniz.
