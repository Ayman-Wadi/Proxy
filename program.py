import requests

def check_proxy(proxy):
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        response = requests.get('https://www.google.com', proxies=proxies, timeout=100)
        if response.status_code == 200:
            return True, response.elapsed.total_seconds()
        else:
            return False, None
    except:
        return False, None

def main():
    proxy = input("Enter proxy server with port: ")
    working, speed = check_proxy(proxy)
    if working:
        print("Proxy is working.")
        print("Speed: {:.2f} seconds".format(speed))
    else:
        print("Proxy is not working.")

if __name__ == '__main__':
    main()
