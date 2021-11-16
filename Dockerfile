FROM python:3.9.0

WORKDIR /home/

RUN echo 'AmuMal3'

RUN git clone https://github.com/timgotango/gis_4ban_timproject22.git

WORKDIR /home/gis_4ban_timproject22/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=timproject_2.settings.deploy && python manage.py migrate --settings=timproject_2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=timproject_2.settings.deploy timproject_2.wsgi --bind 0.0.0.0:8000"]