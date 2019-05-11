import xml.etree.ElementTree as ET

xml_tree = ET.parse('test.xml')

users = xml_tree.getroot()

# print(root.tag)

# for user in users:
# 	# print('id : ',t.attrib['id'])
# 	print('id : ',user.get('id'))
# 	for u in user:
# 		if not u.text == None:
# 			print('{} : {}'.format(u.tag,u.text))
# 		if u.tag == 'hobby':
# 			print('hobby : ',u.get('name'))
# 	print()

# for user in users.iter('name'):  # 迭代根下所有name的元素
# 	print(user.tag,user.text)

# 增加
new_user = ET.Element('user')  # 创建user标签
new_user.attrib['id'] = '4'  # 定义属性

name = ET.SubElement(new_user,'name')  # 设置new_user的子标签
name.text = 'John'	# 设置子标签text
age = ET.SubElement(new_user,'age')
age.text = '40'
sex = ET.SubElement(new_user,'sex')
sex.text = 'Male'
hobby = ET.SubElement(new_user,'hobby',attrib={'name':'sleep'})

users.append(new_user)  # 将new_user追加到users

# 修改
# for user in users.findall('user'):
# 	name = user.find('name')
# 	print(name.text)
# 	if name.text == 'Tom':
# 		user.find('age').text = '35' 

# 删除
# for user in users.findall('user'):
# 	age = int(user.find('age').text)
# 	# print(age.text)
# 	if age > 27:
# 		users.remove(user)  # 删除age大于27的user
# 		print('remove success!!!')

xml_tree.write('test3.xml')