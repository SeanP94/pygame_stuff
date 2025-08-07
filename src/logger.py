import logging
import os
from pathlib import Path


############## Import this object ############
logger_instance = logging.getLogger(__name__)#
##############################################

# Change this between DEBUG, ERROR, etc if you want to hide higher level logs.
LEVEL = logging.DEBUG





log_file = Path(os.path.abspath(__file__)).parent.parent / 'non_statics' / 'program_log.txt'


# Configure the logging data.
logging.basicConfig(
    filename=log_file,
    encoding='utf-8',
    filemode='w',
    level=LEVEL,
    format='%(asctime)s %(message)s',
    datefmt='%Y/%m/%d %I:%M:%S %p'
)
