#### Build the Docker image
```bash
docker build -t fbapi:latest .
```

#### Run the container and map port 8080 from host to container
```bash
docker run -d -p 8080:8080 fbapi:latest
```

#### Run the container with a proxy as an environment variable
```bash
docker run -d -p 8080:8080 -e PROXY="<proxy_url>" fbapi:latest
```

#### Available endpoints
```python
/facebooks/ads?query=shoes
```
```python
/tiktok/ads?query=gadgets
```
