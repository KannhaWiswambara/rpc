from xmlrpc.server import SimpleXMLRPCServer

# Data sederhana untuk menyimpan jumlah uang
savings = {
    'USD': 0,
    'IDR': 0,
    'EUR': 0,
    'GBP': 0
}

# Fungsi untuk mengkonversi mata uang
def convert_currency(amount, from_currency, to_currency):
    # Menentukan kurs mata uang
    currency_rates = {
        'USD': {
            'IDR': 14425.50,
            'EUR': 0.85,
            'GBP': 0.72
        },
        'IDR': {
            'USD': 0.000069,
            'EUR': 0.0000063,
            'GBP': 0.0000054
        },
        'EUR': {
            'USD': 1.18,
            'IDR': 158797.55,
            'GBP': 0.85
        },
        'GBP': {
            'USD': 1.39,
            'IDR': 184883.83,
            'EUR': 1.17
        }
    }

    # Mengonversi mata uang
    if from_currency == to_currency:
        return amount
    else:
        try:
            conversion_rate = currency_rates[from_currency][to_currency]
            converted_amount = amount * conversion_rate
            return round(converted_amount, 2)
        except KeyError:
            return "Kurs mata uang tidak tersedia."

# Fungsi untuk menyimpan uang
def save_money(amount):
    try:
        savings['IDR'] += amount
        return "Uang berhasil disimpan."
    except:
        return "Terjadi kesalahan saat menyimpan uang."

def show_savings():
    return savings
        

# Membuat server XML-RPC
server = SimpleXMLRPCServer(('10.41.113.148', 8000))
server.register_function(convert_currency, 'convert_currency')
server.register_function(save_money, 'save_money')
server.register_function(show_savings, 'show_savings')
print("Server XML-RPC berjalan di port 8000...")
server.serve_forever()
