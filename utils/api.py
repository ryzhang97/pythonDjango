import requests


def _get(url):
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 处理成功的响应
        data = response.json()  # 如果响应是JSON格式的话
        return data
    else:
        # 处理请求失败的情况
        return None


def _res(data, msg='ok', code=200):
    if data is None:
        return {'message': msg, 'code': code, 'data': None}
    else:
        return {'message': msg, 'code': code, 'data': data}
