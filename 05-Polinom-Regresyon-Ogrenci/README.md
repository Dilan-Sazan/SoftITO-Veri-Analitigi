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

---

## 📓 Notebook Adım Adım — `polinom_regresyon_pratik.ipynb`

Notebook'un kendisinde yalnızca kod bulunur; her adımın açıklaması burada.

#### 0. Veri Yolu (Colab/Drive Uyumlu)

**Google Colab + Drive kullanıyorsan** ilk üç satırın başındaki `#` işaretlerini kaldır ve
`VERI_KLASORU`'nu csv dosyasını koyduğun Drive klasörüne göre düzenle.

#### 1. 📦 Kütüphaneler

#### 2. 🗂️ Veri Yükleme ve İlk İnceleme

**describe() tablosu daha ilk bakışta üç alarm veriyor:**
- `Study_Hours` min = **-2** → negatif çalışma saati imkânsız! (mantıksal hata)
- `Study_Hours` max = **25** → günde 25 saat de imkânsız (gün 24 saat 😄)
- `Attendance(%)` max = **%115.6** → devam yüzdesi 100'ü aşamaz

Ayrıca eksik değerler var: `Study_Hours` (31), `Attendance(%)` (30), `Grade` (9).

#### 3. 🔧 Veri Ön İşleme

Dersteki sırayla: duplicate → eksik değer → mantıksal hata → IQR aykırı değer analizi.

⚠️ **Kritik karar — derste vurgulanan nokta:** IQR bu yüksek saatleri (≈11+ saat) "aykırı"
işaretledi ama **her aykırı değer hata değildir!** Günde 12-20 saat çalışan öğrenci az ama mümkün;
üstelik describe ve EDA bu öğrencilerin notlarının *düştüğünü* gösteriyor — yani bu gözlemler tam da
yakalamak istediğimiz tükenmişlik sinyalini taşıyor. İmkânsız değerleri zaten sildik; **geçerli uç
değerleri veri setinde tutuyoruz.** (Silseydik parabolün sağ kolunu kendi elimizle koparmış olurduk!)

#### 4. 📊 Keşifsel Veri Analizi (EDA)

**Sağdaki grafik her şeyi anlatıyor:** ilişki net biçimde **ters-U şeklinde** — notlar ~10 saat
civarında zirve yapıyor, sonrasında düşüyor. Düz bir doğru bu deseni asla yakalayamaz.
İşte polinom regresyonun tam kullanım yeri (dersteki "ne zaman kullanılır?" sorusunun cevabı).

#### 5. 🤖 Polinom Regresyon Modeli

##### 5.1 Train-Test Ayrımı

##### 5.2 PolynomialFeatures Ne Yapıyor? (Somut Örnek)

##### 5.3 Farklı Derecelerde Model Eğitimi (1'den 5'e)

**Grafiğin hikayesi:** Derece 1 (kırmızı doğru) ters-U'yu tamamen ıskalıyor. Derece 2 (yeşil)
zirveyi ve düşüşü yakalıyor; derece 3 ise eğrinin **asimetrisini** (yavaş yükseliş, dik düşüş) biraz
daha iyi takip ediyor. 4 ve 5. dereceler ise eğriyi neredeyse hiç değiştirmiyor — ekstra karmaşıklık
bir şey kazandırmıyor. **Bias-variance dengesinin** görsel hali!

#### 6. 📉 K-Fold Cross-Validation ile Derece Seçimi

Tek bir train/test ayrımı şansa bağlı olabilir. Dersteki gibi 5 katlı çapraz doğrulamayla
her derecenin *ortalama* performansına bakıyoruz.

#### 7. 🏆 En İyi Modelin Detaylı Analizi

⚠️ **Dikkat — modelin sınırı burada görünüyor:** Tepe noktasındaki tahmin **100'ü aşıyor** (116.3),
oysa sınav notu en fazla 100 olabilir! Bunun sebebi: 12-16 saat aralığında gözlem sayısı az ve polinom
eğrileri veri seyrekleştiğinde **uçlarda taşkın davranır** — dersteki "dezavantajlar" listesindeki
uyarının ta kendisi. Bu yüzden bir sonraki bölümdeki tahmin fonksiyonuna `np.clip(tahmin, 0, 100)`
güvenlik sınırı ekledik. Model, *desenin şeklini* (yükseliş → zirve → düşüş) doğru yakalıyor; ama uç
bölgelerdeki *mutlak değerlerine* körü körüne güvenilmemeli.

#### 8. 🎯 İnteraktif Tahmin Fonksiyonu

Dersteki gibi, modeli pratik bir fonksiyona sarıyoruz.

#### 9. 📝 Özet ve Sonuçlar

##### Bulgular

1. **İlişki doğrusal değil:** Çalışma saati ile not arasında net bir **ters-U** ilişkisi var —
   "daha çok çalışmak her zaman daha iyi" varsayımı ~10 saat civarında kırılıyor (tükenmişlik etkisi)
2. **Derece 3 kazandı:** CV'nin en yüksek ortalama R²'si 3. derecede (0.744) — ters-U simetrik
   olmadığı için (yavaş yükseliş, dik düşüş) kübik terim işe yaradı. Derece 4 ve 5 pratikte aynı
   performansı verdi → eşit başarıda *en basit model tercih edilir* ilkesiyle 3 seçildi
3. **Polinom, doğrusala açık fark attı** — doğrusal model ters-U'nun düşen kolunu tamamen ıskalıyordu
4. **Model yorumlanabilir bir içgörü üretti:** eğri, nottaki getirinin ~14 saat civarında zirve
   yapıp düşüşe geçtiğini söylüyor — ama zirvedeki tahmin 100'ü aştığı için (uçlarda taşma sorunu)
   bu bölgedeki sayılara temkinli yaklaşmak gerektiğini de öğrenmiş olduk

##### Ön İşlemede Verilen Kararlar (ve nedenleri)

| Sorun | Karar | Neden |
|---|---|---|
| 20 duplicate satır | Silindi | Aynı öğrencinin tekrarı modeli yanıltır |
| Study_Hours eksik (31) | Satır silindi | x-y ilişkisi öğrenilirken x uydurulmaz |
| Attendance eksik (30) | Medyanla dolduruldu | Modelde kullanılmıyor, tabloyu tam tutmak için |
| Saat < 0 veya > 24 | Silindi | Fiziksel olarak imkânsız |
| Devam > %100 | 100'e kırpıldı | Ölçüm hatası varsayımı |
| IQR aykırıları (11+ saat) | **Tutuldu** | Geçerli uç değerler; parabolün sağ kolunun kanıtı! |

##### Dersle Bağlantı

Bias-variance dengesi, PolynomialFeatures + Pipeline, K-Fold ile derece seçimi, "her aykırı değer
hata değildir" ilkesi — hepsi bu pratikte kendi verimde karşıma çıktı ve uygulandı. ✅
