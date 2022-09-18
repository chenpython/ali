import requests
import json


headers = {
    "authority": "gateway.jiangongdata.com",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; VOG-AL10; FISCore 5.3.0.312; GMSCore 20.15.16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 FZSUCKBrowser/11.1.2.210 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Windows\"",
    "origin": "https://www.jiangongdata.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.jiangongdata.com/",
    "accept-language": "zh-CN,zh;q=0.9"
}

url = "http://gateway.jiangongdata.com/jian-butler-member-biz/login/loginByUsername"
data = {
    "mobile": "18580848116",
    "password": "1548545312aa",
    "loginName": "18580848116",
    "params": {
        "sig": "05XqrtZ0EaFgmmqIQes-s-CP7pktvqSyqZwPxWKWo8i4wPUIa6t0yBQwqap5n9HUeFmNuBUuX9Qbue8i6UYLvzL6l_oFAevYCgMuraP-KAPTd5NTtQa_I-ypNW3z-16fznJ3ar0ypjrMQhm5IpsP40kNu1BjhgR5FJxE-BZRRrCuK2ATVZ53XNpKbZSxnHiTkxOrcvuHf-YvsOIwOLBBapAMMJOGBvDVcqqL0E9GRB7EGID5OqBPEd2_D3dQSviHdJzlam9hp0hadISturm59cQ1BkZg3rHYsB6UweXQww72ohk2eV4vZkUBBUfeNIRR_sQywLWTtByEnWd6YicaANIPK1NxG8J_oMA9kEneC8jjmbH7LEOQWZZyqt9iy-4BFmkkx3UZrbNC4Cc8R9_x1mvzeS860tAuZ2BLxLHZkWG1Q",
        "sessionId": "01UN1tyQuhV6YatPVUtvSed268gT1fuSPY0V97hyr8qE5dvGvUWUs1Ue5prwQcO9QWN8HPWMx6QlMWV-Nw9LKhFln6-0AXmw2z9nEi93BnEETvxkayohH2h8G5Br4fYayOuvKFK83A1vsZQc391Nqjm2L-BmwooyR1AZiCdvfStIk_A6ellcUIQcOI-1kMt9Lh",
        "token": "FFFF0N0000000000A971: register:1663470192022:0.15929684161112556",
        "sign": "05XqrtZ0EaFgmmqIQes-s-CP7pktvqSyqZwPxWKWo8i4wPUIa6t0yBQwqap5n9HUeFmNuBUuX9Qbue8i6UYLvzL6l_oFAevYCgMuraP-KAPTd5NTtQa_I-ypNW3z-16fznJ3ar0ypjrMQhm5IpsP40kNu1BjhgR5FJxE-BZRRrCuK2ATVZ53XNpKbZSxnHiTkxOrcvuHf-YvsOIwOLBBapAMMJOGBvDVcqqL0E9GRB7EGID5OqBPEd2_D3dQSviHdJzlam9hp0hadISturm59cQ1BkZg3rHYsB6UweXQww72ohk2eV4vZkUBBUfeNIRR_sQywLWTtByEnWd6YicaANIPK1NxG8J_oMA9kEneC8jjmbH7LEOQWZZyqt9iy-4BFmkkx3UZrbNC4Cc8R9_x1mvzeS860tAuZ2BLxLHZkWG1Q"
    }
}
data = json.dumps(data)
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)