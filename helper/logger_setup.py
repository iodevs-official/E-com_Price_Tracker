
import logging
import asyncio
from helper.report_error import report_error

class ErrorReportingHandler(logging.Handler):
    def __init__(self, app):
        super().__init__(level=logging.ERROR)
        self.app = app

    def emit(self, record):
        if record.levelno == logging.ERROR:
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(report_error(self.app, record.getMessage()))
            except RuntimeError:
                asyncio.run(report_error(self.app, record.getMessage()))

def init_logger(app, name=__name__, level=logging.INFO):
    # Set up global logging format and level
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(funcName)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Suppress info logs from pyrogram
    logging.getLogger("pyrogram").setLevel(logging.ERROR)

    # Attach error reporting handler to the root logger, so all errors are caught
    root_logger = logging.getLogger()
    root_logger.addHandler(ErrorReportingHandler(app))

    # Return your app's logger if you want
    return logging.getLogger(name)




#-----------------------
#USAGE
#import logging

#logger = logging.getLogger(__name__)

#logger.error("eror msg", exc_info=True)
