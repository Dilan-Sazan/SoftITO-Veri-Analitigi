# Lojistik Regresyon Pratiği: Diyabet Riski Tahmini 🩺

Bu klasör, **Lojistik Regresyon** dersindeki iş akışının kendi veri setime uygulandığı kişisel pratik çalışmamı içerir. Derste kalp hastalığı verisi kullanılmıştı; burada CDC'nin BRFSS 2015 sağlık anketinden **253.680 kişilik** diyabet göstergeleri veri setiyle çalıştım — şu ana kadarki en büyük veri setim.

## ❓ Araştırma Sorusu

> Bir kişinin diyabet riski; tansiyon, kolesterol, BMI, yaş ve genel sağlık algısı gibi göstergelerden tahmin edilebilir mi? Ve **dengesiz** bir veri setinde (%16 riskli) model başarısı nasıl doğru ölçülür?

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `lojistik_regresyon_pratik.ipynb` | Uçtan uca pratik: keşif → ölçekleme → 2 model → metrik karşılaştırması (tüm çıktılarla) |
| `diabetes_012_health_indicators_BRFSS2015.csv` | CDC BRFSS 2015 anketi (253.680 kişi, 22 sağlık göstergesi) |

📱 **Colab/Drive uyumu:** Notebook'un başındaki hazır hücrede üç satırın yorumunu kaldırıp Drive klasör yolunu yazman yeterli.

## 🛠️ Verilen Kararlar (ve Gerekçeleri)

| Konu | Karar | Neden |
|---|---|---|
| 3 sınıflı hedef (0/1/2) | Prediyabet+diyabet birleştirilip **ikili** hedef yapıldı | Ders ikili sınıflandırma üzerineydi; prediyabet klinik bir risk durumu |
| ~24 bin duplicate satır | **Tutuldu** | ID'siz ankette aynı cevap profili meşrudur — her tekrar hata değildir |
| Train/test ayrımı | `stratify=y` ile yapıldı | Dengesiz veride sınıf oranları her iki sette korunmalı |
| Ölçekleme | Scaler yalnızca eğitime fit edildi | Data leakage önlemi (dersteki altın kural) |

## 📌 Ana Bulgu: Doğruluk Yanılsaması ⭐

Bu pratiğin kalbi burası. İki model kurup karşılaştırdım:

| Model | Accuracy | Recall (Riskli) | Precision (Riskli) | F1 |
|---|---|---|---|---|
| Standart LogisticRegression | **0.848** | 0.187 | 0.554 | 0.280 |
| `class_weight="balanced"` | 0.727 | **0.755** | 0.343 | 0.472 |

- Standart model **%85 doğrulukla** harika görünüyor — ama riskli hastaların **%81'ini kaçırıyor!** Veri setinin %84'ü zaten sağlıklı olduğu için herkese "sağlıklı" diyen bir model bile benzer doğruluk alırdı.
- Dengeli model doğruluktan feragat edip riskli hastaların **%76'sını yakalar** hale geldi.
- Hangisi "daha iyi"? **İş problemine bağlı:** sağlık taramasında hasta kaçırmak (false negative), yanlış alarm (false positive) demekten çok daha maliyetli → burada recall öncelikli.

## 🔍 Risk Faktörleri (Katsayı Analizi)

Ölçeklenmiş özelliklerle model katsayıları adil karşılaştırılabilir. Riski en çok artıranlar sırasıyla: **genel sağlık algısı (kötü), BMI, yaş, yüksek tansiyon, yüksek kolesterol** — tıbbi literatürle tutarlı, modelin açıklanabilirliğinin güzel bir örneği.

## 🛠️ Uygulanan Yöntemler

Stratified train/test • StandardScaler (doğru fit/transform ayrımıyla) • LogisticRegression (standart + class_weight) • karmaşıklık matrisi ısı haritaları • classification_report (precision/recall/F1) • katsayı önem grafiği • `predict_proba` ile olasılık okuma

## 🎯 Sonraki Adım Fikirleri

Karar eşiğiyle (0.5) oynayıp precision-recall eğrisi çıkarmak, ROC-AUC ile eşikten bağımsız karşılaştırma.

> ⚠️ Bu bir eğitim çalışmasıdır; gerçek tıbbi değerlendirme yalnızca sağlık profesyonellerince yapılır.
