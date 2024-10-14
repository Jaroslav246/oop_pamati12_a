
import itertools
import datetime
from datetime import time

class Pakalpojums:

    Pakalpojums_kategorija = ""
    Pakalpojums_nosaukums = ""
    Pakalpojums_atlaide = ""
    Pakalpojums_cena = 0
    
    id_iter = itertools.count()

    def __init__(self, pak_kat=None, pak_nos=None, pak_atl=None, pak_cena=10):
        self.Pakalpojums_id = next(self.id_iter) + 1
        self.Pakalpojums_kategorija = pak_kat
        self.Pakalpojums_nosaukums = pak_nos
        self.Pakalpojums_atlaide = pak_atl
        self.Pakalpojums_cena_stunda = pak_cena
        self.Laiks_pieejams = True
   

    def Pakalpojuma_info(self):
        return [
            self.Pakalpojums_kategorija, self.Pakalpojums_nosaukums, 
            self.Pakalpojums_atlaide, self.Pakalpojums_cena_stunda
            ]
        
    def Pakalpojuma_info_print(self):
        print("Pakalpojuma kategorija: " + str(self.Pakalpojums_kategorija))
        print("Pakalpojuma nosaukums: " + str(self.Pakalpojums_nosaukums))
        print("Pakalpojuma atlaide: " + str(self.Pakalpojums_atlaide))
        print("Pakalpojuma cena par stundu: " + str(self.Pakalpojums_cena_stunda))
        print("Laiks pieejams: " + str(self.Laiks_pieejams) + "/n")

class Worker:
    Worker_vaards = ""
    Worker_uzvaards = ""
    Worker_PK = ""
    Worker_tel_numurs = 0

    id_iter_kl = itertools.count()

    def __init__(self, _vaards, _uzvaards, _pk, _tel_numurs):
        self.Worker_id = next(self.id_iter_kl) + 1
        self.Workera_vaards = _vaards
        self.Workera_uzvaards = _uzvaards
        self.Workera_PK = _pk
        self.Workera_tel_numurs = _tel_numurs

    def Worker_info(self):
        return [
            self.Worker_vaards, self.Worker_uzvaards, self.Worker_PK, 
            self.Worker_tel_numurs
        ]
    
    # Worker info
    def Worker_info_print(self):
        print("Klienta vaards: " + self.Klienta_vaards)
        print("Klienta uzvaards: " + self.Klienta_vaards)
        print("Klienta personas kods: " + self.Klienta_PK)
        print("Klienta telefons: " + str(self.Klienta_tel_numurs) + "/n")

class Izmantosana:

    Pakalpojuma_saakuma_laiks = 0
    Pakalpojuma_beigu_laiks = 0
    Pakalpojuma_datums = 0 
    Izmantosana_cena_stunda = 10
    id_Pakalpojums = 0
    id_Klients = 0
    Izmantosana_id = 0

    id_iter_izmantosana = itertools.count()


    def Cena_kopa(self):
        kopeja_cena = self.Izmantosanas_cena_stunda * ((
            (self.Pakalpojuma_beigu_laiks - self.Pakalpojuma_sakuma_laiks)))
        return kopeja_cena

    def Izmantosana_info_print(self):
        print("Pakalpojuma sakuma laiks: " +
              str(self.Pakalpojuma_saakuma_laiks))
        print("Pakalpojuma beigu laiks: " + str(self.Pakalpojuma_beigu_laiks))
        print("Pakalpojums id: " + str(self.id_Pakalpojums))
        print("Klients id: " + str(self.id_Klients))
        print("Pakalpojuma cena stunda, EUR: " + 
              str(self.Izmantosana_cena_stunda) + "/n")

pak1 = Pakalpojums("Frizētāva", "Matu grieāna", "20%", 30)
pak2 = Pakalpojums("Uzacu un skropstu krāsošana", "Uzacu krāsošana", "25%")
pak3 = Pakalpojums("Kosmētiskās procedūras", "Higiēniskā sejas tīrīšana")

print(pak1.Pakalpojums_id)
pak1.Pakalpojuma_info()
pak1.Pakalpojuma_info_print()
print(pak2.Pakalpojums_id)
pak2.Pakalpojuma_info()
pak2.Pakalpojuma_info_print()
print(pak3.Pakalpojums_id)
pak3.Pakalpojuma_info()
pak3.Pakalpojuma_info_print()

klients1 = Klients("Aija", "Zālīte", "190490-11490", 29800789)
klients2 = Klients("Jānis", "Ozoliņš", "030589-11430", 26755689)
klients3 = Klients("Sintija", "Eglīte", "260998-12215", 20898777)

print(klients1.Klienta_id)
klients1.Klienta_info()
klients1.Klienta_info_print()
print(klients2.Klienta_id)
klients2.Klienta_info()
klients2.Klienta_info_print()
print(klients3.Klienta_id)
klients3.Klienta_info()
klients3.Klienta_info_print()