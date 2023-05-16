#magaza adlı classımızı oluşturalım
class Magaza:
    def __init__(self,magaza_adi,satici_adi,satici_cinsi,satis_tutari):
        self.__magaza_adi=magaza_adi
        self.__satici_adi=satici_adi
        self.__satici_cinsi=satici_cinsi
        self.__satis_tutari=satis_tutari

    # Accessor/Mutator metodlarını kullanalım
    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    def get_satis_tutari(self):
        return self.__satis_tutari

    def set_satis_tutari(self, satis_tutari):
        self.__satis_tutari = satis_tutari

    #str metodunu kullanalım
    def __str__(self):
        return f"Mağaza Adı: {self._magaza_adi}, Satıcı Adı: {self.__satici_adi}, Satıcı Cinsi: {self.__satici_cinsi}, Satış Tutarı: {self.__satis_tutari}"

#Mağaza nesnelerini tutacak dictionaryimizi oluşturalım
magazalar = {}

while True:
    #Kullanıcıdan veri alalım
    magaza_adi = input("Mağaza adı: ")
    satici_adi = input("Satıcı adı: ")
    satici_cinsi = input("Satıcı cinsi: ")
    satis_tutari = float(input("Satış tutarı: "))

    #Mağaza nesnesi oluşturalım
    magaza = Magaza(magaza_adi, satici_adi, satici_cinsi, satis_tutari)

    #dictionary'e ekleyelim
    if magaza_adi not in magazalar:
        magazalar[magaza_adi] = []

    magazalar[magaza_adi].append(magaza)

    #Kullanıcıya çıkış talebi soralım
    devam = input("Başka satış eklemek ister misiniz? (E/H)")


    if devam.upper() != "E":
        break

#Kullanıcının arama yapmak istediği mağaza adını alalım
arama_adi = input("Aramak istediğiniz mağaza adını nedir: ")

#Arama yapalım
if arama_adi in magazalar:
    for magaza in magazalar[arama_adi]:
        print(magaza)
else:
   print("dictionary'de yok")
