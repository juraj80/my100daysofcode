import pyperclip
import logbook

app_log = logbook.Logger('Clipboard')

def paste_from_clipboard():
    text = pyperclip.paste()
    app_log.trace(text)
    return None


def init_logging(filename: str = None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application() # default date format
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging of clipboard initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)

if __name__ == '__main__':
    init_logging('clipboard_file.log')
    paste_from_clipboard()
