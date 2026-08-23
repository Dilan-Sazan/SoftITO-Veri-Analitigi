# Isolation Forest Pratiği: Kredi Kartı Dolandırıcılığı Tespiti 🌲🔍

Bu klasör, **Isolation Forest — Anomali Tespiti** dersindeki iş akışının gerçek bir veri setine uygulandığı kişisel pratik çalışmamı içerir. Derste algoritma yapay (sentetik) veri üzerinde anlatılmıştı; burada anomali tespitinin en klasik gerçek dünya problemini çözüyorum: **kredi kartı dolandırıcılığı**.

## ❓ Araştırma Sorusu

> Hiç etiket görmeden, yalnızca "sıra dışılık" ölçerek dolandırıcılık işlemlerini yakalayabilir miyiz? 60.000 işlemin içinde saklı 104 sahte işlemi bulabilir mi?

Bu, önceki sınıflandırma pratiklerinden temel bir farkla ayrılıyor: model **denetimsiz (unsupervised)** çalışıyor. Eğitim sırasında `Class` etiketi hiç kullanılmıyor — etiketler yalnızca sonuçları *değerlendirmek* için var.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `isolation_forest_pratik_dolandiricilik.ipynb` | Uçtan uca pratik: EDA → model → skorlar → contamination taraması → algoritma karşılaştırması |
| `creditcard_ornek.csv.gz` | Veri seti (60.000 işlem, sıkıştırılmış ~9 MB) |

## 📊 Veri Seti Hakkında

Avrupalı kart sahiplerinin 2013 Eylül'ünde iki gün içinde yaptığı işlemler — anomali tespiti literatürünün standart karşılaştırma veri seti. Orijinali 284.807 işlem ve 98 MB; repoya sığması için **doğal dolandırıcılık oranını koruyan** 60.000 işlemlik katmanlı örneklem alındı.

- 60.000 işlem, bunların **104'ü dolandırıcılık (%0.173)** → yaklaşık her 577 işlemde 1 sahte
- `V1`–`V28`: gizlilik nedeniyle PCA ile dönüştürülmüş özellikler (ham anlamları açıklanmıyor)
- `Time`, `Amount`: dönüştürülmemiş tek iki sütun
- `Class`: 1 = dolandırıcılık (yalnızca değerlendirme için)

## 📌 Sonuçlar

Model, hiç etiket görmeden test setindeki 30 işlemi anomali olarak işaretledi (gerçekte 31 dolandırıcılık vardı):

| Metrik | Değer |
|---|---|
| ROC-AUC | **0.921** |
| PR-AUC | **0.239** |
| Precision | 0.333 |
| Recall | 0.323 |

**ROC-AUC 0.92 dikkate değer:** model, rastgele seçilen bir sahte işlemi rastgele seçilen normal bir işlemden %92 olasılıkla daha anormal buluyor — hiçbir örnek görmeden. PR-AUC 0.239 ise düşük görünse de, rastgele bir modelin PR-AUC'si veri oranına eşit olurdu: **0.0017**. Yani model rastgeleden ~140 kat iyi.

### ⭐ Contamination Parametresinin Etkisi

Dersin en önemli parametresi. Modele "verinin yüzde kaçı anomalidir" diye söylüyoruz ve bu doğrudan precision-recall dengesini belirliyor:

| contamination | İşaretlenen | Precision | Recall |
|---|---|---|---|
| 0.0005 | 7 | 0.43 | 0.10 |
| **0.0017** (gerçek oran) | 30 | 0.33 | **0.32** |
| 0.005 | 108 | 0.14 | 0.48 |
| 0.05 | 887 | 0.03 | **0.87** |

Contamination büyüdükçe model daha çok işlemi şüpheli sayıyor: **yakalama (recall) yükseliyor ama kesinlik (precision) çöküyor.** %5'e çıkarıldığında dolandırıcılığın %87'si yakalanıyor, ama 887 işlem incelemeye gidiyor ve bunların yalnızca 27'si gerçek. Doğru değer teknik değil, **iş kararıdır**: bir inceleme ekibi günde kaç uyarıyı kaldırabilir?

### ⚖️ Algoritma Karşılaştırması

| Model | Eğitim örneği | Süre | Precision | Recall | F1 |
|---|---|---|---|---|---|
| Isolation Forest | 42.000 | 0.87 sn | 0.33 | 0.32 | 0.33 |
| One-Class SVM | 5.000 | 0.37 sn | 0.03 | **0.90** | 0.06 |
| Local Outlier Factor | 5.000 | 0.62 sn | **0.48** | 0.42 | **0.45** |

Bu tabloda üç ders var:

1. **Ölçeklenebilirlik:** Isolation Forest 42.000 satırın tamamıyla eğitilebildi; One-Class SVM ve LOF için 5.000'lik alt örneklem gerekti (OCSVM örnek sayısıyla karesel büyür — [`07`](../07-SVM-AI-Isleri) pratiğinde de aynı sınıra çarpmıştık).
2. **One-Class SVM aşırı hassas:** dolandırıcılığın %90'ını yakalıyor ama binlerce yanlış alarm üretiyor — precision %3.
3. **En iyi F1'i LOF verdi** — yani "en popüler algoritma her zaman en iyisi değil". Küçük veride LOF rekabetçi; veri büyüdükçe Isolation Forest'ın hız avantajı belirleyici hale gelir.

### 🔎 En Şüpheli 10 İşlem

Modelin en yüksek anomali skoru verdiği 10 işlemin **4'ü gerçekten dolandırıcılık** çıktı. İlginç detay: en şüpheli bulunan işlemin tutarı sadece **0.01 USD** — dolandırıcıların kartın çalışıp çalışmadığını sınamak için yaptığı klasik "test işlemi" deseni.

## 🛠️ Uygulanan Yöntemler

Denetimsiz öğrenme kurgusu • `Time` sütununun dışlanması (mutlak zaman damgası anomali sinyali taşımaz) • StandardScaler (fit yalnızca eğitimde) • `IsolationForest` (200 ağaç, max_samples=256) • `decision_function` ile sürekli anomali skoru • ROC-AUC ve PR-AUC (dengesiz veride PR-AUC'nin neden daha bilgilendirici olduğu) • skor dağılımı ve kutu grafiği • PCA ile 2B görselleştirme (gerçek etiketler vs modelin tespitleri yan yana) • contamination taraması • üç algoritmanın karşılaştırması

## 💡 Öğrenmeler

- **Denetimsiz de iş görür:** hiç etiket olmadan ROC-AUC 0.92 — yeni dolandırıcılık türleri için etiketli veri beklemek zorunda kalmazsın
- **Dengesiz veride accuracy anlamsız:** %99.8 doğruluk çıkardı ama hiçbir şey ifade etmezdi; bu yüzden hiç raporlamadım ([`06`](../06-Lojistik-Regresyon-Diyabet) pratiğindeki doğruluk yanılsaması dersinin devamı)
- **contamination bir iş kararıdır**, teknik bir ayar değil
- **Anomali ≠ dolandırıcılık:** model "sıra dışı"yı bulur; bunun kötü niyetli olup olmadığına insan karar verir. İşaretlenen işlemlerin çoğu meşru ama alışılmadık harcamalardı
