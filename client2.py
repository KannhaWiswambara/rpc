import xmlrpc.client

# Membuat proxy untuk server XML-RPC
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

while True:
    print("1. Simpan uang dalam IDR")
    print("2. Konversi uang dari IDR ke mata uang lain")
    print("3. Tampilkan jumlah uang yang dimiliki")
    print("0. Keluar")
    choice = int(input("Masukkan pilihan Anda: "))

    if choice == 1:
        amount = float(input("Masukkan jumlah uang dalam IDR yang ingin disimpan: "))
        result = proxy.save_money(amount)
        print(result)
    elif choice == 2:
        amount = float(input("Masukkan jumlah uang dalam IDR yang ingin dikonversi: "))
        from_currency = 'IDR'
        to_currency = input("Masukkan kode mata uang tujuan: ")
        result = proxy.convert_currency(amount, from_currency, to_currency)
        print(f"Hasil konversi: {result} {to_currency}")
    elif choice == 3:
        savings = proxy.show_savings()
        print("Jumlah uang yang dimiliki:")
        for currency, amount in savings.items():
            print(f"{currency}: {amount}")
    elif choice == 0:
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
