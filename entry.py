from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner

from cases.test_wechat import TestWechat


suite = TestSuite([
    TestLoader().loadTestsFromTestCase(TestWechat),

    # 在此处继续添加其他用例
    # 或者自行定制更好的加载方式？：）
])

runner = HTMLTestRunner(output='sample_suite')
runner.run(suite)
