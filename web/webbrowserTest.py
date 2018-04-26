# webbrowser python自带, 打开浏览器获取指定页面
# 在系统的默认浏览器中访问url地址，如果new=0,url会在同一个浏览器窗口中打开；如果new=1，新的浏览器窗口会被打开;new=2新的浏览器tab会被打开。
import webbrowser
webbrowser.open('http://songshuiyang.com/')

webbrowser.open('http://songshuiyang.com/', 1)

webbrowser.open('http://songshuiyang.com/', 2)
