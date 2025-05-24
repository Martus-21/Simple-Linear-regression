Build and test:

powershell
# 1. Build the image
docker build -t ml-api .

# 2. Remove old container
docker rm -f ml-container

# 3. Run new container
docker run -p 5000:5000 --name ml-container -d ml-api

# 4. Check if its working
curl http://localhost:5000/

# 5. RUN pytest tests
docker run -it ml-api pytest tests/