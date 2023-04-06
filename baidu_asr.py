import base64
import urllib
import requests
import json


def get_speech_text(file_path, API_KEY, SECRET_KEY):
        
    url = "https://vop.baidu.com/server_api"
    
    # speech 可以通过 get_file_content_as_base64("C:\fakepath\0000.wav",False) 方法获取
    payload = json.dumps({
        "format": "wav",
        "rate": 16000,
        "channel": 1,
        "cuid": "1aa72600",
        "token": get_access_token(API_KEY, SECRET_KEY),
        "speech": get_file_content_as_base64(file_path),
        "len": get_len(file_path)
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

def get_len(file_path):
    with open(file_path, "rb") as f:
        d = f.read()
    return len(d)

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content

def get_access_token(API_KEY, SECRET_KEY):
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
