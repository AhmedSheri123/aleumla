import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "ahmedsheri324@gmail.com"
password = "ahmed.sheri.as"


def send_email(receiver_email, username, href):

    message = MIMEMultipart("alternative")
    message["Subject"] = "تفعيل الحساب"
    message["From"] = "العملة"
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = f"""\
<html>
<body style="background-color:#FFFFFF; padding:0;  margin: 0;">
<div style="text-align:left;">
  <div style="vertical-align: top; position:relative; display: inline-block; width:100%; min-height:559px; background-color:#F1F1F1; " id="container_8538c1f">
    <div style="text-align:left;">
      <div style="vertical-align: top; position:relative; display: inline-block; width:100%; min-height:87px; background-color:#F1F1F1; " id="container_26be2b">
        <div style="margin: 30px 10px 10px 10px;display: block; " id="container_26be2b_padding" >
          <div style="text-align:center;">
            <span style="font-size:20pt; font-family:Arial, Helvetica, sans-serif; color:#3FCD99; font-weight:bold; ">{username} مرحبا بك يا </span>
            </div>
          </div>
        </div>
      <div style="vertical-align: top; position:relative; display: inline-block; width:100%; min-height:201px; background-color:#3FCD99; " id="container_54a1c552">
        <div style="margin: 10px; display: block; " id="container_54a1c552_padding" >
          <div style="text-align:center;">
            <span style="font-size:16pt; font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; ">يجب عليك تفعيل حسابك في موقع </span>
            <span style="font-size:20pt; font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; font-weight:bold; text-shadow: 2px 2px 2px #000000; ">العملة</span>
            <span style="font-size:16pt; font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; "> ليمكنك الحصول على المزيد من الميزات<br/><br/>لتفعيل حسابك اضغط على الزر الموجود في الاسفل</span>
            </div>
          <div style="text-align:left;">
            <div style="vertical-align: top; position:relative; display: inline-block; width:100%; min-height:96px; background:none; " id="container_45c793e9">
              <div style="margin: 30px 10px 10px 10px;display: block; " id="container_45c793e9_padding" >
                <div style="text-align:center;">
                  <a href="{href}" target="_blank" style="text-decoration:none"><div style="box-sizing: border-box; vertical-align: bottom; border-radius: 9px; position:relative; display: inline-block; width:150px; height:40px; background:none; border: 2px solid #FEFFFE; " id="button_4789644e">
                    <div style="display: table; width: 100%; height: 100%;"><div style="display: table-cell; vertical-align: middle;">                      <div style="text-align:center;">
                        <span style="font-size:15pt; font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; font-weight:bold; ">تفعيل</span>
                        </div>
                      <div style="text-align:left;">
                        </div>
                      </div></div>
                    </div></a>
                  </div>
                <div style="clear:both"></div>
                </div>
              </div>
            </div>
          <div style="clear:both"></div>
          </div>
        </div>
      </div>
    </div>
  <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; "><br/></span>
  </div>
</body>
</html>    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )







def send_email_resetpass(receiver_email, username, href):

    message = MIMEMultipart("alternative")
    message["Subject"] = "تفعيل الحساب"
    message["From"] = "العملة"
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = f"""\
<html>
<body style="background-color:#FFFFFF; padding:0;  margin: 0;">
<div style="text-align:left;">
  <div style="vertical-align: top; position:relative; display: inline-block; width:100%; min-height:559px; background-color:#F1F1F1; " id="container_8538c1f">
    <div style="text-align:left;">
      <div style="vertical-align: top; position:relative; display: inline-block; width:100%; min-height:87px; background-color:#F1F1F1; " id="container_26be2b">
        <div style="margin: 30px 10px 10px 10px;display: block; " id="container_26be2b_padding" >
          <div style="text-align:center;">
            <span style="font-size:20pt; font-family:Arial, Helvetica, sans-serif; color:#3FCD99; font-weight:bold; ">{username} مرحبا بك يا </span>
            </div>
          </div>
        </div>
      <div style="vertical-align: top; position:relative; display: inline-block; width:100%; min-height:201px; background-color:#3FCD99; " id="container_54a1c552">
        <div style="margin: 10px; display: block; " id="container_54a1c552_padding" >
          <div style="text-align:center;">
            <span style="font-size:16pt; font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; ">يجب تغير كلمة المرور على موقع </span>
            <span style="font-size:20pt; font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; font-weight:bold; text-shadow: 2px 2px 2px #000000; ">العملة</span>
            <span style="font-size:16pt; font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; "> ليمكنك الدخول الى حسابك<br/><br/>لتغير كلمة المرور اضغط على الزر الموجود في الاسفل</span>
            </div>
          <div style="text-align:left;">
            <div style="vertical-align: top; position:relative; display: inline-block; width:100%; min-height:96px; background:none; " id="container_45c793e9">
              <div style="margin: 30px 10px 10px 10px;display: block; " id="container_45c793e9_padding" >
                <div style="text-align:center;">
                  <a href="{href}" target="_blank" style="text-decoration:none"><div style="box-sizing: border-box; vertical-align: bottom; border-radius: 9px; position:relative; display: inline-block; width:150px; height:40px; background:none; border: 2px solid #FEFFFE; " id="button_4789644e">
                    <div style="display: table; width: 100%; height: 100%;"><div style="display: table-cell; vertical-align: middle;">                      <div style="text-align:center;">
                        <span style="font-size:15pt; font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; font-weight:bold; ">تغير</span>
                        </div>
                      <div style="text-align:left;">
                        </div>
                      </div></div>
                    </div></a>
                  </div>
                <div style="clear:both"></div>
                </div>
              </div>
            </div>
          <div style="clear:both"></div>
          </div>
        </div>
      </div>
    </div>
  <span style="font-size:12pt; font-family:Arial, Helvetica, sans-serif; color:#000000; "><br/></span>
  </div>
</body>
</html>    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )



