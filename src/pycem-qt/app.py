"""Run PyCEM-Qt application."""

# %% Imports
# Standard system imports
import sys
from enum import IntEnum

# Related third party imports
from PySide6.QtCore import QSize
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QAbstractButton,
    QLabel,
    QPushButton,
    QFrame,
)

# Local application/library specific imports
from modules.PyCEM_GUI import Ui_MainWindow
from modules.fda_scenario_dicts import (
    symmetric_stripline_dict,
    microstrip_dict,
    coaxial_dict,
    asymmetric_stripline_dict,
    diff_microstrip_dict,
    broadside_stripline_dict,
    diff_stripline_dict,
    fda_scenarios_list
)
from modules.fdtd_scenario_dicts import fdtd_scenario_dict


# %% Custom Classes
class StackedPages(IntEnum):
    """Indices of pages in stacked widget."""
    WELCOME = 0
    FDA_CARDS = 1
    FDA_SCENARIOS = 2
    FDTD_CARDS = 3
    FDTD_SCENARIOS = 4


class PicButton(QAbstractButton):
    """Custom class to allow clickable image."""

    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()


# %% PyCEM-Qt main window
class MainWindow(QMainWindow, Ui_MainWindow):
    """Define PyCEM-Qt GUI."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # File menu signals.
        self.actionFDA.triggered.connect(self.load_fda_cards_page)
        self.actionFDTD.triggered.connect(self.load_fdtd_cards_page)

        # Widget signals on navigation pane.
        # Intially hide buttons
        nav_buttons = self.frame_nav.findChildren(QPushButton)
        for button in nav_buttons:
            button.released.connect(self.nav_pushbutton_slot)
        self.hide_nav_pushbuttons()

        # Add clickable PyCEM logo to nav bar
        self.pycem_logo = PicButton(
            QPixmap(u":/icons/img/icons/PyCEM.png"))
        self.pycem_logo.setMaximumSize(QSize(225, 16777215))
        self.pycem_logo.clicked.connect(self.load_welcome_page)
        self.verticalLayout_nav.insertWidget(0, self.pycem_logo)

        # Widget signals on FDA Cards page.
        self.pushButton_sstrip.released.connect(self.load_fda_scenario_page)
        self.pushButton_ms.released.connect(self.load_fda_scenario_page)
        self.pushButton_coax.released.connect(self.load_fda_scenario_page)
        self.pushButton_astrip.released.connect(self.load_fda_scenario_page)
        self.pushButton_diffms.released.connect(self.load_fda_scenario_page)
        self.pushButton_bstrip.released.connect(self.load_fda_scenario_page)
        self.pushButton_dstrip.released.connect(self.load_fda_scenario_page)

        # Widget signals on FDTD Cards page.
        self.pushButton_ricker.released.connect(self.load_fdtd_scenario_page)
        self.pushButton_tfsf.released.connect(self.load_fdtd_scenario_page)
        self.pushButton_tfsf_plate.released.connect(
            self.load_fdtd_scenario_page)
        self.pushButton_tfsf_disk.released.connect(
            self.load_fdtd_scenario_page)
        self.pushButton_tfsf_corner.released.connect(
            self.load_fdtd_scenario_page)
        self.pushButton_tfsf_minefield.released.connect(
            self.load_fdtd_scenario_page)

    def hide_nav_pushbuttons(self):
        """Hide buttons in navigation pane."""
        for i in range(0, self.verticalLayout_nav.count()):
            try:
                widget = self.verticalLayout_nav.itemAt(i).wid
                if not isinstance(widget, PicButton):
                    widget.setVisible(False)
            except:
                pass

    def nav_pushbutton_slot(self):
        """Choose appropriate solver when nav buttons are pushed."""
        current_index = self.stackedWidget.currentIndex()
        if current_index == StackedPages.FDA_CARDS or \
                current_index == StackedPages.FDA_SCENARIOS:
            self.load_fda_scenario_page()
        elif current_index == StackedPages.FDTD_CARDS or \
                current_index == StackedPages.FDTD_SCENARIOS:
            self.load_fdtd_scenario_page()

    def load_welcome_page(self):
        """Bring page containing welcome screen to top of stacked widget."""
        if self.stackedWidget.currentIndex() == StackedPages.FDA_SCENARIOS:
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_CARDS)
        elif self.stackedWidget.currentIndex() == StackedPages.FDTD_SCENARIOS:
            self.stackedWidget.setCurrentIndex(StackedPages.FDTD_CARDS)
        else:
            self.hide_nav_pushbuttons()
            self.stackedWidget.setCurrentIndex(StackedPages.WELCOME)

    def load_fda_cards_page(self):
        """Bring page containing FDA scenarios to top of stacked widget."""
        self.stackedWidget.setCurrentIndex(StackedPages.FDA_CARDS)
        # Update navigation menu
        self.hide_nav_pushbuttons()
        self.label_section_header.setText('FDA Scenarios')
        nav_labels = self.frame_nav.findChildren(QLabel)
        for label in nav_labels:
            label.setVisible(True)
        nav_lines = self.frame_nav.findChildren(QFrame)
        for line in nav_lines:
            line.setVisible(True)
        nav_buttons = self.frame_nav.findChildren(QPushButton)
        for button, scenario in zip(nav_buttons, fda_scenarios_list):
            button.setText(scenario['title'])
            button.setVisible(True)

    def load_fdtd_cards_page(self):
        """Bring page containing FDTD scenarios to top of stacked widget."""
        self.stackedWidget.setCurrentIndex(StackedPages.FDTD_CARDS)
        # Update navigation menu
        self.hide_nav_pushbuttons()
        self.label_section_header.setText('FDTD Scenarios')
        nav_labels = self.frame_nav.findChildren(QLabel)
        for label in nav_labels:
            label.setVisible(True)
        nav_lines = self.frame_nav.findChildren(QFrame)
        for line in nav_lines:
            line.setVisible(True)
        nav_buttons = self.frame_nav.findChildren(QPushButton)
        for button, scenario in zip(nav_buttons, fdtd_scenario_dict.values()):
            button.setText(scenario['title'])
            button.setVisible(True)

    def load_fda_scenario_page(self):
        """Bring page with user-selected FDA scenario to top."""
        if self.pushButton_sstrip.isChecked() or \
                self.pushButton_nav_1.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_sstrip.setChecked(False)
            self.pushButton_nav_1.setChecked(False)
            self.load_fda_scenario(symmetric_stripline_dict)
        if self.pushButton_ms.isChecked() or \
                self.pushButton_nav_2.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_ms.setChecked(False)
            self.pushButton_nav_2.setChecked(False)
            self.load_fda_scenario(microstrip_dict)
        if self.pushButton_coax.isChecked() or \
                self.pushButton_nav_3.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_coax.setChecked(False)
            self.pushButton_nav_3.setChecked(False)
            self.load_fda_scenario(coaxial_dict)
        if self.pushButton_astrip.isChecked() or \
                self.pushButton_nav_4.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_astrip.setChecked(False)
            self.pushButton_nav_4.setChecked(False)
            self.load_fda_scenario(asymmetric_stripline_dict)
        if self.pushButton_diffms.isChecked() or \
                self.pushButton_nav_5.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_diffms.setChecked(False)
            self.pushButton_nav_5.setChecked(False)
            self.load_fda_scenario(diff_microstrip_dict)
        if self.pushButton_bstrip.isChecked() or \
                self.pushButton_nav_6.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_bstrip.setChecked(False)
            self.pushButton_nav_6.setChecked(False)
            self.load_fda_scenario(broadside_stripline_dict)
        if self.pushButton_dstrip.isChecked() or \
                self.pushButton_nav_7.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_dstrip.setChecked(False)
            self.pushButton_nav_7.setChecked(False)
            self.load_fda_scenario(diff_stripline_dict)

    def load_fda_scenario(self, scenario):
        """Populate FDA page with appropriate scenario text and diagram."""
        self.label_fda_diagram.setPixmap(QPixmap(scenario['diagram']))
        self.label_fda_title.setText(scenario['title'])
        self.label_fda_desc.setText(scenario['description'])
        self.label_fdaform1_title.setText(scenario['input1_title'])
        self.doubleSpinBox_fdaform1_input.setValue(scenario['input1_val'])
        self.label_fdaform1_desc.setText(scenario['input1_desc'])
        self.label_fdaform2_title.setText(scenario['input2_title'])
        self.doubleSpinBox_fdaform2_input.setValue(scenario['input2_val'])
        self.label_fdaform2_desc.setText(scenario['input2_desc'])
        self.label_fdaform3_title.setText(scenario['input3_title'])
        self.doubleSpinBox_fdaform3_input.setValue(scenario['input3_val'])
        self.label_fdaform3_desc.setText(scenario['input3_desc'])
        self.label_fdaform4_title.setText(scenario['input4_title'])
        self.doubleSpinBox_fdaform4_input.setValue(scenario['input4_val'])
        self.label_fdaform4_desc.setText(scenario['input4_desc'])
        self.label_fdaform5_title.setText(scenario['input5_title'])
        self.doubleSpinBox_fdaform5_input.setValue(scenario['input5_val'])
        self.label_fdaform5_desc.setText(scenario['input5_desc'])
        if scenario['num_inputs'] == 6:
            self.label_fdaform6_title.show()
            self.doubleSpinBox_fdaform6_input.show()
            self.label_fdaform6_desc.show()
            self.label_fdaform6_title.setText(scenario['input6_title'])
            self.doubleSpinBox_fdaform6_input.setValue(scenario['input6_val'])
            self.label_fdaform6_desc.setText(scenario['input6_desc'])
        else:
            self.label_fdaform6_title.hide()
            self.doubleSpinBox_fdaform6_input.hide()
            self.label_fdaform6_desc.hide()

    def load_fdtd_scenario_page(self):
        """Bring page with user-selected FDTD scenario to top."""
        if self.pushButton_ricker.isChecked() or \
                self.pushButton_nav_1.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDTD_SCENARIOS)
            self.pushButton_ricker.setChecked(False)
            self.pushButton_nav_1.setChecked(False)
            self.load_fdtd_scenario(fdtd_scenario_dict['ricker'])
        if self.pushButton_tfsf.isChecked() or \
                self.pushButton_nav_2.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDTD_SCENARIOS)
            self.pushButton_tfsf.setChecked(False)
            self.pushButton_nav_2.setChecked(False)
            self.load_fdtd_scenario(fdtd_scenario_dict['tfsf'])
        if self.pushButton_tfsf_plate.isChecked() or \
                self.pushButton_nav_3.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDTD_SCENARIOS)
            self.pushButton_tfsf_plate.setChecked(False)
            self.pushButton_nav_3.setChecked(False)
            self.load_fdtd_scenario(fdtd_scenario_dict['tfsf_plate'])
        if self.pushButton_tfsf_disk.isChecked() or \
                self.pushButton_nav_4.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDTD_SCENARIOS)
            self.pushButton_tfsf_disk.setChecked(False)
            self.pushButton_nav_4.setChecked(False)
            self.load_fdtd_scenario(fdtd_scenario_dict['tfsf_disk'])
        if self.pushButton_tfsf_corner.isChecked() or \
                self.pushButton_nav_5.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDTD_SCENARIOS)
            self.pushButton_tfsf_corner.setChecked(False)
            self.pushButton_nav_5.setChecked(False)
            self.load_fdtd_scenario(fdtd_scenario_dict['tfsf_corner'])
        if self.pushButton_tfsf_minefield.isChecked() or \
                self.pushButton_nav_6.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDTD_SCENARIOS)
            self.pushButton_tfsf_minefield.setChecked(False)
            self.pushButton_nav_6.setChecked(False)
            self.load_fdtd_scenario(fdtd_scenario_dict['tfsf_minefield'])

    def load_fdtd_scenario(self, scenario):
        """Populate FDTD page with appropriate scenario text."""
        self.label_fdtd_title.setText(scenario['title'])
        self.label_fdtd_desc.setText(scenario['description'])
        self.label_fdtd_anim_title.setText(scenario['title'] + ' Animation')


app = QApplication(sys.argv)
w = MainWindow()
app.exec()