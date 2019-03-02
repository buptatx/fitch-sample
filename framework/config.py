import os


# 目标设备
# 当然，这里只是一个例子
# 在实际应用中你可以用更加灵活的设计用于处理更复杂的情况
TARGET_DEVICE_ID = '123456F'

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
CASE_DIR = os.path.join(PROJECT_PATH, 'cases')

# 默认在同目录下的pics文件夹，但建议是与代码分开管理，不用git（用git管理图片会让仓库变得非常臃肿）
PIC_DIR = os.path.join(PROJECT_PATH, 'pics')

# 用例运行期间的截图保存位置
RUNTIME_PIC_DIR = os.path.join(PROJECT_PATH, 'runtime_pic')
