# Support Vector Machine (SVM) — Hindistan İş Piyasası Verisiyle (Ders Çalışması) 📘

Bu klasör, SoftİTO Veri Analistliği eğitiminde **derste işlenen** SVM notebook'unu içerir. Notebook, eğitmenimiz tarafından hazırlanmış olup Hindistan iş piyasası verisi üzerinden, iş ilanlarının aradığı tecrübe seviyesinin tahmin edilmesini anlatır — serinin ikinci sınıflandırma algoritması.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `svm_analiz.ipynb` | SVM'i teori + uygulama olarak anlatan ders notebook'u |

> ⚠️ **Not:** Notebook'un kullandığı `india_job_market_2024_2026.csv` veri dosyası bu klasörde bulunmamaktadır (eğitmenden temin edilebilir). Aynı iş akışının çalışır hali için pratik klasörüne bakınız.

## ❓ Dersin Konusu

> Sınıfları birbirinden ayıran en iyi sınır nasıl çizilir? SVM, sınıflar arasındaki boşluğu (margin) en geniş yapan hiper düzlemi bulur; doğrusal ayrılamayan verilerde ise **kernel hilesiyle** veriyi daha yüksek boyuta taşıyıp orada ayırır.

## 📚 İçindekiler ve Öğretilen Kavramlar

1. **SVM teorisi** — destek vektörleri, margin maksimizasyonu, hiper düzlem kavramı
2. **Kernel fonksiyonları** ⭐ — linear, RBF ve polynomial kernel'lerin ne zaman kullanılacağı
3. **Hiperparametreler** — C (hata toleransı/düzenlileştirme) ve gamma (RBF'in etki alanı) dengesi
4. **Veri keşfi** — değişken isimleri/açıklamaları, hedef değişkenin (Experience_Level) tanınması
5. **Ön işleme** — kategorik değişken kodlama, train/test ayrımı, StandardScaler ile ölçekleme
6. **Üç kernel ile model eğitimi** — linear vs RBF vs poly karşılaştırması
7. **GridSearchCV** ⭐ — C/gamma/kernel kombinasyonlarının çapraz doğrulamayla sistematik taranması, `best_estimator_` kullanımı
8. **Sonuç ve değerlendirme** — en iyi modelin seçimi ve çıkarımlar

## 💡 Dersten Akılda Kalması Gerekenler

- SVM ölçeklemeye çok duyarlıdır — StandardScaler şarttır
- Kernel seçimi varsayımla değil denemeyle (CV ile) yapılır
- C küçük = geniş margin + daha fazla hataya tolerans; C büyük = dar margin + ezberleme riski
- GridSearchCV, hiperparametre seçimini el yordamından kurtarır

## 🔗 İlgili Pratik

Bu yöntemlerin 90.000 ilanlık küresel AI işleri verisine uygulandığı pratik için:
👉 [`14-SVM-Pratik-AI-Isleri`](../14-SVM-Pratik-AI-Isleri) klasörüne bakabilirsiniz.
