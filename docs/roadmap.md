# Project Roadmap

This roadmap defines a realistic, phased plan for building the AI Retrieval System.  
It reflects an intentionally constrained scope, prioritizing a working, trustworthy retrieval system over feature breadth or speculative capabilities.

The roadmap assumes development by a single developer and focuses on delivering value early through an end-to-end, retrieval-first implementation.

---

## Phase 1: Core Retrieval MVP (Non-Negotiable)

**Goal:**  
Build a complete, end-to-end retrieval system that searches only user-ingested documents.

This phase defines the minimum system that must exist for the project to be considered successful.

### Scope
- Local document ingestion (PDF, TXT, Markdown)
- Text cleaning and normalization
- Chunk-based document processing
- Embedding generation
- Local vector index creation
- Query embedding and similarity-based retrieval
- CLI-based query interface
- Source-backed retrieval results (no answer generation)
- Source-aware retrieval output with basic citation metadata (document ID, source, location)

### Explicit Non-Goals
- No live web search
- No cloud infrastructure
- No language-model-based answer generation
- No scalability optimizations

### Deliverables
- A reproducible indexing pipeline
- A query pipeline that returns relevant document chunks
- Clear separation between indexing and querying
- Working retrieval on a small, curated dataset

### Success Criteria
- Documents can be indexed end-to-end without manual intervention
- Queries return relevant chunks from the indexed data
- The system behaves deterministically and offline
- Every retrieved chunk can be traced back to its original source

---

## Phase 2: Retrieval Quality and Robustness

**Goal:**  
Improve result quality and system reliability without increasing conceptual complexity.

### Scope
- Metadata extraction and storage
- Metadata-based filtering
- Improved chunking strategies
- Basic ranking and score normalization
- Graceful handling of empty or low-confidence results
- Structured logging and clearer error messages

### Deliverables
- More consistent and explainable retrieval behavior
- Better observability during indexing and querying

### Success Criteria
- Noticeable improvement in retrieval relevance
- Easier debugging and tuning of retrieval behavior

---

## Phase 3: Optional Retrieval-Augmented Generation (RAG)

**Goal:**  
Add optional answer generation while keeping retrieval as the primary and required capability.

### Scope
- Language model integration for answer synthesis
- Strict prompt constraints using retrieved chunks only
- Generated answers include explicit citations derived from retrieved source
- Configuration toggle to enable or disable generationcv 

### Constraints
- Retrieval must always precede generation
- The system must remain usable without generation enabled

### Deliverables
- RAG pipeline layered cleanly on top of retrieval
- Clear separation between retrieval and generation logic

### Success Criteria
- Generated answers are grounded in retrieved sources
- Retrieval remains the core system capability

---

## Phase 4: Developer Interfaces and Usability

**Goal:**  
Make the system easier to use, extend, and integrate without changing core behavior.

### Scope
- Improved CLI ergonomics
- Python API for programmatic use
- Configuration via files or environment variables
- Clear usage documentation

### Deliverables
- Stable interfaces for indexing and querying
- Improved developer experience

### Success Criteria
- System can be used as a library or tool without code modification
- Interfaces remain stable across iterations

---

## Explicitly Out of Scope (for This Project)

The following items are intentionally excluded to preserve feasibility and focus:

- Live internet search at query time
- Autonomous or self-updating knowledge bases
- Multi-user or multi-tenant systems
- Distributed or cloud-native deployment
- Internet-scale indexing
- Model training or fine-tuning
- General-purpose chatbot behavior

These may be explored separately but are not goals of this project.

---

## Guiding Principles

- Always maintain a working end-to-end system
- Prefer correctness and determinism over feature count
- Keep retrieval independent from generation
- Defer complexity until it is clearly justified
- Treat documentation as part of the system

---

## Summary

This roadmap reflects a deliberate commitment to **feasibility, clarity, and correctness**.  
By focusing on a retrieval-first, user-controlled knowledge base and layering additional capabilities only when justified, the AI Retrieval System remains achievable for a solo developer while aligning with real-world retrieval system practices.
