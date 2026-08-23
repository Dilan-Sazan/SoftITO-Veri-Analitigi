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

---

## 📓 Notebook Adım Adım — `lojistik_regresyon_pratik.ipynb`

Notebook'un kendisinde yalnızca kod bulunur; her adımın açıklaması burada.

#### 0. Veri Yolu (Colab/Drive Uyumlu)

**Google Colab + Drive kullanıyorsan** ilk üç satırın başındaki `#` işaretlerini kaldır ve
`VERI_KLASORU`'nu csv dosyasını koyduğun Drive klasörüne göre düzenle.

#### 1. Kütüphaneler

#### 2. Veriyi Yükleme ve Keşfetme

**İki gözlem, iki karar:**

1. **Duplicate'ler hakkında:** ~24 bin "aynı" satır var ama bu veri setinde kişi kimliği (ID) yok ve
   22 sütunun neredeyse tamamı kategorik/tam sayı. 253 bin kişilik bir ankette iki farklı kişinin
   bütün sorulara aynı cevabı vermesi gayet olası. Bu yüzden bunları **silmiyoruz** — pandas
   derslerindeki ilke burada da geçerli: *her tekrar, hata değildir; karar veriye göre verilir.*

2. **Hedefi ikili yapıyoruz:** Ders ikili (binary) sınıflandırma üzerineydi. Prediyabet (1) klinik
   olarak diyabet yolunda bir risk durumu olduğundan, 1 ve 2'yi birleştirip
   **"diyabet riski var (1) / yok (0)"** hedefi tanımlıyoruz.

#### 3. Özellik/Hedef Ayrımı ve Train/Test

Dengesiz veri setlerinde ayrımı `stratify` ile yapıyoruz ki her iki sette de sınıf oranları korunusun
(dersin train/test adımına dengesizlik nedeniyle eklediğimiz güvence).

#### 4. Özellik Ölçeklendirme (StandardScaler)

Dersteki kritik kural: **scaler yalnızca eğitim verisine fit edilir**, test verisi aynı dönüşümle
sadece transform edilir — aksi test bilgisinin modele sızması (data leakage) olur.

#### 5. Model 1: Standart Lojistik Regresyon

%85 doğruluk — kulağa harika geliyor, değil mi? **Ama durun.** Veri setinin %84'ü zaten sağlıklı;
herkese "sağlıklı" diyen kafasız bir model bile %84 doğruluk alırdı. Yani modelimiz o kafasız
modelden neredeyse hiç iyi değil! Gerçeği karmaşıklık matrisi söyler.

**İşte yanılsama ortaya çıktı:** Model, gerçekten riskli olan hastaların yalnızca **%19'unu**
yakalayabiliyor (recall). Yani 100 diyabet riskli kişiden ~81'ine "sağlıklısın" diyor! Sağlık
taramasında bu kabul edilemez — kaçırılan hasta (false negative), yanlış alarm verilen sağlıklıdan
(false positive) çok daha maliyetlidir.

#### 6. Model 2: Sınıf Ağırlıklı Lojistik Regresyon

`class_weight="balanced"` azınlık sınıfının hatalarını daha ağır cezalandırır — model artık
riskli sınıfı ciddiye almak zorunda.

**Takas (trade-off) net görülüyor:** Dengeli model genel doğruluktan feragat etti ama riskli
hastaları yakalama oranını (recall) kat kat artırdı. Hangi model "daha iyi"? **Amaca bağlı:**
tarama amaçlı bir sistemde recall kritiktir → Model 2; kesin teşhis öncesi ön filtrede yanlış
alarm maliyetliyse precision önem kazanır. Metrik seçimi, iş probleminin kendisidir.

#### 7. Katsayı Yorumu: Riski Ne Artırıyor?

Lojistik regresyonun güzelliği (dersteki vurgu): katsayılar yorumlanabilir. Pozitif katsayı riski
artırır, negatif azaltır. Özellikler ölçeklendiği için büyüklükleri adilce karşılaştırılabilir.

#### 8. Örnek Tahmin (Olasılıklarıyla)

Dersteki gibi tek bir kişi için tahmin yapıyoruz — ama `predict_proba` ile sigmoid çıktısını,
yani **risk olasılığını** da gösteriyoruz.

#### 9. Özet — Bu Pratikte Öğrendiklerim

1. **3 sınıflı hedef ikiliye dönüştürüldü** (prediyabet + diyabet = riskli) — gerekçesi açıklanarak
2. **Duplicate kararı veriye göre verildi:** ID'siz anket verisinde aynı cevap profilleri meşru → tutuldu
3. **Stratified train/test ayrımı** ile sınıf oranları her iki sette korundu
4. **StandardScaler doğru kullanıldı:** fit yalnızca eğitimde — data leakage önlendi
5. ⭐ **Doğruluk yanılsaması canlı yaşandı:** %85 accuracy'li model, riskli hastaların %81'ini kaçırıyordu;
   karmaşıklık matrisi ve classification_report gerçeği gösterdi
6. **class_weight='balanced'** ile recall kat kat artırıldı; precision-recall takasının iş problemine
   göre seçilmesi gerektiği anlaşıldı
7. **Katsayılar yorumlandı:** genel sağlık algısı, yüksek tansiyon, BMI ve kolesterol riski en çok
   artıran faktörler olarak öne çıktı
8. `predict_proba` ile sigmoidin ürettiği **risk olasılıkları** okundu

**Sonraki adım fikirleri:** karar eşiğini (0.5) oynayarak precision-recall eğrisi çıkarmak,
ROC-AUC ile modelleri eşikten bağımsız karşılaştırmak.

> ⚠️ **Not:** Bu bir eğitim çalışmasıdır; gerçek tıbbi teşhis ancak sağlık profesyonellerince konur.
