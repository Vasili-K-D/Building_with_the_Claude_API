# Create an instance of PromptEvaluator
# Increase `max_concurrent_tasks` for greater concurrency, but beware of rate limit errors!
from prompt_engineering_techniques.set_up import PromptEvaluator
from prompt_engineering_techniques.utils import chat, add_user_message

evaluator = PromptEvaluator(max_concurrent_tasks=3)


# dataset = evaluator.generate_dataset(
#     # Describe the purpose or goal of the prompt you're trying to test
#     task_description="Extract topics out of a passage of text from a scholarly article into a JSON array of strings",
#     # Describe the different inputs that your prompt requires
#     prompt_inputs_spec={
#         "content": "One paragraph of text from a scholarly journal written in English"
#     },
#     # Where to write the generated dataset
#     output_file="dataset_ex.json",
#     # Number of test cases to generate (recommend keeping this low if you're getting rate limit errors)
#     num_cases=4,
# )


# Prompt evolution

# First attempt - Average score: 2.25
# prompt = f"""
# What topics are in this text?
#
# {prompt_inputs["content"]}
# """

# Second attempt - Average score: 2.5
# prompt = f"""
# Extract out all the topics from the scholarly article
# or
# Extract all the topics discussed in the following scholarly article.
#
# {prompt_inputs["content"]}
# """

# Third attempt - Average score: 7.75
# prompt = f"""
# Extract all the topics discussed in the following scholarly article into JSON array of strings.
#
# {prompt_inputs["content"]}
# """

# Forth attempt - Average score: 7.75 - 8
# prompt = f"""
# Extract all the topics discussed in the following scholarly article.
#
# {prompt_inputs["content"]}
#
# Guidelines
# 1. Identify all topics explicitly discussed or mentioned in the article.
# 2. A topic is a specific concept, method, domain, problem or application area.
# 3. Each topic must be a concise phrase, not a full sentence.
# 4. Include both major and minor topics, as long as they are clearly supported by the text.
# 5. Avoid duplicates; merge synonyms and closely related formulations into one normalized topic.
# 6. Return topics as JSON array of strings without any extra commentary
# """

# Adding XML tags made it more stable but did not increase the best score
# Adding example with a good answer raised the score to 8 - 8.75
# Adding additional example with a not very good answer raised the scor to 8.25 - 9


def run_prompt(prompt_inputs):
    prompt = f"""
    Extract all the topics discussed in the following scholarly article into JSON array of strings.

    <scholarly_article>
    {prompt_inputs["content"]}
    </scholarly_article>
    
    Guidelines:
    1. Identify all topics explicitly discussed or mentioned in the article.
    2. A topic is a specific concept, method, domain, problem or application area.
    3. Each topic must be a concise phrase, not a full sentence.
    4. Include both major and minor topics, as long as they are clearly supported by the text.
    5. Avoid duplicates; merge synonyms and closely related formulations into one normalized topic.
    6. Return topics as JSON array of strings without any extra commentary
    
    This are a couple of examples of sample input and a really good output and not very good output:
    <sample_input>
    Machine learning approaches to natural language processing have revolutionized computational linguistics. Deep learning models, particularly neural networks and their specialized variants like recurrent neural networks (RNNs) and transformer architectures, have become the dominant paradigm. Transformers, which rely on attention mechanisms, have proven especially effective for tasks such as machine translation, sentiment analysis, and named entity recognition. Within the broader context of artificial intelligence, natural language processing applications now power virtual assistants, chatbots, and information retrieval systems. Recent advances in large language models represent a convergence of transformer architectures, attention mechanisms, and massive-scale pretraining on diverse text corpora, enabling unprecedented performance on downstream language understanding tasks.
    </sample_input>
    <good_output>
    [
      "Machine learning",
      "Natural language processing",
      "Computational linguistics",
      "Deep learning",
      "Neural networks",
      "Recurrent neural networks",
      "Transformer architectures",
      "Attention mechanisms",
      "Machine translation",
      "Sentiment analysis",
      "Named entity recognition",
      "Artificial intelligence",
      "Virtual assistants",
      "Chatbots",
      "Information retrieval",
      "Large language models",
      "Pretraining",
      "Language understanding",
      "Text corpora"
    ]
    </good_output>
    <reasoning>
    The solution fully satisfies all mandatory requirements: it is a valid JSON array containing only topic strings with no additional metadata or commentary. Regarding secondary criteria, the solution appropriately handles hierarchical relationships by including both parent topics (Machine learning, Neural networks) and child topics (Deep learning, RNNs, Transformers) without unnecessary duplication. The extraction is thorough and captures topics across different levels of abstraction as required. Minor weaknesses exist around borderline inclusions like 'Text corpora' which functions more as a supporting detail than a primary topic, but these are marginal issues that don't significantly detract from an otherwise comprehensive and well-executed extraction.
    </reasoning>
    
    <sample_input>
    The interplay between cognitive load and information retention during asynchronous learning environments presents complex challenges for instructional design. When learners encounter fragmented content delivery across multiple platforms, their working memory becomes constrained, yet paradoxically, the spacing effect—the phenomenon where distributed practice enhances long-term encoding—suggests that such fragmentation, if strategically implemented, may facilitate deeper neural consolidation than massed presentation would achieve.
    </sample_input>
    <not_very_good_output>
    [
      "Cognitive load",
      "Information retention",
      "Asynchronous learning",
      "Instructional design",
      "Content delivery",
      "Working memory",
      "Spacing effect",
      "Distributed practice",
      "Long-term encoding",
      "Neural consolidation",
      "Massed presentation"
    ]
    </not_very_good_output>
    <reasoning>
    The solution meets all mandatory requirements: it is a valid JSON array of strings containing topics from the article with no extra commentary. It successfully extracts the six explicitly mentioned topics and several inferred concepts. However, it falls short on the secondary criteria by missing the key emergent theme of 'learning design trade-offs'—the central paradox of the passage—which represents an important implicit connection between concepts. The inclusion of minor supporting details ('content delivery', 'massed presentation') slightly dilutes focus from core topics, though this is a minor issue. The solution demonstrates good comprehension but incomplete capture of the passage's conceptual architecture.
    </reasoning>
    """

    messages = []
    add_user_message(messages, prompt)
    return chat(messages)


results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset_ex.json",
    extra_criteria="""
    - Contains a JSON array, containing each topic mentioned in the article
    - The strings should contain only a topic without any extra commentary
    - Response should contain the JSON array and nothing else
    """,
)

# prompt = f"""
# Extract all the topics discussed in the following scholarly article into JSON array of strings.
#
# <scholarly_article>
# {prompt_inputs["content"]}
# </scholarly_article>
#
# Guidelines:
# 1. Identify all topics explicitly discussed or mentioned in the article.
# 2. A topic is a specific concept, method, domain, problem or application area.
# 3. Each topic must be a concise phrase, not a full sentence.
# 4. Include both major and minor topics, as long as they are clearly supported by the text.
# 5. Avoid duplicates; merge synonyms and closely related formulations into one normalized topic.
# 6. Return topics as JSON array of strings without any extra commentary
#
# This are a couple of examples of sample input and a really good output and not very good output:
# <sample_input>
#     Machine learning approaches to natural language processing have revolutionized computational linguistics. Deep learning models, particularly neural networks and their specialized variants like recurrent neural networks (RNNs) and transformer architectures, have become the dominant paradigm. Transformers, which rely on attention mechanisms, have proven especially effective for tasks such as machine translation, sentiment analysis, and named entity recognition. Within the broader context of artificial intelligence, natural language processing applications now power virtual assistants, chatbots, and information retrieval systems. Recent advances in large language models represent a convergence of transformer architectures, attention mechanisms, and massive-scale pretraining on diverse text corpora, enabling unprecedented performance on downstream language understanding tasks.
# </sample_input>
# <good_output>
# [
#   "Machine learning",
#   "Natural language processing",
#   "Computational linguistics",
#   "Deep learning",
#   "Neural networks",
#   "Recurrent neural networks",
#   "Transformer architectures",
#   "Attention mechanisms",
#   "Machine translation",
#   "Sentiment analysis",
#   "Named entity recognition",
#   "Artificial intelligence",
#   "Virtual assistants",
#   "Chatbots",
#   "Information retrieval",
#   "Large language models",
#   "Pretraining",
#   "Language understanding",
#   "Text corpora"
# ]
# </good_output>
# <reasoning>
# The solution fully satisfies all mandatory requirements: it is a valid JSON array containing only topic strings with no additional metadata or commentary. Regarding secondary criteria, the solution appropriately handles hierarchical relationships by including both parent topics (Machine learning, Neural networks) and child topics (Deep learning, RNNs, Transformers) without unnecessary duplication. The extraction is thorough and captures topics across different levels of abstraction as required. Minor weaknesses exist around borderline inclusions like 'Text corpora' which functions more as a supporting detail than a primary topic, but these are marginal issues that don't significantly detract from an otherwise comprehensive and well-executed extraction.
# </reasoning>
#
# <sample_input>
# The interplay between cognitive load and information retention during asynchronous learning environments presents complex challenges for instructional design. When learners encounter fragmented content delivery across multiple platforms, their working memory becomes constrained, yet paradoxically, the spacing effect—the phenomenon where distributed practice enhances long-term encoding—suggests that such fragmentation, if strategically implemented, may facilitate deeper neural consolidation than massed presentation would achieve.
# </sample_input>
# <not_very_good_output>
# [
#   "Cognitive load",
#   "Information retention",
#   "Asynchronous learning",
#   "Instructional design",
#   "Content delivery",
#   "Working memory",
#   "Spacing effect",
#   "Distributed practice",
#   "Long-term encoding",
#   "Neural consolidation",
#   "Massed presentation"
# ]
# </not_very_good_output>
# <reasoning>
# The solution meets all mandatory requirements: it is a valid JSON array of strings containing topics from the article with no extra commentary. It successfully extracts the six explicitly mentioned topics and several inferred concepts. However, it falls short on the secondary criteria by missing the key emergent theme of 'learning design trade-offs'—the central paradox of the passage—which represents an important implicit connection between concepts. The inclusion of minor supporting details ('content delivery', 'massed presentation') slightly dilutes focus from core topics, though this is a minor issue. The solution demonstrates good comprehension but incomplete capture of the passage's conceptual architecture.
# </reasoning>
#
# """