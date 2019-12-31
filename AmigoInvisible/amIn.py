# Enviar correo Gmail con Python
# www.pythondiario.com


#Para que GMAIL admita esta fuente como válida activar esta opción: https://myaccount.google.com/lesssecureapps


import random, smtplib, socket, sys, getpass
 
Ali_Luis = 0
Jav_Chus = 0
Ire_Andr = 0
Gui_Dani = 0
    
def main():
 
    global Ali_Luis, Jav_Chus, Ire_Andr, Gui_Dani 
    
    # Conexion con el servidor 
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        print "Conexion exitosa con Gmail"
        print "Concectado a Gmail"
    # Datos 
        try:
            gmail_user = str(raw_input("Escriba su correo: ")).lower().strip()
            gmail_pwd = getpass.getpass("Escriba su password: ").strip()
            smtpserver.login(gmail_user, gmail_pwd)
        except smtplib.SMTPException:
            print ""
            print "Autenticacion incorrecta" + "\n"
            smtpserver.close()
            getpass.getpass("Presione ENTER para continuar...")
            sys.exit(1)
 
 
    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
        print "Fallo en la conexion con Gmail"
        print getpass.getpass("Presione ENTER para continuar...")
        sys.exit(1)
 
 
    """while True:
        to = str(raw_input("Enviar correo a: ")).lower().strip()
        if to != "":
            break
        else:
            print "El correo es necesario!!!"
    """

    sub = "Amigo Invisible"                  #str(raw_input("Asunto: ")).strip()
    
    #Ali_Luis
    to = "@gmail.com" #TODO

    bodymsg = """
Hola a todos!!

Feliz Navidad! Este es un mensaje automatico, pero no quita la alegria que me da, a mi como maquina, asignarte tu objetivo para este amigo invisible fiestero.

El juego esta estructurado por parejas: Alicia y Luis, Irene y Andrej, Javier y Chusa y los maravillosos Daniel y Guille!!!
Se mandara un solo mail por pareja, las reglas son las siguientes:
    Precio Maximo:  50 Chavos por pareja
    Precio Minimo:  0 Lereles
    Dia de entrega: En Reyes, pos claro
Y sin mas preambulos, tu objetivo a regalar es....
...
. . .
.   .   .
    """ + getRegalado(Ali_Luis) + """
.   .   .
. . .
...
Enhorabuena!!
Que comience el espectaculo!!

Danieluris ;)

P.D.: A quien se haya dado cuenta, el mensaje esta sin acentos... Lo se, problemas de la programacion, perdonadme la vida
A quien no se haya dado cuenta. Ay....
    """
    print ""
    header = "Para: " + to +"\n" + "De: " + gmail_user + "\n" + "Asunto: " + sub + "\n"
    print header
    msg = header + "\n" + bodymsg + "\n\n"
    #print msg
 
    try:
        smtpserver.sendmail(gmail_user, to, msg)
    except smtplib.SMTPException:
        print "El correo no pudo ser enviado" + "\n"
        smtpserver.close()
        getpass.getpass("Presione ENTER para continuar...")
        sys.exit(1)
 
        print "El correo se envio correctamente" + "\n"
        smtpserver.close()
        getpass.getpass("Presione ENTER para continuar")
        sys.exit(1)


    #Ire y Andrej
    to = "@hotmail.com" #TODO

    bodymsg = """
Hola a todos!!

Feliz Navidad! Este es un mensaje automatico, pero no quita la alegria que me da, a mi como maquina, asignarte tu objetivo para este amigo invisible fiestero.

El juego esta estructurado por parejas: Alicia y Luis, Irene y Andrej, Javier y Chusa y los maravillosos Daniel y Guille!!!
Se mandara un solo mail por pareja, las reglas son las siguientes:
    Precio Maximo:  50 Chavos por pareja
    Precio Minimo:  0 Lereles
    Dia de entrega: En Reyes, pos claro
Y sin mas preambulos, tu objetivo a regalar es....
...
. . .
.   .   .
    """ + getRegalado(Ire_Andr) + """
.   .   .
. . .
...
Enhorabuena!!
Que comience el espectaculo!!

Danieluris ;)

P.D.: A quien se haya dado cuenta, el mensaje esta sin acentos... Lo se, problemas de la programacion, perdonadme la vida
A quien no se haya dado cuenta. Ay....
    """
    print ""
    header = "Para: " + to +"\n" + "De: " + gmail_user + "\n" + "Asunto: " + sub + "\n"
    print header
    msg = header + "\n" + bodymsg + "\n\n"
    #print msg
 
    try:
        smtpserver.sendmail(gmail_user, to, msg)
    except smtplib.SMTPException:
        print "El correo no pudo ser enviado" + "\n"
        smtpserver.close()
        getpass.getpass("Presione ENTER para continuar...")
        sys.exit(1)
 
        print "El correo se envio correctamente" + "\n"
        smtpserver.close()
        getpass.getpass("Presione ENTER para continuar")
        sys.exit(1)


    #Javier y Chus
    to = "@gmail.com" #TODO

    bodymsg = """
Hola a todos!!

Feliz Navidad! Este es un mensaje automatico, pero no quita la alegria que me da, a mi como maquina, asignarte tu objetivo para este amigo invisible fiestero.

El juego esta estructurado por parejas: Alicia y Luis, Irene y Andrej, Javier y Chusa y los maravillosos Daniel y Guille!!!
Se mandara un solo mail por pareja, las reglas son las siguientes:
    Precio Maximo:  50 Chavos por pareja
    Precio Minimo:  0 Lereles
    Dia de entrega: En Reyes, pos claro
Y sin mas preambulos, tu objetivo a regalar es....
...
. . .
.   .   .
    """ + getRegalado(Jav_Chus) + """
.   .   .
. . .
...
Enhorabuena!!
Que comience el espectaculo!!

Danieluris ;)

P.D.: A quien se haya dado cuenta, el mensaje esta sin acentos... Lo se, problemas de la programacion, perdonadme la vida
A quien no se haya dado cuenta. Ay....
    """
    print ""
    header = "Para: " + to +"\n" + "De: " + gmail_user + "\n" + "Asunto: " + sub + "\n"
    print header
    msg = header + "\n" + bodymsg + "\n\n"
    #print msg
 
    try:
        smtpserver.sendmail(gmail_user, to, msg)
    except smtplib.SMTPException:
        print "El correo no pudo ser enviado" + "\n"
        smtpserver.close()
        getpass.getpass("Presione ENTER para continuar...")
        sys.exit(1)
 
        print "El correo se envio correctamente" + "\n"
        smtpserver.close()
        getpass.getpass("Presione ENTER para continuar")
        sys.exit(1)


    #Daniel y Guille
    to = "@gmail.com" #TODO 

    bodymsg = """
Hola a todos!!

Feliz Navidad! Este es un mensaje automatico, pero no quita la alegria que me da, a mi como maquina, asignarte tu objetivo para este amigo invisible fiestero.

El juego esta estructurado por parejas: Alicia y Luis, Irene y Andrej, Javier y Chusa y los maravillosos Daniel y Guille!!!
Se mandara un solo mail por pareja, las reglas son las siguientes:
    Precio Maximo:  50 Chavos por pareja
    Precio Minimo:  0 Lereles
    Dia de entrega: En Reyes, pos claro
Y sin mas preambulos, tu objetivo a regalar es....
...
. . .
.   .   .
    """ + getRegalado(Gui_Dani) + """
.   .   .
. . .
...
Enhorabuena!!
Que comience el espectaculo!!

Danieluris ;)

P.D.: A quien se haya dado cuenta, el mensaje esta sin acentos... Lo se, problemas de la programacion, perdonadme la vida
A quien no se haya dado cuenta. Ay....
    """
    print ""
    header = "Para: " + to +"\n" + "De: " + gmail_user + "\n" + "Asunto: " + sub + "\n"
    print header
    msg = header + "\n" + bodymsg + "\n\n"
    #print msg
 
    try:
        smtpserver.sendmail(gmail_user, to, msg)
    except smtplib.SMTPException:
        print "El correo no pudo ser enviado" + "\n"
        smtpserver.close()
        getpass.getpass("Presione ENTER para continuar...")
        sys.exit(1)
 
        print "El correo se envio correctamente" + "\n"
        smtpserver.close()
        getpass.getpass("Presione ENTER para continuar")
        sys.exit(1)

def getRandom():
    global Ali_Luis, Jav_Chus, Ire_Andr, Gui_Dani  
    
    while(Ali_Luis == 0):    
        Ali_Luis = random.randint(2, 4)
    while(Jav_Chus == 2 or Ali_Luis == Jav_Chus or Jav_Chus == 0):
        Jav_Chus = random.randint(1, 4)
    while(Ire_Andr == 3 or Ire_Andr == Ali_Luis or Ire_Andr == Jav_Chus or Ire_Andr == 0):
        Ire_Andr = random.randint(1, 4)
    while(Gui_Dani == 4 or Gui_Dani == Ali_Luis or Gui_Dani == Jav_Chus or Gui_Dani == Ire_Andr or Gui_Dani == 0):
        Gui_Dani = random.randint(1, 4)    

def getRegalado(target):    
    if(target == 1):
        return "Alicia y Luis"
    elif(target == 2):
        return "Javier y Chusa"
    elif(target == 3):
        return "Irene y Andrej"
    elif(target == 4):
        return "Daniel y Guille"
    
getRandom()
main()








