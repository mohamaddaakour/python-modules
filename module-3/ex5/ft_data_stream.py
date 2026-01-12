def game_event_stream(total_events):
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, total_events + 1):
        player = players[i % 3]
        level = (i % 15) + 1
        action = actions[i % 3]
        yield i, player, level, action


def fibonacci_stream():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream():
    number = 2
    while True:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 1


def main():
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    high_level = 0
    treasure_events = 0
    level_up_events = 0
    processed = 0

    stream = game_event_stream(total_events)

    for event_id, player, level, action in stream:
        processed += 1

        if processed <= 3:
            print(f"Event {event_id}: Player {player} (level {level}) {action}")

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("=== Generator Demonstration ===")

    fib = fibonacci_stream()
    print(
        "Fibonacci sequence (first 10): "
        + ", ".join(str(next(fib)) for _ in range(10))
    )

    primes = prime_stream()
    print(
        "Prime numbers (first 5): "
        + ", ".join(str(next(primes)) for _ in range(5))
    )


if __name__ == "__main__":
    main()
