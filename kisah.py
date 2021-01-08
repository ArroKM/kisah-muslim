import os,requests,json,re
from time import sleep
from bs4 import BeautifulSoup as _pas

class kisah:
	def __init__(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.url = "https://kisahmuslim.com/"
		self.url2 = "https://kisahmuslim.com/page/"
		self.page = 1
		self.men = "\n[ {B} Untuk Ke Halaman Utama\n[ {N} Untuk Ke Halaman Berikutnya\n[ {P} Untuk Ke Halaman Sebelumnya\n[ {E} Untuk Keluar\n[ {#} Untuk Lompat Ke Halaman Tertentu\n[ Note : Ex( #12 ) untuk lompat ke Halaman Tertentu\n"
		self.logo = """ ___ ___  __                __\n|   Y   )|__|.-----..---.-.|  |--.\n|.  1  / |  ||__ --||  _  ||     |\n|.  _  \ |__||_____||___._||__|__|\n|:  |   \  :: Coded By Asecx ::\n|::.| .  )  :: Kisah Muslim ::\n`--- ---' """
		self.me = "\n[ {A} Cari Artikel\n[ {B} Semua Artikel\n[ {E} Untuk Keluar\n"
		print(self.logo)
		print("="*30+self.me+"="*30)
		self.menu(self.url)

	def menu(self, url):
		sah = requests.get(url)
		kis = _pas(sah.text, "html.parser")
		men = kis.find(id="menu-main")
		hom = men.find_all("a")
		ti = [jd.text for jd in hom]
		l = [lo["href"] for lo in hom]
		del ti[1],ti[8],ti[11],ti[11],ti[0]
		del l[1],l[8],l[11],l[11],l[0]
		no = 0
		for da in ti:
			no += 1
			print(f"({no}) {da}")
		pil = input("(+) >>>> ")
		tot = 0
		for man in l:
			try:
				tot += 1
				if pil == "A" or pil == "a":
					car = input("\n(?) Cari Kisah : ")
					sleep(2)
					self.ber = (url+"?s="+car)
					bir = self.ber
					self.home(bir)
				elif pil == "B" or pil == "b":
					self.ber = (url)
					bir = self.ber
					self.home(bir)
				elif pil == "E" or pil == "e":
					exit("[*] Oke Terima Kasih")
				elif tot >= int(pil):
					self.ber = (man)
					bir = self.ber
					self.home(bir)
			except ValueError:
				exit("[!] Pilihan Tidak Ada..!")

	def home(self, bir):
		tut = 0
		while True:
			noo = 0
			os.system('cls' if os.name == 'nt' else 'clear')
			print(self.logo)
			print("="*30+self.men+"="*30)
			bor = requests.get(self.ber)
			if bor.status_code == 200:
				bur = _pas(bor.text, "html.parser")
			else:
				bor = requests.get(self.berr)
			bur = _pas(bor.text, "html.parser")
			nun = bur.find(id="main")
			nen = nun.find_all("a", class_="read-more button")
			lii = [lk["href"] for lk in nen]
			for m in nen:
				noo += 1
				dull = m["title"]
				print(f"({noo}) {dull}")
			pul = input(f"(<<<[ {self.page} ]>>>) ")
			if pul.isdigit():
				tut += 1
				if tut >= int(pul):
					ko = requests.get(lii[int(pul)])
					ku = _pas(ko.text, "html.parser")
					km = ku.find("h1", class_="entry-title").text
					sv = ku.find("div", class_="entry-content").text
					po = input("\n(?) Simpan/Membaca Artikel [S/M]? : ")
					if po == "S" or po == "s":
						with open("/data/data/com.termux/files/home/storage/shared/KISAH-MUSLIM/"+km.replace(" ","-")+".txt", "w") as f:
							f.write(sv)
						sleep(3)
						print("(+) Artikel berhasil disimpan")
						sleep(3)
						pass
					else:
						print(sv)
					bac = input("(+) Home/Quit/Back [H/Q/B]? : ")
					if bac == "H" or bac == "h":
						self.__init__()
					elif bac == "Q" or bac == "q":
						exit("[*] Oke Terima Kasih")
					else: pass
				else: pass
			else:
				if pul == "B" or pul == "b":
					self.__init__()
				elif pul == "N" or pul == "n":
					self.page += 1
					self.ber = bir.replace(self.url,self.url2+str(self.page))
					self.berr = bir+"/page/"+str(self.page)
				elif pul == "P" or pul == "p":
					self.page -= 1
					self.ber = bir.replace(self.url,self.url2+str(self.page))
					self.berr = bir+"/page/"+str(self.page)
				elif pul == "E" or pul == "e":
					exit("[*] Oke Terima Kasih")
				elif pul.startswith("#"):
					oke = int(pul.replace('#',''))
					self.page = oke
					self.ber = bir.replace(self.url,self.url2+str(oke))
					self.berr = bir+"/page/"+str(oke)
				else:
					print("[!] Pilihan Tidak Ada")
					sleep(3);pass


if __name__ == '__main__':
	try:
		kisah()

	except KeyboardInterrupt:
		exit("[*] Oke Terima Kasih")
