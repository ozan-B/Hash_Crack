#otomatik olarak sid.txt dosyasını kullanırı hash kırmak için .Md5 veya sha256 ile hashlenmiş veriyi ister ve hash türünü ister.
#sid.txt dosyasındaki tüm dataların hash değerini alır ve ve bizim verdiğimiz hash ile karşılaştırır olumlu sonuçlanırsa verdiğimiz hash değerinin çözülmüş halini bize gösterir.
#NOT: bu kodu terminalden çalıştır..


import hashlib

def md5_hash(data):
    found = False  # Eşleşen bir değer bulunduğunu kontrol etmek için bir bayrak

    with open("sid.txt", "r") as f:
        for passwd_try in f:
            h = hashlib.new("md5")
            h.update(passwd_try.strip().encode('utf-8'))
            ozan = h.hexdigest()


            if ozan == data:
                found = True
                print(f"data = {data} = {passwd_try.strip()}")
    if not found:
        print(f"data = {data} için eşleşen değer bulunamadı.")


def sha256_hash(data):
    found = False  # Eşleşen bir değer bulunduğunu kontrol etmek için bir bayrak

    with open("sid.txt", "r") as f:
        for passwd_try in f:
            h = hashlib.new("sha256")
            h.update(passwd_try.strip().encode('utf-8'))
            ozan = h.hexdigest()

            if ozan == data:
                found = True
                print(f"data = {data} = {passwd_try.strip()}")

    if not found:
        print(f"data = {data} için eşleşen değer bulunamadı.")

def main():
    print("Hash türünü seçiniz:")
    print("1- MD5")
    print("2- SHA256")

    data = input("hash'i giriniz: ")
    secim = input("Seçiminizi yapınız (1 veya 2): ")

    if secim == "1":
        hash_tur = "md5"
        md5_hash(data)
    elif secim == "2":
        hash_tur = "sha256"
        sha256_hash(data)
    else:
        print("Geçersiz seçim. Program sonlandırılıyor.")

if __name__ == "__main__":
    main()
