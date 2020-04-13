FROM python:3

WORKDIR /docker

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .

CMD [ "python", "./copebot_python_edition.py"]