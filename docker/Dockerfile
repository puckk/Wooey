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
                       apktool



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
RUN gem install wpscan zsteg;
RUN cd / ; git clone https://github.com/sullo/nikto.git; ln -s /nikto/program/nikto.pl /usr/bin/nikto;
RUN cd /; git clone https://github.com/hellman/xortool.git; cd xortool; python setup.py install;
RUN cd /; mkdir /wordlists; cd /wordlists; wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt


RUN cd /; git clone https://github.com/aboul3la/Sublist3r.git; cd Sublist3r; pip install -r requirements.txt; python setup.py install
RUN cd /; wget https://github.com/OJ/gobuster/releases/download/v3.0.1/gobuster-linux-amd64.7z; 7z e gobuster-linux-amd64.7z; chmod +x gobuster; ln -s /gobuster /usr/bin/gobuster
RUN cd /; git clone https://github.com/commixproject/commix.git commix; cd commix; python2.7 commix.py --install
RUN cd /; git clone https://github.com/magnumripper/JohnTheRipper.git; cd JohnTheRipper/src; ./configure; make -s clean && make -sj4; echo -e '#!/bin/bash\ncd /JohnTheRipper/run; ./john "$@"' > /usr/bin/john; chmod +x /usr/bin/john

COPY scripts_uploads/ /${WOOEY_PROJECT}/scripts_uploads
CMD ["sh", "-c", "make -C ${BUILD_DIR} test"]
