# Author:Liwen
import time,json,requests

# 获取数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
print(data)

# 列举：打印武汉数据
# print(data['areaTree'][0]['children'][0]['children'][0])

# 数据更新时间
time = data['lastUpdateTime']
print("数据更新时间：",time)
# data键
print(data.keys())
# 整体数据
total_data = data['areaTree']
print(total_data)

# 创建列表
china_confirm_total = list() #全国确诊
china_suspect_total = list() #全国疑似
china_dead_total = list() #全国死亡
china_heal_total = list() #全国治愈

# 全国确诊人数
china_confirm_total.append(int(data['chinaTotal']['confirm']))
print("全国确诊人数:",china_confirm_total)
# 全国疑似人数
china_suspect_total.append(int(data['chinaTotal']['suspect']))
print("全国疑似病例人数:",china_suspect_total)
# 全国死亡人数
china_dead_total.append(int(data['chinaTotal']['dead']))
print("全国死亡人数:",china_dead_total)
# 全国治愈人数
china_heal_total.append(int(data['chinaTotal']['heal']))
print("全国治愈人数:",china_heal_total)
# 有病例国家
list_country = []
for i in total_data:
    list_country.append(i['name'])
print("有病例国家：",list_country)
# 各国家病例人数
list_country_num = []
for i in total_data:
    list_country_num.append(i['total']['confirm'])
print("各国家病例人数:",list_country_num)
# 中国地区
list_china = [total_data[0]['children']]
print("中国地区病例总数:",list_china)
# 中国各省份
list_china_province = []
for i in list_china[0]:
    list_china_province.append(i['name'])
print("中国各省份病例:",list_china_province)
# 中国各省份病例人数
list_china_province_num = []
for i in list_china[0]:
    list_china_province_num.append(i['total']['confirm'])
print("中国各省份病例人数：",list_china_province_num)
# 中国存在病例的所有城市列表 -确诊,死亡,治愈
china_city0_list = []
for i in list_china[0]:
    china_city0_list.append(i['children'])
china_city1_list = sum(china_city0_list,[])
china_city_list =[]
for a in china_city1_list:
    china_city_list.append(a['name'])
print('各省份城市存在病例列表',china_city_list)
# 各省份城市确诊数目列表
china_city_confirm_num_list = []
for a in china_city1_list:
    china_city_confirm_num_list.append(a['total']['confirm'])
print('各省份城市确诊数目列表',china_city_confirm_num_list)