from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, QMetaObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self, scr_size):
        super().__init__()
        # Setting names
        self.setWindowTitle("Requester")
        self.setObjectName("Requester")

        # Setting font
        self.font = QFont()
        self.font.setFamily("Ligconsolata")
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.setFont(self.font)

        # Setting size
        self.scr_width = scr_size.width()
        self.scr_height = scr_size.height()
        self.setGeometry(0, 0, self.scr_width, self.scr_height)
        self.setMaximumSize(QSize(1920, 1080))

        # Setting main window layout
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("vertical_layout")

        self.init_interface()

    def init_interface(self):
        self.main_tab = QtWidgets.QTabWidget(self.central_widget)
        self.main_tab.setObjectName("main_tab")
        self.init_payload_tab()
        self.init_attack_tab()
        self.init_options_tab()
        self.vertical_layout.addWidget(self.main_tab)
        self.setCentralWidget(self.central_widget)

        self.set_names()
        self.main_tab.setCurrentIndex(2)
        self.results_view.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def init_payload_tab(self):
        self.payload_tab = QtWidgets.QWidget()
        self.payload_tab.setObjectName("payload_tab")

        # Payload tab layout
        self.payload_vertical_layout = QtWidgets.QVBoxLayout(self.payload_tab)
        self.payload_vertical_layout.setObjectName("verticalLayout_2")

        # "Header:" label
        self.header_label = QtWidgets.QLabel(self.payload_tab)
        self.header_label.setFont(self.font)
        self.header_label.setObjectName("header_label")
        self.payload_vertical_layout.addWidget(self.header_label)

        # Text editor (header)
        self.header_editor = QtWidgets.QTextEdit(self.payload_tab)
        self.header_editor.setObjectName("header_editor")
        self.payload_vertical_layout.addWidget(self.header_editor)

        # Add payload button
        self.add_payload_button = QtWidgets.QPushButton(self.payload_tab)
        self.add_payload_button.setFont(self.font)
        self.add_payload_button.setObjectName("add_payload_button")
        self.payload_vertical_layout.addWidget(self.add_payload_button)

        # Payload list
        self.payload_list = QtWidgets.QListView(self.payload_tab)
        self.payload_list.setObjectName("payload_list")
        self.payload_vertical_layout.addWidget(self.payload_list)

        # Start button
        self.start_atack_button = QtWidgets.QPushButton(self.payload_tab)
        self.start_atack_button.setObjectName("start_atack_b")
        self.payload_vertical_layout.addWidget(self.start_atack_button)

        self.main_tab.addTab(self.payload_tab, "")

    def init_attack_tab(self):
        self.attack_tab = QtWidgets.QWidget()
        self.attack_tab.setObjectName("attack_tab")

        # Attack tab layout
        self.attack_grid_layout = QtWidgets.QGridLayout(self.attack_tab)
        self.attack_grid_layout.setObjectName("grid_layout")

        # Results label
        self.a_results_label = QtWidgets.QLabel(self.attack_tab)
        self.a_results_label.setObjectName("a_results_label")
        self.attack_grid_layout.addWidget(self.a_results_label, 0, 1, 1, 1)

        # Results tab (request, response)
        self.results_view = QtWidgets.QTabWidget(self.attack_tab)
        self.results_view.setObjectName("results_view")

        # Request view tab in results
        self.req_tab = QtWidgets.QWidget()
        self.req_tab.setObjectName("req_tab")
        self.request_tab_v_layout = QtWidgets.QVBoxLayout(self.req_tab)
        self.request_tab_v_layout.setObjectName("request_tab_v_layout")

        # Text browser
        self.req_view = QtWidgets.QTextBrowser(self.req_tab)
        self.req_view.setObjectName("req_view")
        self.request_tab_v_layout.addWidget(self.req_view)
        self.results_view.addTab(self.req_tab, "")

        # Response view tab in results
        self.resp_tab = QtWidgets.QWidget()
        self.resp_tab.setObjectName("resp_tab")
        self.resp_tab_v_layout = QtWidgets.QVBoxLayout(self.resp_tab)
        self.resp_tab_v_layout.setObjectName("resp_tab_v_layout")

        # Text browser
        self.resp_view = QtWidgets.QTextBrowser(self.resp_tab)
        self.resp_view.setObjectName("resp_view")
        self.resp_tab_v_layout.addWidget(self.resp_view)
        self.results_view.addTab(self.resp_tab, "")

        self.attack_grid_layout.addWidget(self.results_view, 2, 1, 1, 1)

        # Results list view
        self.a_results_view = QtWidgets.QListView(self.attack_tab)
        self.a_results_view.setObjectName("a_results_view")
        self.attack_grid_layout.addWidget(self.a_results_view, 1, 1, 1, 1)

        # Progress bar
        self.attack_proggress = QtWidgets.QProgressBar(self.attack_tab)
        self.attack_proggress.setProperty("value", 24)
        self.attack_proggress.setObjectName("a_proggress")
        self.attack_grid_layout.addWidget(self.attack_proggress, 3, 1, 1, 1)

        self.main_tab.addTab(self.attack_tab, "")

    def init_options_tab(self):
        self.options_tab = QtWidgets.QWidget()
        self.options_tab.setObjectName("options_tab")

        # Options tab layout
        self.options_g_layout = QtWidgets.QGridLayout(self.options_tab)
        self.options_g_layout.setObjectName("gridLayout_2")

        # Timings label
        self.timing_label = QtWidgets.QLabel(self.options_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timing_label.sizePolicy().hasHeightForWidth())
        self.timing_label.setSizePolicy(sizePolicy)
        self.timing_label.setObjectName("timing_label")
        self.options_g_layout.addWidget(self.timing_label, 0, 0, 1, 1)

        # Frame containing options to set
        self.timings_frame = QtWidgets.QFrame(self.options_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.timings_frame.sizePolicy().hasHeightForWidth())
        self.timings_frame.setSizePolicy(sizePolicy)
        self.timings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timings_frame.setObjectName("timings_frame")

        # Timings main layout
        self.timing_g_layout = QtWidgets.QGridLayout(self.timings_frame)
        self.timing_g_layout.setObjectName("gridLayout_3")

        # Throttle label
        self.throttle_label = QtWidgets.QLabel(self.timings_frame)
        self.throttle_label.setObjectName("throttle_label")
        self.timing_g_layout.addWidget(self.throttle_label, 0, 0, 1, 1)

        # Timings layout
        self.timings_v_layout = QtWidgets.QVBoxLayout()
        self.timings_v_layout.setObjectName("timings_v_layout")

        # Fixed option horizontal layout
        self.fixed_h_layout = QtWidgets.QHBoxLayout()
        self.fixed_h_layout.setContentsMargins(5, -1, 5, -1)
        self.fixed_h_layout.setObjectName("fixed_h_layout")

        # Fixed option checkbox
        self.fixed_chceckbox = QtWidgets.QCheckBox(self.timings_frame)
        self.fixed_chceckbox.setObjectName("fixed_chceckbox")
        self.fixed_h_layout.addWidget(self.fixed_chceckbox)

        # Fixed option input
        self.fixed_input = QtWidgets.QLineEdit(self.timings_frame)
        self.fixed_input.setObjectName("fixed_input")
        self.fixed_h_layout.addWidget(self.fixed_input)

        # Horizontal spacers (fixed)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fixed_h_layout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fixed_h_layout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fixed_h_layout.addItem(spacerItem2)
        self.timings_v_layout.addLayout(self.fixed_h_layout)

        # Rising option horizontal layout
        self.rising_h_layout = QtWidgets.QHBoxLayout()
        self.rising_h_layout.setContentsMargins(5, -1, 5, -1)
        self.rising_h_layout.setObjectName("rising_h_layout")

        # Rising option checkbox
        self.rising_chceck = QtWidgets.QCheckBox(self.timings_frame)
        self.rising_chceck.setObjectName("rising_chceck")
        self.rising_h_layout.addWidget(self.rising_chceck)

        # Fixed option start label
        self.start_label = QtWidgets.QLabel(self.timings_frame)
        self.start_label.setObjectName("start_label")
        self.rising_h_layout.addWidget(self.start_label)

        # Fixed option start input
        self.risint_start_input = QtWidgets.QLineEdit(self.timings_frame)
        self.risint_start_input.setObjectName("risint_start_input")
        self.rising_h_layout.addWidget(self.risint_start_input)

        # Fixed option step label
        self.step_label = QtWidgets.QLabel(self.timings_frame)
        self.step_label.setObjectName("step_label")
        self.rising_h_layout.addWidget(self.step_label)

        # Fixed option step input
        self.step_input = QtWidgets.QLineEdit(self.timings_frame)
        self.step_input.setObjectName("step_input")
        self.rising_h_layout.addWidget(self.step_input)

        # Horizontal spacer (rising)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rising_h_layout.addItem(spacerItem3)

        # Putting it all together
        self.timings_v_layout.addLayout(self.rising_h_layout)
        self.timing_g_layout.addLayout(self.timings_v_layout, 3, 0, 1, 1)

        # Vertical spacer in main layout
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.timing_g_layout.addItem(spacerItem4, 4, 0, 1, 1)

        self.options_g_layout.addWidget(self.timings_frame, 1, 0, 1, 1)
        self.main_tab.addTab(self.options_tab, "")

    def set_names(self):
        self.header_label.setText("Header:")
        self.add_payload_button.setText("Add payload")
        self.start_atack_button.setText("Start")
        self.main_tab.setTabText(self.main_tab.indexOf(self.payload_tab), "Payload")
        self.a_results_label.setText("Results:")
        self.results_view.setTabText(self.results_view.indexOf(self.req_tab), "Request")
        self.results_view.setTabText(self.results_view.indexOf(self.resp_tab), "Response")
        self.main_tab.setTabText(self.main_tab.indexOf(self.attack_tab), "Attack")
        self.timing_label.setText("Timing:")
        self.throttle_label.setText("Throttle (ms):")
        self.fixed_chceckbox.setText("Constant:")
        self.rising_chceck.setText("Rising:")
        self.start_label.setText("start:")
        self.step_label.setText("step:")
        self.main_tab.setTabText(self.main_tab.indexOf(self.options_tab), "Options")


def run():
    app = QApplication(sys.argv)
    screen_size = app.primaryScreen().size()
    window = MainWindow(screen_size)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()
