from PyQt4.QtCore import Qt, QRect, QSize, QPoint
from PyQt4.QtGui  import QLayout, QSizePolicy, QWidgetItem, \
    QDialog, QVBoxLayout, QHBoxLayout, QButtonGroup, QRadioButton, QPushButton, QDesktopWidget, QWidget


class FloatingLayout(QLayout):
    def __init__(self, parent=None):
        QLayout.__init__(self, parent)
        self._items = []
        self._updateMinimumSize()

    def _updateMinimumSize(self, height=None):
        w, h = 0, 0
        for item in self._items:
            w = max(w, item.minimumSize().width())
            h = max(h, item.minimumSize().height())

        left, top, right, bottom = self.getContentsMargins()
        w += left + right
        h += top + bottom

        if height is None:
            current_width = self.contentsRect().width()
            if current_width > 0:
                height = self.heightForWidth(current_width + left + right)
        if height is not None:
            h = max(h, height)

        self._min_w, self._min_h = w, h

    def _layoutChildren(self, rect, appl=True):
        left, top, right, bottom = self.getContentsMargins()
        r = rect.adjusted(+left, +top, -right, -bottom)
        x, y = r.x(), r.y()
        lineHeight = 0

        for item in self._items:
            wid = item.widget()
            spaceX = wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Horizontal)
            spaceY = wid.style().layoutSpacing(QSizePolicy.PushButton, QSizePolicy.PushButton, Qt.Vertical)

            sz_hint = item.sizeHint()
            if x != r.x() and x + sz_hint.width() >= r.right():
                # start new line
                x = r.x()
                y += lineHeight + spaceY
                lineHeight = 0
            if appl:
                item.setGeometry(QRect(QPoint(x, y), sz_hint))

            x += sz_hint.width() + spaceX
            lineHeight = max(lineHeight, sz_hint.height())

        return y + lineHeight - r.y() + top + bottom

    def heightForWidth(self, width):
        return self._layoutChildren(QRect(0, 0, width, 0), False)

    def setGeometry(self, r):
        QLayout.setGeometry(self, r)
        new_height = self._layoutChildren(r)
        if new_height != self._min_h:
            self._updateMinimumSize(new_height)
            i = 0
            wid = self.parentWidget()
            while wid is not None:
                wid.updateGeometry()
                wid = wid.parentWidget()
                i += 1

    def insertItem(self, pos, item):
        self._items.insert(pos, item)
        self.invalidate()

    def insertWidget(self, pos, wid):
        self.addChildWidget(wid)
        self.insertItem(pos, QWidgetItem(wid))

    def addItem(self, item):
        self._items.append(item)

    def count(self):
        return len(self._items)

    def hasHeightForWidth(self):
        return True

    def itemAt(self, index):
        if index < 0 or index >= len(self._items):
            return None
        return self._items[index]

    def minimumSize(self):
        return QSize(self._min_w, self._min_h)

    def takeAt(self, index):
        if index < 0 or index >= len(self._items):
            return None
        else:
            item = self._items[index]
            del self._items[index]
            return item

    def sizeHint(self):
        return self.minimumSize()


class ClsDialog(QDialog):
    """
    Control Button dont support 'tab' 
    radioButtons layout not perfect, because of the floatingLayout 
    """
    def __init__(self, parent=None, clss=[], cls=''):
        QDialog.__init__(self, parent)
        self._clss = clss
        self._cls = cls
        self.cls = cls
        self.index = clss.index(cls)
        self.initUI()
        self.center()
        self.show()

    def initUI(self):
        self.setWindowTitle('Label class Modify')
        self.resize(300, 120)

        self.mainLayout = QVBoxLayout()  # layout for the central widget
        self.setLayout(self.mainLayout)
        floatLayout = FloatingLayout()
        self.group = QButtonGroup(self)

        for i, cls in enumerate(self._clss):
            radio = QRadioButton(cls)
            radio.setChecked(cls == self._cls)
            # radio.clicked.connect(self.getChecked)
            radio.setFocusPolicy(Qt.NoFocus)
            self.group.addButton(radio, i)
            floatLayout.addWidget(radio)
        floatLayout.setMargin(15)
        self.group.buttonClicked.connect(self.getChecked)
        self.mainLayout.addLayout(floatLayout)

        hbox = QHBoxLayout()
        _cancel = QPushButton('&Cancel')
        _ok = QPushButton('&OK')
        _cancel.setFocusPolicy(Qt.NoFocus)
        _ok.setFocusPolicy(Qt.NoFocus)
        _cancel.clicked.connect(self.reject)
        _ok.clicked.connect(self.accept)
        hbox.addWidget(_cancel)
        hbox.addWidget(_ok)
        self.mainLayout.addLayout(hbox)
        self.group.button(self.index).setFocus()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getChecked(self):
        self.index = self.group.checkedId()
        self.cls = self.group.checkedButton().text()

    def keyPressEvent(self, event):
        # two value '\r\n'
        if event.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.accept()
        else:
            QWidget.keyPressEvent(self, event)