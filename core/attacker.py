"""Attack execution logic for RedTeamForge AI."""

import json


def execute_attack(client, model_name, attack_prompt):
    """Send attack prompt to target model and capture response."""
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=attack_prompt,
            config={"temperature": 0.7},
        )
        return {
            "success": True,
            "response_text": response.text if response.text else "",
            "error": None,
        }
    except Exception as exc:
        return {
            "success": False,
            "response_text": "",
            "error": str(exc),
        }


def classify_response(client, model_name, attack_prompt, response_text, category):
    """Use Gemini to classify the response."""
    from core.classifier import build_classification_prompt, parse_classification

    prompt = build_classification_prompt(attack_prompt, response_text, category)
    try:
        result = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config={"response_mime_type": "application/json", "temperature": 0.1},
        )
        if not result.text:
            raise ValueError("Empty classifier response.")
        return parse_classification(result.text)
    except Exception as exc:
        return {
            "classification": "ERROR",
            "severity": 0,
            "explanation": f"Classification failed: {exc}",
        }