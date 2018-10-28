import csv
img = 'https://scontent.xx.fbcdn.net/v/t1.15752-9/44959178_324623451698802_997175768431722496_n.jpg?_nc_cat=104&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=980d0890b7ae2bff396423e2267b89c8&oe=5C7FE9D9'
text = '0.99'
with open('data/img.csv', 'w') as csvfile:
    csvfile.writelines(img)
    csvfile.writelines('\n')
    csvfile.writelines(text)


from bot.facebook import Messenger
messenger = Messenger()
messenger.get_message()