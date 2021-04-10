import os
import time
import requests
import shutil
import glob
from veriff.helper.logger_util import get_logger

logger = get_logger(__name__)


def download_data(file_url):
    start_time = time.time()
    logger.info("data-set download start - %r", file_url)

    file_name = os.path.basename(file_url)
    r = requests.get(file_url, stream=True)

    # Check if the data was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded data file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception("data-set download failed {}, cause {}".format(file_url, r.reason))

    logger.info("data-set download completed. took %r seconds", (time.time() - start_time))
    return file_name


def unzip(zip_file_path, output_dir=None):
    start_time = time.time()
    logger.info("data-set unzip start")

    if output_dir is not None:
        shutil.rmtree(output_dir, ignore_errors=True)
        os.mkdir(output_dir)

    shutil.unpack_archive(zip_file_path, output_dir)
    logger.info("data-set unzip completed. took %r seconds", (time.time() - start_time))


def download_and_unzip(file_url, output_dir=None):
    zip_file_path = download_data(file_url)
    unzip(zip_file_path, output_dir)
    os.remove(zip_file_path)


def list_files(dir_path):
    return glob.glob(dir_path)