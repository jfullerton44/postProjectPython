import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import emailcreds
import connecttodb

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

    objectID = connecttodb.addToDB(json_myschema,json_myform,json_mylist)

    #Creaete link to hosted page with the object ID from the database specified
    url = "https://ixo-create-project.herokuapp.com/?oidHex="+ objectID
    print url

    #Create body of email
    html1 = """\
    <html>
        <head></head>
        <body>
            <p>Hello, <br>Thank you for your interest in creating a project.
                <br><br>
                There is one final step to upload your project. Please visit
                <a href= {URL} >this link</a>, 
                and paste the schema, form and project details found below into their respective text boxes.
                <br><br><br>
                <b>Schema</b>
            </p>
        </body>
    </html>
    """
    html1 = html1.format(URL=url)
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

    html4 = """\
    <html>
        <head></head>
        <body>
            <p>
                <br>
                If you have any questions, just reply to this email.
                <br><br> Welcome to ixo.world!
                <br><br><br> Best wishes,
                <br> The ixo Team
            </p>
        </body> 
    </html>
     """

    complete = html1 + json_myschema + html2 + json_myform + html3 + json_mylist + html4

    msg.attach(MIMEText(complete, 'html'))
    text = msg.as_string()
    #Try to send email
    #If address is invalid print invalid email
    try:
        server.sendmail(fromaddr, toaddr, text)
        print "Sent email to address:   " + toaddr
    except:
        print "Invalid Email"
    server.quit()

