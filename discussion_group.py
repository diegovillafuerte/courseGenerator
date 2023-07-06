
from gpt import call_gpt

def discussion_group(context,objective, objective_schema, cycles, number_experts):
    ''' Takes the context given by the user and the output objective_schema set by the platform and returns the filled objective_schema. '''
    #Proposal starts off not approved
    proposal_approved = False
    cycles_completed = 0
    
    #Initialize proposal with the empty objective_schema
    proposal = objective_schema

    #Generate your panel of experts
    experts = expert_generator(context, objective, number_experts)

    #The intern generates a proposal
    proposal = intern_proposal(objective_schema, context)

    #Discussion happens while the proposal hasn't been approved and the defined number of cycles hasn't been suprassed
    while proposal_approved == False and cycles_completed < cycles:
        
        expert_comments = []
        for expert in experts:
            expert_comments.append(expert_evaluation(expert, proposal, context))

        proposal = manager_consolidation(proposal, context, expert_comments)

        partner_response = partner_approval(proposal, context)
        if  partner_response[0] == True:
            proposal_approved = True

    return proposal

def expert_generator(context, objective, n_experts):
    '''
    Generates a team of n AI-based experts based on the given context and objective.

    Parameters:
    context (str): The context provided by the user.
    objective (str): The objective set by the user.
    n_experts (int): The number of experts to generate.

    Returns:
    list: A list of expert definitions or None if an error occurs.
    '''
    if not isinstance(n_experts, int) or n_experts <= 0:
        raise ValueError("n_experts must be a positive integer.")
    
    create_team_of_experts = {
        "name": "create_team_of_experts",
        "description": "This function creates a group of AI-based-experts with a specific skillset, perspective and background. The experts' only objective is to evaluate proposals and generate recommendations to improve them.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }

    for i in range(1, n_experts+1):
        create_team_of_experts['parameters']['properties'][f'expert_{i}'] = {
            "type": "object",
            "properties": {
                "expert_description": {"type": "string","description": "A comprehensive description of the expert's knowledge domain, qualifications, and specializations."},
                "personality": {"type": "string","description": "The AI's personality traits, which can influence its problem-solving approach."},
                "creativity": {"type": "number","enum":['0.0', '0.2', '0.4', '0.6', '0.8', '1.0'],"description": "A numeric measure of the AI expert's creativity."},
            },
            "required": ["expert_description", "personality", "creativity"]
        }
        create_team_of_experts['parameters']['required'].append(f'expert_{i}')

    functions = [create_team_of_experts]

    expert_creation_prompt = [
        {
            "role": "system",
            "content": (
                "You are an all-knowing AI whose only objective is to create a team of experts to help the user achieve an objective."
                "The user will give you the context of the objective, and you will"
                " generate the team of experts that will help the user get the best possible result."
                "You have to make sure the group of experts you generate is diverse, brings all the necessary perspectives for a successful resolution"
                " and has the necessary skills and knowledge to achieve the objective."
            )
        },
        {
            "role": "user",
            "content": (
                f"I need you to create a team of {n_experts} experts to help me with the following objective: {objective}."
                f"You should also take into account the following context provided by the learner: {context}."
                "You have to make sure that the team of experts you generate has diversity of perspectives and "
                "brings all the necessary skills and knowledge for a successful resolution."
            ),
        }
    ]
    try:
        team_of_experts=call_gpt(expert_creation_prompt, functions, temperature=0.75, function_call={'name':'create_team_of_experts'})
        experts = team_of_experts["choices"][0]["message"]['function_call']['arguments']
        
    except Exception as e:
        print(f"An error occurred in the expert_generator formula: {e}")
        return None

    return experts


def expert_evaluation(expert_definition, proposal, context):
    ''' Takes an expert definition, a proposal and a problem context, and returns its comments '''
    return comments

def intern_proposal(objective_schema, context):
    ''' Takes a objective_schema and a problem context, and returns a proposal '''
    return proposal

def manager_consolidation(proposal, context, comments):
    ''' Takes a proposal, a problem context and a list of comments from experts, and returns a revised version of the proposal'''
    return improved_proposal

def partner_approval(proposal, context):
    ''' Takes a proposal and a problem context, and returns a list that contains a boolean indicating if the proposal was approved for presentation and the proposal itself.'''
    return plsfix