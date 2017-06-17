# multistage-build

compile source file using an image with JDK, image is about 600MB
puth the class file into a JRE image of about 80MB

```bash
docker build -t java-helloworld .
```

run container and remove it

```bash
docker run -it --rm java-helloworld
```
