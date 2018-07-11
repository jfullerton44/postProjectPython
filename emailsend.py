import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sendMail(emailaddr):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("ixoverify@gmail.com", "IXOverification1")

    with open('project.json') as json_data:
        d = json.load(json_data)
        #print(d)
    json_mylist = json.dumps(d, separators=(',',':'))

    msg = "YOUR MESSAGE!"

    msg = MIMEMultipart()

    fromaddr = "ixoverify@gmail.com"

    # Where to send JSON to be verified
    toaddr = emailaddr

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Verification of New Project"

    body = " Thank you for your interest in creating a project. \nIn order to finalize" \
           " your project in our system please visit this link (https://ixo-create-project.herokuapp.com/) and paste the" \
           " text below into the text box and click ixo Sign and Verify. \n \n"+ json_mylist + "\n"

    msg.attach(MIMEText(body, 'plain'))

    filename = "project.json"
    attachment = open("project.json", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)


    text = msg.as_string()
    try:
        server.sendmail(fromaddr, toaddr, text)
        print "Sent email to address:   " + toaddr
    except:
        print "Invalid Email"
    server.quit()
