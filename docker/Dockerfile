FROM python:3.7

ARG BUILD_DIR=/wooey_build
COPY setup.py requirements.txt MANIFEST.in Makefile README.md ${BUILD_DIR}/
COPY scripts ${BUILD_DIR}/scripts
COPY wooey ${BUILD_DIR}/wooey
COPY tests ${BUILD_DIR}/tests


RUN apt-get update; apt-get install -y apt-utils \
                       foremost \
                       binwalk \
                       exiftool \
                       outguess \
                       pngtools \
                       pngcheck \
                       dirb \
                       libmpfr-dev \
                       libmpc-dev \
                       nmap \
                       sqlmap \
                       steghide \
                       ruby \
                       gem \
                       ruby-dev \
                       apktool \
                       john



WORKDIR ${BUILD_DIR}

RUN pip install -r requirements.txt; pip install -e . ; chmod -R a+rwx ${BUILD_DIR}

WORKDIR /
ARG WOOEY_PROJECT=docker_wooey

RUN wooify -p ${WOOEY_PROJECT}

WORKDIR ${WOOEY_PROJECT}

COPY docker/scripts/run-server run-server


RUN mkdir ${WOOEY_PROJECT}/user_uploads && \
    chmod -R a+rwx /${WOOEY_PROJECT}

# Install zsteg, nikto, xortool and download wordlist
RUN gem install wpscan zsteg; \
    cd / ; git clone https://github.com/sullo/nikto.git; ln -s /nikto/program/nikto.pl /usr/bin/nikto; \
    cd /; git clone https://github.com/hellman/xortool.git; cd xortool; python setup.py install; \
    cd /; mkdir /wordlists; cd /wordlists; wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt;

#crypto xortool john rsaCTFTool? rsolver hashcat hydra john2todo

#forensics aircrack volatility?

#networking masscan zmap?

#reversing uncompyle

#stego convert pngtools steganabara
COPY scripts_uploads/ /${WOOEY_PROJECT}/scripts_uploads
CMD ["sh", "-c", "make -C ${BUILD_DIR} test"]
