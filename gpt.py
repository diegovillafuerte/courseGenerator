import openai

def call_gpt(prompt, functions, model="gpt-4-0613", temperature=0, function_call='auto'):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            functions = functions,
            messages = prompt,
            temperature=temperature,
            function_call=function_call)
        return response
    except Exception as e:
        print("There was an exception: ", e)