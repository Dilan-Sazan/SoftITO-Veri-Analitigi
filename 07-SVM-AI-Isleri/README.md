# SVM Pratiği: Global AI İş İlanlarında Tecrübe Seviyesi Tahmini 💼

Bu klasör, **SVM** dersindeki iş akışının kendi veri setime uygulandığı kişisel pratik çalışmamı içerir. Derste Hindistan iş piyasası verisi kullanılmıştı; burada **90.000 ilanlık küresel yapay zekâ işleri** veri setiyle aynı problemi çözdüm: bir ilanın aradığı tecrübe seviyesini (Entry / Mid / Senior / Lead) ilan özelliklerinden tahmin etmek.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `svm_pratik.ipynb` | Uçtan uca pratik: sızıntı tespiti → örneklem → 3 kernel → GridSearch (tüm çıktılarla) |
| `global_ai_jobs.csv` | Küresel AI iş ilanları (90.000 satır, 35 sütun: maaş, ülke, rol, şirket bilgileri...) |

📱 **Colab/Drive uyumu:** Notebook'un başındaki hazır hücrede üç satırın yorumunu kaldırıp Drive klasör yolunu yazman yeterli.

## ⭐ Bu Pratiğin İki Kritik Anı

### 1. Veri Sızıntısı Yakalandı
Veri setinde `experience_years` sütunu, hedef olan `experience_level`'ı **birebir belirliyordu** (Entry: 0-1 yıl, Mid: 2-5, Senior: 6-11, Lead: 12-19 — aralıklar hiç örtüşmüyor). Bu sütun modele girseydi model %100 başarı gösterir ama hiçbir şey öğrenmemiş olurdu. Groupby tablosuyla tespit edilip **dışlandı** — 04. pratikteki `Sira` dersinin devamı niteliğinde.

### 2. SVM'in Ölçek Sınırı Yaşandı
SVM'in eğitim süresi örnek sayısıyla karesel-kübik büyüdüğü için 90.000 satır + GridSearchCV pratik değil. Çözüm: sınıf oranlarını koruyan **katmanlı örneklem** (`groupby().sample()`, 8.000 satır). Gerçek projede alternatiflerin (LinearSVC, SGDClassifier) ne zaman devreye gireceği de notebook'ta tartışıldı.

## 📌 Sonuçlar

| Kernel (varsayılan ayarlar) | Test Doğruluğu |
|---|---|
| **linear** | **0.859** |
| rbf | 0.830 |
| poly | 0.762 |

*(4 dengeli sınıfta rastgele tahmin taban çizgisi: 0.25)*

- GridSearchCV (kernel + C + gamma taraması) da kazanan olarak **linear kernel'i** seçti → Test doğruluğu **%85.9**
- ⭐ **"Karmaşık olan her zaman kazanmaz":** RBF ve polinom kernel'ler doğrusala yenildi — sınıflar büyük ölçüde maaş ekseninde doğrusal ayrılabiliyor. Kernel seçimi varsayımla değil denemeyle yapılır
- Entry sınıfı neredeyse kusursuz tahmin edildi (F1 = 0.98); hatalar **komşu seviyelerde** yoğunlaştı (Senior↔Lead, Senior↔Mid) — modelin hataları bile problemin doğasını yansıtıyor
- Seviye yükseldikçe ortalama maaş merdiven gibi artıyor (62k → 77k → 105k → 143k USD) — modelin ana sinyali

## 🛠️ Uygulanan Yöntemler

Sızıntı analizi (groupby ile) • katmanlı örneklem • `get_dummies` ile one-hot kodlama • stratified train/test • StandardScaler (fit yalnızca eğitimde) • 3 kernel karşılaştırması • GridSearchCV (3-fold) • 4×4 karmaşıklık matrisi • classification_report

## 🎯 Sonraki Adım Fikirleri

LinearSVC ile 90 bin satırın tamamını kullanmak; RandomForest ile karşılaştırıp özellik önemlerini görmek.

---

## 📓 Notebook Adım Adım — `svm_pratik.ipynb`

Notebook'un kendisinde yalnızca kod bulunur; her adımın açıklaması burada.

#### 0. Veri Yolu (Colab/Drive Uyumlu)

**Google Colab + Drive kullanıyorsan** ilk üç satırın başındaki `#` işaretlerini kaldır ve
`VERI_KLASORU`'nu csv dosyasını koyduğun Drive klasörüne göre düzenle.

#### 1. Veri Setini Keşfetme

#### 2. ⭐ Veri Sızıntısı Tespiti

Modele özellik seçmeden önce şüpheli bir sütunu kontrol edelim: `experience_years`.
Tecrübe *seviyesi*ni tahmin ederken tecrübe *yılını* kullanmak mantıklı mı?

**Tuzak ortaya çıktı:** Yıl aralıkları hiç örtüşmüyor — Entry: 0-1, Mid: 2-5, Senior: 6-11,
Lead: 12-19. Yani `experience_level` doğrudan `experience_years`'tan **türetilmiş**. Bu sütunu
modele koyarsak model hiçbir örüntü öğrenmez, cevabı kopya çeker ve %100 başarıyla bizi kandırır.
Buna **veri sızıntısı (data leakage)** denir — 08. pratikte `Sira` sütununu dışlamıştık, aynı ilke.

`experience_years`'ı (ve bilgi taşımayan `id` ile `year`'ı) özellik listesinden **çıkarıyoruz**.
Model, seviyeyi ilanın *diğer* özelliklerinden (maaş, mülakat turu, şirket bilgileri...) öğrenmek
zorunda kalacak — gerçek ve dürüst bir tahmin problemi.

#### 3. ⭐ SVM'in Ölçeklenme Sınırı ve Örneklem

SVM'in eğitim süresi örnek sayısıyla **karesel-kübik** büyür; 90.000 satır + GridSearchCV
saatler sürer. Gerçek hayatta bu durumda ya LinearSVC/SGD gibi ölçeklenebilir alternatifler
kullanılır ya da **katmanlı (stratified) örneklem** alınır. Biz dersle aynı araçları (SVC +
GridSearchCV) kullanabilmek için ikinci yolu seçiyoruz: sınıf oranlarını koruyan 8.000 satırlık örneklem.

#### 4. Veri Ön İşleme

Dersteki sırayla: kategorik kodlama → özellik/hedef ayrımı → train/test → ölçekleme.

#### 5. Üç Kernel ile SVM (Dersteki Karşılaştırma)

Doğrusal, RBF ve polinom kernel'lerini varsayılan ayarlarla eğitip karşılaştırıyoruz.

#### 6. GridSearchCV ile Hiperparametre Optimizasyonu

Dersteki gibi C/gamma taraması — ama kernel seçimini de aramaya dahil ediyoruz, çünkü ilk denemede
linear kernel'in RBF'i geçmesi "acaba?" dedirtti. Karar veriye bırakılır, varsayıma değil.

**Matrisin okunması:** Hatalar rastgele dağılmıyor — model en çok **komşu seviyeleri**
karıştırıyor (Mid↔Senior gibi). Bu mantıklı: bir Mid ilanıyla Senior ilanının maaş/koşul profilleri
birbirine yakınken, Entry ile Lead'i ayırt etmek çok daha kolay. Modelin hataları bile problemin
doğasını yansıtıyor.

#### 7. Hangi Özellikler İşe Yaradı? (Basit Kontrol)

SVM (RBF kernel) katsayı vermez; ama en güçlü sinyalin maaş olduğunu basit bir tabloyla doğrulayabiliriz.

#### 8. Özet — Bu Pratikte Öğrendiklerim

1. ⭐ **Veri sızıntısı yakalandı:** `experience_years` hedefi birebir belirliyordu → dışlandı.
   Sızıntılı model %100 başarı gösterip hiçbir şey öğrenmemiş olurdu
2. ⭐ **SVM'in ölçek sınırı yaşandı:** 90 bin satır SVC + GridSearch için pratik değil →
   sınıf oranlarını koruyan katmanlı örneklemle (8.000) çalışıldı; alternatiflerin
   (LinearSVC, SGDClassifier) ne zaman gerektiği öğrenildi
3. **Üç kernel karşılaştırıldı** — dengeli 4 sınıflı problemde taban çizgisi %25'ti,
   modeller bunun çok üzerine çıktı
4. **GridSearchCV** ile C/gamma taraması yapıldı (dersteki akışın aynısı)
5. ⭐ **"Karmaşık olan her zaman kazanmaz":** linear kernel, RBF ve polinomu geçti — sınıflar
   büyük ölçüde (maaş ekseninde) doğrusal ayrılabiliyor; kernel seçimi denenerek yapılır
6. **Karmaşıklık matrisi yorumlandı:** hatalar komşu seviyeler arasında yoğunlaştı (özellikle
   Senior↔Lead ve Senior↔Mid) — modelin hataları bile anlamlı
7. Kategorik kodlama (`get_dummies`) + ölçekleme + stratify artık standart refleks

**Sonraki adım fikirleri:** LinearSVC ile 90 bin satırın tamamını kullanmak, RandomForest ile
karşılaştırıp özellik önemlerini görmek.
