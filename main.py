'''
Belajarlah memahami code daripada
buang masa memahami perempuan.

Stop jadi script kiddies
'''

try:
	import requests
except ModuleNotFoundError:
	exit("Try pasang requests \"pip install requests\"")
import ipaddress
import os

def is_reserved_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_private or ipaddress.ip_address(ip).is_loopback
    except ValueError:
        return False

def track_ip(ip):
    if is_reserved_ip(ip):
        print("IP ini adalah reserved (localhost atau private network), tidak boleh dikesan.")
        return
    url = f"https://ipwho.is/{ip}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            print("\n📍 **Maklumat IP**")
            print(f"IP: {data['ip']}")
            print(f"Jenis: {data['type']}")

            print("\n🌍 **Lokasi**")
            print(f"Benua: {data['continent']} ({data['continent_code']})")
            print(f"Negara: {data['country']} ({data['country_code']})")
            print(f"Wilayah: {data['region']} ({data['region_code']})")
            print(f"Bandar: {data['city']}")
            print(f"Poskod: {data['postal']}")
            print(f"Koordinat: {data['latitude']}, {data['longitude']}")

            print("\n📞 **Maklumat Panggilan**")
            print(f"Kod Negara: +{data['calling_code']}")
            print(f"Ibu Negara: {data['capital']}")
            print(f"Sempadan Negara: {data['borders']}")

            print("\n📡 **Maklumat Sambungan**")
            print(f"ASN: {data['connection']['asn']}")
            print(f"Organisasi: {data['connection']['org']}")
            print(f"ISP: {data['connection']['isp']}")
            print(f"Domain ISP: {data['connection']['domain']}")

            print("\n⏰ **Zon Masa**")
            print(f"ID: {data['timezone']['id']}")
            print(f"Kod Singkatan: {data['timezone']['abbr']}")
            print(f"UTC Offset: {data['timezone']['utc']}")
            print(f"Waktu Semasa: {data['timezone']['current_time']}")

            print("\n🏳 **Bendera Negara**")
            print(f"Emoji: {data['flag']['emoji']}")
            print(f"Unicode: {data['flag']['emoji_unicode']}")
            print(f"Link: {data['flag']['img']}")

        else:
            print(f"Error: {data.get('message', 'IP tidak sah')}")
    else:
        print("Gagal mendapatkan data.")

# Contoh penggunaan
banner = '''
\t  RxnHorse
\t        ,--,
\t  _ ___/ /\|
\t ;( )__, )
\t; //   '--;
\t  \     |
\t   ^    ^
\t  @Mika259
'''
input("Enter to continue")
clear = "clear" if os.name == 'posix' else "cls"
os.system(clear)
print(banner)
ip = input("\tMasukkan IP: ")
track_ip(ip)
