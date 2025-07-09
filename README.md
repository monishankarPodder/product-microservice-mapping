# Product Microservice with AI Test Mapping

## How to Run

1. Build and run the Spring Boot application:
```bash
mvn spring-boot:run
```

2. Commit changes in the `src/` folder and push to GitHub.

3. GitHub Action (`.github/workflows/test-mapping.yml`) will:
   - Detect changed files.
   - Run Python script to map changed files to test cases using `testcases/testcases.json`.
   - Print suggested test cases in the Actions log.
