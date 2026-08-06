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
