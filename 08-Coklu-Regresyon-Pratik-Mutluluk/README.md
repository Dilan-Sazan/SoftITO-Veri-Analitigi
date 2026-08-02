# Çoklu Regresyon Pratiği: Mutluluğu Ne Tahmin Eder? 🌍📈

Bu klasör, **sklearn ile Basit ve Çoklu Regresyon** dersindeki iş akışının kendi veri setime uygulandığı kişisel pratik çalışmamı içerir. Derste Süper Lig verisiyle "atılan gol" tahmin edilmişti; burada aynı adımlarla ülkelerin **mutluluk skorunu** tahmin ediyorum.

Bu pratiğin güzel yanı: kullandığım veri, [`04-Pandas-Pratik-Dunya-Mutluluk`](../04-Pandas-Pratik-Dunya-Mutluluk) klasöründeki **veri temizleme pratiğimin çıktısı**. Yani repo içinde gerçek bir analist iş akışı zinciri oluştu: *temizle → keşfet → modelle*. 🔗

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `mutluluk_coklu_regresyon_pratik.ipynb` | Basit + çoklu regresyonun uçtan uca uygulandığı pratik notebook (tüm çıktı ve grafiklerle) |
| `mutluluk_2015_2019_temiz.csv` | Girdi verisi: 04. klasördeki temizleme pratiğinin çıktısı (782 satır, 2015–2019) |

📱 **Colab/Drive uyumu:** Notebook'un başında hazır bir "veri yolu" hücresi var — Google Colab'da çalışıyorsan üç satırın yorumunu kaldırıp Drive klasörünü yazman yeterli.

## ❓ Araştırma Sorusu

> Bir ülkenin mutluluk skorunu; GSYH, sosyal destek, sağlık, özgürlük ve yolsuzluk algısı ne kadar iyi tahmin eder? Tek başına para (GSYH) mı, yoksa faktörlerin birleşimi mi daha güçlü?

## 🛠️ Uygulanan Adımlar (Dersle Birebir)

| Adım | Detay |
|---|---|
| Veri yükleme + sağlık kontrolü | Temiz veri doğrulandı (0 eksik değer) |
| Korelasyon matrisi (heatmap) | Skor ile en güçlü ilişkiler: GSYH, sağlık, sosyal destek |
| ⚠️ Veri sızıntısı önlemi | `Sira` sütunu hedeften türetildiği için modele **alınmadı** |
| Basit regresyon (GSYH → Skor) | `train_test_split` (%80/%20) + `LinearRegression` |
| Metrikler | R², MAE, RMSE — hepsi test seti üzerinde |
| Görselleştirme | Regresyon doğrusu, artık grafiği, gerçek-vs-tahmin grafiği |
| Özellik seçimi | Korelasyonu > 0.35 olan 5 özellik seçildi (Cömertlik elendi) |
| Çoklu regresyon | 5 özellikli model eğitildi ve karşılaştırıldı |
| Özellik önem sırası | Katsayı büyüklükleri + ölçek uyarısı |

## 📌 Sonuçlar

| Model | Test R² | MAE | RMSE |
|---|---|---|---|
| Basit (sadece GSYH) | 0.619 | 0.549 | 0.681 |
| **Çoklu (5 özellik)** | **0.721** | **0.448** | **0.583** |

- Çoklu model, basit modele göre R²'yi **%16.5 iyileştirdi**; ortalama tahmin hatası 0.55 puandan 0.45 puana düştü
- GSYH tek başına mutluluğun ~%62'sini açıklıyor — para önemli, ama sosyal destek, sağlık ve özgürlük eklenince tablo belirgin şekilde netleşiyor
- Ham katsayılara göre Özgürlük ve Yolsuzluk Algısı en üstte görünüyor; ancak bu değişkenlerin ölçeği dar olduğundan katsayıları şişkin çıkar — **ölçekleme yapılmadan kesin önem sıralaması iddia edilemez** (dersteki ölçek uyarısının canlı örneği!)

## 🎯 Sonraki Adım Fikirleri

`StandardScaler` ile özellik ölçekleme, polinom özellikler, yıl bazlı çapraz doğrulama.

## 🔗 İlgili Ders

Bu pratiğin dayandığı ders notebook'u için:
👉 [`07-Coklu-Regresyon-Ders`](../07-Coklu-Regresyon-Ders) klasörüne bakabilirsiniz.
