FROM openjdk:8-jdk as compiling
LABEL maintainer "Marcel Akkerman <ikbenMarcelAkkerman@hotmail.com>"
WORKDIR /tmp/java
COPY HelloWorld.java .
RUN javac HelloWorld.java

FROM openjdk:8-jre-alpine
WORKDIR /usr/src/myapp
COPY --from=compiling /tmp/java/HelloWorld.class .
CMD ["java", "HelloWorld"]



