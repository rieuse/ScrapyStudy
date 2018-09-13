# from yarl import URL



# def url_skip(response_url, path):
#     # url_parent
#     if '../../' in path:
#         new_url = '/'.join(str(URL(response_url).parent).split('/')[:-2]) + path[5:]
#     elif '../' in path:
#         new_url = '/'.join(str(URL(response_url).parent).split('/')[:-1]) + path[2:]
#     else:
#         new_url = str(URL(response_url).parent) + path[1:]
#     return new_url

# raw_url = 'http://www.cs.com.cn/xwzx/hg/index.shtml'
# path = './201807/t20180717_5842682.html'

def url_skip(response_url, path):
    url = response_url.replace('.html','').replace('.shtml','')
    first_param = ''.join(url.split('/')[-1:])
    second_param = ''.join(url.split('/')[-2:-1])
    thrid_param = ''.join(url.split('/')[-3:-2])
    if '../../' in path:
        new_url = url.replace(first_param, '').replace(second_param, '').replace(thrid_param, '')[:-3] + path[5:]
    elif '../' in path:
        new_url = url.replace(first_param, '').replace(second_param, '')[:-2] + path[2:]
    else:
        new_url = url.replace(first_param, '') + path[2:]
    return new_url