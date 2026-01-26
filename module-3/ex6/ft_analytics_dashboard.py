def main() -> None:
    print("=== Game Analytics Dashboard ===")

    print("")

    players = [
        {"name": "alice", "score": 2300, "achievements": 5,
         "active": True, "region": "north"},
        {"name": "bob", "score": 1800, "achievements": 3,
         "active": True, "region": "east"},
        {"name": "charlie", "score": 2150, "achievements": 7,
         "active": True, "region": "central"},
        {"name": "diana", "score": 2050, "achievements": 4,
         "active": False, "region": "north"},
    ]

    achievements = [
        ("alice", "first_kill"),
        ("alice", "level_10"),
        ("bob", "first_kill"),
        ("charlie", "boss_slayer"),
        ("diana", "level_10"),
    ]

    print("=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p["score"] * 2 for p in players if p["active"]]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p["name"] for p in players if p["active"]]
    print(f"Active players: {active_players}")

    print("")

    print("=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in players if p["active"]}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": len([p for p in players if p["score"] >= 2100]),
        "medium": len([p for p in players if 1800 <= p["score"] < 2100]),
        "low": len([p for p in players if p["score"] < 1800]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p["name"]: p["achievements"] for p in players}
    print(f"Achievement counts: {achievement_counts}")

    print("")

    print("=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {a[1] for a in achievements}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p["region"] for p in players if p["active"]}
    print(f"Active regions: {active_regions}")

    print("")

    print("=== Combined Analysis ===")

    total_players = len(unique_players)
    print(f"Total players: {total_players}")

    total_unique_achievements = len(unique_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")

    average_score = sum(p["score"] for p in players) / len(players)
    print(f"Average score: {average_score}")

    top_player = max(players, key=lambda p: p["score"])
    print(
        f"Top performer: {top_player['name']} "
        f"({top_player['score']} points,"
        f"{top_player['achievements']} achievements)"
    )


if __name__ == "__main__":
    main()
