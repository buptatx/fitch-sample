import time

from fitch import FTestCase
from framework.config import TARGET_DEVICE_ID, PIC_DIR, RUNTIME_PIC_DIR


class BaseTestCase(FTestCase):
    # 测试用的设备ID
    f_device_id = TARGET_DEVICE_ID

    # 默认情况下，每条用例结束后设备会被重新初始化
    # 如果你认为不需要，可以设置为False取消这个行为
    f_device_kill_after_usage = False

    # 图片文件夹的根目录，默认为你的当前工作目录
    f_pic_store_root = PIC_DIR

    # 用例运行期间的截图记录，默认是不保存
    f_runtime_pic_dir_path = RUNTIME_PIC_DIR

    # 自由定制你需要的参数
    KEY_CODE_HOME = 3
    KEY_CODE_RECENT = 187

    # 与方法
    def clean_recent(self):
        """ 清理后台 """

        """
        这里提供了一个清理后台的方法
        不同厂商清理后台的方式不尽相同，这个例子并不能保证正常运行
        可以根据自身需要修改逻辑
        """

        self.f_init_store('global')
        self.f_device.toolkit.input_key_event(self.KEY_CODE_HOME)
        time.sleep(0.5)
        self.f_device.toolkit.input_key_event(self.KEY_CODE_RECENT)
        time.sleep(0.5)
        self.f_tap_target('x')
        time.sleep(1)
        self.f_device.toolkit.input_key_event(self.KEY_CODE_HOME)
