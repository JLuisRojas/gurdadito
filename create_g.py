from cipher import password_encrypt

# CHANGE THIS TO YOUR DATA AND KEY
key_file = './key.dat'
data_file = './raw.dat'

# OUTPUT TOKEN
token_path = './token.dat'

with open(key_file, 'r') as kf:
    key = kf.read()

with open(data_file, 'r') as kf:
    raw_data = str.encode(kf.read())

token = password_encrypt(raw_data, key)

with open(token_path, 'w') as ft:
    ft.write("".join(map(chr, token)))

    print('[INFO] Succesfully created token')

