import os

os_name = os.name

if os_name == 'nt':
    OS = 'win64'
elif os_name == 'posix':
    OS = 'mac-arm64'

URL = 'https://cathaypacific.queue-it.net/?c=cathaypacific&e=hkewowflyandshinehk&cid=en-US&l=HKEXPRESS%20WOW2.0%20FlyAndShine%20%28Campaign_HK%29&t_wowParamUrl=hk/en-hk'

CHROMEDRIVER_URL = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json'

TOTAL_TABS = 30

YOUR_TURN_ELEMENT_ID = 'first-in-line'

TRY_ELEMENT_ID = 'MainPart_lbWhichIsIn'