import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj=MIMEMultipart()

mesaj["From"]="hamzaaydin51@gmail.com"
mesaj["To"] ="hamzaaydin51@gmail.com"
mesaj["Subject"]="Python ile otomatik toplu mail gönderme denemesi"

yazi="""
Python smtp ile mail gönderme
Hamza Aydın
"""

mesaj_gövdesi=MIMEText(yazi,"plain") #normal yazı karakteri anlamında "plain"

mesaj.attach(mesaj_gövdesi) #birbirlerine bağlamış olduk


try:
    mail=smtplib.SMTP("smtp.gmail.com",587) #smtp objesini try'a atadık ki obje olarak bir sıkıntı çıkarsa hata mesajı alalım.(gmail de 587.port izin veriyor sadece)

    mail.ehlo() #böylece smtp objemize bağlandık

    mail.starttls() #gireceğimiz kullanıcı adı ve şifrelerimizin şifrelenmesi için bu metodu kullanıyoruz

    mail.login("hamzaaydin51@gmail.com","alkas0198.")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("mail başarıyla gönderildi")

    mail.close()

except:
    sys.stderr.write("bir sorun oluştu!!!\n")
    sys.stderr.flush()
    mail.close()


