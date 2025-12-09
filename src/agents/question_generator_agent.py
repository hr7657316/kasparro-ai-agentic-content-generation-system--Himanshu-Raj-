from typing import Dict, Any, List
from .base_agent import BaseAgent

class QuestionGeneratorAgent(BaseAgent):
    """
    Generates categorized user questions based on product data.
    """
    def run(self, product_data: Dict[str, Any]) -> List[Dict[str, str]]:
        name = product_data.get('name', 'the product')
        benefits = product_data.get('benefits', '')
        usage = product_data.get('how_to_use', '')
        ingredients = product_data.get('key_ingredients', '')
        
        questions = []
        
        # Usage Category
        questions.append({
            "category": "Usage",
            "question": f"How often should I use {name}?",
            "answer": f"For best results, follow the usage instructions: {usage}."
        })
        questions.append({
            "category": "Usage",
            "question": "Can I use this in my morning routine?",
            "answer": "Yes, it is suitable for morning use. " + usage
        })
        questions.append({
            "category": "Usage",
            "question": "Is it complicated to apply?",
            "answer": "No, simply: " + usage
        })

        # Ingredients Category
        questions.append({
            "category": "Ingredients",
            "question": "What are the key ingredients?",
            "answer": f"The key ingredients are {ingredients}."
        })
        questions.append({
            "category": "Ingredients",
            "question": "Does it contain Vitamin C?",
            "answer": "Yes, check the ingredient list: " + ingredients
        })
        questions.append({
            "category": "Ingredients",
            "question": "Are the ingredients safe?",
            "answer": "It is formulated with " + ingredients
        })

        # Benefits Category
        questions.append({
            "category": "Benefits",
            "question": "What will this do for my skin?",
            "answer": f"It helps with: {benefits}."
        })
        questions.append({
            "category": "Benefits",
            "question": "Will it brighten my skin?",
            "answer": f"Yes, one of the main benefits is: {benefits}."
        })
        questions.append({
            "category": "Benefits",
            "question": "Why should I choose this serum?",
            "answer": f"Because it offers: {benefits}."
        })

        # Safety Category
        questions.append({
            "category": "Safety",
            "question": "Is this safe for sensitive skin?",
            "answer": f"Please check the side effects: {product_data.get('side_effects', 'None')}."
        })
        questions.append({
            "category": "Safety",
            "question": "Are there side effects?",
            "answer": f"You might experience: {product_data.get('side_effects', 'None')}."
        })
        questions.append({
            "category": "Safety",
            "question": "Can I use it every day?",
            "answer": "Refer to usage instructions: " + usage
        })

        # Purchase/General
        questions.append({
            "category": "Purchase",
            "question": "What is the price?",
            "answer": f"It is priced at {product_data.get('price')}."
        })
        questions.append({
            "category": "General",
            "question": "Is this a good value?",
            "answer": f"At {product_data.get('price')}, it offers great benefits like {benefits}."
        })
        questions.append({
            "category": "General",
            "question": "Who is this for?",
            "answer": f"It is designed for skin types: {product_data.get('skin_type')}."
        })

        return questions
