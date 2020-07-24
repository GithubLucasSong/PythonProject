import requests
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Cookie':'aliyungf_tc=AQAAAPoe0xTjawkA89Ta3WOyH9ZuAGdD; acw_tc=2760823715925509256308582e213337880e88480c66d01e599cc874163e76; xq_a_token=ea139be840cf88ff8c30e6943cf26aba8ad77358; xqat=ea139be840cf88ff8c30e6943cf26aba8ad77358; xq_r_token=863970f9d67d944596be27965d13c6929b5264fe; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU5NDAwMjgwOCwiY3RtIjoxNTkyNTUwODkyMzQzLCJjaWQiOiJkOWQwbjRBWnVwIn0.fRAgP18IKA3T_toYc7bYT64p9IWvsJkDMMyMGv6Wl9qjLm_3qjV9_g9WUZDdGjMExTd-IQ5BA0pxQACVDaiPEff-6izQeOr7-7G5dVvp-erjAIdi_FPziRteSYunN7LPZfB_GZXaw5qEpcMOi6Uyq2gJW-hJBhCTRpFoxm11yncRRoD8VIhuleeq3gvoDX833GCJqlHw7Da-edhvxaa0Go1BQnMw-9OmMURuJtTP2owwM37IDLGL7WyrpaSQX9C5kSQV0VSwWliXDUkmrREknoew7uKhYd44o6wLFh8l-SwZ-7AGYfecWEqSxrgd1RWkag13U8QkX4oTH0G1eUN81A; u=101592550925932; Hm_lvt_1db88642e346389874251b5a1eded6e3=1592550926; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1592550963'
}

# json_data = requests.get(url, headers=headers, ).json()
sess = requests.session()
url = 'https://xueqiu.com/'
sess.get(url, headers=headers,)
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=66589&size=15'
# 已经表示携带cookie发起请求
json_data = sess.get(url, headers=headers,).json()
print(json_data)
