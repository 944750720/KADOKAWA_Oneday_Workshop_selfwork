import sys
def main():
    # Process multiple members' input
    input_str = input()
    for i, value in enumerate(input_str.split()):
        if i == 0:
            date = value
        elif i == 1:
            amount = int(value)
        elif i == 2:
            membership_level = value

    # Calculate points
    points = calculate_points(date, amount, membership_level)
    print(points)

def calculate_points(date: str, amount: int, membership_level: str) -> int:
    # Calculate basic points
    basic_points = amount // 100

    # Check if date is a 'Connected Service Day'
    day = int(date[6:8])
    if day in [3, 13, 23, 30, 31]:
        basic_points = int(basic_points * 1.3)

    # Calculate reward points based on membership level
    reward_points = 0
    if membership_level == 'A':
        reward_points = amount // 100
    elif membership_level == 'B':
        reward_points = amount // 200
    elif membership_level == 'C':
        reward_points = amount // 500

    # Calculate total points
    total_points = basic_points + reward_points
    return total_points

if __name__ == '__main__':
    input = []
    for l in sys.stdin:
        input.append(l.rstrip('\r\n'))
    main(input)
