import xmlrpc.client

# Membuat proxy untuk server XML-RPC
proxy = xmlrpc.client.ServerProxy('http://10.41.113.148:8000)

# Memanggil fungsi convert_currency pada server
result = proxy.convert_currency(100, 'USD', 'IDR')
print(result)  # Output: 1,442,550

result = proxy.convert_currency(50, 'EUR', 'USD')
print(result)  # Output: 59.0

result = proxy.convert_currency(200, 'GBP', 'EUR')
print(result)  # Output: 234.0

result = proxy.convert_currency(1000, 'USD', 'JPY')
print(result)  # Output: Kurs mata uang tidak tersedia.

# Menginput jumlah uang yang dimiliki
savings_amount = float(input("Masukkan jumlah uang yang Anda miliki: "))

# Memanggil fungsi save_money pada server
result = proxy.save_money(savings_amount, 'USD')
print(result)  # Output: Uang berhasil disimpan.
