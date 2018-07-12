import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import emailcreds

# this function sends an email to a given email address containing information to
# finalize the creation of their project

def sendMail(emailaddr):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(emailcreds.login, emailcreds.password)

    with open('project.json') as json_data:
        d = json.load(json_data)
    json_mylist = json.dumps(d, separators=(',', ':'))

    print open('newForm.json')
    with open('newForm.json') as json_data:
        d = json.load(json_data)
    json_myform = json.dumps(d, separators=(',', ':'))
    print 'JSON DATA', json_myform

    with open('newSchema.json') as json_data:
        d = json.load(json_data)
    json_myschema = json.dumps(d, separators=(',', ':'))

    msg = "YOUR MESSAGE!"

    msg = MIMEMultipart()

    fromaddr = "ixoverify@gmail.com"

    # Where to send JSON to be verified
    toaddr = emailaddr

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Verification of New Project"

    html1 = """\
    <html>
        <head></head>
        <body>
            <p>Thank you for your interest in creating a project.
                <br><br>
                In order to finalize your project in our system please visit 
                <a href="https://ixo-create-project.herokuapp.com/">this link</a>, 
                and paste the schema, form, and project details found below into their respective text boxes.
                <br><br><br>
                <b>Schema</b>
            </p>
        </body>
    </html>
    """
    html2 = """\
    <html>
        <head></head>
        <body>
            <p>
                <br>
                <b>Form</b>
            </p>
        </body>
    </html>
    """

    html3 = """\
    <html>
        <head></head>
        <body>
            <p>
                <br>
                <b>Project Details</b>
            </p>
        </body>
    </html>
     """
    space = """\ <html><head></head><body></body><br><br><br></html>"""

    complete = html1 + json_myschema + html2 + json_myform + html3 + json_mylist + space

    msg.attach(MIMEText(complete, 'html'))


    text = msg.as_string()
    try:
        server.sendmail(fromaddr, toaddr, text)
        print "Sent email to address:   " + toaddr
    except:
        print "Invalid Email"
    server.quit()

