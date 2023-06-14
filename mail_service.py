
import smtplib

# sending an email (accepts recipient email, message and optional subject line
def send_email_pothodet(mailToEmail, message, subject="New notification from Pothole App!"):
    try:
        gmailaddress = "dothodet2023@gmail.com" # EMAIL ADDRESS HERE
        gmailpassword = "Pothodet2023captsone!" # EMAIL PASSWORD HERE
        mailto = mailToEmail
        msg = 'From: PotHoDet App\nSubject: {}\n\n{}'.format(subject, message)
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(gmailaddress, gmailpassword)
        mailServer.sendmail(gmailaddress, mailto, msg)
        mailServer.quit()
        return ("Email Sent")
    except:
        return ("Email Not Sent")
