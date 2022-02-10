#################################
# WEEKLY QUALITY TRACKING REPORT EMAIL
#######################################
import time
import pytz
from datetime import datetime, timedelta, timezone, date
from dateutil.tz import *

REPORTDATE=datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')

utc_hour = datetime.strptime(REPORTDATE,'%Y-%m-%d %H:%M:%S').hour
if utc_hour >= 14: #send alerts only after 3pm UTC = 10am EST
    if (date.today().weekday() == 3):#(1=Tuesday, 3=Thursday...)          
    
    #https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server
        ######################################
        # WEEKLY QUALITY TRACKING REPORT EMAIL
        #######################################
        import smtplib, ssl
        from email import encoders
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email.mime.image import MIMEImage
        ######################################################
        ######################################################

        HIGHLIGHT1=" "
        HIGHLIGHT2=" "
        HIGHLIGHT3=" "

        SENDER_EMAIL = ""
        REPLY_TO_ADDRESS = ""
#         RECEIVER_EMAIL = [""]
        RECEIVER_EMAIL = ["","",""]
        SENDER_EMAIL_PASSWORD=''

        message = MIMEMultipart('related')
        message["Subject"] = "SUBJECT {} {}".format(REPORTDATE, TZ_NAME)
        message["From"] = SENDER_EMAIL
#         message["To"] = RECEIVER_EMAIL
        message["To"] = ", ".join(RECEIVER_EMAIL)
        message.add_header('reply-to', REPLY_TO_ADDRESS)

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)
        msgText = MIMEText('')
        msgAlternative.attach(msgText)

        output_head="""\
        <html>
          <head></head>
          <body>"""
        output_body="Hello Red Hat Marketplace Team,<br><br>"
        output_body=output_body+"Here is this week's Quality Tracking Report - {} {}:<br><br>".format(REPORTDATE, TZ_NAME)
        output_body=output_body+"<a href='{}'>SUBJECT {}</a><br>".format(SUBJECT)
        output_body=output_body+"<br><b>HIGHLIGHTS: </b><br>"
        output_body=output_body+"<ul>"
        output_body=output_body+"<li>{}</li>".format(HIGHLIGHT1)
        output_body=output_body+"<li>{}</li>".format(HIGHLIGHT2)
        output_body=output_body+"<li>{}</li>".format(HIGHLIGHT3)
        output_body=output_body+"</ul><br>"
        output_images="<br>"
        output_images=output_images+"<center><br><img src='cid:image0' alt='ALT_TEXT0' style='width:600px;'></center><br>"
        output_images=output_images+"<center><br><img src='cid:image1' alt='ALT_TEXT1' style='width:600px;'></center><br>"
        output_links="<br><b>ADDITIONAL_STUFF_TITLE:</b>"
        output_links=output_links+"<ul>"
        output_links=output_links+"<li><a href='{}'>TITLE_OF_WEBPAGE0</a></li>".format(WEBPAGE_URL0)
        output_links=output_links+"<li><a href='{}'>TITLE_OF_WEBPAGE1</a></li>".format(WEBPAGE_URL1)
        output_links=output_links+"</ul><br><br>"
        output_signature="CLOSING_STATEMENT<br><br>"
        output_signature=output_signature+"Regards,<br>"
        output_signature=output_signature+"YOUR_NAME<br>"
        output_foot="""\
          </body>
        </html>
        """
        html=output_head+output_body+output_images+output_links+output_signature+output_foot

        # Turn into html MIMEText objects
        part2 = MIMEText(html, "html")
        message.attach(part2)

        def messageImage(file_name,image_id):
            fp = open(file_name, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            msgImage.add_header('Content-ID', image_id) # Define the image's ID as referenced above
            msgImage.add_header('Content-Disposition', 'inline', filename=file_name)
            return msgImage

        message.attach(messageImage('IMAGE0.png','<image0>')) 
        message.attach(messageImage('IMAGE1.png','<image1>'))


        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
            server.sendmail(
                SENDER_EMAIL, RECEIVER_EMAIL, message.as_string()
            )
