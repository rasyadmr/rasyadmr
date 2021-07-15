#Imports
import time


#Initiation
merah, kuning, hijau = True, True, True
power = True
cooldown = int(time.time())


#Functions
def timenow():
	sekarang = int(time.time())
	return sekarang


def activated(waktu):
	global hijau, kuning, merah, cooldown
	while hijau:
		kuning = False
		timer = 30
		print("Lampu hijau aktif, Silakan menyeberang!")
		while timer != -1:
			print(timer)
			time.sleep(1)
			timer -= 1
		print("Lampu merah aktif, mohon tekan tombol untuk menyeberang")
		hijau = False
	merah = True
	cooldown = waktu + 45


def clicked(waktu):
	global kuning, hijau, merah
	while kuning:
		merah = False
		print("Lampu kuning aktif!")
		countdown = 5
		while countdown != -1:
			print(countdown)
			time.sleep(1)
			countdown -= 1
		hijau = True
		activated(waktu)


#Main code
while power:
	tombol = int(input("1 untuk mulai menyeberang"))
	if tombol == 1 and timenow() >= cooldown:
		kuning = True
		clicked(timenow())
		cooldown = timenow() + 45
		continue
	elif tombol == 0 and timenow() >= cooldown:
		print("Fail 1")
		continue
	elif timenow() + 5 < cooldown and tombol == 1:
		print("Sedang cooldown")
		while timenow() + 5 < cooldown:
			print(str(cooldown - timenow()))
			time.sleep(1)
		kuning = True
		clicked(timenow())
		continue
	else:
		print("Fail 2")
		continue

	'''Jika akan dipasang dengan alat, variabel tombol akan diganti dengan fungsi tombol tersebut.
	Kode pada bagian power akan diubah.'''