# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'PyCEM_GUI.ui'
##
# Created by: Qt User Interface Compiler version 6.4.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
                               QHeaderView, QLabel, QMainWindow, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
                               QStackedWidget, QStatusBar, QTableView, QVBoxLayout,
                               QWidget)
import modules.images_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QSize(1920, 2000))
        self.actionFDA = QAction(MainWindow)
        self.actionFDA.setObjectName(u"actionFDA")
        self.actionFDTD = QAction(MainWindow)
        self.actionFDTD.setObjectName(u"actionFDTD")
        self.actionMoM = QAction(MainWindow)
        self.actionMoM.setObjectName(u"actionMoM")
        self.actionMoM.setEnabled(False)
        self.actionFEM = QAction(MainWindow)
        self.actionFEM.setObjectName(u"actionFEM")
        self.actionFEM.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 1000))
        self.horizontalLayout_12 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(268, 0, 1600, 991))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QSize(1600, 16777215))
        self.stackedWidget.setStyleSheet(u"")
        self.Welcome_Page = QWidget()
        self.Welcome_Page.setObjectName(u"Welcome_Page")
        self.label = QLabel(self.Welcome_Page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 381, 61))
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label_2 = QLabel(self.Welcome_Page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 130, 551, 31))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.stackedWidget.addWidget(self.Welcome_Page)
        self.FDA_Cards = QWidget()
        self.FDA_Cards.setObjectName(u"FDA_Cards")
        self.FDA_Cards.setStyleSheet(u".QFrame {\n"
                                     "border: 1px solid #4c4c4c;\n"
                                     "background-color: rgb(220, 217, 252);\n"
                                     "}\n"
                                     ".QPushButton {\n"
                                     "background-color: rgb(76, 76, 76);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "QFrame {\n"
                                     "color: rgb(0,0,0);\n"
                                     "}\n"
                                     "QLabel[scaledContents=\"false\"]{\n"
                                     "margin-left: 10;\n"
                                     "margin-right: 10;\n"
                                     "}")
        self.frame_4 = QFrame(self.FDA_Cards)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 20, 300, 450))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_216 = QLabel(self.frame_4)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(
            self.label_216.sizePolicy().hasHeightForWidth())
        self.label_216.setSizePolicy(sizePolicy1)
        self.label_216.setMinimumSize(QSize(300, 225))
        self.label_216.setMaximumSize(QSize(300, 225))
        self.label_216.setSizeIncrement(QSize(4, 3))
        self.label_216.setBaseSize(QSize(256, 192))
        self.label_216.setPixmap(
            QPixmap(u":/fda/img/fda/cards/SymmetricStripline.png"))
        self.label_216.setScaledContents(True)
        self.label_216.setAlignment(Qt.AlignCenter)
        self.label_214 = QLabel(self.frame_4)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.label_214.sizePolicy().hasHeightForWidth())
        self.label_214.setSizePolicy(sizePolicy2)
        self.label_214.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_214.setFont(font2)
        self.label_214.setStyleSheet(u"")
        self.label_219 = QLabel(self.frame_4)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setGeometry(QRect(0, 250, 300, 125))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.label_219.sizePolicy().hasHeightForWidth())
        self.label_219.setSizePolicy(sizePolicy3)
        self.label_219.setMinimumSize(QSize(0, 125))
        self.label_219.setMaximumSize(QSize(300, 16777215))
        self.label_219.setStyleSheet(u"")
        self.label_219.setWordWrap(True)
        self.pushButton_sstrip = QPushButton(self.frame_4)
        self.pushButton_sstrip.setObjectName(u"pushButton_sstrip")
        self.pushButton_sstrip.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.pushButton_sstrip.sizePolicy().hasHeightForWidth())
        self.pushButton_sstrip.setSizePolicy(sizePolicy4)
        self.pushButton_sstrip.setCheckable(True)
        self.frame_5 = QFrame(self.FDA_Cards)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(340, 20, 300, 450))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton_ms = QPushButton(self.frame_5)
        self.pushButton_ms.setObjectName(u"pushButton_ms")
        self.pushButton_ms.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_ms.sizePolicy().hasHeightForWidth())
        self.pushButton_ms.setSizePolicy(sizePolicy4)
        self.pushButton_ms.setCheckable(True)
        self.label_218 = QLabel(self.frame_5)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_218.sizePolicy().hasHeightForWidth())
        self.label_218.setSizePolicy(sizePolicy2)
        self.label_218.setMaximumSize(QSize(300, 16777215))
        self.label_218.setFont(font2)
        self.label_215 = QLabel(self.frame_5)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setGeometry(QRect(0, 250, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_215.sizePolicy().hasHeightForWidth())
        self.label_215.setSizePolicy(sizePolicy3)
        self.label_215.setMinimumSize(QSize(0, 125))
        self.label_215.setMaximumSize(QSize(300, 16777215))
        self.label_215.setWordWrap(True)
        self.label_220 = QLabel(self.frame_5)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_220.sizePolicy().hasHeightForWidth())
        self.label_220.setSizePolicy(sizePolicy1)
        self.label_220.setMinimumSize(QSize(300, 225))
        self.label_220.setMaximumSize(QSize(300, 225))
        self.label_220.setSizeIncrement(QSize(4, 3))
        self.label_220.setBaseSize(QSize(256, 192))
        self.label_220.setPixmap(
            QPixmap(u":/fda/img/fda/cards/Microstrip.png"))
        self.label_220.setScaledContents(True)
        self.label_220.setAlignment(Qt.AlignCenter)
        self.frame_6 = QFrame(self.FDA_Cards)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 490, 300, 450))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_221 = QLabel(self.frame_6)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_221.sizePolicy().hasHeightForWidth())
        self.label_221.setSizePolicy(sizePolicy2)
        self.label_221.setMaximumSize(QSize(300, 16777215))
        self.label_221.setFont(font2)
        self.label_221.setStyleSheet(u"")
        self.label_222 = QLabel(self.frame_6)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(0, 270, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_222.sizePolicy().hasHeightForWidth())
        self.label_222.setSizePolicy(sizePolicy3)
        self.label_222.setMinimumSize(QSize(0, 125))
        self.label_222.setMaximumSize(QSize(300, 16777215))
        self.label_222.setStyleSheet(u"")
        self.label_222.setWordWrap(True)
        self.pushButton_diffms = QPushButton(self.frame_6)
        self.pushButton_diffms.setObjectName(u"pushButton_diffms")
        self.pushButton_diffms.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_diffms.sizePolicy().hasHeightForWidth())
        self.pushButton_diffms.setSizePolicy(sizePolicy4)
        self.pushButton_diffms.setCheckable(True)
        self.label_217 = QLabel(self.frame_6)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_217.sizePolicy().hasHeightForWidth())
        self.label_217.setSizePolicy(sizePolicy1)
        self.label_217.setMinimumSize(QSize(300, 225))
        self.label_217.setMaximumSize(QSize(300, 225))
        self.label_217.setSizeIncrement(QSize(4, 3))
        self.label_217.setBaseSize(QSize(256, 192))
        self.label_217.setPixmap(
            QPixmap(u":/fda/img/fda/cards/DifferentialMicrostrip.png"))
        self.label_217.setScaledContents(True)
        self.label_217.setAlignment(Qt.AlignCenter)
        self.frame_7 = QFrame(self.FDA_Cards)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(340, 490, 300, 450))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_224 = QLabel(self.frame_7)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_224.sizePolicy().hasHeightForWidth())
        self.label_224.setSizePolicy(sizePolicy2)
        self.label_224.setMaximumSize(QSize(300, 16777215))
        self.label_224.setFont(font2)
        self.label_224.setStyleSheet(u"")
        self.label_225 = QLabel(self.frame_7)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setGeometry(QRect(0, 250, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_225.sizePolicy().hasHeightForWidth())
        self.label_225.setSizePolicy(sizePolicy3)
        self.label_225.setMinimumSize(QSize(0, 125))
        self.label_225.setMaximumSize(QSize(300, 16777215))
        self.label_225.setStyleSheet(u"")
        self.label_225.setWordWrap(True)
        self.pushButton_bstrip = QPushButton(self.frame_7)
        self.pushButton_bstrip.setObjectName(u"pushButton_bstrip")
        self.pushButton_bstrip.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_bstrip.sizePolicy().hasHeightForWidth())
        self.pushButton_bstrip.setSizePolicy(sizePolicy4)
        self.pushButton_bstrip.setCheckable(True)
        self.label_241 = QLabel(self.frame_7)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_241.sizePolicy().hasHeightForWidth())
        self.label_241.setSizePolicy(sizePolicy1)
        self.label_241.setMinimumSize(QSize(300, 225))
        self.label_241.setMaximumSize(QSize(300, 225))
        self.label_241.setSizeIncrement(QSize(4, 3))
        self.label_241.setBaseSize(QSize(256, 192))
        self.label_241.setPixmap(
            QPixmap(u":/fda/img/fda/cards/BroadsideStripline.png"))
        self.label_241.setScaledContents(True)
        self.label_241.setAlignment(Qt.AlignCenter)
        self.frame_8 = QFrame(self.FDA_Cards)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(660, 20, 300, 450))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_227 = QLabel(self.frame_8)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_227.sizePolicy().hasHeightForWidth())
        self.label_227.setSizePolicy(sizePolicy2)
        self.label_227.setMaximumSize(QSize(300, 16777215))
        self.label_227.setFont(font2)
        self.label_227.setStyleSheet(u"")
        self.label_228 = QLabel(self.frame_8)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(0, 260, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_228.sizePolicy().hasHeightForWidth())
        self.label_228.setSizePolicy(sizePolicy3)
        self.label_228.setMinimumSize(QSize(0, 125))
        self.label_228.setMaximumSize(QSize(300, 16777215))
        self.label_228.setStyleSheet(u"")
        self.label_228.setWordWrap(True)
        self.pushButton_coax = QPushButton(self.frame_8)
        self.pushButton_coax.setObjectName(u"pushButton_coax")
        self.pushButton_coax.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_coax.sizePolicy().hasHeightForWidth())
        self.pushButton_coax.setSizePolicy(sizePolicy4)
        self.pushButton_coax.setCheckable(True)
        self.label_226 = QLabel(self.frame_8)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_226.sizePolicy().hasHeightForWidth())
        self.label_226.setSizePolicy(sizePolicy1)
        self.label_226.setMinimumSize(QSize(300, 225))
        self.label_226.setMaximumSize(QSize(300, 225))
        self.label_226.setSizeIncrement(QSize(4, 3))
        self.label_226.setBaseSize(QSize(256, 192))
        self.label_226.setPixmap(QPixmap(u":/fda/img/fda/cards/Coaxial.png"))
        self.label_226.setScaledContents(True)
        self.label_226.setAlignment(Qt.AlignCenter)
        self.frame_9 = QFrame(self.FDA_Cards)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(660, 490, 300, 450))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_233 = QLabel(self.frame_9)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_233.sizePolicy().hasHeightForWidth())
        self.label_233.setSizePolicy(sizePolicy2)
        self.label_233.setMaximumSize(QSize(300, 16777215))
        self.label_233.setFont(font2)
        self.label_233.setStyleSheet(u"")
        self.label_234 = QLabel(self.frame_9)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setGeometry(QRect(0, 270, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_234.sizePolicy().hasHeightForWidth())
        self.label_234.setSizePolicy(sizePolicy3)
        self.label_234.setMinimumSize(QSize(0, 125))
        self.label_234.setMaximumSize(QSize(300, 16777215))
        self.label_234.setStyleSheet(u"")
        self.label_234.setWordWrap(True)
        self.pushButton_dstrip = QPushButton(self.frame_9)
        self.pushButton_dstrip.setObjectName(u"pushButton_dstrip")
        self.pushButton_dstrip.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_dstrip.sizePolicy().hasHeightForWidth())
        self.pushButton_dstrip.setSizePolicy(sizePolicy4)
        self.pushButton_dstrip.setCheckable(True)
        self.label_243 = QLabel(self.frame_9)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_243.sizePolicy().hasHeightForWidth())
        self.label_243.setSizePolicy(sizePolicy1)
        self.label_243.setMinimumSize(QSize(300, 225))
        self.label_243.setMaximumSize(QSize(300, 225))
        self.label_243.setSizeIncrement(QSize(4, 3))
        self.label_243.setBaseSize(QSize(256, 192))
        self.label_243.setPixmap(
            QPixmap(u":/fda/img/fda/cards/DifferentialStripline.png"))
        self.label_243.setScaledContents(True)
        self.label_243.setAlignment(Qt.AlignCenter)
        self.frame_10 = QFrame(self.FDA_Cards)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(980, 20, 300, 450))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_236 = QLabel(self.frame_10)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_236.sizePolicy().hasHeightForWidth())
        self.label_236.setSizePolicy(sizePolicy2)
        self.label_236.setMaximumSize(QSize(300, 16777215))
        self.label_236.setFont(font2)
        self.label_236.setStyleSheet(u"")
        self.label_237 = QLabel(self.frame_10)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setGeometry(QRect(0, 250, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_237.sizePolicy().hasHeightForWidth())
        self.label_237.setSizePolicy(sizePolicy3)
        self.label_237.setMinimumSize(QSize(0, 125))
        self.label_237.setMaximumSize(QSize(300, 16777215))
        self.label_237.setStyleSheet(u"")
        self.label_237.setWordWrap(True)
        self.pushButton_astrip = QPushButton(self.frame_10)
        self.pushButton_astrip.setObjectName(u"pushButton_astrip")
        self.pushButton_astrip.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_astrip.sizePolicy().hasHeightForWidth())
        self.pushButton_astrip.setSizePolicy(sizePolicy4)
        self.pushButton_astrip.setCheckable(True)
        self.label_235 = QLabel(self.frame_10)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_235.sizePolicy().hasHeightForWidth())
        self.label_235.setSizePolicy(sizePolicy1)
        self.label_235.setMinimumSize(QSize(300, 225))
        self.label_235.setMaximumSize(QSize(300, 225))
        self.label_235.setSizeIncrement(QSize(4, 3))
        self.label_235.setBaseSize(QSize(300, 225))
        self.label_235.setPixmap(
            QPixmap(u":/fda/img/fda/cards/AsymmetricStripline.png"))
        self.label_235.setScaledContents(True)
        self.label_235.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.FDA_Cards)
        self.FDA_Sim = QWidget()
        self.FDA_Sim.setObjectName(u"FDA_Sim")
        self.frame_20 = QFrame(self.FDA_Sim)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 20, 421, 251))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_fda_title = QLabel(self.frame_20)
        self.label_fda_title.setObjectName(u"label_fda_title")
        self.label_fda_title.setMaximumSize(QSize(16777215, 35))
        self.label_fda_title.setFont(font2)
        self.label_fda_title.setWordWrap(True)
        self.label_fda_title.setMargin(0)

        self.verticalLayout_3.addWidget(self.label_fda_title)

        self.verticalSpacer_9 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)

        self.label_fda_desc = QLabel(self.frame_20)
        self.label_fda_desc.setObjectName(u"label_fda_desc")
        self.label_fda_desc.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_fda_desc)

        self.verticalSpacer_11 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.pushButton_analytical = QPushButton(self.frame_20)
        self.pushButton_analytical.setObjectName(u"pushButton_analytical")
        self.pushButton_analytical.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_analytical)

        self.verticalSpacer_12 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_12)

        self.pushButton_simulate = QPushButton(self.frame_20)
        self.pushButton_simulate.setObjectName(u"pushButton_simulate")
        self.pushButton_simulate.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_simulate)

        self.verticalSpacer_10 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.frame_21 = QFrame(self.FDA_Sim)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(10, 290, 421, 641))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_21)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_29 = QLabel(self.frame_21)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_29)

        self.verticalSpacer_2 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_fdaform1_title = QLabel(self.frame_21)
        self.label_fdaform1_title.setObjectName(u"label_fdaform1_title")

        self.verticalLayout_2.addWidget(self.label_fdaform1_title)

        self.doubleSpinBox_fdaform1_input = QDoubleSpinBox(self.frame_21)
        self.doubleSpinBox_fdaform1_input.setObjectName(
            u"doubleSpinBox_fdaform1_input")
        self.doubleSpinBox_fdaform1_input.setDecimals(3)

        self.verticalLayout_2.addWidget(self.doubleSpinBox_fdaform1_input)

        self.label_fdaform1_desc = QLabel(self.frame_21)
        self.label_fdaform1_desc.setObjectName(u"label_fdaform1_desc")
        font3 = QFont()
        font3.setPointSize(9)
        self.label_fdaform1_desc.setFont(font3)
        self.label_fdaform1_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_fdaform1_desc)

        self.verticalSpacer_4 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_fdaform2_title = QLabel(self.frame_21)
        self.label_fdaform2_title.setObjectName(u"label_fdaform2_title")

        self.verticalLayout_2.addWidget(self.label_fdaform2_title)

        self.doubleSpinBox_fdaform2_input = QDoubleSpinBox(self.frame_21)
        self.doubleSpinBox_fdaform2_input.setObjectName(
            u"doubleSpinBox_fdaform2_input")
        self.doubleSpinBox_fdaform2_input.setDecimals(3)

        self.verticalLayout_2.addWidget(self.doubleSpinBox_fdaform2_input)

        self.label_fdaform2_desc = QLabel(self.frame_21)
        self.label_fdaform2_desc.setObjectName(u"label_fdaform2_desc")
        self.label_fdaform2_desc.setFont(font3)
        self.label_fdaform2_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_fdaform2_desc)

        self.verticalSpacer_5 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.label_fdaform3_title = QLabel(self.frame_21)
        self.label_fdaform3_title.setObjectName(u"label_fdaform3_title")

        self.verticalLayout_2.addWidget(self.label_fdaform3_title)

        self.doubleSpinBox_fdaform3_input = QDoubleSpinBox(self.frame_21)
        self.doubleSpinBox_fdaform3_input.setObjectName(
            u"doubleSpinBox_fdaform3_input")
        self.doubleSpinBox_fdaform3_input.setDecimals(3)

        self.verticalLayout_2.addWidget(self.doubleSpinBox_fdaform3_input)

        self.label_fdaform3_desc = QLabel(self.frame_21)
        self.label_fdaform3_desc.setObjectName(u"label_fdaform3_desc")
        font4 = QFont()
        font4.setPointSize(8)
        self.label_fdaform3_desc.setFont(font4)
        self.label_fdaform3_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_fdaform3_desc)

        self.verticalSpacer_6 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.label_fdaform4_title = QLabel(self.frame_21)
        self.label_fdaform4_title.setObjectName(u"label_fdaform4_title")

        self.verticalLayout_2.addWidget(self.label_fdaform4_title)

        self.doubleSpinBox_fdaform4_input = QDoubleSpinBox(self.frame_21)
        self.doubleSpinBox_fdaform4_input.setObjectName(
            u"doubleSpinBox_fdaform4_input")
        self.doubleSpinBox_fdaform4_input.setDecimals(3)

        self.verticalLayout_2.addWidget(self.doubleSpinBox_fdaform4_input)

        self.label_fdaform4_desc = QLabel(self.frame_21)
        self.label_fdaform4_desc.setObjectName(u"label_fdaform4_desc")
        self.label_fdaform4_desc.setFont(font3)
        self.label_fdaform4_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_fdaform4_desc)

        self.verticalSpacer_7 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.label_fdaform5_title = QLabel(self.frame_21)
        self.label_fdaform5_title.setObjectName(u"label_fdaform5_title")

        self.verticalLayout_2.addWidget(self.label_fdaform5_title)

        self.doubleSpinBox_fdaform5_input = QDoubleSpinBox(self.frame_21)
        self.doubleSpinBox_fdaform5_input.setObjectName(
            u"doubleSpinBox_fdaform5_input")
        self.doubleSpinBox_fdaform5_input.setDecimals(3)

        self.verticalLayout_2.addWidget(self.doubleSpinBox_fdaform5_input)

        self.label_fdaform5_desc = QLabel(self.frame_21)
        self.label_fdaform5_desc.setObjectName(u"label_fdaform5_desc")
        self.label_fdaform5_desc.setFont(font3)
        self.label_fdaform5_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_fdaform5_desc)

        self.verticalSpacer_8 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.label_fdaform6_title = QLabel(self.frame_21)
        self.label_fdaform6_title.setObjectName(u"label_fdaform6_title")

        self.verticalLayout_2.addWidget(self.label_fdaform6_title)

        self.doubleSpinBox_fdaform6_input = QDoubleSpinBox(self.frame_21)
        self.doubleSpinBox_fdaform6_input.setObjectName(
            u"doubleSpinBox_fdaform6_input")
        self.doubleSpinBox_fdaform6_input.setDecimals(3)

        self.verticalLayout_2.addWidget(self.doubleSpinBox_fdaform6_input)

        self.label_fdaform6_desc = QLabel(self.frame_21)
        self.label_fdaform6_desc.setObjectName(u"label_fdaform6_desc")
        self.label_fdaform6_desc.setFont(font3)
        self.label_fdaform6_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_fdaform6_desc)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.frame_19 = QFrame(self.FDA_Sim)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(460, 20, 920, 721))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_19)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_fda_diagram = QLabel(self.frame_19)
        self.label_fda_diagram.setObjectName(u"label_fda_diagram")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.label_fda_diagram.sizePolicy().hasHeightForWidth())
        self.label_fda_diagram.setSizePolicy(sizePolicy5)
        self.label_fda_diagram.setMaximumSize(QSize(16777215, 1677215))
        self.label_fda_diagram.setPixmap(
            QPixmap(u":/fda/img/fda/diagrams/SymmetricStripline.png"))
        self.label_fda_diagram.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.label_fda_diagram)

        self.tableView = QTableView(self.frame_19)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_4.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.FDA_Sim)
        self.FDTD_Cards = QWidget()
        self.FDTD_Cards.setObjectName(u"FDTD_Cards")
        self.FDTD_Cards.setStyleSheet(u".QFrame {\n"
                                      "border: 1px solid #4c4c4c;\n"
                                      "background-color: rgb(220, 217, 252);\n"
                                      "}\n"
                                      ".QPushButton {\n"
                                      "background-color: rgb(76, 76, 76);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QFrame {\n"
                                      "color: rgb(0,0,0);\n"
                                      "}\n"
                                      "QLabel[scaledContents=\"false\"]{\n"
                                      "margin-left: 10;\n"
                                      "margin-right: 10;\n"
                                      "}")
        self.frame_11 = QFrame(self.FDTD_Cards)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(20, 490, 300, 450))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_223 = QLabel(self.frame_11)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_223.sizePolicy().hasHeightForWidth())
        self.label_223.setSizePolicy(sizePolicy2)
        self.label_223.setMaximumSize(QSize(300, 16777215))
        self.label_223.setFont(font2)
        self.label_223.setStyleSheet(u"")
        self.label_229 = QLabel(self.frame_11)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(0, 270, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_229.sizePolicy().hasHeightForWidth())
        self.label_229.setSizePolicy(sizePolicy3)
        self.label_229.setMinimumSize(QSize(0, 125))
        self.label_229.setMaximumSize(QSize(300, 16777215))
        self.label_229.setStyleSheet(u"")
        self.label_229.setWordWrap(True)
        self.pushButton_tfsf_corner = QPushButton(self.frame_11)
        self.pushButton_tfsf_corner.setObjectName(u"pushButton_tfsf_corner")
        self.pushButton_tfsf_corner.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_tfsf_corner.sizePolicy().hasHeightForWidth())
        self.pushButton_tfsf_corner.setSizePolicy(sizePolicy4)
        self.pushButton_tfsf_corner.setCheckable(True)
        self.label_230 = QLabel(self.frame_11)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_230.sizePolicy().hasHeightForWidth())
        self.label_230.setSizePolicy(sizePolicy1)
        self.label_230.setMinimumSize(QSize(300, 225))
        self.label_230.setMaximumSize(QSize(300, 225))
        self.label_230.setSizeIncrement(QSize(4, 3))
        self.label_230.setBaseSize(QSize(256, 192))
        self.label_230.setPixmap(
            QPixmap(u":/fdtd/img/fdtd/cards/TFSFCornerReflector.png"))
        self.label_230.setScaledContents(True)
        self.label_230.setAlignment(Qt.AlignCenter)
        self.frame_12 = QFrame(self.FDTD_Cards)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(20, 20, 300, 450))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_231 = QLabel(self.frame_12)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_231.sizePolicy().hasHeightForWidth())
        self.label_231.setSizePolicy(sizePolicy1)
        self.label_231.setMinimumSize(QSize(300, 225))
        self.label_231.setMaximumSize(QSize(300, 225))
        self.label_231.setSizeIncrement(QSize(4, 3))
        self.label_231.setBaseSize(QSize(256, 192))
        self.label_231.setPixmap(
            QPixmap(u":/fdtd/img/fdtd/cards/RickerTMz2D.png"))
        self.label_231.setScaledContents(True)
        self.label_231.setAlignment(Qt.AlignCenter)
        self.label_232 = QLabel(self.frame_12)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_232.sizePolicy().hasHeightForWidth())
        self.label_232.setSizePolicy(sizePolicy2)
        self.label_232.setMaximumSize(QSize(300, 16777215))
        self.label_232.setFont(font2)
        self.label_232.setStyleSheet(u"")
        self.label_238 = QLabel(self.frame_12)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setGeometry(QRect(0, 250, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_238.sizePolicy().hasHeightForWidth())
        self.label_238.setSizePolicy(sizePolicy3)
        self.label_238.setMinimumSize(QSize(0, 125))
        self.label_238.setMaximumSize(QSize(300, 16777215))
        self.label_238.setStyleSheet(u"")
        self.label_238.setWordWrap(True)
        self.pushButton_ricker = QPushButton(self.frame_12)
        self.pushButton_ricker.setObjectName(u"pushButton_ricker")
        self.pushButton_ricker.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_ricker.sizePolicy().hasHeightForWidth())
        self.pushButton_ricker.setSizePolicy(sizePolicy4)
        self.pushButton_ricker.setCheckable(True)
        self.frame_13 = QFrame(self.FDTD_Cards)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(340, 490, 300, 450))
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_239 = QLabel(self.frame_13)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_239.sizePolicy().hasHeightForWidth())
        self.label_239.setSizePolicy(sizePolicy2)
        self.label_239.setMaximumSize(QSize(300, 16777215))
        self.label_239.setFont(font2)
        self.label_239.setStyleSheet(u"")
        self.label_240 = QLabel(self.frame_13)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setGeometry(QRect(0, 250, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_240.sizePolicy().hasHeightForWidth())
        self.label_240.setSizePolicy(sizePolicy3)
        self.label_240.setMinimumSize(QSize(0, 125))
        self.label_240.setMaximumSize(QSize(300, 16777215))
        self.label_240.setStyleSheet(u"")
        self.label_240.setWordWrap(True)
        self.pushButton_tfsf_minefield = QPushButton(self.frame_13)
        self.pushButton_tfsf_minefield.setObjectName(
            u"pushButton_tfsf_minefield")
        self.pushButton_tfsf_minefield.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_tfsf_minefield.sizePolicy().hasHeightForWidth())
        self.pushButton_tfsf_minefield.setSizePolicy(sizePolicy4)
        self.pushButton_tfsf_minefield.setCheckable(True)
        self.label_242 = QLabel(self.frame_13)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_242.sizePolicy().hasHeightForWidth())
        self.label_242.setSizePolicy(sizePolicy1)
        self.label_242.setMinimumSize(QSize(300, 225))
        self.label_242.setMaximumSize(QSize(300, 225))
        self.label_242.setSizeIncrement(QSize(4, 3))
        self.label_242.setBaseSize(QSize(256, 192))
        self.label_242.setPixmap(
            QPixmap(u":/fdtd/img/fdtd/cards/TFSFMinefield.png"))
        self.label_242.setScaledContents(True)
        self.label_242.setAlignment(Qt.AlignCenter)
        self.frame_14 = QFrame(self.FDTD_Cards)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(660, 20, 300, 450))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_244 = QLabel(self.frame_14)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy2)
        self.label_244.setMaximumSize(QSize(300, 16777215))
        self.label_244.setFont(font2)
        self.label_244.setStyleSheet(u"")
        self.label_245 = QLabel(self.frame_14)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setGeometry(QRect(0, 260, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_245.sizePolicy().hasHeightForWidth())
        self.label_245.setSizePolicy(sizePolicy3)
        self.label_245.setMinimumSize(QSize(0, 125))
        self.label_245.setMaximumSize(QSize(300, 16777215))
        self.label_245.setStyleSheet(u"")
        self.label_245.setWordWrap(True)
        self.pushButton_tfsf_plate = QPushButton(self.frame_14)
        self.pushButton_tfsf_plate.setObjectName(u"pushButton_tfsf_plate")
        self.pushButton_tfsf_plate.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_tfsf_plate.sizePolicy().hasHeightForWidth())
        self.pushButton_tfsf_plate.setSizePolicy(sizePolicy4)
        self.pushButton_tfsf_plate.setCheckable(True)
        self.label_246 = QLabel(self.frame_14)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_246.sizePolicy().hasHeightForWidth())
        self.label_246.setSizePolicy(sizePolicy1)
        self.label_246.setMinimumSize(QSize(300, 225))
        self.label_246.setMaximumSize(QSize(300, 225))
        self.label_246.setSizeIncrement(QSize(4, 3))
        self.label_246.setBaseSize(QSize(256, 192))
        self.label_246.setPixmap(
            QPixmap(u":/fdtd/img/fdtd/cards/TFSFPlate.png"))
        self.label_246.setScaledContents(True)
        self.label_246.setAlignment(Qt.AlignCenter)
        self.frame_15 = QFrame(self.FDTD_Cards)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(980, 20, 300, 450))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_247 = QLabel(self.frame_15)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_247.sizePolicy().hasHeightForWidth())
        self.label_247.setSizePolicy(sizePolicy2)
        self.label_247.setMaximumSize(QSize(300, 16777215))
        self.label_247.setFont(font2)
        self.label_247.setStyleSheet(u"")
        self.label_248 = QLabel(self.frame_15)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setGeometry(QRect(0, 250, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_248.sizePolicy().hasHeightForWidth())
        self.label_248.setSizePolicy(sizePolicy3)
        self.label_248.setMinimumSize(QSize(0, 125))
        self.label_248.setMaximumSize(QSize(300, 16777215))
        self.label_248.setStyleSheet(u"")
        self.label_248.setWordWrap(True)
        self.pushButton_tfsf_disk = QPushButton(self.frame_15)
        self.pushButton_tfsf_disk.setObjectName(u"pushButton_tfsf_disk")
        self.pushButton_tfsf_disk.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_tfsf_disk.sizePolicy().hasHeightForWidth())
        self.pushButton_tfsf_disk.setSizePolicy(sizePolicy4)
        self.pushButton_tfsf_disk.setCheckable(True)
        self.label_249 = QLabel(self.frame_15)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_249.sizePolicy().hasHeightForWidth())
        self.label_249.setSizePolicy(sizePolicy1)
        self.label_249.setMinimumSize(QSize(300, 225))
        self.label_249.setMaximumSize(QSize(300, 225))
        self.label_249.setSizeIncrement(QSize(4, 3))
        self.label_249.setBaseSize(QSize(300, 225))
        self.label_249.setPixmap(
            QPixmap(u":/fdtd/img/fdtd/cards/TFSFDisk.png"))
        self.label_249.setScaledContents(True)
        self.label_249.setAlignment(Qt.AlignCenter)
        self.frame_16 = QFrame(self.FDTD_Cards)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(340, 20, 300, 450))
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.pushButton_tfsf = QPushButton(self.frame_16)
        self.pushButton_tfsf.setObjectName(u"pushButton_tfsf")
        self.pushButton_tfsf.setGeometry(QRect(85, 420, 130, 25))
        sizePolicy4.setHeightForWidth(
            self.pushButton_tfsf.sizePolicy().hasHeightForWidth())
        self.pushButton_tfsf.setSizePolicy(sizePolicy4)
        self.pushButton_tfsf.setCheckable(True)
        self.label_250 = QLabel(self.frame_16)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(0, 230, 300, 24))
        sizePolicy2.setHeightForWidth(
            self.label_250.sizePolicy().hasHeightForWidth())
        self.label_250.setSizePolicy(sizePolicy2)
        self.label_250.setMaximumSize(QSize(300, 16777215))
        self.label_250.setFont(font2)
        self.label_251 = QLabel(self.frame_16)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setGeometry(QRect(0, 250, 300, 125))
        sizePolicy3.setHeightForWidth(
            self.label_251.sizePolicy().hasHeightForWidth())
        self.label_251.setSizePolicy(sizePolicy3)
        self.label_251.setMinimumSize(QSize(0, 125))
        self.label_251.setMaximumSize(QSize(300, 16777215))
        self.label_251.setWordWrap(True)
        self.label_252 = QLabel(self.frame_16)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setGeometry(QRect(0, 0, 300, 225))
        sizePolicy1.setHeightForWidth(
            self.label_252.sizePolicy().hasHeightForWidth())
        self.label_252.setSizePolicy(sizePolicy1)
        self.label_252.setMinimumSize(QSize(300, 225))
        self.label_252.setMaximumSize(QSize(300, 225))
        self.label_252.setSizeIncrement(QSize(4, 3))
        self.label_252.setBaseSize(QSize(256, 192))
        self.label_252.setPixmap(
            QPixmap(u":/fdtd/img/fdtd/cards/TFSFSource.png"))
        self.label_252.setScaledContents(True)
        self.label_252.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.FDTD_Cards)
        self.FDTD_Sim = QWidget()
        self.FDTD_Sim.setObjectName(u"FDTD_Sim")
        self.frame_17 = QFrame(self.FDTD_Sim)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(20, 20, 571, 391))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_fdtd_title = QLabel(self.frame_17)
        self.label_fdtd_title.setObjectName(u"label_fdtd_title")
        self.label_fdtd_title.setGeometry(QRect(20, 20, 501, 41))
        self.label_fdtd_title.setFont(font2)
        self.label_fdtd_desc = QLabel(self.frame_17)
        self.label_fdtd_desc.setObjectName(u"label_fdtd_desc")
        self.label_fdtd_desc.setGeometry(QRect(20, 86, 411, 101))
        self.label_fdtd_desc.setWordWrap(True)
        self.pushButton_fdtd_simulate = QPushButton(self.frame_17)
        self.pushButton_fdtd_simulate.setObjectName(
            u"pushButton_fdtd_simulate")
        self.pushButton_fdtd_simulate.setGeometry(QRect(20, 210, 89, 25))
        self.pushButton_fdtd_animate = QPushButton(self.frame_17)
        self.pushButton_fdtd_animate.setObjectName(u"pushButton_fdtd_animate")
        self.pushButton_fdtd_animate.setGeometry(QRect(20, 280, 89, 25))
        self.label_fdtd_simulate = QLabel(self.frame_17)
        self.label_fdtd_simulate.setObjectName(u"label_fdtd_simulate")
        self.label_fdtd_simulate.setGeometry(QRect(180, 210, 331, 17))
        self.label_fdtd_animate = QLabel(self.frame_17)
        self.label_fdtd_animate.setObjectName(u"label_fdtd_animate")
        self.label_fdtd_animate.setGeometry(QRect(180, 280, 361, 17))
        self.frame_18 = QFrame(self.FDTD_Sim)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(619, 20, 881, 561))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.label_fdtd_anim_title = QLabel(self.frame_18)
        self.label_fdtd_anim_title.setObjectName(u"label_fdtd_anim_title")
        self.label_fdtd_anim_title.setGeometry(QRect(20, 20, 821, 17))
        self.label_fdtd_anim_title.setFont(font2)
        self.stackedWidget.addWidget(self.FDTD_Sim)
        self.frame_nav = QFrame(self.frame)
        self.frame_nav.setObjectName(u"frame_nav")
        self.frame_nav.setGeometry(QRect(20, 20, 225, 600))
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.frame_nav.sizePolicy().hasHeightForWidth())
        self.frame_nav.setSizePolicy(sizePolicy6)
        self.frame_nav.setMinimumSize(QSize(225, 600))
        self.frame_nav.setMaximumSize(QSize(225, 800))
        self.frame_nav.setFrameShape(QFrame.StyledPanel)
        self.frame_nav.setFrameShadow(QFrame.Raised)
        self.verticalLayout_nav = QVBoxLayout(self.frame_nav)
        self.verticalLayout_nav.setObjectName(u"verticalLayout_nav")
        self.label_section_header = QLabel(self.frame_nav)
        self.label_section_header.setObjectName(u"label_section_header")
        sizePolicy3.setHeightForWidth(
            self.label_section_header.sizePolicy().hasHeightForWidth())
        self.label_section_header.setSizePolicy(sizePolicy3)
        self.label_section_header.setMaximumSize(QSize(225, 16777215))
        font5 = QFont()
        font5.setBold(True)
        font5.setUnderline(False)
        self.label_section_header.setFont(font5)
        self.label_section_header.setStyleSheet(u"padding-bottom: -5;\n"
                                                "margin-bottom: -5;\n"
                                                "")
        self.label_section_header.setAlignment(Qt.AlignCenter)
        self.label_section_header.setMargin(0)

        self.verticalLayout_nav.addWidget(self.label_section_header)

        self.line = QFrame(self.frame_nav)
        self.line.setObjectName(u"line")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy7)
        self.line.setMinimumSize(QSize(0, 5))
        self.line.setMaximumSize(QSize(225, 16777215))
        font6 = QFont()
        font6.setPointSize(11)
        self.line.setFont(font6)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_nav.addWidget(self.line)

        self.pushButton_nav_1 = QPushButton(self.frame_nav)
        self.pushButton_nav_1.setObjectName(u"pushButton_nav_1")
        self.pushButton_nav_1.setMaximumSize(QSize(225, 16777215))
        self.pushButton_nav_1.setAutoFillBackground(False)
        self.pushButton_nav_1.setCheckable(True)

        self.verticalLayout_nav.addWidget(self.pushButton_nav_1)

        self.pushButton_nav_2 = QPushButton(self.frame_nav)
        self.pushButton_nav_2.setObjectName(u"pushButton_nav_2")
        self.pushButton_nav_2.setMaximumSize(QSize(225, 16777215))
        self.pushButton_nav_2.setCheckable(True)

        self.verticalLayout_nav.addWidget(self.pushButton_nav_2)

        self.pushButton_nav_3 = QPushButton(self.frame_nav)
        self.pushButton_nav_3.setObjectName(u"pushButton_nav_3")
        self.pushButton_nav_3.setMaximumSize(QSize(225, 16777215))
        self.pushButton_nav_3.setCheckable(True)

        self.verticalLayout_nav.addWidget(self.pushButton_nav_3)

        self.pushButton_nav_4 = QPushButton(self.frame_nav)
        self.pushButton_nav_4.setObjectName(u"pushButton_nav_4")
        self.pushButton_nav_4.setMaximumSize(QSize(225, 16777215))
        self.pushButton_nav_4.setCheckable(True)

        self.verticalLayout_nav.addWidget(self.pushButton_nav_4)

        self.pushButton_nav_5 = QPushButton(self.frame_nav)
        self.pushButton_nav_5.setObjectName(u"pushButton_nav_5")
        self.pushButton_nav_5.setMaximumSize(QSize(225, 16777215))
        self.pushButton_nav_5.setCheckable(True)

        self.verticalLayout_nav.addWidget(self.pushButton_nav_5)

        self.pushButton_nav_6 = QPushButton(self.frame_nav)
        self.pushButton_nav_6.setObjectName(u"pushButton_nav_6")
        self.pushButton_nav_6.setMaximumSize(QSize(225, 16777215))
        self.pushButton_nav_6.setCheckable(True)

        self.verticalLayout_nav.addWidget(self.pushButton_nav_6)

        self.pushButton_nav_7 = QPushButton(self.frame_nav)
        self.pushButton_nav_7.setObjectName(u"pushButton_nav_7")
        self.pushButton_nav_7.setMaximumSize(QSize(225, 16777215))
        self.pushButton_nav_7.setCheckable(True)

        self.verticalLayout_nav.addWidget(self.pushButton_nav_7)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_nav.addItem(self.verticalSpacer)

        self.horizontalLayout_12.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        self.menuSimulator = QMenu(self.menubar)
        self.menuSimulator.setObjectName(u"menuSimulator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSimulator.menuAction())
        self.menuSimulator.addAction(self.actionFDA)
        self.menuSimulator.addAction(self.actionFDTD)
        self.menuSimulator.addAction(self.actionMoM)
        self.menuSimulator.addAction(self.actionFEM)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"PyCEM", None))
        self.actionFDA.setText(
            QCoreApplication.translate("MainWindow", u"FDA", None))
        self.actionFDTD.setText(
            QCoreApplication.translate("MainWindow", u"FDTD", None))
        self.actionMoM.setText(
            QCoreApplication.translate("MainWindow", u"MoM", None))
        self.actionFEM.setText(
            QCoreApplication.translate("MainWindow", u"FEM", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Welcome to PyCEM!", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Choose a solver and a scenario to begin.", None))
        self.label_216.setText("")
        self.label_214.setText(QCoreApplication.translate(
            "MainWindow", u"Symmetric Stripline", None))
        self.label_219.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a symmetric stripline. The signal conductor is centered in the dielectric with two PEC ground planes - one above one and below. ", None))
        self.pushButton_sstrip.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.pushButton_ms.setText(QCoreApplication.translate(
            "MainWindow", u"Click here", None))
        self.label_218.setText(QCoreApplication.translate(
            "MainWindow", u"Microstrip", None))
        self.label_215.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a microstrip transmission line. The signal conductor rests on top of a substrate. The ground plane is on the bottom of the substrate. The region above the substrate is air. ", None))
        self.label_220.setText("")
        self.label_221.setText(QCoreApplication.translate(
            "MainWindow", u"Differential Microstrip", None))
        self.label_222.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a microstrip differential pair. The differential impedance is calculated by applying +/- 0.5V to the two conductors. The common impedance is calculated by applying a common 1V voltage to the two conductors. ", None))
        self.pushButton_diffms.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_217.setText("")
        self.label_224.setText(QCoreApplication.translate(
            "MainWindow", u"Broadside Stripline", None))
        self.label_225.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates broadside-coupled differential stripline. A +0.5V voltage is applied to the top stripline, and a -0.5V voltage is applied to the bottom stripline. ", None))
        self.pushButton_bstrip.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_241.setText("")
        self.label_227.setText(QCoreApplication.translate(
            "MainWindow", u"Coaxial", None))
        self.label_228.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a coaxial transmission line. The center conductor is encased in a dielectric and surrounded by the outer conductor. The default dimensions are based on an SMA female connector with a Teflon dielectric. ", None))
        self.pushButton_coax.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_226.setText("")
        self.label_233.setText(QCoreApplication.translate(
            "MainWindow", u"Differential Stripline", None))
        self.label_234.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates edge-coupled differential stripline. The differential impedance is calculated by applying +/- 0.5V to the two conductors. The common impedance is calculated by applying a common 1V voltage to the two conductors. ", None))
        self.pushButton_dstrip.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_243.setText("")
        self.label_236.setText(QCoreApplication.translate(
            "MainWindow", u"Asymmetric Stripline", None))
        self.label_237.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates asymmetric stripline. The signal conductor is closer to the top ground plane than the bottom ground plane. ", None))
        self.pushButton_astrip.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_235.setText("")
        self.label_fda_title.setText(QCoreApplication.translate(
            "MainWindow", u"Symmetric Stripline", None))
        self.label_fda_desc.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a symmetric stripline. The signal conductor is centered in the dielectric with two PEC ground planes - one above one and below. ", None))
        self.pushButton_analytical.setText(QCoreApplication.translate(
            "MainWindow", u"Analytical Solution", None))
        self.pushButton_simulate.setText(
            QCoreApplication.translate("MainWindow", u"Simulate", None))
        self.label_29.setText(QCoreApplication.translate(
            "MainWindow", u"Refer to the diagram to the right and enter the transmission line parameters in the form below.", None))
        self.label_fdaform1_title.setText(
            QCoreApplication.translate("MainWindow", u"Width (W)", None))
        self.label_fdaform1_desc.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the width of the trace in millimeters.", None))
        self.label_fdaform2_title.setText(
            QCoreApplication.translate("MainWindow", u"Height (H)", None))
        self.label_fdaform2_desc.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the height of the substrate in millimeters.", None))
        self.label_fdaform3_title.setText(QCoreApplication.translate(
            "MainWindow", u"Trace Thickness (T)", None))
        self.label_fdaform3_desc.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the thickness of the trace in millimeters. This is also the size of the grid cell in the Y-direction.", None))
        self.label_fdaform4_title.setText(QCoreApplication.translate(
            "MainWindow", u"Dielectric Constant (Er)", None))
        self.label_fdaform4_desc.setText(QCoreApplication.translate(
            "MainWindow", u"Enter the dielectric constant of the substrate material.", None))
        self.label_fdaform5_title.setText(QCoreApplication.translate(
            "MainWindow", u"X-direction grid cell size (dx)", None))
        self.label_fdaform5_desc.setText(QCoreApplication.translate(
            "MainWindow", u"Enter size of the grid cell in the X-direction (horizontal).", None))
        self.label_fdaform6_title.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_fdaform6_desc.setText(
            QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_fda_diagram.setText("")
        self.label_223.setText(QCoreApplication.translate(
            "MainWindow", u"TF/SF Corner Reflector", None))
        self.label_229.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a Total Field/Scattered Field wave impinging on a corner reflector. The edges of the grid have an absorbing boundary condition (ABC) to capture the radiated waves. ", None))
        self.pushButton_tfsf_corner.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_230.setText("")
        self.label_231.setText("")
        self.label_232.setText(QCoreApplication.translate(
            "MainWindow", u"Ricker Wavelet", None))
        self.label_238.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a Ricker Wavelet source at the center of a 2D grid. The edges of the grid have a perfect electric conductor (PEC) boundary that reflects the radiated waves. ", None))
        self.pushButton_ricker.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_239.setText(QCoreApplication.translate(
            "MainWindow", u"TF/SF Minefield Scatterers", None))
        self.label_240.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a Total Field/Scattered Field wave impinging on multiple circular scatterers. The edges of the grid have an absorbing boundary condition (ABC) to capture the radiated waves. ", None))
        self.pushButton_tfsf_minefield.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_242.setText("")
        self.label_244.setText(QCoreApplication.translate(
            "MainWindow", u"TF/SF Plate", None))
        self.label_245.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a Total Field/Scattered Field wave impinging on a vertical PEC plate. The edges of the grid have an absorbing boundary condition (ABC) to capture the radiated waves. ", None))
        self.pushButton_tfsf_plate.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_246.setText("")
        self.label_247.setText(QCoreApplication.translate(
            "MainWindow", u"TF/SF Disk", None))
        self.label_248.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a Total Field/Scattered Field wave impinging on a circular PEC desk. The edges of the grid have an absorbing boundary condition (ABC) to capture the radiated waves. ", None))
        self.pushButton_tfsf_disk.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_249.setText("")
        self.pushButton_tfsf.setText(
            QCoreApplication.translate("MainWindow", u"Click here", None))
        self.label_250.setText(QCoreApplication.translate(
            "MainWindow", u"TF/SF", None))
        self.label_251.setText(QCoreApplication.translate(
            "MainWindow", u"This scenario simulates a Total Field/Scattered Field wave traveling across a 2D grid. The edges of the grid have an absorbing boundary condition (ABC) to capture the radiated waves. ", None))
        self.label_252.setText("")
        self.label_fdtd_title.setText(QCoreApplication.translate(
            "MainWindow", u"Scenario Title", None))
        self.label_fdtd_desc.setText(QCoreApplication.translate(
            "MainWindow", u"Scenario description", None))
        self.pushButton_fdtd_simulate.setText(
            QCoreApplication.translate("MainWindow", u"Simulate", None))
        self.pushButton_fdtd_animate.setText(
            QCoreApplication.translate("MainWindow", u"Animate", None))
        self.label_fdtd_simulate.setText(QCoreApplication.translate(
            "MainWindow", u"Simulation not run", None))
        self.label_fdtd_animate.setText(QCoreApplication.translate(
            "MainWindow", u"Animation created!", None))
        self.label_fdtd_anim_title.setText(QCoreApplication.translate(
            "MainWindow", u"Scenario Animation", None))
        self.label_section_header.setText(
            QCoreApplication.translate("MainWindow", u"Section Header", None))
        self.pushButton_nav_1.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_nav_2.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_nav_3.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_nav_4.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_nav_5.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_nav_6.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_nav_7.setText(
            QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuSimulator.setTitle(QCoreApplication.translate(
            "MainWindow", u"CEM Solver", None))
    # retranslateUi
