# Polinom Regresyon Pratiği: Çalışma Saati → Sınav Notu 📈

Bu klasör, **Polinom Regresyon** dersindeki iş akışının kendi veri setime uygulandığı kişisel pratik çalışmamı içerir. Derste hava durumu verisi kullanılmıştı; burada 1.020 öğrencilik bir performans veri setiyle, veri analizinin en klasik sorularından birini test ediyorum.

## ❓ Araştırma Sorusu

> "Daha çok çalışmak her zaman daha yüksek not mu demek?" — Yoksa bir noktadan sonra **tükenmişlik** devreye girip ilişki tersine mi dönüyor?

**Cevap (spoiler):** İlişki net biçimde **ters-U şeklinde** çıktı — notlar ~10 saat civarında zirve yapıyor, sonrasında sert düşüyor. Düz bir doğrunun asla yakalayamayacağı bu deseni polinom model yakaladı: doğrusal modelin Test R²'si 0.64 iken, CV ile seçilen 3. derece polinomun Test R²'si **0.83**.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `polinom_regresyon_pratik.ipynb` | Uçtan uca pratik: ön işleme → EDA → derece seçimi → analiz (tüm çıktı ve grafiklerle) |
| `student_performance.csv` | 1.020 öğrencilik ham veri (yaş, cinsiyet, çalışma saati, devam, sınav notu, harf notu) |

📱 **Colab/Drive uyumu:** Notebook'un başındaki hazır hücrede üç satırın yorumunu kaldırıp Drive klasör yolunu yazman yeterli — veri doğrudan Drive'dan okunur.

## 🧹 Veri Ön İşleme Kararları

Bu veri seti bilinçli olarak "kirli" — ve her sorun için verilen karar notebook'ta gerekçesiyle açıklandı:

| Sorun | Karar | Neden |
|---|---|---|
| 20 duplicate satır | Silindi | Aynı kaydın tekrarı modeli yanıltır |
| `Study_Hours` eksik (31 satır) | Satır silindi | x-y ilişkisi öğrenilirken x uydurulmaz |
| `Attendance(%)` eksik (30 satır) | Medyanla dolduruldu | Modelde kullanılmıyor |
| Çalışma saati **-2** ve **25** | Silindi | Fiziksel olarak imkânsız değerler |
| Devam yüzdesi **%115'e kadar** | 100'e kırpıldı | Ölçüm hatası varsayımı |
| IQR'ın işaretlediği 11+ saatler | ⭐ **Tutuldu** | Geçerli uç değerler — parabolün düşen kolunun kanıtı! Silinseydi tükenmişlik sinyali yok olurdu |

## 🛠️ Uygulanan Yöntemler (Dersle Birebir)

- `PolynomialFeatures` dönüşümünün somut gösterimi ([1, x, x²])
- `make_pipeline` ile 1-5. derecelerde model eğitimi ve eğrilerin tek grafikte karşılaştırılması
- Eğitim R² vs Test R² tablosuyla overfitting takibi
- **5-Fold Cross-Validation** ile derece seçimi (ortalama ± standart sapma grafiğiyle)
- En iyi modelin katsayı analizi ve eğrinin tepe noktasının hesaplanması
- Güvenlik sınırlı (`np.clip`) interaktif tahmin fonksiyonu

## 📌 Sonuçlar ve Öğrenilenler

| Model | Test R² |
|---|---|
| Doğrusal (derece 1) | 0.638 |
| **Polinom (derece 3, CV seçimi)** | **0.831** |

- **Derece 3 kazandı:** ters-U simetrik olmadığı için (yavaş yükseliş, dik düşüş) kübik terim işe yaradı; derece 4-5 aynı performansı fazladan karmaşıklıkla verdi → eşit başarıda en basit model ilkesi
- **Pearson korelasyonu yanılttı:** Study_Hours-Test_Score korelasyonu 0.66 "orta" görünüyordu; ilişki aslında çok güçlü ama doğrusal olmadığı için korelasyon düşük gösterdi — korelasyon yalnızca *doğrusal* ilişkiyi ölçer!
- **Polinomun sınırı canlı görüldü:** eğrinin tepe noktasındaki tahmin 100'ü aştı (116!) — veri seyrekleşen uçlarda polinomların taşkın davranışının birebir örneği; dersteki "dezavantajlar" uyarısı kendi modelimde karşıma çıktı ve tahmin fonksiyonuna `np.clip` güvenlik sınırı eklendi

## 🔗 İlgili Ders

Bu pratiğin dayandığı ders notebook'u için:
👉 [`09-Polinom-Regresyon-Ders`](../09-Polinom-Regresyon-Ders) klasörüne bakabilirsiniz.
