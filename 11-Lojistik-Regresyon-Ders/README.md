# Lojistik Regresyon — Kalp Hastalığı Verisiyle (Ders Çalışması) 📘

Bu klasör, SoftİTO Veri Analistliği eğitiminde **derste işlenen** lojistik regresyon notebook'unu içerir. Notebook, eğitmenimiz tarafından hazırlanmış olup kalp hastalığı verisi (`heart.csv`) üzerinden regresyondan **sınıflandırmaya** geçişi anlatır — serinin ilk sınıflandırma algoritması.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `logistic_regression.ipynb` | Lojistik regresyonu teori + uygulama olarak anlatan ders notebook'u |

> ⚠️ **Not:** Notebook'un kullandığı `heart.csv` veri dosyası bu klasörde bulunmamaktadır (eğitmenden temin edilebilir). Aynı iş akışının çalışır hali için pratik klasörüne bakınız.

## ❓ Dersin Konusu

> Hedef değişken sayı değil de kategori (hasta/sağlıklı) olduğunda ne yaparız? Doğrusal regresyonun çıktısını sigmoid fonksiyonuyla 0-1 arası olasılığa dönüştüren lojistik regresyon nasıl çalışır?

## 📚 İçindekiler ve Öğretilen Kavramlar

1. **Konu anlatımı** — sınıflandırma vs regresyon farkı ve lojistik regresyonun temel mantığı
2. **Sigmoid (lojistik) fonksiyonu** ⭐ — her gerçek sayıyı 0-1 arası olasılığa sıkıştıran S eğrisi
3. **Karar sınırı (decision boundary)** — olasılığın sınıf etiketine çevrildiği eşik (varsayılan 0.5)
4. **Maliyet fonksiyonu (Cross-Entropy Loss)** — sınıflandırmada neden MSE değil log-loss kullanılır
5. **Gradient Descent** — katsayıların adım adım nasıl öğrenildiği
6. **Veri hazırlığı** — özellik/hedef ayrımı, train/test split
7. **StandardScaler ile ölçekleme** ⭐ — scaler'ın *yalnızca eğitim verisine* fit edilmesi kuralı (data leakage önlemi)
8. **Model eğitimi ve katsayı yorumu** — hangi özellik riski artırıyor/azaltıyor, önem sıralaması grafiği
9. **Model değerlendirme** — accuracy, **karmaşıklık matrisi (confusion matrix)** ve görselleştirmesi
10. **Örnek tahmin** — eğitilmiş modelle tek bir hasta için tahmin üretme
11. **Sonuç tablosu** — önemli kavramların özeti

## 💡 Dersten Akılda Kalması Gerekenler

- Lojistik regresyon adında "regresyon" geçse de bir **sınıflandırma** algoritmasıdır
- Sigmoid çıktısı olasılıktır; sınıf etiketi, eşikle (0.5) karşılaştırılarak elde edilir
- Ölçekleme lojistik regresyonda önemlidir ve scaler asla test verisiyle fit edilmez
- Accuracy tek başına yeterli değildir — karmaşıklık matrisi tam resmi gösterir
- Katsayıların işareti ve büyüklüğü model kararlarını *açıklanabilir* kılar

## 🔗 İlgili Pratik

Bu yöntemlerin 253.680 kişilik diyabet verisine uygulandığı (ve sınıf dengesizliğinin ele alındığı) pratik için:
👉 [`12-Lojistik-Regresyon-Pratik-Diyabet`](../12-Lojistik-Regresyon-Pratik-Diyabet) klasörüne bakabilirsiniz.
