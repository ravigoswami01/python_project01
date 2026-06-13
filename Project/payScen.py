import qrcode

# take upi id 

upi_id = input("Enter your Upi Id = ")

# uip ://pay?pa=upi_IDS


phonePay_Url = f"Upi://pay?pa={upi_id}&pn=Recipient%"


phonePay_Url =qrcode.make(phonePay_Url)

# for save the image 
phonePay_Url.save('phonepay_qr.png')

# show qr code 

phonePay_Url.show()

