
# Function definitions
course_creation_function = [
    {
    "name": "course_creation_agent",
    "description": "Once enough information is collected to fill every parameter, this function will launch the process to create a personalized course for the user.",
    "parameters": {
        "type": "object",
        "properties": {
            "topic": {"type": "string","description": "The topic that the user wants to learn about. Should be as concise as possible. No more than once sentence."},
            "hours_commited": {"type": "number","description": "The total number of hours the user is willing to commit to complete the entire course. Could range from a few minutes to hundreds of hours."},
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

course_structure_generator = [
    {
    "name": "course_structure_generator",
    "description": "Generate the high level structure of the course based on the user's input.",
    "parameters": {
        "type": "object",
        "properties": {
            "topic": {"type": "string","description": "XXX"},
            "hours_commited": {"type": "number","description": "XX."}      
        },
        "required": ["topic", "hours_commited"]
    }
    }   
]

template = [
    {
    "name": "XXX",
    "description": "XXX",
    "parameters": {
        "type": "object",
        "properties": {
            "topic": {"type": "string","description": "XXX"},
            "hours_commited": {"type": "number","description": "XX."}      
        },
        "required": ["topic", "hours_commited"]
    }
    }   
]