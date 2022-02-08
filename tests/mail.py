# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

if __name__ == '__main__':

	output = get_contacts('contact.txt')
	template = read_template('message.txt')

	message = template.substitute(PERSON_NAME='Jeongseup')

	# print(output)
	print(message)

