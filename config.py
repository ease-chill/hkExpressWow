import os

os_name = os.name

if os_name == 'nt':
    OS = 'win64'
elif os_name == 'posix':
    OS = 'mac-arm64'

URL = 'https://cathaypacific.queue-it.net/?c=cathaypacific&e=hkewowflyandshinegba&cid=en-US&t_wowParamUrl=gba/en-cn'

CHROMEDRIVER_URL = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json'

TOTAL_TABS = 30

YOUR_TURN_ELEMENT_ID = 'first-in-line'

TRY_ELEMENT_ID = 'MainPart_lbWhichIsIn'