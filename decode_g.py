from cipher import password_decrypt

# CHANGE THIS TO YOUR TOKEN AND KEY
token_file = './token.dat'
key_file = './key.dat'

with open(key_file, 'r') as kf:
    key = kf.read()

with open(token_file, 'r') as tf:
    token = str.encode(tf.read())

decrypt = password_decrypt(token, key)

print('[INFO] Succesfully decrypted token\n')

print('---START---')
print(decrypt)
print('---END---')
