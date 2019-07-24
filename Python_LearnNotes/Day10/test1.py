"""
使用id定位	find_element_by_id(“id值”)
使用class定位	find_element_by_class_name(“class值”)
使用name定位	find_element_by_name(“name值”)
使用链接的全部文字内容定位	find_element_by_link_text(“链接的全部文字内容”)
使用链接的部分文字内容定位	find_element_by_partial_link_text(“链接的部分文字内容”)
使用标签名称定位	find_element_by_tag_name(“页面中html的标签名称”)

使用xpath定位	find_element_by_xpath(“Xpath定义表达式”)
使用css定位	find_element_by_css_selector(“CSS定位表达式”)



xpath的更多用法：
第一种方法：

通过绝对路径做定位
By.xpath("html/body/div/form/input")

第二种方法：

通过相对路径定位
By.xpath("//input")

第三种方法：

通过元素索引定位
By.xpath("//input[4]")

第四种方法：

使用xpath属性定位（结合第2、第3中方法可以使用）
By.xpath("//input[@id='kw1']")
By.xpath("//input[@type='name' and @name='kw1']")

第五种方法：

使用部分属性值匹配（最强大的方法）
By.xpath("//input[start-with(@id，'nice')
By.xpath("//input[ends-with(@id，'很漂亮')
By.xpath("//input[contains(@id，'那么美')]")

第6种方法：

使用xpath轴（未曾使用）



css(以百度首页为例):

定位输入框

一：单一属性定位

1：type selector
driver.find_element_by_css_selector('input')

2：id 定位
driver.find_element_by_css_selector('#kw')

3：class 定位
driver.find_element_by_css_selector('.s_ipt')

4：其他属性定位
driver.find_element_by_css_selector('[name='wd']')
driver.find_element_by_css_selector("[type='text']")

二：组合属性定位

1：id组合属性定位
driver.find_element_by_css_selector("input#kw")

2：class组合属性定位
driver.find_element_by_css_selector("input.s_ipt")

3：其他属性组合定位
driver.find_element_by_css_selector("input[name='wd']")

4：仅有属性名，没有值也可以
driver.find_element_by_css_selector("input[name]")

5：两个其他属性组合定位
driver.find_element_by_css_selector("[name='wd'][autocomplete='off']")

6：模糊匹配属性值方法

1>属性值由多个空格隔开，匹配其中一个值的方法
driver.find_element_by_css_selector("input[class~='btn']")

2>匹配属性值为字符串开头的方法
driver.find_element_by_css_selector("input[class^='btn']")

3>匹配属性值字符串结尾的方法
driver.find_element_by_css_selector("input[class$='s_btn']")

4>匹配被-分割的属性值的方法,如上图的class
driver.find_element_by_css_selector("input[class|='s']")  #要求精确填写的属性值

三：层级定位
 1：E>F    E下面的F这个元素
driver.find_element_by_css_selector('from#form>span>input')#id是form的form下面的span下面的input

2：E:nth-child(n)
driver.find_element_by_css_selector('#u_sp > a:nth-child(1)')#id为u_sp的下面的第一个a标签。

#实测，这个定位不到，但是方法是对的，- -

3：E:nth-last-child(n)，如字面意思：倒数第几个标签

4：E:first-child,第一个标签

5：E:last-child,最后一个标签

6：E:only-child,唯一的标签



"""