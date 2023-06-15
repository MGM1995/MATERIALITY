from os.path import join, dirname, abspath

from qtpy.QtCore import Qt, QMetaObject, Signal, Slot, QEvent
from qtpy.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QToolButton,
                            QLabel, QSizePolicy)
from ._utils import QT_VERSION, PLATFORM
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt




_FL_STYLESHEET = join(dirname(abspath(__file__)), 'resources/frameless.qss')
""" str: Frameless window stylesheet. """


class WindowDragger(QWidget):
    """ Window dragger.

        Args:
            window (QWidget): Associated window.
            parent (QWidget, optional): Parent widget.
    """

    doubleClicked = Signal()

    def __init__(self, window, parent=None):
        QWidget.__init__(self, parent)

        self._window = window
        self._mousePressed = False

    def mousePressEvent(self, event):
        self._mousePressed = True
        self._mousePos = event.globalPos()
        self._windowPos = self._window.pos()

    def mouseMoveEvent(self, event):
        if self._mousePressed:
            self._window.move(self._windowPos +
                              (event.globalPos() - self._mousePos))

    def mouseReleaseEvent(self, event):
        self._mousePressed = False

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()


class ModernWindow(QWidget):
    """ Modern window.

        Args:
            w (QWidget): Main widget.
            parent (QWidget, optional): Parent widget.
    """

    def __init__(self, w, parent=None):
        QWidget.__init__(self, parent)

        self._w = w
        self.setupUi()

        contentLayout = QHBoxLayout()
        contentLayout.setContentsMargins(0, 0, 0, 0)
        contentLayout.addWidget(w)

        self.windowContent.setLayout(contentLayout)

        self.setWindowTitle(w.windowTitle())
        self.setGeometry(w.geometry())

        # Adding attribute to clean up the parent window when the child is closed
        self._w.setAttribute(Qt.WA_DeleteOnClose, False)
        self.CloseShortcut = QShortcut(QKeySequence("Ctrl+F4"), self)
        self.CloseShortcut.activated.connect(self.on_btnClose_clicked)


    def setupUi(self):
        # create title bar, content
        self.vboxWindow = QVBoxLayout(self)
        self.vboxWindow.setContentsMargins(0, 0, 0, 0)

        self.windowFrame = QWidget(self)
        self.windowFrame.setObjectName('windowFrame')

        self.vboxFrame = QVBoxLayout(self.windowFrame)
        self.vboxFrame.setContentsMargins(0, 0, 0, 0)

        self.titleBar = WindowDragger(self, self.windowFrame)
        self.titleBar.setObjectName('titleBar')
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,
                                                QSizePolicy.Fixed))

        self.hboxTitle = QHBoxLayout(self.titleBar)
        self.hboxTitle.setContentsMargins(0, 0, 0, 0)
        self.hboxTitle.setSpacing(0)

        self.lblTitle = QLabel('Title')
        self.lblTitle.setObjectName('lblTitle')
        self.lblTitle.setAlignment(Qt.AlignCenter)

        spButtons = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btnMinimize = QToolButton(self.titleBar)
        self.btnMinimize.setObjectName('btnMinimize')
        self.btnMinimize.setSizePolicy(spButtons)


        self.btnMaximize = QToolButton(self.titleBar)
        self.btnMaximize.setObjectName('btnMaximize')
        self.btnMaximize.setSizePolicy(spButtons)

        self.btnClose = QToolButton(self.titleBar)
        self.btnClose.setObjectName('btnClose')
        self.btnClose.setSizePolicy(spButtons)

        self.vboxFrame.addWidget(self.titleBar)

        self.windowContent = QWidget(self.windowFrame)
        self.vboxFrame.addWidget(self.windowContent)

        self.vboxWindow.addWidget(self.windowFrame)

        if PLATFORM == "Darwin":
            self.hboxTitle.addWidget(self.btnClose)
            self.hboxTitle.addWidget(self.btnMinimize)
            self.hboxTitle.addWidget(self.btnMaximize)
            self.hboxTitle.addWidget(self.lblTitle)
        else:
            self.hboxTitle.addWidget(self.lblTitle)
            self.hboxTitle.addWidget(self.btnMinimize)
            self.hboxTitle.addWidget(self.btnMaximize)
            self.hboxTitle.addWidget(self.btnClose)

        # set window flags
        self.setWindowFlags(
                Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        if QT_VERSION >= (5,):
            self.setAttribute(Qt.WA_TranslucentBackground)

        # set stylesheet
        with open(_FL_STYLESHEET) as stylesheet:
            self.setStyleSheet(stylesheet.read())

        # automatically connect slots
        QMetaObject.connectSlotsByName(self)

    def closeEvent(self, event):
        if not self._w:
            event.accept()
        else:
            self._w.isHidden()

    def setWindowTitle(self, title):
        """ Set window title.

            Args:
                title (str): Title.
        """

        super(ModernWindow, self).setWindowTitle(title)
        self.lblTitle.setText(title)

    @Slot()
    def on_btnMinimize_clicked(self):
        self.on_btnClose_clicked()


    @Slot()
    def on_btnMaximize_clicked(self):
        if self.windowState() != Qt.WindowMaximized and self.isVisible():
            self.setWindowState(Qt.WindowNoState)
            self.setWindowState(Qt.WindowMaximized)
            self.setWindowState(Qt.WindowNoState)
            self.setWindowState(Qt.WindowMaximized)
        else:
            self.setWindowState(Qt.WindowNoState)
        
        
        

    @Slot()
    def on_btnClose_clicked(self):
        self.hide()

