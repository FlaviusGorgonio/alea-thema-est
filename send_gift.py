def import_emails(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        email_string = fp.read()

    email_list = [email.strip() for email in email_string.split(';') if email.strip()]

    return email_list

email_full_list = import_emails("student_email_list.txt")
print(email_full_list)