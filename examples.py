from prompt_engine.engine import PromptEngine

# Initialize the prompt engine
engine = PromptEngine("templates")

# --------------------------------------------------
# 1. SHOW THAT TEMPLATES ARE LOADED
# --------------------------------------------------
print("Loaded templates:")
for name in engine.templates:
    print("-", name)

# --------------------------------------------------
# 2. ZERO-SHOT PROMPT
# --------------------------------------------------
print("\n--- ZERO-SHOT PROMPT ---")
print(engine.render(
    "zero_shot_qa",
    {"question": "What is Artificial Intelligence?"}
))

# --------------------------------------------------
# 3. FEW-SHOT PROMPT
# --------------------------------------------------
print("\n--- FEW-SHOT PROMPT ---")
print(engine.render(
    "few_shot_sentiment",
    {"text": "This product works perfectly"}
))

# --------------------------------------------------
# 4. CHAIN-OF-THOUGHT PROMPT
# --------------------------------------------------
print("\n--- CHAIN-OF-THOUGHT PROMPT ---")
print(engine.render(
    "cot_reasoning",
    {"problem": "If one pen costs 10 rupees, how much do 5 pens cost?"}
))

# --------------------------------------------------
# 5. ROLE-BASED PROMPT
# --------------------------------------------------
print("\n--- ROLE-BASED PROMPT ---")
print(engine.render(
    "role_python_expert",
    {"task": "Explain Python decorators in simple terms"}
))

# --------------------------------------------------
# 6. STRUCTURED OUTPUT PROMPT
# --------------------------------------------------
print("\n--- STRUCTURED OUTPUT PROMPT ---")
print(engine.render(
    "structured_json",
    {"text": "Artificial Intelligence enables machines to learn from data."}
))

# --------------------------------------------------
# 7. PROMPT CHAINING
# --------------------------------------------------
print("\n--- PROMPT CHAINING DEMO ---")

summary = engine.render(
    "zero_shot_summarize",
    {
        "text": "Machine learning is a subset of artificial intelligence focused on data-driven models."
    }
)

final_output = engine.render(
    "structured_json",
    {"text": summary}
)

print(final_output)

# --------------------------------------------------
# 8. VALIDATION ERROR DEMO (IMPORTANT)
# --------------------------------------------------
print("\n--- VALIDATION ERROR DEMO ---")
try:
    engine.render("structured_json", {})
except Exception as e:
    print(e)
