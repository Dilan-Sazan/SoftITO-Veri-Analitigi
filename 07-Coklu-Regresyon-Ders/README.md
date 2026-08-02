# Basit ve Çoklu Doğrusal Regresyon — sklearn ile (Ders Çalışması) 📘

Bu klasör, SoftİTO Veri Analistliği eğitiminde **derste işlenen** regresyon notebook'unu içerir. Notebook, eğitmenimiz tarafından hazırlanmış olup Süper Lig takım istatistikleri üzerinden, bu kez **scikit-learn kütüphanesiyle** basit ve çoklu doğrusal regresyonu anlatır. (05. klasördeki derste regresyon formülden elle hesaplanmıştı; bu ders aynı işin profesyonel kütüphaneyle yapılışını gösterir.)

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `regresyon_analizi.ipynb` | sklearn ile basit + çoklu regresyonu anlatan ders notebook'u |

> ⚠️ **Not:** Notebook'un kullandığı `Superlig_Proje.xlsx` veri dosyası bu klasörde bulunmamaktadır (eğitmenden temin edilebilir). Aynı iş akışının çalışır ve tekrarlanabilir hali için pratik klasörüne bakınız.

## ❓ Dersin Araştırma Sorusu

> Bir takımın attığı gol sayısı; xG (beklenen gol), şut, isabetli şut gibi istatistiklerden ne kadar iyi tahmin edilebilir? Tek özellik mi, çok özellik mi daha iyi çalışır?

## 📚 İçindekiler ve Öğretilen Kavramlar

1. **Veri yükleme ve keşif** — `read_excel`, veri tipleri, istatistiksel özet
2. **Veri temizliği** — string sütunlardaki görünmez non-breaking space (`\xa0`) karakterlerinin temizlenmesi
3. **Keşifçi Veri Analizi (EDA)** — korelasyon matrisi (heatmap), hedef değişkenle korelasyonların sıralanması, hedef dağılımı
4. **Basit doğrusal regresyon** — tek özellikle (xG) model kurma:
   - `train_test_split` ile eğitim/test ayrımı (%80/%20) ve bunun *neden şart olduğu*
   - `LinearRegression` ile model eğitme, katsayıların okunması
   - **R², MAE, RMSE** metrikleri ve anlamları
   - Regresyon doğrusu ve **artık (residual) grafiği**
5. **Çoklu doğrusal regresyon** — korelasyona dayalı **özellik seçimi**, çok özellikli model eğitimi
6. **Model karşılaştırması** — basit vs çoklu modelin test metrikleriyle yan yana değerlendirilmesi
7. **Özellik önem sırası** — katsayıların mutlak değerine göre sıralama ve ölçek uyarısı
8. **Sonuç ve yorumlar** — tüm modellerin özet tablosu

## 💡 Dersten Akılda Kalması Gerekenler

- Model, **görmediği veriyle** (test seti) değerlendirilmelidir; eğitim verisindeki başarı yanıltıcıdır
- R² tek başına yetmez: MAE/RMSE hatanın *gerçek birim cinsinden* büyüklüğünü söyler
- Daha fazla özellik genelde tahmini iyileştirir ama her özellik katkı vermez → özellik seçimi
- Farklı ölçekli özelliklerde ham katsayı büyüklüğü "önem" demek değildir

## 🔗 İlgili Pratik

Bu iş akışının Dünya Mutluluk veri setine uygulandığı pratik için:
👉 [`08-Coklu-Regresyon-Pratik-Mutluluk`](../08-Coklu-Regresyon-Pratik-Mutluluk) klasörüne bakabilirsiniz.
