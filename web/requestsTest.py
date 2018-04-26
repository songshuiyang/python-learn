# 从Web下载文件 不是Python自带， 需要导入pip install requests
import requests
response = requests.get('http://songshuiyang-oss.oss-cn-shenzhen.aliyuncs.com/blogsys/upload/%E6%96%87%E4%BB%B6%E5%90%8D.txt')
print('文件类型: ' + str(type(response)))
print(len('字符长度: ' + response.text))
print('输出字符: ' + response.text[:250])
print('状态码: ' + str(response.status_code))

# 保存文件
writeFile = open('test.txt', 'wb')
for chunk in response.iter_content(1000000):
    writeFile.write(chunk)

writeFile.close()