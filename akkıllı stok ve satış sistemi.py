
import numpy as np
urunler = np.array(["Süt", "Ekmek", "Su", "Kahve"])
stok = np.array([60, 55, 70, 40])
satis_fiyatlari = np.array([35, 50, 20, 80])
maliyetler = np.array([20, 32, 12, 55])

talep = np.array([
    [8, 5, 12, 3],
    [7, 9, 10, 4],
    [10, 7, 9, 6],
    [6, 12, 11, 2],
    [9, 8, 13, 5],
    [12, 10, 8, 7],
    [5, 6, 10, 4]
])

haftalik_talep = np.sum(talep, axis=0)

en_yuksek = np.argmax(haftalik_talep)
en_dusuk = np.argmin(haftalik_talep)

print("Haftalık ürün talepleri:", haftalik_talep)
print("En çok talep edilen ürün:", urunler[en_yuksek])
print("En az talep edilen ürün:", urunler[en_dusuk])


gercek_satislar = np.zeros((7, 4), dtype=int)
stok_kalan = stok.copy()

for gun in range(7):
    for urun in range(4):

        gercek_satislar[gun][urun] = np.minimum(
            stok_kalan[urun],
            talep[gun][urun]
        )

        stok_kalan[urun] -= gercek_satislar[gun][urun]

print("\nGerçek satışlar:")
print(gercek_satislar)

print("\nKalan stok:")
print(stok_kalan)

toplam_satis = np.sum(gercek_satislar, axis=0)

urun_gelirleri = toplam_satis * satis_fiyatlari
urun_maliyetleri = toplam_satis * maliyetler
urun_karlari = urun_gelirleri - urun_maliyetleri

toplam_gelir = np.sum(urun_gelirleri)
toplam_maliyet = np.sum(urun_maliyetleri)
toplam_kar = np.sum(urun_karlari)

print("\nToplam gelir:", toplam_gelir)
print("Toplam maliyet:", toplam_maliyet)
print("Toplam kâr:", toplam_kar)


karsilanamayan_talep = talep - gercek_satislar
toplam_kayip = np.sum(karsilanamayan_talep)

print("\nKarşılanamayan talepler:")
print(karsilanamayan_talep)
print("Toplam kaybedilen satış:", toplam_kayip)


print("\nKritik stok raporu:")

for i in range(len(urunler)):
    if stok_kalan[i] <= 10:
        print(urunler[i], "kritik stok seviyesinde!")


class MarketAnaliz:

    def __init__(self, urunler, stok, satis_fiyatlari, maliyetler, talep):
        self.urunler = urunler
        self.stok = stok.copy()
        self.satis_fiyatlari = satis_fiyatlari
        self.maliyetler = maliyetler
        self.talep = talep

        self.gercek_satislar = np.zeros((7, 4), dtype=int)
        self.stok_kalan = self.stok.copy()

    def satislari_hesapla(self):

        for gun in range(7):
            for urun in range(4):
                self.gercek_satislar[gun][urun] = np.minimum(
                    self.stok_kalan[urun],
                    self.talep[gun][urun]
                )

                self.stok_kalan[urun] -= self.gercek_satislar[gun][urun]

        return self.gercek_satislar

    def kar_raporu(self):

        toplam_satis = np.sum(self.gercek_satislar, axis=0)

        gelir = toplam_satis * self.satis_fiyatlari
        maliyet = toplam_satis * self.maliyetler
        kar = gelir - maliyet

        print("\nToplam gelir:", np.sum(gelir))
        print("Toplam maliyet:", np.sum(maliyet))
        print("Toplam kâr:", np.sum(kar))

    def stok_raporu(self):

        print("\nKalan stok raporu:")

        for i in range(len(self.urunler)):
            print(self.urunler[i], ":", self.stok_kalan[i])

    def haftalik_rapor(self):

        print("\nHaftalık talep:", np.sum(self.talep, axis=0))
        print("Gerçek satışlar:", np.sum(self.gercek_satislar, axis=0))
        print("Karşılanamayan talep:", np.sum(self.talep - self.gercek_satislar))



market = MarketAnaliz(
    urunler,
    stok,
    satis_fiyatlari,
    maliyetler,
    talep
)

market.satislari_hesapla()
market.kar_raporu()
market.stok_raporu()
market.haftalik_rapor()
