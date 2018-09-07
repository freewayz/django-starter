echo '### Building Docker Image ###'
python3 setup.py sdist
mv dist/*.tar.gz docker/
docker build -t {{ project_name | lower }} docker/
echo 'Visit http://localhost:8080'
exec docker-compose up
