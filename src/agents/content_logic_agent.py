from typing import Dict, Any, List
from .base_agent import BaseAgent

class ContentLogicAgent(BaseAgent):
    """
    Generates specific content blocks and fictional competitor data.
    """
    def run(self, product_data: Dict[str, Any], competitor: Dict[str, Any]) -> Dict[str, Any]:
        
        # 1. Generate Description Block
        description = self._generate_description(product_data)
        
        # 2. Generate Benefits List (Formatted)
        benefits = self._generate_benefits(product_data)
        
        # 3. Generate Comparison Rows
        comparison_rows = self._generate_comparison_rows(product_data, competitor)
        
        # 4. Generate Comparison Verdict
        verdict = self._generate_verdict(product_data, competitor)
        
        return {
            "description": description,
            "benefits": benefits,
            "comparison_rows": comparison_rows,
            "comparison_verdict": verdict
        }

    def _generate_description(self, product_data: Dict[str, Any]) -> str:
        # Template-based description
        return (f"Experience the power of {product_data['name']}. "
                f"Formulated with {product_data['key_ingredients']}, it delivers results like {product_data['benefits']}. "
                f"Perfect for {product_data.get('skin_type', 'all skin types')}, it is the ultimate addition to your routine.")

    def _generate_benefits(self, product_data: Dict[str, Any]) -> List[str]:
        # Just splitting the string for simplicity
        raw = product_data.get('benefits', '')
        return [b.strip() for b in raw.split(',')]

    def _generate_comparison_rows(self, product: Dict[str, Any], competitor: Dict[str, Any]) -> List[List[str]]:
        # Logic to create comparison rows
        return [
            ["Price", product['price'], competitor.get('price', 'N/A')],
            ["Key Ingredients", product['key_ingredients'], competitor.get('ingredients', 'N/A')],
            ["Benefits", product['benefits'], competitor.get('benefits', 'N/A')]
        ]

    def _generate_verdict(self, product: Dict[str, Any], competitor: Dict[str, Any]) -> str:
        return (
            f"{product['name']} highlights ingredients like {product['key_ingredients']}, "
            f"while {competitor['name']} focuses on {competitor['ingredients']}."
        )
