# PDF to Structured Markdown Converter Project

**Project Goal:** Convert PDF documents to structured Markdown (.md) files, preserving headings, subheadings, bullet points, and removing unnecessary content.

**Phase 1: Conversion System**

* **Pipeline:** Input handling, text extraction, preprocessing/cleaning, structuring/formatting, output writing.
* **Requirements:** Accepts PDF files (file upload or path), extracts clean text preserving hierarchy, removes page numbers, headers/footers, metadata, and repeated sections.  Output is formatted Markdown using appropriate syntax (# for headings, -/* for bullet points, optional bold). System should be extensible.
* **Deliverables:** Python codebase, sample PDF/Markdown, system architecture diagram.

**Phase 2: Flask API Integration**

* **API:** Flask-based REST API with POST /convert (PDF upload, returns Markdown) and GET /health endpoints.  Includes error handling with JSON responses and HTTP status codes.
* **Frontend:** Minimal HTML/CSS frontend for file upload and Markdown display (optional JavaScript).
* **Testing:** Postman for API testing, test cases saved in a shared collection.  Security measures include file validation and size limits.
* **Deliverables:** Flask API, HTML/CSS frontend, Postman test collection, API documentation.
