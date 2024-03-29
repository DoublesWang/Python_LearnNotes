"""
软件开发的生命周期:需求调研——》需求分析评审——》软件架构设计——》编码——》单元测试——》集成测试——》系统测试——》预发布系统测试——》上线

测试分类:
黑盒测试（功能测试）：功能符合用户的需求。
白盒测试：了解里面的逻辑，验证符合用户的需求。
冒烟测试：主功能、主路径测试。
性能测试：模拟多种峰值和负载去测试各项性能指标（一般对接口做性能测试，一个网站最多能够接收多少请求）。
性能测试工具：jmeter，loadrunner
自动化测试：人工测试转为工具自动执行（没有谁取代谁，有些场景适合自动化测试，有些场景适合手工测试）
后端开发，前端开发，大数据开发， Java开发

自动化测试和手工测试的优缺点:
1.自动化测试方便，自动验证功能是否有问题
2.更好的利用资源，节约人力成本
3.覆盖更全，增加软件的稳定性
自动化测试和手工测试是相辅相成的。（没有谁好谁坏，只是有些场景适合不适合。）
应用场景：
需求变更少；项目周期长；稳定性要强，环境要隔离独立（要保证开发一套环境，测试一套环境）。
如果整个系统需求变更多，只能抽取部分功能做自动化测试。

"""