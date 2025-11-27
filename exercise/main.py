# Put the code for your API here.
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


def go() -> None:
    pass


if __name__ == "__main__":
    logger.debug("Starting the application...")
    go()
