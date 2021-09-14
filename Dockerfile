FROM python:3.9.0

WORKDIR /home/

RUN echo 'Amu Mal'

RUN git clone https://github.com/timgotango/gis_4ban_timproject22.git

WORKDIR /home/gis_4ban_timproject22/

RUN echo "SECRET_KEY=django-insecure-v@9wisezc3$ikj@*c3xs(vmm9)a(^isu=sornz$sj&c81#paqx" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "timproject_2.wsgi", "--bind", "0.0.0.0:8000"]