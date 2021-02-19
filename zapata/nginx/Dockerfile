FROM nginx:stable

COPY nginx.conf /etc/nginx/conf.d/nginx.conf

RUN curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "/options-ssl-nginx.conf"
RUN curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "/ssl-dhparams.pem"

EXPOSE 5000 8443
