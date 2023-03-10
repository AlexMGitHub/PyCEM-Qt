"""Run PyCEM-Qt application."""
# %% Imports
# Standard system imports
import sys
from enum import IntEnum

# Related third party imports
import pandas as pd
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QSize, QRunnable, QThreadPool, Slot
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
from modules.fda_scenarios import (
    SymmetricStripline,
    Microstrip, Coaxial,
    AsymmetricStripline,
    DifferentialMicrostrip,
    BroadsideStripline,
    DifferentialStripline
)
from modules.utilities import get_project_root, list_files


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


class TableModel(QtCore.QAbstractTableModel):
    """QTableView model for data in Pandas dataframe format."""

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            if isinstance(value, float):
                # Render float to 2 dp
                return str("%.2f" % value)
            return str(value)

        if role == Qt.TextAlignmentRole:
            value = self._data.iloc[index.row(), index.column()]
            if isinstance(value, int) or isinstance(value, float):
                # Align center, vertical middle.
                return Qt.AlignVCenter + Qt.AlignHCenter
            else:
                # Align left, vertical middle.
                return Qt.AlignVCenter + Qt.AlignLeft

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class FDA_Simulation(QRunnable):
    """
    Worker thread to concurrently execute FDA simulation.
    """

    def __init__(self, analytical_results, filepath, scenario, qt_gui):
        """Pass variables from Qt GUI to this worker thread."""
        super().__init__()
        self.analytical_results = analytical_results
        self.filepath = filepath
        self.scenario = scenario
        self.qt_gui = qt_gui

    @Slot()
    def run(self):
        """Run FDA simulation in its own thread."""
        analytical_results = self.analytical_results
        filepath = self.filepath
        scenario = self.scenario
        qt_gui = self.qt_gui
        qt_gui.pushButton_simulate.setChecked(False)
        if not scenario.differential:
            _, _, sim_z0 = scenario.run_sim(filepath=filepath,
                                            set_progress=None)
            qt_gui.update_fda_scenario_table(analytical_results, sim_z0)
        else:
            _, _, diff_z0, _, _, comm_z0, _, _ = scenario.run_sim(filepath=filepath,
                                                                  set_progress=None)
            qt_gui.update_fda_scenario_table(
                analytical_results, (diff_z0, comm_z0))
        qt_gui.progressBar_FDA_sim.hide()
        qt_gui.fda_image_idx = 0
        qt_gui.set_fda_image_path()
        qt_gui.fda_next_image.setEnabled(True)
        qt_gui.fda_prev_image.setEnabled(True)

# %% PyCEM-Qt main window


class MainWindow(QMainWindow, Ui_MainWindow):
    """Define PyCEM-Qt GUI."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Set up multithreading
        self.threadpool = QThreadPool()

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

        # Widget signals on FDA Sim page.
        self.pushButton_analytical.released.connect(self.analytical_soln)
        self.pushButton_simulate.released.connect(self.run_fda_sim)
        self.fda_next_image.released.connect(self.next_fda_image)
        self.fda_prev_image.released.connect(self.prev_fda_image)

        # Scenario-related variables
        self.fda_scenario = None
        self.fda_image_list = None
        self.fda_image_idx = 0

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

    def set_fda_image_path(self):
        """Set path to images generated by FDA simulation."""
        img_path = get_project_root() / 'img/fda/scenarios'
        diag_path = get_project_root() / 'img/fda/diagrams'
        scenario_path = img_path / self.fda_scenario.name
        self.fda_image_list = list_files(scenario_path)
        diag_img_path = diag_path / (self.fda_scenario.name + '.png')
        self.fda_image_list.insert(0, diag_img_path)
        self.qlabel_fda_image.setText(self.fda_scenario.name)

    def load_fda_scenario_page(self):
        """Bring page with user-selected FDA scenario to top."""
        self.fda_image_idx = 0
        if self.pushButton_sstrip.isChecked() or \
                self.pushButton_nav_1.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_sstrip.setChecked(False)
            self.pushButton_nav_1.setChecked(False)
            self.fda_scenario = SymmetricStripline
            self.set_fda_image_path()
            self.load_fda_scenario(symmetric_stripline_dict)
        if self.pushButton_ms.isChecked() or \
                self.pushButton_nav_2.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_ms.setChecked(False)
            self.pushButton_nav_2.setChecked(False)
            self.fda_scenario = Microstrip
            self.set_fda_image_path()
            self.load_fda_scenario(microstrip_dict)
        if self.pushButton_coax.isChecked() or \
                self.pushButton_nav_3.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_coax.setChecked(False)
            self.pushButton_nav_3.setChecked(False)
            self.fda_scenario = Coaxial
            self.set_fda_image_path()
            self.load_fda_scenario(coaxial_dict)
        if self.pushButton_astrip.isChecked() or \
                self.pushButton_nav_4.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_astrip.setChecked(False)
            self.pushButton_nav_4.setChecked(False)
            self.fda_scenario = AsymmetricStripline
            self.set_fda_image_path()
            self.load_fda_scenario(asymmetric_stripline_dict)
        if self.pushButton_diffms.isChecked() or \
                self.pushButton_nav_5.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_diffms.setChecked(False)
            self.pushButton_nav_5.setChecked(False)
            self.fda_scenario = DifferentialMicrostrip
            self.set_fda_image_path()
            self.load_fda_scenario(diff_microstrip_dict)
        if self.pushButton_bstrip.isChecked() or \
                self.pushButton_nav_6.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_bstrip.setChecked(False)
            self.pushButton_nav_6.setChecked(False)
            self.fda_scenario = BroadsideStripline
            self.set_fda_image_path()
            self.load_fda_scenario(broadside_stripline_dict)
        if self.pushButton_dstrip.isChecked() or \
                self.pushButton_nav_7.isChecked():
            self.stackedWidget.setCurrentIndex(StackedPages.FDA_SCENARIOS)
            self.pushButton_dstrip.setChecked(False)
            self.pushButton_nav_7.setChecked(False)
            self.fda_scenario = DifferentialStripline
            self.set_fda_image_path()
            self.load_fda_scenario(diff_stripline_dict)

    def load_fda_scenario(self, scenario):
        """Populate FDA page with appropriate scenario text and diagram."""
        if len(self.fda_image_list) > 1:
            self.fda_next_image.setEnabled(True)
            self.fda_prev_image.setEnabled(True)
        else:
            self.fda_next_image.setEnabled(False)
            self.fda_prev_image.setEnabled(False)
        self.progressBar_FDA_sim.setVisible(False)
        self.tableView.setModel(None)
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

    def analytical_soln(self, update=True):
        """Calculate and display analytical solution of transmission line."""
        if self.fda_scenario == SymmetricStripline:
            scenario = self.fda_scenario(
                trace_w=self.doubleSpinBox_fdaform1_input.value()/1000,
                sub_thk=self.doubleSpinBox_fdaform2_input.value()/1000,
                dy=self.doubleSpinBox_fdaform3_input.value()/1000,
                Er=self.doubleSpinBox_fdaform4_input.value(),
                dx=self.doubleSpinBox_fdaform5_input.value()/1000,
            )
        elif self.fda_scenario == Microstrip:
            scenario = self.fda_scenario(
                trace_w=self.doubleSpinBox_fdaform1_input.value()/1000,
                sub_thk=self.doubleSpinBox_fdaform2_input.value()/1000,
                dy=self.doubleSpinBox_fdaform3_input.value()/1000,
                Er=self.doubleSpinBox_fdaform4_input.value(),
                dx=self.doubleSpinBox_fdaform5_input.value()/1000,
            )
        elif self.fda_scenario == Coaxial:
            scenario = self.fda_scenario(
                inner_rad=self.doubleSpinBox_fdaform1_input.value()/2000,
                outer_rad=self.doubleSpinBox_fdaform2_input.value()/2000,
                dy=self.doubleSpinBox_fdaform3_input.value()/1000,
                Er=self.doubleSpinBox_fdaform4_input.value(),
                dx=self.doubleSpinBox_fdaform5_input.value()/1000,
            )
        elif self.fda_scenario == AsymmetricStripline:
            scenario = self.fda_scenario(
                trace_w=self.doubleSpinBox_fdaform1_input.value()/1000,
                sub_thk=self.doubleSpinBox_fdaform2_input.value()/1000,
                dy=self.doubleSpinBox_fdaform3_input.value()/1000,
                Er=self.doubleSpinBox_fdaform4_input.value(),
                dx=self.doubleSpinBox_fdaform5_input.value()/1000,
                offset=self.doubleSpinBox_fdaform6_input.value()/1000,
            )
        elif self.fda_scenario == DifferentialMicrostrip:
            scenario = self.fda_scenario(
                trace_w=self.doubleSpinBox_fdaform1_input.value()/1000,
                sub_thk=self.doubleSpinBox_fdaform2_input.value()/1000,
                dy=self.doubleSpinBox_fdaform3_input.value()/1000,
                Er=self.doubleSpinBox_fdaform4_input.value(),
                dx=self.doubleSpinBox_fdaform5_input.value()/1000,
                spacing=self.doubleSpinBox_fdaform6_input.value()/1000,
            )
        elif self.fda_scenario == BroadsideStripline:
            scenario = self.fda_scenario(
                trace_w=self.doubleSpinBox_fdaform1_input.value()/1000,
                sub_thk=self.doubleSpinBox_fdaform2_input.value()/1000,
                dy=self.doubleSpinBox_fdaform3_input.value()/1000,
                Er=self.doubleSpinBox_fdaform4_input.value(),
                dx=self.doubleSpinBox_fdaform5_input.value()/1000,
                spacing=self.doubleSpinBox_fdaform6_input.value()/1000,
            )
        elif self.fda_scenario == DifferentialStripline:
            scenario = self.fda_scenario(
                trace_w=self.doubleSpinBox_fdaform1_input.value()/1000,
                sub_thk=self.doubleSpinBox_fdaform2_input.value()/1000,
                dy=self.doubleSpinBox_fdaform3_input.value()/1000,
                Er=self.doubleSpinBox_fdaform4_input.value(),
                dx=self.doubleSpinBox_fdaform5_input.value()/1000,
                spacing=self.doubleSpinBox_fdaform6_input.value()/1000,
            )
        results = scenario.analytical_soln()
        print(results)
        self.pushButton_analytical.setChecked(False)
        if update:
            self.update_fda_scenario_table(results)
        return scenario, results

    def run_fda_sim(self):
        """Run FDA simulation using input values for scenario."""
        scenario, analytical_results = self.analytical_soln(update=False)
        self.progressBar_FDA_sim.show()
        root = get_project_root()
        filepath = root / 'img/fda/scenarios'
        worker = FDA_Simulation(analytical_results, filepath, scenario, self)
        worker = self.threadpool.start(worker)

    def next_fda_image(self):
        """Display next FDA simulation image in rotation."""
        self.fda_image_idx += 1
        if self.fda_image_idx >= len(self.fda_image_list):
            self.fda_image_idx = 0
        next_image = self.fda_image_list[self.fda_image_idx]
        pixmap = QPixmap(next_image)
        self.label_fda_diagram.setPixmap(pixmap)
        self.qlabel_fda_image.setText(next_image.stem)

    def prev_fda_image(self):
        """Display previous FDA simulation image in rotation."""
        self.fda_image_idx -= 1
        if self.fda_image_idx < 0:
            self.fda_image_idx = len(self.fda_image_list) - 1
        prev_image = self.fda_image_list[self.fda_image_idx]
        pixmap = QPixmap(prev_image)
        self.label_fda_diagram.setPixmap(pixmap)
        self.qlabel_fda_image.setText(prev_image.stem)

    def update_fda_scenario_table(self, results, sim_results=0.0):
        """Update the results table for the FDA scenario."""
        if not isinstance(results, tuple):
            if sim_results == 0:
                perc_diff = 0.0
            else:
                perc_diff = (sim_results - results) / sim_results * 100
            data = pd.DataFrame([
                ['Characteristic Impedance (Ohms)',
                 results, sim_results, perc_diff]
            ], columns=['Quantity', 'Analytical Formula', 'FDA Simulation', 'Percent Difference'])
        else:
            if sim_results == 0:
                diff_perc_diff = 0.0
                comm_perc_diff = 0.0
                diff_z0 = 0.0
                comm_z0 = 0.0
            else:
                diff_perc_diff = (
                    sim_results[0] - results[0]) / sim_results[0] * 100
                comm_perc_diff = (
                    sim_results[1] - results[1]) / sim_results[1] * 100
                diff_z0 = sim_results[0]
                comm_z0 = sim_results[1]
            data = pd.DataFrame([
                ['Differential Impedance (Ohms)', results[0],
                 diff_z0, diff_perc_diff],
                ['Common Impedance (Ohms)', results[1],
                 comm_z0, comm_perc_diff],
            ], columns=['Quantity', 'Analytical Formula', 'FDA Simulation', 'Percent Difference'])
        self.tableView.setModel(TableModel(data))
        self.tableView.setColumnWidth(0, 250)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 200)
        self.tableView.setColumnWidth(3, 200)


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
