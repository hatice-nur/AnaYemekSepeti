from django.db import models
from django.contrib.auth.models import User

from account.models import Kullanici


class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):  
        return self.name
class Restoran(models.Model):
    name = models.CharField(max_length=100)
    adres = models.CharField(max_length=255)
    telefon = models.CharField(max_length=15)
    acilis_saati = models.TimeField()
    kapanis_saati = models.TimeField()
    email=models.EmailField(blank=True)
    sifre=models.CharField(max_length=20,default="")
    puan = models.FloatField(())
    resim = models.ImageField()
    min_tutar=models.FloatField(())
    category=models.CharField(max_length=20)
    hesap_tipi=models.CharField(max_length=20, choices=[("Kullanici","Kullanici"),("Restoran","Restoran")],default="")
    
    

    def __str__(self):
        return self.name

class Urun(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField()
    fiyat = models.FloatField()
    detay = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    restoran = models.ForeignKey(Restoran, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.name
    

class Siparis(models.Model):

    @property
    def toplam_tutar(self):
        return sum([item.urun.fiyat*item.miktar for item in self.siparis_items.all()])
            
        
    
class SiparisItem(models.Model):
    siparis_tarihi = models.DateTimeField(auto_now_add=True)
    teslim_tarihi = models.DateField()
    tutar = models.FloatField()
    miktar = models.PositiveIntegerField()
    durum = models.CharField(max_length=20, choices=[("Bekliyor", "Bekliyor"), ("Onaylandı", "Onaylandı"), ("Tamamlandı", "Tamamlandı"), ("İptal Edildi", "İptal Edildi")])
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    siparis=models.ForeignKey(Siparis,related_name="siparis_items", on_delete=models.CASCADE)

    def __str__(self):
        return self.durum
    
    
    


class TeslimatAdresi(models.Model):
    il=models.CharField(max_length=50)
    ilce=models.CharField(max_length=50)
    mahalle=models.CharField(max_length=50)
    cadde=models.CharField(max_length=50)
    bina=models.CharField(max_length=50)
    kapi=models.CharField(max_length=50)
    kullanici=models.ForeignKey(Kullanici,on_delete=models.CASCADE)

    def __str__(self):
        return self.il


class OdemeBilgileri(models.Model):
    kart_sahibi=models.CharField(max_length=100)
    kart_numarasi=models.IntegerField()
    son_kullanma=models.IntegerField()
    cvv=models.IntegerField()

    def __str__(self):
        return self.kart_sahibi




    
    
