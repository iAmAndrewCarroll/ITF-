output = "questions_and_answers = [\n"

with open("studyguide.md", "r") as f:
    lines = f.readlines()
    question = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("-"):
            answer = line[1:].strip()
            output += f"    {{'question': '{question}', 'answer': '{answer}'}},\n"
        else:
            question = line

output += "]"

with open("flashcards_data.py", "w") as f:
    f.write(output)
