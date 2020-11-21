FROM python:3.7

RUN mkdir /workspace
COPY ./* /workspace
WORKDIR /workspace

RUN mkdir ~/.pip
RUN chmod 666 ~/.pip
RUN touch ~/.pip/pip.conf
RUN chmod 666 ~/.pip/pip.conf
RUN echo "[global]" >> ~/.pip/pip.conf
RUN echo "timeout = 6000" >> ~/.pip/pip.conf
RUN echo "index-url = http://pypi.douban.com/simple/" >> ~/.pip/pip.conf
RUN echo "[install]" >> ~/.pip/pip.conf
RUN echo "use-mirrors = true" >> ~/.pip/pip.conf
RUN echo "mirrors = http://pypi.douban.com/simple/" >> ~/.pip/pip.conf
RUN echo "trusted-host = pypi.douban.com" >> ~/.pip/pip.conf

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi
# RUN pip3 install supervisor
# RUN echo_supervisord_conf > supervisord.conf
# COPY ./supervisor_config /code

EXPOSE 8000