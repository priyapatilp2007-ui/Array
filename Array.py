import sys

# Get scores from command-line arguments
scores = list(map(int, sys.argv[1:]))

# Check if scores were provided
if len(scores) == 0:
    print("No scores provided.")
else:
    total = sum(scores)
    average = total / len(scores)

    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Sum of scores:", total)
    print("Average of scores:", average)
    print("Maximum score:", maximum)
    print("Minimum score:", minimum)