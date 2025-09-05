# Pusula_Kübra_Şahin

**Ad Soyad**: Kübra Şahin  
**Email**: shnkubra20@gmail.com  

---

## 📌 Proje Özeti
Bu proje, **Talent Academy Case 2025** kapsamında verilen veri setinin **EDA (Exploratory Data Analysis)** ve **veri ön işleme (data preprocessing)** adımlarını içermektedir.  
Amaç, hedef değişken olan **TedaviSuresi**’ne yönelik olarak veri setini temizlemek, düzenlemek ve modellemeye hazır hale getirmektir.  

---

## 🔎 Yapılan Adımlar

### 1. Veri Keşfi (EDA)
- Veri setinin boyutu, sütun tipleri, eksik değerler ve temel istatistikler incelendi.  
- Kategorik değişkenlerin dağılımları analiz edildi.  
- Sayısal değişkenler üzerinde histogram, scatter plot ve korelasyon matrisi görselleştirildi.  

### 2. Eksik Değer İşlemleri
- **Kategorik değişkenlerde** eksik değerler `"Bilinmiyor"` veya `"Yok"` gibi etiketlerle dolduruldu.  
- **Sayısal değişkenlerde** (`TedaviSuresi_num`, `UygulamaSuresi_num`) eksik değerler ortalama ile dolduruldu.  

### 3. Yeni Özellik
- **TedaviYoğunluk** adında yeni bir değişken üretildi:  
  \[
  \text{TedaviYoğunluk} = \frac{\text{TedaviSuresi\_num}}{\text{UygulamaSuresi\_num}}
  \]

### 4. Tekrarlayan Satırlar
- Tüm sütunları birebir aynı olan satırlar silindi (`drop_duplicates`).  
- Satır sayısı **2235 → 1307** olarak güncellendi.  

### 5. Nadir Kategorilerin Gruplaması
- `Bolum`, `Tanilar`, `UygulamaYerleri`, `Alerji` değişkenlerinde frekansı **20’den az** olan kategoriler **"Diğer"** altında toplandı.  

### 6. Encoding
- Kategorik değişkenler One-Hot Encoding ile dönüştürüldü (`drop_first=True`).  
- Final veri seti boyutu: **(1307, N)** → sütun sayısı nadir kategoriler toplandıktan sonra azaldı.  

### 7. Çıktı
- Temizlenmiş veri seti `cleaned_dataset.xlsx` adıyla dışa aktarıldı.  

---

## 🛠️ Kullanılan Kütüphaneler
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  

---

## ▶️ Çalıştırma Talimatları
1. Bu projeyi bilgisayarına klonla:
   ```bash
   git clone https://github.com/Kubrashn/Pusula_Kubra_Sahin.git
