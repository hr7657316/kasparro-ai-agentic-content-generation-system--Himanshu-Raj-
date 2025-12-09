from typing import Dict, Any
from .base_agent import BaseAgent

class CompetitorGenerationAgent(BaseAgent):
    """
    Generates a fictional competitor product for comparison.
    """
    def run(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        # Rule-based competitor generation
        # We create a competitor that is slightly cheaper but has "inferior" ingredients
        return {
            "name": f"Generic {product_data['name'].split()[-1]} B",
            "ingredients": "Water, Glycerin, Alcohol",
            "benefits": "Basic hydration",
            "price": "₹499"
        }
