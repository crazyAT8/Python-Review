import hashlib 

email = "william.watson2@usbank.com"

# Encode the email address as a bytes object
email_bytes = email.encode('utf-8')

#Create a new SHA-256 hash object
sha256 = hashlib.sha256()

# Update the hash object with the email address
sha256.update(email_bytes)

# Get the hexadecimal representation of the hash
email_hash = sha256.hexdigest()

print(email_hash)