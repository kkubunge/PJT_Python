with open('temp.txt', 'r') as file:
    upload_time = []
    instagram_upload = []
    is_upload_time = False
    is_instagram_upload = False

    for line in file:
        line = line.strip()
        if line == '[Upload Time]':
            is_upload_time = True
            is_instagram_upload = False
        elif line == '[Instargram Upload]':
            is_upload_time = False
            is_instagram_upload = True
        elif is_upload_time and line and not line.startswith(';'):
            upload_time.append(line)
        elif is_instagram_upload and line and not line.startswith(';'):
            product_id, url = line.split('\t')
            instagram_upload.append((product_id, url))

    file.close()

print("========================================")
print('Upload Time:', upload_time)
print('Instagram Upload:', instagram_upload)

uploadTime_new = '230120'
productID_new = '412311'
productUrl_new = 'www.wonik.com'

upload_time.insert(0, uploadTime_new)
instagram_upload.insert(0, productID_new, productUrl_new)

with open('temp.txt', 'r+') as file:
    is_upload_time = False
    is_instagram_upload = False

    for line in file:
        line = line.strip()

        if line == '[Upload Time]':
            is_upload_time = True
            is_instagram_upload = False
        elif line == '[Instargram Upload]':
            is_upload_time = False
            is_instagram_upload = True

        if is_upload_time or is_instagram_upload or line.startswith(';'):
            file.write(line + '\n')

    file.close()
