# Kasparro AI Agentic Content Generation System

This system uses a multi-agent architecture to generate marketing content for products.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd kasparro-ai-agentic-content-generation-system-bhumika-singh
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

Run the application using the following command:

```bash
python main.py --input data/input_product.json --output output
```

### Arguments

-   `--input` or `-i`: Path to the input JSON file (default: `data/input_product.json`).
-   `--output` or `-o`: Directory to save the generated output files (default: `output`).

## Project Structure

-   `src/core`: Core logic and orchestration.
-   `src/agents`: Individual agents for specific tasks.
-   `data`: Input data files.
-   `output`: Generated output files.
 will be in the `output/` directory:
- `faq_page.json`
- `product_page.json`
- `comparison_page.json`

## Documentation

See `docs/projectdocumentation.md` for detailed system design and architecture.
