# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# 非竞拍的项目
# 实例化浏览器的对象，并赋予变量每次driver
driver = webdriver.Firefox()
# 最大化窗口
driver.maximize_window()
# 输入浏览器地址
driver.get("http://rural.whdev.vpclub.cn/#/Home?source=1280346551905972225")
time.sleep(2)
# 点击登录
driver.find_element_by_xpath('//span[text()="登录"]').click()
time.sleep(1)
# 输入账号密码
driver.find_element_by_xpath('//input[@placeholder="输入手机号"]').send_keys('13971296154')
driver.find_element_by_xpath('//input[@placeholder="输入密码"]').send_keys('baise2020!')
# 点击登录
driver.find_element_by_xpath('//div/button/span[text()="登录"]').click()
time.sleep(2)
# 点击我要挂牌
driver.find_element_by_xpath('//span[text()="我要挂牌"]').click()
time.sleep(1)
# 选择挂牌业务类型
driver.find_element_by_xpath('//div[@class="p_1" and text()="自定义"]').click()
time.sleep(1)
# 选择自定义类型
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[2]/form/div[2]/div['
                             '1]/div/div/div/span/span/i').click()
time.sleep(1)
driver.find_element_by_xpath('//span[text()="水产"]').click()
time.sleep(1)
# 输入标的名称信息
driver.find_element_by_xpath('//input[@placeholder="请输入标的名称"]').send_keys('脚本录入测试标非竞拍')
time.sleep(2)
# 选择标的地区，
driver.find_element_by_xpath('//span/i[@class="el-input__icon el-icon-arrow-down"]').click()
time.sleep(2)
# 选择地区
driver.find_element_by_xpath('//span[@class="el-cascader-node__label" and text()="平果市"]').click()
time.sleep(1)
driver.find_element_by_xpath('//span[text()="马头镇"]').click()
time.sleep(2)
# 输入详细地址
driver.find_element_by_xpath('//input[@placeholder="请输入详细地址（如村、庄等）"]').send_keys('光谷测试中心')
time.sleep(1)
# 请输入标的数量
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[2]/form/div[2]/div[5]/div/div[1]/input').send_keys('500')
# 输入标的单位
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="请输入标的单位"]').send_keys('平方')
# 选择转让期限
driver.find_element_by_xpath('//span[@class="el-radio-button__inner"]').click()
time.sleep(1)
# 输入标的信息
driver.find_element_by_xpath(
    '//*[@id="app"]/div/section/div/div/div[2]/div/div[2]/form/div[2]/div[11]/div[2]/input').send_keys('500')
# 选择非竞拍
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[2]/form/div[4]/div[1]/div/div/label['
                             '2]/span[1]/span').click()
# 输入标的价格
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[2]/form/div[4]/div[2]/div[1]/div/div['
                             '1]/input').send_keys('5000')
# 选择是否预付款
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[2]/form/div[4]/div[2]/div['
                             '2]/div/div/div[1]/span/span/i').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span').click()
# 上输入联系电话
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[2]/form/div[6]/div[4]/div/div[1]/input').send_keys('13971296154')
# 点击提交
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[3]/button[3]').click()
# 点击确定
driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]').click()
# 勾选协议
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[4]/div/div[3]/span/div['
                             '1]/label/span/span').click()
# 点击确认提交
driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/div[2]/div/div[4]/div/div[3]/span/div[2]/button[2]').click()

# 登录后台进行审批
driver.get('http://ruraladmin.whdev.vpclub.cn/#/login')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div/input').send_keys('13692169349')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/div/input').send_keys('hui123456')
# 点击登录
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]').click()
# 点击农产权管理
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div/ul/div[3]/li/div').click()
# 点击进入我的审批
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[5]/a/li/span').click()
# 点击查看
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div').click()
# 点击查看我的审批
time.sleep(1)
driver.find_element_by_xpath('//*[@id="tab-7"]').click()
# 点击通过
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/div/div/div[2]/button[2]').click()
# 选择日期
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/div/div/div[4]/div/div[2]/div[5]/div[2]/div/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[7]/td[3]').click()
# 点击确认通过
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/section/div/div/div[4]/div/div[3]/button').click()
# 关闭窗口
time.sleep(2)
driver.quit()

# 选择下拉框承包方式
# driver.find_element_by_xpath('//div[@class="el-form-item__content"]//div[@style="margin-right: 10px;"]').click()
# driver.find_element_by_xpath('//ul/li/span[text()="家庭承包制"]').click()
# time.sleep(1)
# # 请输入土地四至
# driver.find_element_by_xpath('//div/input[@placeholder="请输入土地四至"]').send_keys('土地四至')
# # 输入占地面积
# driver.find_element_by_xpath('//input[@placeholder="请输入占地面积"]').send_keys('500')
# # 选择转让日期
# driver.find_element_by_xpath('//div/input[@placeholder="选择日期"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//tr/td/div/span[text()=30]').click()
# time.sleep(1)
# # 输入土地类型
# driver.find_element_by_xpath('//div/input[@placeholder="请输入土地类型"]').send_keys('土地类型')
# # 输入用途
# driver.find_element_by_xpath('//div/input[@placeholder="请输入用途"]').send_keys('类型用途')
# # 选择权属类型
# driver.find_element_by_xpath('//div[@class="el-form-item__content"]//div[@class="el-select el-select--mini"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//li[@class="el-select-dropdown__item"]/span[text()="集体"]').click()
# time.sleep(1)
# # 输入所有权人
# driver.find_element_by_xpath('//input[@placeholder="请输入所有权人"]').send_keys('桂院林')
# # 输入权证名称
# driver.find_element_by_xpath('//input[@placeholder="请输入权证名称"]').send_keys('桂圆林')
# # 输入转出方式
# driver.find_element_by_xpath('//input[@plac eholder="请输入转出方式"]').send_keys('出售')
# # 请输入标的简介
# driver.find_element_by_xpath('//div[@class="el-textarea el-input--mini"]').send_keys('测试脚本录入标的简介')
# # 请输入起拍价格
# driver.find_element_by_xpath('//input[@placeholder="请输入起拍价格"]').send_keys('5000')
# # 请选择预付款
# time.sleep(1)
# driver.find_element_by_xpath('//input[@placeholder="是/否"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//li[@class="el-select-dropdown__item selected hover"]/span[text()="否"]').click()
# # 输入手机号码
# driver.find_element_by_xpath('//input[@placeholder="请输入联系电话"]').send_keys('13971296154')
