"""Custom classes used by the Qt GUI."""
# %% Imports
# Standard system imports
from enum import IntEnum

# Related third party imports
from PySide6 import QtCore
from PySide6.QtCore import Qt, QRunnable, Slot, QUrl
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QAbstractButton

# Local application/library specific imports
from modules.fdtd_pyvista import save_mesh_movie


# %% Classes
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


class FDTD_Simulation(QRunnable):
    """
    Worker thread to concurrently execute FDTD simulation.
    """

    def __init__(self, scenario, qt_gui):
        """Pass variables from Qt GUI to this worker thread."""
        super().__init__()
        self.scenario = scenario
        self.qt_gui = qt_gui

    @Slot()
    def run(self):
        """Run FDTD simulation in its own thread."""
        self.scenario.run_sim()
        self.qt_gui.fdtd_simulation_complete = True
        self.qt_gui.progressBar_fdtd_sim.hide()
        self.qt_gui.pushButton_fdtd_animate.setEnabled(True)
        self.qt_gui.label_fdtd_simulate.setText('Simulation complete!')


class FDTD_Animation(QRunnable):
    """
    Worker thread to concurrently create FDTD animation.
    """

    def __init__(self, vid_path, scenario, qt_gui):
        """Pass variables from Qt GUI to this worker thread."""
        super().__init__()
        self.vid_path = vid_path
        self.scenario = scenario
        self.qt_gui = qt_gui

    @Slot()
    def run(self):
        """Create FDTD animation in its own thread."""
        save_mesh_movie(self.vid_path, self.scenario)
        self.qt_gui.progressBar_fdtd_animate.hide()
        self.qt_gui.label_fdtd_animate.setText('Animation created!')
        if self.vid_path.is_file():
            url = str(self.vid_path)
            self.qt_gui._player.setSource(QUrl(url))
