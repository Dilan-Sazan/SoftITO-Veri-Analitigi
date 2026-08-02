# Polinom Regresyon — Hava Durumu Verisiyle (Ders Çalışması) 📘

Bu klasör, SoftİTO Veri Analistliği eğitiminde **derste işlenen** polinom regresyon notebook'unu içerir. Notebook, eğitmenimiz tarafından hazırlanmış olup hava durumu verisi (sıcaklık/nem ölçümleri) üzerinden, doğrusal olmayan ilişkilerin nasıl modelleneceğini kapsamlı biçimde anlatır. Regresyon serisinin üçüncü halkasıdır: elle hesap (05) → sklearn ile doğrusal (07) → **polinom (09)**.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `polynomial_regression_gelismis.ipynb` | Polinom regresyonu teoriden uygulamaya anlatan ders notebook'u |

> ⚠️ **Not:** Notebook'un kullandığı hava durumu veri dosyası bu klasörde bulunmamaktadır (eğitmenden temin edilebilir). Aynı iş akışının çalışır hali için pratik klasörüne bakınız.

## ❓ Dersin Konusu

> Değişkenler arası ilişki doğrusal olmadığında ne yaparız? ŷ = b0 + b1x + b2x² + ... + bnxⁿ biçimindeki polinom modeliyle eğrisel desenler nasıl yakalanır, doğru derece nasıl seçilir?

## 📚 İçindekiler ve Öğretilen Kavramlar

1. **Teori** — doğrusal vs polinom regresyon, matris gösterimi, ne zaman kullanılır
2. **Bias-Variance Tradeoff** ⭐ — düşük derece = ilişkiyi ıskalar (underfitting), yüksek derece = gürültüyü ezberler (overfitting); doğru denge nasıl bulunur
3. **Veri ön işleme** — eksik değer analizi, tip dönüşümü, **IQR (çeyrekler arası açıklık) yöntemiyle aykırı değer tespiti**
4. **EDA** — dağılım grafikleri, korelasyon ısı haritası, box plot ile aykırı değer görselleştirmesi
5. **PolynomialFeatures + Pipeline** — x'in [1, x, x², ...] biçimine dönüştürülmesi ve `make_pipeline` ile model zinciri kurma
6. **Farklı derecelerde model eğitimi** — 1'den n'e derece döngüsü, eğitim/test R² karşılaştırması, regresyon eğrilerinin üst üste çizimi
7. **K-Fold Cross-Validation ile derece seçimi** ⭐ — tek train/test ayrımının şansa bağlı olabileceği; 5 katlı doğrulamanın ortalama + standart sapmayla daha güvenilir karar verdirdiği
8. **En iyi modelin analizi** — metrikler, katsayıların okunması
9. **İkinci senaryo** — farklı değişken çiftiyle sürecin tekrarı (MaxTemp → MinTemp)
10. **Artılar/eksiler ve pratik öneriler** — polinomun uçlarda taşkın davranışı, derece seçim tavsiyeleri, polinom yetmezse ne kullanılır

## 💡 Dersten Akılda Kalması Gerekenler

- Eğitim R²'si dereceyle hep artar ama test R²'si bir yerden sonra düşer → overfitting'in imzası
- Derece seçimi CV ile yapılır; eşit başarıda **en basit model** tercih edilir
- Polinom eğrileri veri aralığının dışında ve seyrek bölgelerde güvenilmez tahminler üretir
- IQR aykırı işaretler, ama her aykırı değer hata değildir — karar analistindir

## 🔗 İlgili Pratik

Bu yöntemlerin öğrenci performans verisine uygulandığı (ve ters-U ilişkisinin yakalandığı) pratik için:
👉 [`10-Polinom-Regresyon-Pratik-Ogrenci`](../10-Polinom-Regresyon-Pratik-Ogrenci) klasörüne bakabilirsiniz.
