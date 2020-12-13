build:
	#rm ./mqtt_fake.tar
	docker build -t mqtt_fake:2.0.0 .
	docker save -o mqtt_fake.tar mqtt_fake:2.0.0
	scp ./mqtt_fake.tar teletraan@192.168.1.5:/home/teletraan/workspace/test
	# make remote-load-docker

remote-load-docker:
	ssh -t teletraan@192.168.1.5 "docker rm -f $(docker ps -a|grep mqtt_fake|awk '{print $1}'); \
	docker rmi -f $(docker images|grep mqtt_fake|awk '{print $3}'); \
	cd /home/teletraan/workspace/test; \
	docker load -i mqtt_fake.tar; \
	docker run -p 50002:5000 --name mqtt_fake -d mqtt_fake:2.0.0; "
