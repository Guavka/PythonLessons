
import utils.console as console
import utils.logger as logger

is_console = True


def print_data(msg: str):
    if is_console:
        console.print_data(msg)
    else:
        logger.print_data(msg)


def get_data(msg: str):
    if is_console:
        return console.get_data(msg)
    else:
        return logger.get_data(msg)
