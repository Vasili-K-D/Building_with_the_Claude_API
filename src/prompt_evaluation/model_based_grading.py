import json

from prompt_evaluation.utils import add_user_message, add_assistant_message, chat


def grade_by_model(test_case, output):
    # Create evaluation prompt
    eval_prompt = f"""
        You are an expert AWS code reviewer. Your task is to evaluate the following AI-generated solution.
    
        Original Task:
        <task>
        {test_case["task"]}
        </task>
    
        Solution to Evaluate:
        <solution>
        {output}
        </solution>
        
        Solution criteria:
        <criteria>
        {test_case["solution_criteria"]}
        </criteria>
    
        Output Format
        Provide your evaluation as a structured JSON object with the following fields, in this specific order:
        - "strengths": An array of 1-3 key strengths
        - "weaknesses": An array of 1-3 key areas for improvement
        - "reasoning": A concise explanation of your overall assessment
        - "score": A number between 1-10
    
        Respond with JSON. Keep your response concise and direct.
        Example response shape:
        {{
            "strengths": string[],
            "weaknesses": string[],
            "reasoning": string,
            "score": number
        }}
        """

    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")

    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)