import smtplib as s

ob= s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("sku.globaliasoft", "sweta9801") 

subject = "Sending email using python"
body = "This is first email sending"
message = "Subject:{}\n\n{}".format(subject,body)
# print(message)

listOfAddress = ["sku.globaliasoft@gmail.com"]
ob.sendmail("sku.globaliasoft", listOfAddress, message)
print("Sent Successfully")
ob.quit()