import smtplib as smt
from colorama import Fore
print(Fore.CYAN + '''

███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
█████╗░░██╔████╔██║███████║██║██║░░░░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
███████╗██║░╚═╝░██║██║░░██║██║███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
''')

sender_email = (str(input("Enter Email: ")))
password = (str(input("Enter Password To Email: ")))
rec_email = (str(input("Enter Recieving Email: ")))
message = (str(input("Enter Content Of Message: ")))
num_times = int(input("Enter How Many Times: "))


for i in range(num_times):
    server = smt.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Login Sucess")
    server.sendmail(sender_email,rec_email,message)
    print("Email Sent")