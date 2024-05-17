from socket import gethostbyname as GetIP
from os import system as cmd
from requests import get

def SCANN(url:str = None) -> list:
	if url is not None:
		try:
			req = get(f"https://crt.sh/?q={url}&output=json").json()
			returned = []

			for i in req:
				if i["common_name"] not in returned:
					returned.append(i["common_name"])

			return returned
		except: return []
	else: return []


def main():
	print(" ")
	url = input(" Введите URL: ") or None
	if url == "exit": exit()
	subdomains = SCANN(url)

	try: ip = GetIP(url)
	except TypeError: ip = None

	domains = " Домены, которые удалось найти:\n"
	for domain in subdomains:
		domains += " - " + domain + "\n"

	print(" ______________________________")
	print(f" URL: {url}\n IP: {ip}")
	print(domains)
	cmd("pause")

if __name__ == '__main__':
	while True: main()