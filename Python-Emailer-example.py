
emails=[]
try:
    email_file = open('emails.txt','r')

    for line in email_file:
            emails.append(line.strip())
except FileNotFoundError as err:
    print(err)

    #comment is great
print(emails)
