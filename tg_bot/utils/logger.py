import logging

from loguru import logger

logger.add("./logs/info.log", level="INFO", colorize=False, format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")
logger.add("./logs/error.log", level="ERROR", colorize=False, format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logger(level="DEBUG", ignored=""):
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.getLevelName(level))

    for ignore in ignored:
        logger.disable(ignore)
