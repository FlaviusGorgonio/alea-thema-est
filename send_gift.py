import random

def import_emails(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        email_string = fp.read()

    email_list = [email.strip() for email in email_string.split(';') if email.strip()]

    return email_list


def import_topics(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        topic_list = [linha.strip() for linha in fp if linha.strip()]
    return topic_list





###
### Main program
###

full_email_list = import_emails("student_email_list.txt")
print("Lista de e-mails:")
print("-----------------")
for email in full_email_list:
    print(email)
random.shuffle(full_email_list)
print(full_email_list)

print()
full_topic_list = import_topics("student_topic_list.txt")
print("Lista de temas para projeto:")
print("-----------------------------")
for topic in full_topic_list:
    print(topic)
random.shuffle(full_topic_list)
print(full_topic_list)

tam = len(full_email_list)
for i in range(tam):
    print(i+1, full_email_list[i], full_topic_list[i])

