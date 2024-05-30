from itertools import combinations


def generate_unique_combinations(letters):
    unique_combinations = set()
    for r in range(1, len(letters) + 1):
        for comb in combinations(letters, r):
            unique_combinations.add(''.join(comb))
    return sorted(unique_combinations, key=len)


def numbers_to_letters(numbers):
    letters = [chr(ord('a') + n - 1) for n in numbers]
    return letters


def letters_to_numbers(letters):
    numbers = [ord(letter) - ord('a') + 1 for letter in letters]
    return numbers


def check_merged_columns(workers, prefs):
    beer_types = int(len(prefs)/workers)
    for i in range(workers):
        result = False
        for j in range(beer_types):
            if prefs[i * beer_types + j] == "Y":
                result = True
                break
        if not result:
            return False

    return True


def extract_columns(pref, columns, workers, beer_types):
    result = ''
    for j in range(workers):
        for i in range(len(columns)):
            result += (pref[j * beer_types + int(columns[i])])

    return result


def find_min_beers_types(workers, beer_types, prefs):

    if workers <= 0 or workers >= 50 or beer_types <= 0 or beer_types >= 50:
        return 'INCORRECT INPUT'

    if workers * beer_types != len(prefs):
        return 'INCORRECT INPUT'

    if 'Y' not in prefs or not prefs:
        return 'INCORRECT INPUT'

    # Creates an array of beer types named 0 to N, N = beer_types
    # Converts array's insides to letters to generate combinations properly
    # Generates a set of all possible combinations of beer types that might fulfill needed condition
    # Sorts combinations from smallest to biggest
    unique_combinations = generate_unique_combinations(numbers_to_letters([i for i in range(0, beer_types)]))

    # Go through every combination
    for comb in unique_combinations:

        # Check every combination
        # Convert every individual combination back to numbers
        if check_merged_columns(workers, extract_columns(prefs, letters_to_numbers(comb), workers, beer_types)):

            # Returns current combination of beers that fulfilled condition
            return letters_to_numbers(comb)

    return 'No condition fulfilling option is found. Most likely someone doesn\'t like any beer'

# Note:
# As we sorted combinations from small to big - first combination that fulfills condition will be the smallest possible


print(find_min_beers_types(3, 3, "NNYYNNYYY"))
