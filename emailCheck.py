# Python program to validate an Email 

# import re module 

import re 

# Buat Ekspresi Reguler 
# untuk memvalidasi email 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	
# Tetapkan fungsi untuk
# untuk memvalidasi Email
def check(email): 

	#Kondisi untuk check email 
	if(re.search(regex,email)): 
		print("Email Kamu Valid Bro!") 
		
	else: 
		print("Email Kamu Invalid Bro , Silahkan Coba Lagi!") 
	

# Driver Code 
if __name__ == '__main__' : 
	
	# User menginput email
	email = raw_input("Masukan Email Mu mzz : ")
	
	# menjalankan fungsi
	check(email) 

