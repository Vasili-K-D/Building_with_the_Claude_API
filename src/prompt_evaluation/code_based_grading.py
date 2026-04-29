# helper functions
import ast
import json
import re


def validate_json(text):
    try:
        json.loads(text.strip())
        return 10
    except json.JSONDecodeError:
        return 0

def validate_python(text):
    try:
        ast.parse(text.strip())
        return 10
    except SyntaxError:
        return 0

def validate_regex(text):
    try:
        re.compile(text.strip())
        return 10
    except re.error:
        return 0


def grade_syntax(output, test_case):
    result_format = test_case['format']
    match result_format:
        case "python":
            return validate_python(output)
        case "regex":
            return validate_regex(output)
        case "json":
            return validate_json(output)
        case _:
            return 0

