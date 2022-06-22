import logging
import subprocess

from PySide6.QtWidgets import QMessageBox


from exploredesktop.modules.utils import display_msg  # isort:skip


logger = logging.getLogger("explorepy.exploredesktop.main")


def check_updates():
    process = subprocess.Popen(
        "C:\\Users\\ProSomno\\IfwExamples\\online\\maintenancetool --checkupdates",
        shell=True, stdout=subprocess.PIPE)
    subprocess_return = process.stdout.read().decode("utf-8")
    logger.debug("Check updates output: %s" % subprocess_return)
    if 'Warning' in subprocess_return:
        # print('No updates available')
        logger.debug('No updates available')
        return None
    logger.debug('Updates available')

    new_version = get_version(subprocess_return)
    return new_version


def get_version(string):
    string = string.split('version=')[1]
    string = string.split('size')[0]
    string = string.split('/')[0]
    string = string.split('name')[0]
    string = string.split('id')[0]
    string = string.replace('"', '')
    string = string.replace(' ', '')
    return string


def update_version():
    new_version = check_updates()
    if new_version is None:
        return False

    msg = f"New version available: {new_version}.\t\t\n\nUpdate now?"
    response = display_msg(
        msg,
        title="New version found",
        popup_type="question")

    if response == QMessageBox.StandardButton.Yes:
        subprocess.Popen("C:\\Users\\ProSomno\\IfwExamples\\online\\maintenancetool --updater", shell=False)
        logger.debug('Updater launched')
        return True
    return False
