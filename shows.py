#!/usr/bin/python3
import requests
import json
import re
from bs4 import BeautifulSoup as b4
class dl:
        def __init__(self, url, tk):
                self.url = url
                self.tk = tk
        def generate(self):
                r = requests.get(self.url)
                if r.status_code == 200:
                        try:
                                a = b4(r.content, 'html5lib')
                                b = a.find_all("script")[9].prettify()
                                c = json.loads(b[39:-11])["EpisodeDetail"]["episodeData"]['hls'][0].replace('drm', 'hls')
                                xm = requests.get(self.tk)
                                gj = json.loads(xm.content.decode('utf-8'))['video_token']
                                if "index.m3u8" in c:
                                    print ("\n Generating link.....")
                                    pr = ("https://zee5vod.akamaized.net" + c + gj)
                                    g6 = requests.get(pr)
                                    c2 = g6.content.decode()
                                    print ("""
                                            AVAILABLE QUALITIES:
                                                1️⃣ ~ 96p
                                                2️⃣ ~ 144p
                                                3️⃣ ~ 240P
                                                4️⃣ ~ 360P
                                                5️⃣ ~ 480P
                                                6️⃣ ~ 576P
                                                7️⃣ ~ 720P
                                                8️⃣ ~ 1080P
                                        """)
                                    ZC = int(input('\n Enter choice : '))
                                    if ZC == 1:
                                        G = re.findall('index.*',c2)[7]
                                        print ('\n',pr.replace('index.m3u8', G))
                                    elif ZC == 2:
                                        V = re.findall('index.*',c2)[0]
                                        print ('\n',pr.replace('index.m3u8', V))
                                    elif ZC == 3:
                                        Z = re.findall('index.*',c2)[1]
                                        print ('\n',pr.replace('index.m3u8', Z))
                                    elif ZC == 4:
                                        X = re.findall('index.*',c2)[2]
                                        print ('\n',pr.replace('index.m3u8',X))
                                    elif ZC == 5:
                                        N = re.findall('index.*',c2)[3]
                                        print ('\n',pr.replace('index.m3u8', N))
                                    elif ZC == 6:
                                        B = re.findall('index.*',c2)[4]
                                        print ('\n',pr.replace('index.m3u8', B))
                                    elif ZC == 7:
                                        L = re.findall('index.*',c2)[5]
                                        print ('\n',pr.replace('index.m3u8',L))
                                    elif ZC == 8:
                                        K = re.findall('index.*',c2)[6]
                                        print ('\n',pr.replace('index.m3u8',K))
                                elif "master.m3u8" in c:
                                    d5 = requests.get(c + gj)
                                    do = d5.content.decode('utf-8')
                                    print ("""
                                        LIST OF QUALITIES AVAILABLE:
                                            1️⃣ ~ 144p
                                            2️⃣ ~ 240p
                                            3️⃣ ~ 360p
                                            4️⃣ ~ 480p
                                    """)
                                    sg = int(input('\n Enter Quality :'))
                                    if sg == 1:
                                        a5 = re.findall('index.*',do)[0]
                                        print ('\n\n',c[:-11] + a5)
                                    elif sg == 2:
                                        x4 = re.findall('index.*',do)[1]
                                        print ('\n\n',c[:-11] + x4)
                                    elif sg == 3:
                                        c8 = re.findall('index.*',do)[2]
                                        print ('\n\n',c[:-11] + c8)
                                    elif sg == 4:
                                        bh = re.findall('index.*',do)[3]
                                        print ('\n\n',c[:-11] + bh)
                        except KeyboardInterrupt:
                                print ("quit")
az = input('\n Enter TvShow link : ')
zx = dl(az, "https://useraction.zee5.com/token/")
zx.generate()