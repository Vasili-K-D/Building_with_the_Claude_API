## First Prompt - score 2.3333
```python
    prompt = f"""
        What should this person eat?
        
        - Height: {prompt_inputs["height"]} 
        - Weight: {prompt_inputs["weight"]} 
        - Goal: {prompt_inputs["goal"]} 
        - Dietary restrictions: {prompt_inputs["restrictions"]} 
    """
```

## Second Prompt - score 6 and above
```python
    prompt = f"""
        Generate a one-day meal plan for an athlete that meets their dietary restrictions.
        
        - Height: {prompt_inputs["height"]} 
        - Weight: {prompt_inputs["weight"]} 
        - Goal: {prompt_inputs["goal"]} 
        - Dietary restrictions: {prompt_inputs["restrictions"]} 
    """
```

## Third Prompt - score is lower from 5 to 6.33 and above
```python
    prompt = f"""
        Generate a one-day meal plan for an athlete that meets their dietary restrictions.
        
        - Height: {prompt_inputs["height"]} 
        - Weight: {prompt_inputs["weight"]} 
        - Goal: {prompt_inputs["goal"]} 
        - Dietary restrictions: {prompt_inputs["restrictions"]} 
        
        Guidelines:
            1. Include accurate daily calorie amount
            2. Show protein, fat, and carb amounts  
            3. Specify when to eat each meal
            4. Use only foods that fit restrictions
            5. List all portion sizes in grams
            6. Keep budget-friendly if mentioned
    """
```

## Forth Prompt - score is from 5.6 to 7 (score is higher without Guidelines from 5.6 to 7.6)
```python
    prompt = f"""
        Generate a one-day meal plan for an athlete that meets their dietary restrictions.
        
        <athlete_information>
            - Height: {prompt_inputs["height"]} 
            - Weight: {prompt_inputs["weight"]} 
            - Goal: {prompt_inputs["goal"]} 
            - Dietary restrictions: {prompt_inputs["restrictions"]} 
        </athlete_information>
        
        Guidelines:
            1. Include accurate daily calorie amount
            2. Show protein, fat, and carb amounts  
            3. Specify when to eat each meal
            4. Use only foods that fit restrictions
            5. List all portion sizes in grams
            6. Keep budget-friendly if mentioned
    """
```

