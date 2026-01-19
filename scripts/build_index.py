"""
CLI script to build embeddings index from processed data
"""

from pathlib import Path

from src.embeddings.embedder import Embedder
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("Building embeddings index...")

    processed_dir = Path("data/processed")
    embeddings_dir = Path("data/embeddings")
    embeddings_dir.mkdir(parents=True, exist_ok=True)

    if not processed_dir.exists():
        logger.error("Processed data directory does not exist.")
        return

    # Placeholder: actual loading logic will evolve with ingestion pipeline
    logger.info("Initializing embedder")
    embedder = Embedder()

    logger.info("Embedding processed documents (placeholder)")
    # TODO: Load cleaned text files and generate embeddings

    logger.info(f"Embeddings will be stored in: {embeddings_dir}")
    logger.info("Build index step completed (scaffold)")


if __name__ == "__main__":
    main()
