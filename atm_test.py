atm = {
    100 : {
        "Name" : "Cengiz Atay",
        "Main" : 450000,
        "Sub" : 250000,
    },

    101 : {
        "Name" : "Eyşan Tezcan",
        "Main" : 300000,
        "Sub" : 100000,
    },

    102 : {
        "Name" : "Ali Kırgız",
        "Main" : 100000,
        "Sub" : 0
    }
}

while True:
    user = int(input("Kullanıcı ID Numaranızı Giriniz: "))
    selection = int(input("\n\ChesterBank'a hoş geldiniz, Ne yapmak isterdiniz?\n1 - Bakiye Sorgula\n2 - Para Çek\n3 - Para Yatır\n4 - Kart İade\nSeçim Yapınız: "))

    if selection == 1:
        print(f"Bakiyeniz: {(atm[user]['Main']) + (atm[user]['Sub'])}$")
        break

    elif selection == 2:
        money_out = int(input("Ne Kadar Para Çekmek istiyorsun: "))
        if money_out <= (atm[user]['Main']):
            atm[user]["Main"] -= money_out
            print("Paranızı Çekebilirsiniz...")
            print(f"Ana Hesap Bakiyeniz: {(atm[user]['Main']) - (atm[user]['Sub'])}$")
            break
        else:
            quest = input("Ana hesabınızda yeterli bakiye bulunmamaktadır. Yedek hesap sorgulansın mı? (y/n): ")
            if quest == "y":
                atm[user]['Main'] += atm[user]['Sub']
                if atm[user]['Main'] >= money_out:
                    print("Paranızı Alabilirsiniz.")
                    atm[user]['Main'] -= money_out
                    print(f"Ana Hesap Bakiyeniz: {atm[user]['Main']}$")
                    break
                else:
                    print("Yeterli Bakiye Sağlanamadı. İşlem İptal Edildi...")
                    print(f"Ana Hesap Bakiyeniz: {atm[user]['Main']}$")
                    break
            elif quest == "n":
                print("Para çekme işlemi gerçekleştirilmemiştir...")
                break
            else:
                print("Seçiminiz Yanlıştır...")
                break

    elif selection == 3:
        money_in = int(input("Ne Kadar Para Yatırmak İstiyorsunuz: "))
        atm[user]["Main"] += money_in
        print(f"Bakiyeniz: {(atm[user]['Main']) + (atm[user]['Sub'])}$")
        break

    elif selection == 4:
        print("Çıkışınız Yapılıyor...")
        break

    else:
        print("Yanlış Seçim...")
        print("Çıkış Yapılıyor...")
        break