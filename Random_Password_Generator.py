import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits+ string.punctuation
password = ""
for _ in range(8):
    password = password + str(random.choice(characters))

print("Generated Password:", password)


#To increase the size of the password
#you can increase the range size as desirable

