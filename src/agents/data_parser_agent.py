from typing import Dict, Any
import logging
from .base_agent import BaseAgent
from ..core.models import Product

logger = logging.getLogger(__name__)

class DataParserAgent(BaseAgent):
    """
    Parses and validates the input product data.
    """
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parses input dictionary into a Product object and returns its dictionary representation.

        Args:
            input_data (Dict[str, Any]): Raw input data.

        Returns:
            Dict[str, Any]: Processed product data.

        Raises:
            ValueError: If required fields are missing.
        """
        # Normalize keys to snake_case for internal use
        normalized = {}
        for k, v in input_data.items():
            key = k.lower().replace(" ", "_")
            normalized[key] = v
        
        # Validate required fields
        required = ["product_name", "price", "benefits"]
        for req in required:
            if req not in normalized:
                logger.error(f"Missing required field: {req}")
                raise ValueError(f"Missing required field: {req}")
                
        # Create Product object
        product = Product(
            name=normalized['product_name'],
            concentration=normalized.get('concentration', ''),
            skin_type=normalized.get('skin_type', ''),
            key_ingredients=normalized.get('key_ingredients', ''),
            benefits=normalized.get('benefits', ''),
            how_to_use=normalized.get('how_to_use', ''),
            side_effects=normalized.get('side_effects', ''),
            price=normalized.get('price', '')
        )
        
        return product.to_dict()
