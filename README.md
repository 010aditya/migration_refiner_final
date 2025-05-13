# 🧠 Migration Refiner 

A powerful agent-driven pipeline to refine and complete legacy Java migrations (e.g., EJB, JSP, Struts, iBatis) into **Spring Boot** applications — and make them compile, build, and test successfully using GPT-4o.

---

## 🚀 What It Does

| ✅ Feature                             | Description |
|---------------------------------------|-------------|
| Mapping Verification                  | Validates `sourcePath → targetPath` mapping with semantic similarity |
| Legacy Context Stitching              | Embeds all legacy code using FAISS + LangChain |
| Migrated Code Stitching (1:N)         | Combines multiple partial migrated files |
| GPT-4o Code Refinement                | Completes classes using stitched context and migrated code |
| Package Structure Normalization       | Ensures correct `package` declarations & folder paths |
| Unit Test Generation                  | Creates JUnit 5 test files using GPT |
| Build Validation                      | Validates Gradle/Maven build output |
| Auto-Healing Retry Agent              | Uses build errors to re-prompt GPT for fixing code |
| No Database Needed                    | File-based state management only |

---

## 📂 Folder Structure

```
migration-refiner/
├── legacy_code/                 # Legacy Java input
├── migrated_code/               # Migrated partial output
├── framework_code/              # Base Spring Boot support code
├── embeddings/                  # FAISS vector index
├── review_required/             # Files that still fail after retry
├── agents/                      # All intelligent agents
├── main.py                      # Entry point
├── mapping.json                 # Input mappings
├── mapping.verified.json        # Validated mappings
├── mapping.grouped.json         # Grouped 1:N mappings
├── build.log                    # Build output log
├── Dockerfile                   # Containerized environment
├── init.sh                      # Setup script
├── requirements.txt             # Python dependencies
```

---

## 🧠 Agents Overview

| Agent                          | Role |
|-------------------------------|------|
| `MetadataAgent`               | Extracts DB/build/cache details from legacy |
| `MappingVerifierAgent`        | Filters out invalid mappings using cosine similarity |
| `MappingCollapserAgent`       | Groups repeated mappings into 1:N structures |
| `EmbeddingIndexerAgent`       | Indexes all `.java` files semantically |
| `ContextStitcherAgent`        | Retrieves relevant legacy context |
| `MigratedFileStitcherAgent`   | Merges multiple target migrated files |
| `FixAndCompleteAgent`         | Uses GPT-4o to rewrite a complete class |
| `TestGeneratorAgent`          | Auto-generates JUnit 5 tests |
| `PackageStructureNormalizerAgent` | Adds correct `package` declarations and file structure |
| `BuildValidatorAgent`         | Validates Gradle/Maven build |
| `RetryAgent`                  | Fixes broken files using build logs |

---

## 🛠 Requirements

- Python 3.10+
- Java 21
- Gradle 8.6+ / Maven 3.9+
- OpenAI API Key
- (Optional) Docker

Install dependencies:

```bash
bash init.sh
python main.py
```

Or run using Docker:

```bash
docker build -t migration-refiner .
docker run -v $(pwd):/app migration-refiner
```

---

## 🔥 How It Works

1. Load and verify `mapping.json`
2. Group repeated sourcePath entries into `targetPaths`
3. Index all legacy/framework code
4. For each source:
   - Stitch legacy context
   - Stitch migrated files
   - Generate final class via GPT-4o
   - Generate test case
   - Normalize package
5. Validate build
6. Retry any failures using build logs

---

## ✅ Output

- All Java files placed in correct folders
- All `package` declarations fixed
- `build.gradle` or `pom.xml` used to verify build
- Broken files retried once via GPT auto-heal
- Any remaining issues go to `review_required/`

---

## 📦 No Database Required

- All state handled via JSON, FAISS index, logs, and filesystem

---

## 📌 Want to Extend?

- Add support for merging by service/domain layer
- Integrate GitHub repo push
- Add web-based review UI
- Track migration history using SQLite or Mongo (optional)

---

## 🏁 Conclusion

This is your **silver-bullet migration refinement tool** — automated, intelligent, and build-ready for large-scale legacy modernization.
