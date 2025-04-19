import PyPDF2
from bs4 import BeautifulSoup

def pdf_oku_ve_metni_al(pdf_dosyasi,baslangic_sayfa=0, bitis_sayfa=None):
    try:
        with open(pdf_dosyasi, 'rb') as dosya:
            pdf_okuyucu = PyPDF2.PdfReader(dosya)
            sayfa_sayisi = len(pdf_okuyucu.pages)

            if bitis_sayfa is None:
                bitis_sayfa = sayfa_sayisi

            if baslangic_sayfa < 0 or bitis_sayfa > sayfa_sayisi or baslangic_sayfa >= bitis_sayfa:
                return "Geçersiz sayfa aralığı."

            metin = ""
            
            for sayfa_numarasi in range(baslangic_sayfa, bitis_sayfa):
                sayfa = pdf_okuyucu.pages[sayfa_numarasi]
                sayfa_metni = sayfa.extract_text()
                #metin += f"<h2>Sayfa {sayfa_numarasi + 1}</h2><p>{sayfa_metni}</p>"
                metin += f"{sayfa_metni}\n\n"  # Sayfa metni arasına boş satır eklenir 
            
            # HTML etiketlerini temizlemek için BeautifulSoup kullanın
            soup = BeautifulSoup(metin, "html.parser")
            temizlenmis_metin = soup.get_text(separator="\n")

            return temizlenmis_metin

    except Exception as e:
        return f"Bir hata oluştu: {e}"
