from main import run_agent

# Test cases with expected keywords
test_cases = [
    {
        "question": "Suggest a model for image colorization",
        "expected": ["ResNet", "encoder", "decoder"]
    },
    {
        "question": "Write code for image colorization",
        "expected": ["torch", "nn.Module", "forward"]
    },
    {
        "question": "What hyperparameters should I use?",
        "expected": ["learning rate", "batch", "optimizer"]
    },
    {
        "question": "How to improve accuracy?",
        "expected": ["augmentation", "loss", "dataset", "GAN"]
    }
]

def evaluate_response(response, expected_keywords):
    score = 0

    response_lower = response.lower()

    # Keyword matching
    matches = sum(1 for word in expected_keywords if word.lower() in response_lower)
    keyword_score = (matches / len(expected_keywords)) * 10

    # Length quality
    length_score = 10 if len(response) > 80 else 6

    # Structure (new lines = better readability)
    structure_score = 10 if "\n" in response else 5

    # Final weighted score
    final = (0.5 * keyword_score) + (0.3 * length_score) + (0.2 * structure_score)

    return round(final, 2)


def run_evaluation():
    total_score = 0

    for test in test_cases:
        response = run_agent(test["question"])
        score = evaluate_response(response, test["expected"])
        total_score += score

        print(f"\nTest: {test['question']}")
        print(f"Score: {score}/10")

    avg_score = total_score / len(test_cases)
    final_score = int(avg_score * 1000)

    print("\nFinal Score:", final_score, "/ 10,000")


if __name__ == "__main__":
    run_evaluation()