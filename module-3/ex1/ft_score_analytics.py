import sys

def main():
    if len(sys.argv) == 1:
        print("=== Player Score Analytics ===")
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except:
            print(f"Invalid score ignored: {arg}")

    if len(scores) == 0:
        print("=== Player Score Analytics ===")
        print("No valid scores to analyze.")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print("=== Player Score Analytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")

if __name__ == "__main__":
    main()
