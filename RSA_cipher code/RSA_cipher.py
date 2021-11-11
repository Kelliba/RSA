from Crypto.Util import number
import os
import string
import base64
import eel

eel.init("web")

a = ["",""," ","\n","\t","'",'"',"’"]+list(string.ascii_letters)+list(string.digits)+['а','б','в','г','д','е','ё','ж','з','и','й','к','л',
'м','н','о','п','р','с','т','у','ф','х','ц',
'ч','ш','щ','ъ','ы','ь','э','ю','я']+['А', 'Б', 'В', 'Г', 'Д', 'Е',
'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']+list(string.punctuation)

def random_number(b):
	prime_number = number.getPrime(b)
	return prime_number

def rsa_exponents():
	p,q = random_number(128),random_number(128) 
	n = p*q
	phi = (p-1)*(q-1)
	e = 65537
	d = pow(e,-1,phi)
	return e, d, n, p, q

def file_len():
	with open("C:/RSA_logs/RSA_log.txt","r") as file:
		size = len([0 for _ in file])
		return int(size)

def file_create():
	with open("C:/RSA_logs/RSA_log.txt","a") as file:
		file.write(str(file_len())+str(rsa_exponents())+"\n")

@eel.expose
def RSA_dir():
	try:
		os.mkdir("C:\\RSA_logs")
	except FileExistsError:
		pass

def RSA_encode_file(text):
	file_number = str(file_len()-1)
	file_name = "C:/RSA_logs/"+"RSA_encode_file"+file_number+".txt"
	with open(file_name,"a") as file:
		file.write(file_number+"\n"+text)

def exponents_file(number):
	with open("C:/RSA_logs/RSA_log.txt","r") as file:
		if number != 0:
			for i in range(number+1):
				exponents = file.readline()
		else:
			exponents = file.readline()
	exponents_list = exponents[2:].split(", ")
	return int(exponents_list[0]),int(exponents_list[1]),int(exponents_list[2])

def base64_encode(text):
	text_enc = text.encode("UTF-8") 
	text_base = base64.b64encode(text_enc).decode("UTF-8")
	return text_base

def base64_decode(base_text):
	text_enc = base_text.encode("UTF-8")
	text_base_de = base64.b64decode(text_enc).decode("UTF-8").split()
	return text_base_de

def text_for_namber(text):
		text = list(text)
		list_text = [ a.index(i) for i in text]
		return list_text

def number_for_text(uncipher_list):
		text = "".join([a[i] for i in uncipher_list])
		return text

def rsa_encode(list_text):
	e,d,n = exponents_file(file_len()-1)
	cipher_list = [str(pow(i,e,n)) for i in list_text]
	return cipher_list

def rsa_decode(cipher_list):
	e,d,n = exponents_file(number_enc_file(file_local))
	uncipher_list = [pow(int(i),d,n) for i in cipher_list]
	return uncipher_list

@eel.expose
def cipher(text,file):
	if file!=" ":
		file = "C:/RSA_logs/"+str(file)[1:]
		with open(file,"r",encoding="utf-8") as f:
			text = f.read()
	file_create()
	step1 = text_for_namber(text)
	step2 = " ".join(rsa_encode(step1))
	step3 = base64_encode(step2)
	RSA_encode_file(step3)

@eel.expose
def uncipher(file):
	global file_local
	file_local = file
	text = text_file(file)
	step1 = base64_decode(text)
	step2 = rsa_decode(step1)
	step3 = number_for_text(step2)
	RSA_decode_file(step3,number_enc_file(file))

def number_enc_file(file):
	file_local = "C:/RSA_logs/"+file
	with open(file_local,"r") as f:
		number = int(f.readline())
		return number

def RSA_decode_file(text,number):
	file_name = "C:/RSA_logs/"+"RSA_decode_file"+str(number)+".txt"
	with open(file_name,"a") as file:
		file.write(text)

def text_file(file):
	file_local = "C:/RSA_logs/"+file
	with open(file_local,"r") as open_file:
		text = open_file.read()
		len_1 = len(open_file.readline())+1
		return text[len_1:]

@eel.expose
def prin(text,file):
	print(text)

eel.start("RSA.html",size=(500,500))