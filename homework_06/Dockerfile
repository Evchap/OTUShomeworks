FROM tiangolo/uwsgi-nginx-flask

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./
# COPY entrypoint.sh /var/entrypoint.sh
# RUN chmod +x /var/entrypoint.sh
#
# ENTRYPOINT ["/var/entrypoint.sh"]









# ================================================================
# docker ps                     Для просмотра запущенных контейнеров
# docker start 2c88170e5391
# docker restart 2c88170e5391
# docker-compose up -d --no-deps --build После смены настроек в файле docker-compose.yml (например, проброс порта)
# docker rm hello/root_my-test_1
# docker images



