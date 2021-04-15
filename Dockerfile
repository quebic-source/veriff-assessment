FROM rayproject/ray:nightly

USER root

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    git \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b v19.9 --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

COPY veriff veriff
COPY requirements/host.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "-m", "veriff" ]
