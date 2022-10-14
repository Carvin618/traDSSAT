FROM carvin/dssat

MAINTAINER Carvin Li

RUN echo head -1 /proc/self/cgroup|cut -d/ -f3

ENV PYTHONPATH=/opt/project/src

CMD /bin/bash

