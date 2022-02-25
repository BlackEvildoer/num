import requests
#Ø§Ø°ÙƒØ± Ø§Ù„Ù…ØµØ¯Ø± ÙˆØ§Ù„Ù…Ø·ÙˆØ± Ù„Ø§ ØªØºÙŠØ± Ø­Ù‚ÙˆÙ‚ ðŸ™‚
print('BY BLACK MIROR ')
print("\n~~~~~~~~~~~~~~~~~~~")
print("\nINFO phone _ SHORT LINKS")
print("~~~~~~~~~~~~~~~~~~~")
Inf=int(input('1] Info Phone Num\n2] Short Urls\n___________________\n>'))
if Inf==1:
	NuM=input('[?] Phone Num :\n')
	req9=requests.post(f'http://cvcbnhfuu.ml/HMD/api/Number.php?phone={NuM}')
	print('Number: '+req9.json()['Number'])
	print('Location: '+req9.json()['Location'])
	print('Country: '+req9.json()['Country'])
	print('Valid Number: '+req9.json()['Valid Number'])
	print("--------------------------------------")
	print('Api Developer: '+str(req9.json()['Developer']))
	print("--------------------------------------")
elif Inf==2:
	Long_Url=input('[?] Type The Link:\n')
	print("--------------------------------------")
	req1=requests.post(f'http://cvcbnhfuu.ml/HMD/api/ShortURL.php?url={Long_Url}')
	print("--------------------------------------")
	print('URL after Shorting: '+req1.json()['ShortURL'])
	print("--------------------------------------")
	print('Url befor shorting: '+req1.json()['LongURL'])
	print("--------------------------------------")
	print('Api Developer: '+str(req1.json()['Developer']))
	print("--------------------------------------")

