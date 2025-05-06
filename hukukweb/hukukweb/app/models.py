from django.db import models

# SSS - Sıkça Sorulan Sorular
class SSS(models.Model):
    question = models.CharField(max_length=500, verbose_name="Soru")
    answer = models.TextField(verbose_name="Cevap")
    is_active = models.BooleanField(default=True, verbose_name="Yayında mı?")

    def __str__(self):
        return self.question

#Avukat Özgeçmiş
class AvukatOzgecmis(models.Model):
    ad_soyad = models.CharField(max_length=200, verbose_name="Avukat Adı Soyadı")
    biyografi = models.TextField(verbose_name="Biyografi")

    def __str__(self):
        return self.ad_soyad
    

#vizyon-misyon
class VizyonMisyon(models.Model):
    vizyon = models.TextField(verbose_name="Vizyon")
    misyon = models.TextField(verbose_name="Misyon")

    def __str__(self):
        return "Vizyon ve Misyon"


#basında biz
class BasindaBiz(models.Model):
    baslik = models.CharField(max_length=255, verbose_name="Haber Başlığı")
    link = models.URLField(verbose_name="Haber Linki")
    image = models.ImageField(upload_to='basinda_biz/', null=True, blank=True, verbose_name="Haber Resmi")

    def __str__(self):
        return self.baslik