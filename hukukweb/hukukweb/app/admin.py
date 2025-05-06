from django.contrib import admin
from .models import SSS, AvukatOzgecmis, VizyonMisyon, BasindaBiz

@admin.register(SSS)
class SSSAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('question',)


@admin.register(AvukatOzgecmis)
class AvukatOzgecmisAdmin(admin.ModelAdmin):
    list_display = ('ad_soyad', 'biyografi')
    search_fields = ('ad_soyad', 'biyografi')


@admin.register(VizyonMisyon)
class VizyonMisyonAdmin(admin.ModelAdmin):
    list_display = ('vizyon', 'misyon')



@admin.register(BasindaBiz)
class BasindaBizAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'link')
    search_fields = ('baslik', 'link')
