# AdaBoost vs XGBoost: Gelir Tahmini 🔴🟢

Bu klasör, **AdaBoost vs XGBoost** dersindeki karşılaştırmanın gerçek bir veri setine uygulandığı kişisel pratik çalışmamı içerir. Derste sklearn'ün hazır Breast Cancer veri seti (569 satır) kullanılmıştı; burada **45.000 kişilik** bir nüfus sayımı verisiyle çalıştım — iki algoritmanın **hız farkını** görebilmek için veri boyutu önemliydi.

## ❓ Araştırma Sorusu

> Bir kişinin yıllık gelirinin 50.000 doları aşıp aşmadığı; yaşı, eğitimi, mesleği, medeni durumu ve çalışma saatlerinden tahmin edilebilir mi? İki boosting algoritmasından hangisi daha iyi, hangisi daha hızlı?

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `adaboost_xgboost_pratik_gelir.ipynb` | Uçtan uca pratik: EDA → AdaBoost → XGBoost → karşılaştırma → CV → hız analizi |
| `adult_income.csv.gz` | Adult Income veri seti (48.842 kişi, sıkıştırılmış) |

## 📊 Veri Seti Hakkında

ABD nüfus sayımından türetilen, tablosal makine öğrenmesinin en klasik karşılaştırma veri setlerinden biri. 14 özellik: yaş, çalışma sınıfı, eğitim, medeni durum, meslek, ırk, cinsiyet, sermaye kazancı/kaybı, haftalık çalışma saati, ülke.

Veri "temiz" görünüyor (`isnull()` sıfır döndürüyor) ama eksik değerler **`?` karakteriyle gizlenmiş**: workclass'ta 2.799, occupation'da 2.809, native_country'de 857 kayıt. Temizlik sonrası 45.175 satır kaldı. `fnlwgt` (anket ağırlığı) sütunu, kişinin gelirini açıklamadığı için çıkarıldı.

## 📌 Sonuçlar

| Metrik | 🔴 AdaBoost | 🟢 XGBoost |
|---|---|---|
| Doğruluk | 0.849 | **0.865** |
| Recall (>50K) | 0.567 | **0.641** |
| F1 (>50K) | 0.651 | **0.702** |
| ROC-AUC (test) | 0.907 | **0.927** |
| ROC-AUC (5-fold) | 0.910 ± 0.002 | **0.928 ± 0.002** |
| Eğitim süresi | 5.27 sn | **1.18 sn** |

**XGBoost her kalemde kazandı** — hem daha doğru hem ~4.5 kat daha hızlı. 5-fold çapraz doğrulama da bunu doğruluyor (standart sapmalar çok küçük, fark gerçek).

### ⚡ Hız Farkı Veri Büyüdükçe Açılıyor

| Eğitim satırı | AdaBoost | XGBoost |
|---|---|---|
| 2.000 | 0.51 sn | 0.14 sn |
| 8.000 | 1.27 sn | 0.30 sn |
| 18.000 | 2.44 sn | 0.86 sn |
| 36.000 | 4.87 sn | 1.12 sn |

AdaBoost süresi veriyle neredeyse doğrusal artıyor; XGBoost çok daha yavaş büyüyor. Sebebi: AdaBoost ağaçları **sırayla ve tek tek** eğitir (her ağaç bir öncekinin hatalarına göre ağırlık günceller), XGBoost ise histogram tabanlı bölme ve paralelleştirme kullanır. Dersin "XGBoost büyük veri için tasarlandı" iddiası burada sayısal olarak görüldü.

### 🌳 İki Model Aynı Veriye Farklı Bakıyor

En önemli özellik sıralamaları çarpıcı biçimde farklı:

| Sıra | AdaBoost | XGBoost |
|---|---|---|
| 1 | `capital_gain` (0.226) | `marital_status_Married` (0.252) |
| 2 | `marital_status_Married` (0.151) | `marital_status_Never-married` (0.089) |
| 3 | `capital_loss` (0.144) | `relationship_Own-child` (0.055) |

AdaBoost **sermaye kazancını** öne çıkarıyor (derinlik-1 ağaçlar tek eşikle güçlü ayrım yapabilen sürekli değişkenleri sever), XGBoost ise **ilişki/medeni durum** değişkenlerine ağırlık veriyor (derin ağaçlar değişkenler arası etkileşimi yakalayabiliyor). Aynı veri, iki farklı hikâye — özellik önemi mutlak bir gerçek değil, **modele bağlı bir yorumdur.**

### 📈 Diğer Gözlemler

- **AdaBoost'ta ağaç sayısı eğrisi** düz bir plato çiziyor: en iyi test doğruluğu 192. ağaçta (0.8502) — 200 ağaç yeterli, daha fazlası boşuna
- **Dengesiz veri etkisi:** >50K sınıfı %25 ve iki model de bu sınıfta düşük recall veriyor (0.57 vs 0.64). XGBoost burada belirgin şekilde daha iyi — dolayısıyla asıl fark, azınlık sınıfını yakalamada
- **XGBoost eğitim eğrisi:** eğitim kaybı düşmeye devam ederken test kaybı düzleşiyor — hafif ezberleme başlangıcı; `early_stopping_rounds` ile kesilebilirdi

## 🛠️ Uygulanan Yöntemler

`?` ile gizlenmiş eksik değerlerin tespiti • duplicate temizliği • bilgi taşımayan sütunun çıkarılması • one-hot kodlama (95 özellik) • stratified train/test • `staged_score` ile AdaBoost öğrenme eğrisi (yeniden eğitmeden) • `eval_set` ile XGBoost eğitim eğrisi • karmaşıklık matrisleri • ROC eğrileri • 5-fold stratified CV • artan veri boyutunda süre ölçümü • iki modelin özellik önemi karşılaştırması

## 💡 Öğrenmeler

- **XGBoost'un popülerliği boşuna değil:** hem daha doğru hem çok daha hızlı — Kaggle yarışmalarında neden standart olduğu anlaşılıyor
- **AdaBoost hâlâ değerli:** çok az hiperparametresi var, ayarlaması kolay, küçük veride farkı kapanır
- **Hız farkı veri büyüdükçe belirginleşir** — küçük veride "hangisi daha hızlı" sorusu anlamsız
- **Özellik önemi modele göre değişir** — tek bir modelin önem sıralamasını mutlak gerçek sanmamak lazım
