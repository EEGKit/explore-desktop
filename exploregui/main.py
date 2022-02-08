# This Python file uses the following encoding: utf-8
import logging
import sys

import explorepy
from PySide6.QtWidgets import QApplication


import exploregui  # isort:skip
from exploregui import MainWindow  # isort:skip


logger = logging.getLogger("explorepy.exploregui.main")
logger.debug("Starting ExploreGUI (version: %s) with Explorepy (version: %s)",
             exploregui.__version__, explorepy.__version__)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    print(
        "\nPlease do not close this command prompt window."
        "\nIf any error happens, you can use this window to send the report to Mentalab.\n")
    main()
