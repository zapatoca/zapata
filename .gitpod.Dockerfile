FROM gitpod/workspace-full

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
	&& unzip awscliv2.zip \
	&& sudo ./aws/install \
	&& rm -f awscliv2.zip

RUN sudo apt-get remove -y docker-compose \
	&& sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-Linux-x86_64" -o /usr/local/bin/docker-compose \
	&& sudo chmod +x /usr/local/bin/docker-compose \
	&& sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
