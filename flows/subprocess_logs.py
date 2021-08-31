from prefect import task, Flow, Parameter
from prefect.storage import Git
import sys
from prefect.utilities.logging import get_logger
from pathlib import Path

logger = get_logger()

file_path = Path(__file__).resolve().parent

@task(log_stdout=True)
def mp_external():
    logger.info(file_path)
    sys.path.append(file_path.as_posix())
    logger.info(sys.path)

    import sb
    out = sb.run_process_pool()
    sys.stdout.flush()
    logger.info(out)


with Flow("Subprocess Logs") as flow:
    mp_external()
