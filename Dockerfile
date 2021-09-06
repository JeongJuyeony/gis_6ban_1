FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/JeongJuyeony/gis_6ban_1.git

WORKDIR /home/gis_6ban_1/

RUN echo "SECRET_KEY=django-insecure-1+5%!y8p@0^s6)d!uz)mi@a_w(ys4++*^m9fv3d(tsl8=b^7+e" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]