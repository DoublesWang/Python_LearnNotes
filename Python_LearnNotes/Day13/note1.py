"""
一、单元测试简介
1、单元测试：
	是指对软件中的最小可测试单元进行检查和验证。对单元测试中单元的含义，要根据实际情况去判定其具体含义。
2、unittest框架是python的单元测试框架
3、unittest = TestCae+TestResult  执行+结果


二、单元测试框架unittest入门
1、导入模块
2、测试的类都继承于TestCase类
3、setup() 测试前的初始工作  testDown()测试后的关闭工作
注意：
	1、所有类中方法的入参为self,定义方法的变量也要“self.”变量
	2、定义测试用例，以“test”开头命名的方法，入参为self
	3、unittest.main()方法会搜索该模块下面所有以test开头的测试用例方法，并自动执行
	4、py文件不能以unittest命名，不然找不到TestCae

	成功是输出 . 失败是F


三、测试套件TestSute介绍
1、unitest.TestSuite()类表示一个测试用例集
  (1)用来确定用例的执行
  (2)如果一个class中有四个test开头的方法，则加载到suite中时则有四个测试用例
  (3)由TestLoader加载TestCase到TestSuite
  (4)verbosity参数可以控制执行结果的输出，0是简单报告 1是一般报告 2是详细报告
  默认1 会在每个成功的用例前面加个"." 每个失败的用例前面有个"F"

 2、TextTestRunner() 文本测试用例器
 3、run()方法是运行测试套件的测试用例，入参为suite测试套件






"""