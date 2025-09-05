import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder


df = pd.read_excel("Talent_Academy_Case_DT_2025.xlsx")   

df.shape         
df.info()        
df.head()        
df.describe()    

print(df.info())
print(df.dtypes)


# === Eksik Değerler ===
print(df.isnull().sum())


#Kategorik Kolonların Dağılımı

for col in ["Cinsiyet", "KanGrubu", "Uyruk", "Bolum"]:
    print(f"\n{col} dağılımı:")
    print(df[col].value_counts(dropna=False))


# === Histogramlar ===
num_cols = ["Yas"]  # şimdilik yaş, sonra TedaviSuresi/UygulamaSuresi’ni temizleyince ekleyeceğiz
df[num_cols].hist(bins=20, figsize=(8, 5))
plt.show()




# Tedavi Süresi sadece rakamları al
df["TedaviSuresi_num"] = df["TedaviSuresi"].astype(str).str.extract(r'(\d+)').astype(float)

# Uygulama Süresi sadece rakamları al
df["UygulamaSuresi_num"] = df["UygulamaSuresi"].astype(str).str.extract(r'(\d+)').astype(float)


print(df[["TedaviSuresi", "TedaviSuresi_num"]].head(20))
print(df[["UygulamaSuresi", "UygulamaSuresi_num"]].head(20))


# === Scatter Plot: Yaş vs Tedavi Süresi ===
plt.figure(figsize=(8, 5))
plt.scatter(df["Yas"], df["TedaviSuresi_num"], alpha=0.6)
plt.xlabel("Yaş")
plt.ylabel("Tedavi Süresi (seans)")
plt.title("Yaş vs Tedavi Süresi")
plt.show()

# === Scatter Plot: Yaş vs Uygulama Süresi ===
plt.figure(figsize=(8, 5))
plt.scatter(df["Yas"], df["UygulamaSuresi_num"], alpha=0.6, color="orange")
plt.xlabel("Yaş")
plt.ylabel("Uygulama Süresi")
plt.title("Yaş vs Uygulama Süresi")
plt.show()


#=== Korelasyon Heatmap ===
numeric_df = df.select_dtypes(include=["int64", "float64"])
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.show()


df["Cinsiyet"] = df["Cinsiyet"].fillna("Bilinmiyor")
df["KanGrubu"] = df["KanGrubu"].fillna("Bilinmiyor")
df["Bolum"] = df["Bolum"].fillna("Bilinmiyor")
df["KronikHastalik"] = df["KronikHastalik"].fillna("Yok")
df["Alerji"] = df["Alerji"].fillna("Yok")
df["Tanilar"] = df["Tanilar"].fillna("Bilinmiyor")
df["UygulamaYerleri"] = df["UygulamaYerleri"].fillna("Bilinmiyor")

# --- Sayısal eksikler ---


# Pandas yöntemi (scikit-learn olmadan)
df["TedaviSuresi_num"] = df["TedaviSuresi_num"].fillna(df["TedaviSuresi_num"].mean())
df["UygulamaSuresi_num"] = df["UygulamaSuresi_num"].fillna(df["UygulamaSuresi_num"].mean())


print(df[["TedaviSuresi", "TedaviSuresi_num"]].head(20))
print(df[["UygulamaSuresi", "UygulamaSuresi_num"]].head(20))

print(df.isnull().sum())



#Cinsiyet ve Bolüm ilişkisi
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='Bolum', hue='Cinsiyet')
plt.xticks(rotation=45)
plt.title("Bölüm ve Cinsiyet Dağılımı")
plt.show()

# KronikHastalik ve TedaviSuresi ilişkisi
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='KronikHastalik', y='TedaviSuresi_num')
plt.xticks(rotation=45)
plt.title("Kronik Hastalık ve Tedavi Süresi")
plt.show()

df["TedaviYoğunluk"] = df["TedaviSuresi_num"] / df["UygulamaSuresi_num"]


print("Önce:", df.shape)
df = df.drop_duplicates()
print("Sonra:", df.shape)



# --- 1. Nadir kategorileri "Diğer" altında toplama fonksiyonu ---
def group_rare_categories(df, col, threshold=20):
    value_counts = df[col].value_counts()
    rare_categories = value_counts[value_counts < threshold].index
    df[col] = df[col].apply(lambda x: "Diğer" if x in rare_categories else x)
    return df

# --- 2. Temizlenecek kolonlar ---
categorical_cols = ["Bolum", "Tanilar", "UygulamaYerleri", "Alerji"]

# --- 3. Nadir kategorileri gruplama ---
for col in categorical_cols:
    df = group_rare_categories(df, col, threshold=20)

# --- 4. Son hali kontrol ---
for col in categorical_cols:
    print(f"\n{col} dağılımı (nadirler Diğer altında toplandı):")
    print(df[col].value_counts())

# --- 5. One-Hot Encoding ---
all_categorical_cols = ["Cinsiyet", "KanGrubu", "Uyruk", "Bolum", 
                        "KronikHastalik", "Alerji", "Tanilar", "UygulamaYerleri"]

df_final = pd.get_dummies(df, columns=all_categorical_cols, drop_first=True)

print("\nFinal tablo boyutu:", df_final.shape)

# --- 6. Excel'e kaydet ---
df_final.to_excel("cleaned_dataset.xlsx", index=False)
print("\nTemizlenmiş dataset 'cleaned_dataset.xlsx' olarak kaydedildi ✅")





