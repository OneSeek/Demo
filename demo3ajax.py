from selenium import webdriver

#其他浏览器把Chrome换名就行
#option = webdriver.ChromeOptions()
#option.set_headless() 设置无头浏览器，就是隐藏界面后台运行

driver = webdriver.Chrome()

#创建driver实例

#driver = webdriver.Chrome(chrome_options=option)  创建实例并载入option

url = '**********'
driver.get(url)

#driver.maximize_window() 最大化窗口
#driver.set_window_size(width,height) 设置窗口大小

print(driver.page_source)
#打印网页源码
driver.quit()
# 关闭浏览器
