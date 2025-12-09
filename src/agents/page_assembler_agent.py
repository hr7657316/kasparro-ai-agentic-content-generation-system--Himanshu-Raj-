from typing import Dict, Any, List
from .base_agent import BaseAgent
from ..core.templates import TemplateEngine, FAQ_TEMPLATE, PRODUCT_PAGE_TEMPLATE, COMPARISON_PAGE_TEMPLATE

class PageAssemblerAgent(BaseAgent):
    """
    Assembles final pages using templates and data.
    """
    def __init__(self):
        self.engine = TemplateEngine()

    def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Expects data to contain:
        - product: parsed product data
        - questions: list of Q&A
        - content_blocks: generated content blocks
        - competitor: competitor data
        """
        
        # Assemble FAQ Page
        faq_context = {
            "product": data['product'],
            "questions": data['questions']
        }
        faq_page = self.engine.render(FAQ_TEMPLATE, faq_context)
        
        # Assemble Product Page
        product_context = {
            "product": data['product'],
            "content_blocks": data['content_blocks']
        }
        product_page = self.engine.render(PRODUCT_PAGE_TEMPLATE, product_context)
        
        # Assemble Comparison Page
        comparison_context = {
            "product": data['product'],
            "competitor": data['competitor'],
            "content_blocks": data['content_blocks']
        }
        comparison_page = self.engine.render(COMPARISON_PAGE_TEMPLATE, comparison_context)
        
        return {
            "faq_page": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page
        }
