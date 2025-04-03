# Use OpenJDK 11 as the base image
FROM openjdk:11-jdk

# Create a working directory inside the container
WORKDIR /app

# Copy compiled Java class files and libraries into the container
COPY out/ ./out/
COPY lib/ ./lib/

# Run the main class (update MathUtils to your actual class with a main() method)
CMD ["java", "-cp", "lib/*:out", "MathUtils"]
