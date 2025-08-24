import os
import requests
import json
from openai import AzureOpenAI
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


AZUREAI_ENDPOINT = os.getenv("AZUREAI_ENDPOINT", "https://ai-milanvadhavana7434ai333247097360.openai.azure.com")
AZUREAI_KEY = os.getenv("AZUREAI_KEY", "OWDH4EJzEJ84y1UU918XvZXNr7Xg28CE39gj7CHRdSU3y7cA2W2UJQQJ99BHACHYHv6XJ3w3AAAAACOGdHeK")  # Replace with your actual key
DEPLOYMENT_NAME = "gpt-4"  # Replace with your actual deployment name

@csrf_exempt  # Allow AJAX calls without CSRF issues
def chatbot_view(request):
    return render(request, 'index.html')

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()

        if not user_message:
            return JsonResponse({"error": "Message cannot be empty."}, status=400)

        headers = {
            "Authorization": f"Bearer {AZUREAI_KEY}",
            "Content-Type": "application/json"
        }

        api_url = f"{AZUREAI_ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2023-07-01-preview"

        data = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            "max_tokens": 300,
            "temperature": 0.7
        }

        try:
            response = requests.post(api_url, json=data, headers=headers)
            response.raise_for_status()  # Raises an error for HTTP issues

            response_data = response.json()
            bot_reply = response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response.")

        except requests.exceptions.RequestException as e:
            bot_reply = f"Error: {str(e)}"

        return JsonResponse({"response": bot_reply})

    return JsonResponse({"error": "Invalid request"}, status=400)

