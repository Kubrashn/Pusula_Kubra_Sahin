# 📊 EDA & Data Preprocessing Raporu

**Ad Soyad**: Kübra Şahin  
**Email**: shnkubra20@gmail.com   

---

## 1. Veri Seti Genel Bilgi
- Satır sayısı: 2235  
- Sütun sayısı: 16  
- Hedef değişken (Target): **TedaviSuresi**  
- Veri tipi dağılımı:
  - Sayısal: Yas, TedaviSuresi_num, UygulamaSuresi_num  
  - Kategorik: Cinsiyet, KanGrubu, Uyruk, Bolum, KronikHastalik, Alerji, Tanilar, UygulamaYerleri  

---

## 2. Eksik Değer Analizi
- Eksik değerler bulundu:  
  - Cinsiyet, KanGrubu, Bolum, Tanilar, UygulamaYerleri → `"Bilinmiyor"`  
  - KronikHastalik, Alerji → `"Yok"`  
  - TedaviSuresi_num, UygulamaSuresi_num → **ortalama ile dolduruldu**  

---

## 3. Veri Dönüşümleri
- **TedaviSuresi** ve **UygulamaSuresi** sütunlarından sadece rakamlar çıkarıldı → yeni değişkenler:  
  - `TedaviSuresi_num`  
  - `UygulamaSuresi_num`  

- Yeni özellik (feature engineering):  
  - `TedaviYoğunluk = TedaviSuresi_num / UygulamaSuresi_num`  

---

## 4. Duplicate İşlemi
- Tamamen aynı olan satırlar silindi.  
- Satır sayısı: **2235 → 1307**  

---

## 5. Kategorik Değişken İşlemleri
- Çok fazla kategoriye sahip değişkenler (`Bolum`, `Tanilar`, `UygulamaYerleri`, `Alerji`) sadeleştirildi.  
- **20’den az frekansa sahip değerler** → `"Diğer"` altında toplandı.  

---

## 6. Encoding
- Kategorik değişkenler **One-Hot Encoding** ile dönüştürüldü (`drop_first=True`).  
- Final tablo boyutu: **1307 satır × XXX sütun** (693’ten azaldı).  

---

## 7. Görselleştirme (EDA)
- Histogramlar: Yaş, TedaviSuresi_num, UygulamaSuresi_num  
- Scatter plot: Yaş vs Tedavi Süresi  
- Korelasyon heatmap (sayısal değişkenler)  
- Countplot: Bölüm-Cinsiyet ilişkisi  
- Boxplot: Kronik Hastalık & Tedavi Süresi ilişkisi  

---

## 8. Sonuç
- Veri seti temizlendi, eksikler dolduruldu, nadir kategoriler birleştirildi.  
- Yeni özellik (TedaviYoğunluk) eklendi.  
- Tekrar eden satırlar temizlendi.  
- Kategoriler encode edilerek modellemeye hazır hale getirildi.  

---

