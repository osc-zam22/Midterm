# Use OpenJDK 11 as the base image
FROM openjdk:11-jdk

# Create a working directory inside the container
WORKDIR /app

# Copy source files and libraries into the container
COPY MathUtils.java .
COPY lib/ ./lib

# Compile the Java file inside the image
RUN mkdir -p out && javac -cp "lib/*" -d out MathUtils.java

# Run the main class
CMD ["java", "-cp", "lib/*:out", "MathUtils"]
