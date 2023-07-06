import json
from discussion_group import expert_generator


context = """
Bea Ramirez is a 27-year-old individual who has committed 10 hours to learn about Nuclear Energy. Despite being a beginner, she wants to understand the technicalities of nuclear power, evaluate nuclear projects objectively, and have informed conversations with her technical peers. She is also interested in understanding the history and physics behind nuclear energy.
"""

objective = "Create an online course that maximizes the user's learning objectives and is optimized for the user's previous knowledge and time commitment. It should also be enjoyable and engaging."

print(json.dumps(expert_generator(context, objective, 3), indent=4))



