FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -U pip
RUN pip install pyopenssl
RUN pip install pycrypto
#RUN pip install --force-reinstall oauth2client==1.5.2
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]