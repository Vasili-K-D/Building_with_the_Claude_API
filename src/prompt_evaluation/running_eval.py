import json

from prompt_evaluation.utils import add_user_message, chat, add_assistant_message
from prompt_evaluation.model_based_grading import grade_by_model
from prompt_evaluation.code_based_grading import grade_syntax
from statistics import mean


# Before responce estimate your solution based on 10 point scale and if result less than 9 regenerate the response

def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
        Please solve the following task:
        
        {test_case["task"]}
        
        * Respond only with Python, JSON, or a plain Regex
        * Do not add any comments or commentary or explanation
    """

    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```code")
    output = chat(messages, stop_sequences=["```"])
    return output


def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)

    # TODO - Grading
    model_grade = grade_by_model(test_case, output)
    model_score = model_grade["score"]
    reason = model_grade["reasoning"]

    syntax_score = grade_syntax(output, test_case)

    score = (model_score + syntax_score) / 2

    return {
        "output": output,
        "test_case": test_case,
        "score": score,
        "reasoning": reason,
    }


def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []

    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)

    average_scores = mean([res["score"] for res in results])

    print(f"Average score: {average_scores}")

    return results

with open("dataset.json", "r") as f:
    dataset = json.load(f)

results = run_eval(dataset)

print(results)

