import qrcode
#taking upi id as input
upi_id= input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the  payment URL based on the UPI ID and the payment app you can modify these urls 

phonepe_url=f"upi://pay?pa={upi_id}&pn=Recipent%20Name&tn=Bhagban ke nam pe kuch de de"
paytm_url=f"upi://pay?pa={upi_id}&pn=Recipent%20Name"
googlepay_url=f"upi://pay?pa={upi_id}&pn=Recipent%20Name"

#Create Qr code for each payment app

phonepe_qr= qrcode.make(phonepe_url)
paytm_qr= qrcode.make(paytm_url)
googlepay_qr= qrcode.make(googlepay_url)

#save the qr code to image(optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
googlepay_qr.save("googlepay_qr.png")

phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()