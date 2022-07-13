"""
艺术二维码生成器

@author: zhouhuajian
@version: v1.0
"""
import os
import time

from PySide6.QtCore import QThread, QFile
from PySide6.QtGui import QMouseEvent, Qt, QMovie, QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from amzqr import amzqr

from main_window_ui import Ui_MainWindow


class AmzqrThread(QThread):
    """创建二维码线程"""

    def __init__(self):
        """初始化线程"""
        super().__init__()
        self.kargs = {
            'words': '',
            'picture': '',
            'save_dir': '',
            'save_name': ''
        }
        self.result = {'error': '', 'qrcode_path': ''}

    def run(self):
        """运行"""
        self.result = {'error': '', 'qrcode_path': ''}
        try:
            # 生成二维码
            r = amzqr.run(**self.kargs, version=10, colorized=True)
            self.result['qrcode_path'] = r[2]
        except Exception as e:
            error = str(e)
            if error.startswith("Wrong words!"):
                error = "您输入了" + repr(self.kargs['words']) + "，但目前仅支持以下字符\n0-9 A-Z a-z ·,.:;+-*/\~!@#$%^&`'=<>[]()?_{}|"
            self.result['error'] = error


class ArtisticQrcodeGenerator(QWidget):
    """艺术二维码生成器"""

    # 标签类型
    LABEL_TYPE_BACKGROUND_IMAGE = 0
    LABEL_TYPE_QRCODE = 1

    def __init__(self):
        """初始化"""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 二维码背景图片
        self.ui.backgroundImageLabel.mousePressEvent = self.backgroundImageLabelMousePressEvent
        self.backgroundImagePath = 'images/default_background.png'
        self.backgroundImagePixmap = QPixmap()
        self.backgroundImageMovie = QMovie()
        # 创建二维码
        self.ui.pushButton.clicked.connect(self.createQrcode)
        self.amzqrThread = AmzqrThread()
        self.amzqrThread.finished.connect(self.afterCreateQrcode)
        # 二维码
        self.isQrcodeCreating = False
        self.ui.qrcodeLabel.mousePressEvent = self.qrcodeLabelMousePressEvent
        self.qrcodePath = 'images/default_qrcode.png'
        self.qrcodePixmap = QPixmap()
        self.qrcodeMovie = QMovie()
        self.file = QFile()

    def createQrcode(self):
        """创建二维码"""
        self.isQrcodeCreating = True
        self.ui.plainTextEdit.setReadOnly(True)
        self.ui.pushButton.setDisabled(True)
        self.ui.backgroundImageLabel.setCursor(Qt.CursorShape.ArrowCursor)
        self.ui.qrcodeLabel.setCursor(Qt.CursorShape.ArrowCursor)
        # 提供amzqr运行的参数
        self.amzqrThread.kargs = {
            'words': self.ui.plainTextEdit.toPlainText(),
            'picture': self.backgroundImagePath,
            'save_dir': './temp',
            'save_name': '临时二维码' + self.getExtByImagePath(self.backgroundImagePath)
        }
        self.amzqrThread.start()

    def afterCreateQrcode(self):
        """创建二维码之后"""
        # 创建成功
        if not self.amzqrThread.result['error']:
            self.qrcodePath = self.amzqrThread.result['qrcode_path']
            self.showImageOnLabel(self.LABEL_TYPE_QRCODE)
        # 创建失败
        else:
            QMessageBox.critical(self, "二维码创建失败", self.amzqrThread.result['error'])

        self.isQrcodeCreating = False
        self.ui.plainTextEdit.setReadOnly(False)
        self.ui.pushButton.setDisabled(False)
        self.ui.backgroundImageLabel.setCursor(Qt.CursorShape.OpenHandCursor)
        self.ui.qrcodeLabel.setCursor(Qt.CursorShape.OpenHandCursor)

    def backgroundImageLabelMousePressEvent(self, mouseEvent: QMouseEvent):
        """背景图片标签鼠标按下事件"""
        if self.isQrcodeCreating:
            return
        if mouseEvent.button() == Qt.MouseButton.LeftButton:
            r = QFileDialog.getOpenFileName(parent=self, caption="选择背景图片", filter="图片 (*.png *.jpg *.gif)")
            imagePath = r[0]
            # 当用户选择了背景图片
            if imagePath:
                self.backgroundImagePath = imagePath
                self.showImageOnLabel(self.LABEL_TYPE_BACKGROUND_IMAGE)

    def qrcodeLabelMousePressEvent(self, mouseEvent: QMouseEvent):
        """二维码标签鼠标按下事件"""
        if self.isQrcodeCreating:
            return
        if mouseEvent.button() == Qt.MouseButton.LeftButton:
            ext = self.getExtByImagePath(self.qrcodePath)
            r = QFileDialog.getSaveFileName(parent=self, dir=f'二维码{time.strftime("%Y%m%d%H%M%S")}{ext}', filter=f"图片 (*{ext})")
            imagePath = r[0]
            if imagePath:
                self.file.copy(self.qrcodePath, imagePath)

    def showImageOnLabel(self, labelType: int):
        """在标签上显示图片"""
        if labelType == self.LABEL_TYPE_BACKGROUND_IMAGE:
            label = self.ui.backgroundImageLabel
            imagePath = self.backgroundImagePath
            pixmap = self.backgroundImagePixmap
            movie = self.backgroundImageMovie
        else:
            label = self.ui.qrcodeLabel
            imagePath = self.qrcodePath
            pixmap = self.qrcodePixmap
            movie = self.qrcodeMovie
        # 动态图片 gif
        if self.getExtByImagePath(imagePath) == '.gif':
            movie.stop()
            movie.setFileName(imagePath)
            label.setMovie(movie)
            movie.start()
        # 静态图片 jpg png
        else:
            pixmap.load(imagePath)
            label.setPixmap(pixmap)

    def getExtByImagePath(self, imagePath: str) -> str:
        """根据图片路径，获取图片扩展"""
        return os.path.splitext(imagePath)[1]


if __name__ == '__main__':
    # 应用
    app = QApplication()
    qrcodeGenerator = ArtisticQrcodeGenerator()
    qrcodeGenerator.show()
    # 进入消息循环
    app.exec()
