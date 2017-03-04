import smtplib

def send_mail(to, address):

    sender = "noreply.sodexoapp@gmail.com"
    subject = input('Assunto: ')
    headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % \
                                                (sender, to, subject)
    msg = headers + input('Mensagem: ')

    print('Enviando email para %s para o endereco %s..' % (to, address))   

    #A linha abaixo configura endereço de servidor e porta de entrada
    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login("noreply.sodexoapp@gmail.com", "sodexoapp")
    mailserver.sendmail("noreply.sodexoapp@gmail.com",\
                                    address, msg)
    mailserver.close()
    print("Mensagem Enviada")

def init():
    to = input('Enviar para: ')
    address = input('Email: ')
    send_mail(to, address)
 

if __name__=='__main__':
    init()