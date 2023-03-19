# import asyncio
# import requests

# username = "Rass"
# headers = {"Username": username}
# jsons = {'image': open("osfiles/garage/test/MarkerOf.png", "rb")}
# response = requests.post(url="http://localhost:4755/sendPhoto/Coppa", files=jsons, headers=headers)

# print(response.text)





# import gevent 
# from gevent import socket


# urls = [
#     "asp.com",
#     "youtube.com",
#     "facebook.com",
#     "netflex.com"
# ]

# oppers = [gevent.spawn(socket.gethostbyname, url) for url in urls]
# gevent.joinall(oppers, timeout=2)
# [print(hinter.value, hinter.name ) for hinter in oppers]


