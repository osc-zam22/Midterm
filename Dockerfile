# Use OpenJDK 11 as the base image
FROM openjdk:11-jdk

# Create a working directory inside the container
WORKDIR /app

# Copy source files and libraries into the container
COPY MathUtils.java .
COPY lib/ ./lib

# Install curl and download kubectl
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://dl.k8s.io/release/stable.txt -o /tmp/kubectl_version && \
    KUBECTL_VERSION=$(cat /tmp/kubectl_version) && \
    curl -LO https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl /tmp/kubectl_version

# Compile the Java file inside the image
RUN mkdir -p out && javac -cp "lib/*" -d out MathUtils.java

# Run the main class
CMD ["java", "-cp", "lib/:out", "MathUtils"]
