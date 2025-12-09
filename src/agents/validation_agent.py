from typing import Dict, Any
import logging
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

class ValidationAgent(BaseAgent):
    """
    Validates the structure and content of the generated pages.
    """
    def run(self, pages: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates the generated pages against required schemas.

        Args:
            pages (Dict[str, Any]): The generated pages to validate.

        Returns:
            Dict[str, Any]: The validated pages.

        Raises:
            ValueError: If any validation check fails.
        """
        logger.info("Agent: ValidationAgent working...")
        
        # Validate FAQ Page
        faq = pages.get("faq_page")
        if not faq:
            logger.error("Validation failed: Missing FAQ page")
            raise ValueError("Missing FAQ page")
        if "sections" not in faq:
            logger.error("Validation failed: FAQ page missing 'sections'")
            raise ValueError("FAQ page missing 'sections'")
        if len(faq["sections"][0]["q_and_a"]) < 5:
            logger.error("Validation failed: FAQ page must have at least 5 questions")
            raise ValueError("FAQ page must have at least 5 questions")

        # Validate Product Page
        product_page = pages.get("product_page")
        if not product_page:
            logger.error("Validation failed: Missing Product page")
            raise ValueError("Missing Product page")
        for key in ["title", "price", "description", "benefits_list"]:
            if key not in product_page:
                logger.error(f"Validation failed: Product page missing required key: {key}")
                raise ValueError(f"Product page missing required key: {key}")

        # Validate Comparison Page
        comparison_page = pages.get("comparison_page")
        if not comparison_page:
            logger.error("Validation failed: Missing Comparison page")
            raise ValueError("Missing Comparison page")
        for key in ["title", "comparison_table", "verdict"]:
            if key not in comparison_page:
                logger.error(f"Validation failed: Comparison page missing required key: {key}")
                raise ValueError(f"Comparison page missing required key: {key}")

        logger.info("Validation successful.")
        return pages
