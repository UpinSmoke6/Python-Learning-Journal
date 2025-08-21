contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

new_contact = input("Enter Name:")
new_email = input("Enter email:")
contact_emails[new_contact] = new_email

for c in contact_emails:
    print('{} is {}'.format(contact_emails[c], c))