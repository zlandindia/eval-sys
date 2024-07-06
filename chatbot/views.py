from django.shortcuts import render
from django.http import JsonResponse
from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "microsoft/DialoGPT-small"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def chatbot_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    response_ids = model.generate(input_ids, max_length=1000, num_return_sequences=1)
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text

def chat(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        bot_response = chatbot_response(user_input)
        return JsonResponse({'response': bot_response})
    return render(request, 'chatbot/chat.html')
