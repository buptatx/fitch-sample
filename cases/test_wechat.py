"""
这里给出一个简单的用例

1. 检测桌面上是否存在微信图标，并点击
2. 检测微信是否启动（通过微信首页中的相机icon）
"""
import time
from framework.base_case import BaseTestCase


class TestWechat(BaseTestCase):
    def setUp(self):
        # 这里可以根据需要加载你需要的图片目录
        self.f_init_store('wechat')
        # 可以加载多个
        self.f_init_store('global')

        # 调用在BaseTestCase中定制好的方法
        self.clean_recent()
        time.sleep(1)

    def test_enter_wechat(self):
        # 点击目标图片
        # 这里会在你已经加载好的图片目录下寻找名为 wechat_logo 的图片
        self.f_tap_target('wechat_logo')

        # 等待微信启动
        time.sleep(1)

        # 检测目标图片是否存在
        assert self.f_find_target('wechat_camera_icon'), 'wechat camera icon not found'

    def tearDown(self):
        # 在测试结束后清理后台
        self.clean_recent()
