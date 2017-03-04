import smtplib

sender = "noreply.sodexoapp@gmail.com"
to = input("Para: ")
subject = input("Assunto: ")
headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % \
											(sender, to, subject)
email = input("Enviar para: ")
msg = headers + input("Mensagem: ")

#A linha abaixo configura endereço de servidor e porta de entrada
mailserver = smtplib.SMTP("smtp.gmail.com", 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login("noreply.sodexoapp@gmail.com", "sodexoapp")
mailserver.sendmail("noreply.sodexoapp@gmail.com",\
								email, msg)
mailserver.close()
print("Mensagem Enviada")
