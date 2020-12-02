cd ..
tar -zcvf fund_server.tar.gz fund_server
scp -i ~/.ssh/aliyun_ubuntu.pem fund_server.tar.gz ubuntu@139.196.212.119:~/workspace/project
ssh -i ~/.ssh/aliyun_ubuntu.pem ubuntu@139.196.212.119 << EOF

cd /home/ubuntu/workspace/project
tar -zxvf fund_server.tar.gz
mv fund_server/docker-compose.yml .
docker-compose up -d

EOF