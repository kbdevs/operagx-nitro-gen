import requests
import time


url = 'https://api.discord.gx.games/v1/direct-fulfillment'
headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
}
data = {
    'partnerUserId': '522951b8bd19bfb7b8e836fede6810ac3ba424244f159bc23b12888f8e78c6a4'
}
while True:
    response = requests.post(url, headers=headers, json=data)

    with open('response.txt', 'a') as file:
        file.write(response.text + '\n')

    print(response.text)
    time.sleep(5)

# https://discord.com/billing/partner-promotions/1180231712274387115/TOKEN_HERE