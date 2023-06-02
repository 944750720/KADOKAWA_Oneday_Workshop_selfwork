def main():
    # Read input
    input_str = input()
    date, amount, membership_level = input_str.split()
    amount = int(amount)

    # Calculate points
    points = calculate_points(date, amount, membership_level)
    print(points)

def calculate_points(date: str, amount: int, membership_level: str) -> int:
    REWARD_POINTS_A = 100
    REWARD_POINTS_B = 200
    REWARD_POINTS_C = 500
    # Calculate original points
    original_points = amount // 100

    # Check if date is a 'Connected Service Day'
    day = int(date[6:8])
    if day in [3, 13, 23, 30, 31]:
        original_points = int(original_points * 1.3)

    # Calculate reward points according to membership‘s level
    reward_points = 0
    if membership_level == 'A':
        reward_points = amount // REWARD_POINTS_A
    elif membership_level == 'B':
        reward_points = amount // REWARD_POINTS_B
    elif membership_level == 'C':
        reward_points = amount // REWARD_POINTS_C

    # Calculate total points
    total_points = original_points + reward_points
    return total_points

if __name__ == '__main__':
    main()

