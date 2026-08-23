# Random Forest Pratiği: Elmas Fiyatı ve Kesim Kalitesi 💎

Bu klasör, **Random Forest** dersindeki iş akışının bir veri setine uygulandığı kişisel pratik çalışmamı içerir. Derste tek bir veri seti üzerinde hem regresyon hem sınıflandırma yapılmıştı; burada aynı ikili yapıyı **53.940 elmasın** özellikleriyle kuruyorum.

## ❓ Araştırma Soruları

> 🎯 **Regresyon:** Bir elmasın fiyatı fiziksel özelliklerinden tahmin edilebilir mi? Fiyatı asıl ne belirliyor?
>
> 🏷️ **Sınıflandırma:** Elmasın kesim kalitesi (Fair → Ideal, 5 seviye) ölçülerinden tahmin edilebilir mi?

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `random_forest_pratik_elmas.ipynb` | Uçtan uca pratik: EDA → ön işleme → regresyon → GridSearch → sınıflandırma → CV |
| `diamonds.csv` | Elmas veri seti (53.940 satır, 10 sütun) |

## 📊 Veri Seti Hakkında

Her satır bir elmas: ağırlık (karat), kesim kalitesi, renk, berraklık, oransal ölçüler (depth, table), fiziksel boyutlar (x, y, z) ve fiyat.

Veri "temiz" görünüyor (`isnull()` sıfır döndürüyor) ama `describe()` iki sessiz sorunu ortaya çıkarıyor:
- `x`, `y`, `z` minimumları **0** — bir elmasın boyutu sıfır olamaz
- `y` maksimumu **58.9 mm**, `z` maksimumu **31.8 mm** — en uzun elmas 10.7 mm iken bunlar açık veri giriş hatası

## 📌 Sonuçlar

| Görev | Metrik | Test Skoru | 5-Fold Ortalama |
|---|---|---|---|
| Regresyon (`price`) | R² | **0.982** | 0.976 |
| Sınıflandırma (`cut`) | Doğruluk | **0.787** | 0.749 |

Regresyonda ortalama hata (MAE) sadece **264 USD** — ortalama elmas fiyatının ~3.900 USD olduğu düşünülürse oldukça iyi. Sınıflandırmada taban çizgisi %40'tı (hep "Ideal" demek), model bunu belirgin şekilde geçti.

### 💡 Öne Çıkan Bulgular

**Fiyatı belirleyen şey büyüklük.** Özellik önemlerine göre karat tek başına %59, fiziksel boyut (y) %30 pay alıyor. Berraklık %6, renk %3... **Kesim kalitesinin katkısı ise binde 2** — yani elmasın fiyatına neredeyse hiç etkisi yok.

**Kesim kalitesini belirleyen şey oranlar.** Sınıflandırma modelinde `depth` (%36) ve `table` (%17) başı çekiyor — çok mantıklı, çünkü kesim derecesi tam olarak taşın oranlarıyla tanımlanan bir ölçüt. Fiyat ve karat bu görevde neredeyse işe yaramıyor.

**😲 Karıştırıcı değişken (confounding) tuzağı:** EDA'da en iyi kesim olan *Ideal* elmasların ortalama fiyatının en **düşük** olduğu ortaya çıktı! Sebep: Ideal elmaslar ortalama olarak daha küçük. Büyük taşlar, ağırlıktan kaybetmemek için daha düşük kesim kalitesiyle işleniyor. İki değişken arasındaki ham ilişki, üçüncü bir değişken yüzünden tersine dönebiliyor.

**Sınıf bazlı zorluk:** *Fair* (F1 = 0.89) ve *Ideal* (0.87) kolay ayırt ediliyor; en zoru **Very Good** (0.61) — iki komşusu arasında sıkışmış bir orta kategori. Hatalar hep komşu kalite seviyelerinde yoğunlaşıyor.

## 🛠️ Uygulanan Yöntemler

| Adım | Detay |
|---|---|
| Veri temizliği | 146 duplicate + fiziksel olarak imkânsız boyutlu satırlar silindi |
| Kategorik kodlama | `color` ve `clarity` **sıralı (ordinal)** değişkenler → sıralamayı koruyan kodlama (one-hot yapılsaydı "D, E'den iyidir" bilgisi kaybolurdu) |
| Regresyon | `RandomForestRegressor`, R²/MAE/RMSE, gerçek-vs-tahmin grafiği, özellik önemleri |
| Hiperparametre | `GridSearchCV` (8 kombinasyon, 3-fold) |
| ⚠️ Sızıntı önlemi | Grid arama örneklemi **yalnızca eğitim setinden** alındı; tüm veriden alınsaydı test satırları karışır ve skor haksız yere şişerdi |
| Sınıflandırma | `RandomForestClassifier` + `class_weight="balanced"` (Ideal 21bin, Fair 1.6bin — dengesiz) |
| Doğrulama | Her iki görev için 5-fold cross validation |

## 🌲 Random Forest'ın Bu Pratikte Görülen Avantajları

1. **Doğrusal olmayan ilişkileri kendiliğinden yakalar** — karat/fiyat eğrisi için polinom terimi eklemeye gerek kalmadı ([`05`](../05-Polinom-Regresyon-Ogrenci) pratiğinde gerekmişti)
2. **Ölçekleme istemez** — StandardScaler adımı yok ([`06`](../06-Lojistik-Regresyon-Diyabet) ve [`07`](../07-SVM-AI-Isleri) pratiklerinde şarttı)
3. **Aynı algoritma iki farklı görevi** çözebiliyor
4. **Özellik önemi** verir → model sadece tahmin etmiyor, *açıklıyor*

**Dezavantajı:** Tek bir karar ağacı gibi görselleştirilip okunamaz; yorumlanabilirlik özellik önemleriyle sınırlı.
