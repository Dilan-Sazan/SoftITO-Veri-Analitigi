# Çoklu Regresyon Pratiği: Mutluluğu Ne Tahmin Eder? 🌍📈

Bu klasör, **sklearn ile Basit ve Çoklu Regresyon** dersindeki iş akışının kendi veri setime uygulandığı kişisel pratik çalışmamı içerir. Derste Süper Lig verisiyle "atılan gol" tahmin edilmişti; burada aynı adımlarla ülkelerin **mutluluk skorunu** tahmin ediyorum.

Bu pratiğin güzel yanı: kullandığım veri, [`02-Pandas-Dunya-Mutluluk`](../02-Pandas-Dunya-Mutluluk) klasöründeki **veri temizleme pratiğimin çıktısı**. Yani repo içinde gerçek bir analist iş akışı zinciri oluştu: *temizle → keşfet → modelle*. 🔗

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

---

## 📓 Notebook Adım Adım — `mutluluk_coklu_regresyon_pratik.ipynb`

Notebook'un kendisinde yalnızca kod bulunur; her adımın açıklaması burada.

#### 0. Kurulum ve Veri Yolu (Colab/Drive Uyumlu)

Aşağıdaki hücre hem bilgisayarda hem Google Colab'da çalışır. **Colab + Drive kullanıyorsan**
ilk üç satırın yorumunu kaldırıp `VERI_KLASORU`'nu dosyanın Drive'daki konumuna göre düzenle.

#### 1. Veriyi Yükleme ve Keşif

#### 2. Keşifçi Veri Analizi (EDA)

Dersteki gibi önce **korelasyon matrisi** ile değişkenler arası ilişkilere bakıyoruz.
Hedef değişkenimiz: `Skor` (mutluluk skoru).

**EDA'dan çıkanlar:** Skor ile en güçlü ilişkiler GSYH, sağlık ve sosyal destekte;
cömertlik ise şaşırtıcı şekilde zayıf. Skor dağılımı 5.4 civarında toplanmış, yaklaşık simetrik.

#### 3. Basit Doğrusal Regresyon: GSYH → Skor

Dersteki "xG → Atılan Gol" adımının karşılığı: en yüksek korelasyonlu tek özellikle başlıyoruz.

GSYH tek başına fena değil ama artıklar hâlâ ±1.5 puan bandında dağılıyor — mutlulukta
paranın açıklayamadığı ciddi bir kısım var. Çoklu regresyonun tam zamanı.

#### 4. Çoklu Doğrusal Regresyon

##### 4.1 Özellik Seçimi

Dersteki mantıkla: hedefle korelasyonu güçlü özellikleri seçiyoruz. Cömertlik'in korelasyonu
çok zayıf olduğu için modele katmıyoruz.

##### 4.2 İki Modelin Karşılaştırılması

##### 4.3 Özellik Önem Sırası

Dersteki gibi katsayıların mutlak değerine göre sıralıyoruz.

⚠️ Ama derste değinilen inceliği unutmuyoruz: özellikler farklı ölçeklerde olduğu için ham katsayı
büyüklüğü tek başına "önem" demek değildir. Yine de tüm özelliklerimiz 0-2 aralığında benzer
ölçekli endeksler olduğundan burada kabaca yorumlanabilir.

#### 5. Sonuç ve Yorumlar

#### Özet — Bu Pratikte Öğrendiklerim

1. **Temiz veri → model** zinciri kuruldu: 04. klasördeki temizleme çıktısı burada girdi oldu
2. **Korelasyon matrisi** ile özellik-hedef ilişkileri keşfedildi; `Sira` gibi hedeften türetilmiş
   sütunun modele konmaması gerektiği (veri sızıntısı) öğrenildi
3. sklearn ile **train/test ayrımı** yapıldı — modelin görmediği veriyle test edilmesinin önemi
4. **Basit regresyon** (GSYH → Skor) kuruldu, R²/MAE/RMSE metrikleriyle ölçüldü
5. **Çoklu regresyon** ile 5 özellik birlikte kullanıldı → tahmin gücü belirgin arttı
6. **Özellik önem sırası** çıkarıldı: ham katsayıya göre Özgürlük ve Yolsuzluk Algısı en üstte görünüyor —
   ama dikkat: bu iki değişkenin değer aralığı diğerlerinden dar olduğu için katsayıları "şişkin" çıkar.
   Ölçekleme (StandardScaler) yapılmadan kesin bir önem sıralaması iddia edilemez — bu, dersteki
   ölçek uyarısının kendi verimde karşıma çıkmış hali!
7. Colab/Drive uyumlu **taşınabilir veri yolu** hücresi eklendi

**Sonraki adımlar için fikirler:** özellik ölçekleme (StandardScaler) ile katsayıları adil karşılaştırmak,
polinom özellikler denemek, yıl bazlı çapraz doğrulama.
