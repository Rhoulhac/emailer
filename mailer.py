import smtplib

def send_emails(emails, schedule, forecast):
    # Connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    server.starttls()

    # Login
    # from_email = input("Enter a gmail account ")
    from_email = 'grr.programming@gmail.com'
    password = input("What is your email password? ")
    server.login(from_email,password)

    # Send to entire email list
    for to_email, name in emails.items():
        message = "Subject: Welcome to Iowa!\n"
        message += "Hello " + name + "!\n\n"
        message += forecast + "\n\n"
        message += schedule + "\n\n"
        message += "Enjoy your day!"
        server.sendmail(from_email, to_email, message)
        
    server.quit()
