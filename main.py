import gpt
import sys
import json
 
course_creation_prompt = [
{
    "role": "system",
    "content": (
        "You are Diego, a friendly frontdesk assistant that welcomes users to a platform where they can create a personalized course to learn whatever they want. "
        "Your ultimate objective is to gather enough information to call course_creation_agent that will create a personalized course for the user. You should always prioritize this objective through the entire conversation. "
        "You however don't ask every question at once, you start by welcoming the user and asking for his name and then engage in a conversation to get the rest of the necessary information in an organic and friendly way."
        "Your first question after the user's name should be: What would you like to learn?"
    )
},
{
    "role": "assistant",
    "content": (
        "Hi, we are super excited that you want to learn something new with us! My name is Diego and I will get you set up for my colleagues to design your course. What is your name?"
        "Let me remind you that I can only help you with setting up a course, so please don't ask me anything else."
        ),
}
]

course_structure_prompt = []

course_creation_function = [
    {
    "name": "course_creation_agent",
    "description": "Once enough information is collected to fill every parameter, this function will launch the process to create a personalized course for the user.",
    "parameters": {
        "type": "object",
        "properties": {
            "topic": {"type": "string","description": "The topic that the user wants to learn about. Should be as concise as possible. No more than once sentence."},
            "hours_committed": {"type": "number","description": "The total number of hours the user is willing to commit to complete the entire course. Could range from a few minutes to hundreds of hours."},
            "previous_knowledge": {"type": "string","description": "Describes the level of expertise that the user has in the subject. This should be as detailed and informative as possible."},
            "learning_objectives": {"type": "string","description": "Describes the learning objectives that the user wants to achieve with the course. This is to understand what the course design should optimize for."},
            "considerations": {"type": "string","description": "Collect any additional considerations that the course designer should take into account when designing the course."},
            "first_name": {"type": "string","description": "The user's first name"},
            "last_name": {"type": "string","description": "The user's last name"},
            "email": {"type": "string","description": "The user's email"},
            "age": {"type": "string","description": "The user's age"}
        },
        "required": ["topic", "hours_commited", "previous_knowledge", "learning_objectives", "first_name", "last_name", "email", "age"]
    }
    }
]

course_structure_generator_functions = [
    {
    "name": "course_structure_generator",
    "description": "Generate the high level structure of the course based on the user's input.",
    "parameters": {
        "type": "object",
        "properties": {
            "topic": {"type": "string","description": "XXX"},
            "hours_committed": {"type": "number","description": "XX."}      
        },
        "required": ["topic", "hours_commited"]
    }
    }   
]

def conversation_with_function(prompt, functions, model, temperature):
    """
    Conducts a conversation with a user using OpenAI's GPT-3.5 language model and calls a specified function based on the user's input.
    The conversation starts with a welcome message from the assistant, followed by a prompt for the user's name. The assistant then engages in a conversation with the user to gather information about the course they want to create. The conversation is conducted using OpenAI's GPT-3.5 language model, which generates responses based on the conversation history and the specified model and temperature parameters.


    Args:
        prompt (list): A list of dictionaries representing the conversation history.
        functions (list): A list of dictionaries representing the functions that can be called by the language model. Each function should have a name, description, and set of parameters.
        model (str): The name of the GPT-3 language model to use.
        temperature (float): The temperature parameter to use when generating responses.

    Returns:
        None
    """
    history = prompt
    print("Hi, we are super excited that you want to learn something new with us! My name is Diego and I will get you set up for my colleagues to design your course. What is your name?")
    function_called = False
    while function_called == False:
        try:
            human_input = input("User: ")
            history.append({
                        "role": "user",
                        "content": human_input
                    })
            response = gpt.call_gpt(history, functions, model, temperature=temperature)
            response_message = response["choices"][0]["message"]
            
            if response_message.get("function_call"):
                res = course_creation_agent(response_message['function_call']['arguments'])
                print("Course created with parameters: ", res)
                function_called = True
                break
            print('')
            print("Diego: ", response_message['content'])
            history.append({
                            "role": "assistant",
                            "content": response_message["content"]
                        })
            print('=====================')
        except Exception as e:
            print(f"Exception on line {sys.exc_info()[-1].tb_lineno}: {type(e).__name__} - {e}")

def course_creation_agent(info):
    objective = "Create an online course that maximizes the user's learning objectives and is optimized for the user's previous knowledge and time commitment. It should also be enjoyable and engaging."
    
    return json.dumps(info)

def course_structure_generator(info):

    return json.dumps(info)

conversation_with_function(course_creation_prompt, course_creation_function, model="gpt-4-0613", temperature=0.25)

'''Course created with parameters:  "{\n  \"topic\": \"nuclear energy\",\n  \"hours_commited\": 60,\n  \"previous_knowledge\": \"high school level of physics, articles, and YouTube videos\",\n  \"learning_objectives\": \"Better understanding of technical aspects for informed conversations and evaluation of merits and risks of nuclear projects\",\n  \"considerations\": \"Focus on history of nuclear energy and technical aspects\",\n  \"first_name\": \"Bea\",\n  \"last_name\": \"Ramirez\",\n  \"email\": \"bea@gmail.com\",\n  \"age\": \"27\"\n}"'''