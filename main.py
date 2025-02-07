'''
Belajarlah memahami code daripada
buang masa memahami perempuan.

Stop jadi script kiddies
'''
try:
	import phonenumbers
	from phonenumbers import geocoder, carrier, timezone
except ModuleNotFoundError:
	exit("Try pasang phonenumbers \"pip install phonenumbers\"")
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
        print("Ip private sape nape nak track? , takleh detect oi.")
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
            print(f"Ip tak sah pulak aduh.")
    else:
        print("Gagal ambik data.")

def get_phone_info(phone_number):
    try:
        # Parse nombor telefon
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Periksa jika nombor sah
        if not phonenumbers.is_valid_number(parsed_number):
            print("❌ Nombor telefon x sah!")
            return
        
        print("\n📞 **Maklumat Nombor Telefon**")
        print(f"Nombor: {phone_number}")
        print(f"Format Antarabangsa: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"Format E164: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f"Format Nasional: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}")

        # Dapatkan negara
        country = geocoder.description_for_number(parsed_number, "en")
        print(f"Negara: {country}")

        # Dapatkan pembekal rangkaian (mungkin tidak tersedia untuk semua nombor)
        provider = carrier.name_for_number(parsed_number, "en")
        print(f"Pembekal Rangkaian: {provider if provider else 'Tidak diketahui'}")

        # Dapatkan zon waktu
        timezones = timezone.time_zones_for_number(parsed_number)
        print(f"Zon Waktu: {', '.join(timezones)}")

    except phonenumbers.phonenumberutil.NumberParseException:
        print("❌ Format nombor tidak betul!")


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
print("1] Ip Info")
print("2] Phonenumber Info")
choose = int(input("(Pilihan )> "))

if choose == 1:
	os.system(clear)
	print(banner)
	ip = input("\tMasukkan IP: ")
	track_ip(ip)
elif choose == 2:
    os.system(clear)
    print(banner)
    phone = input("Masukkan nombor telefon (contoh: +60123456789): ")
    get_phone_info(phone)
else:
	exit("error menu!")


