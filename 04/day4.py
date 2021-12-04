from util.fileReader import read_strings, read_2d_list

sample = read_strings(open("sample"))
data = read_strings(open("input"))


def print_bingo_cards(bingo_cards):
    for card in bingo_cards:
        for row in card:
            row_string = ""
            for entry in row:
                if len(entry) == 0:
                    row_string += "XX "
                elif len(entry) == 1:
                    row_string += " " + entry + " "
                else:
                    row_string += entry + " "
            print(row_string)
        print()


def read_game(game_string):
    game_nums = game_string[0].split(",")
    bingo_tables = []
    # first table starts in line 2
    current_line = 2
    while current_line + 4 < len(game_string):
        bingo_tables.append(read_2d_list([game_string[current_line], game_string[current_line + 1], game_string[current_line + 2], game_string[current_line + 3], game_string[current_line + 4]]))
        current_line += 6
    return game_nums, bingo_tables


def add_number(num, bingo_cards):
    for card in range(len(bingo_cards)):
        for row in range(len(bingo_cards[card])):
            for column in range(len(bingo_cards[card][row])):
                if bingo_cards[card][row][column] == num:
                    bingo_cards[card][row][column] = ""


def check_row_complete(card):
    for row in card:
        winner = True
        for num in row:
            if num != "":
                winner = False
                break
        if winner:
            return True
    return False


def check_column_complete(card):
    for column in range(len(card[0])):
        winner = True
        for row in card:
            if row[column] != "":
                winner = False
                break
        if winner:
            return True
    return False


def check_game_won(bingo_cards):
    for card in bingo_cards:
        if check_row_complete(card) or check_column_complete(card):
            return card


def determine_winning_score(winning_card, num):
    score = 0
    for row in winning_card:
        for entry in row:
            if entry != "":
                score += int(entry)
    return score * int(num)


def play_round(game_nums, bingo_cards):
    for num in game_nums:
        add_number(num, bingo_cards)
        winning_card = check_game_won(bingo_cards)
        if winning_card != None:
            return determine_winning_score(winning_card, num)


# part 2:
def check_game_lost(bingo_cards):
    unfinished_cards = 0
    last_cards = []
    for card in bingo_cards:
        if not check_row_complete(card) and not check_column_complete(card):
            unfinished_cards += 1
            last_cards = card
    return last_cards


def lose_round(game_nums, bingo_cards):
    last_cards_backup = []
    for num in game_nums:
        add_number(num, bingo_cards)
        last_cards = check_game_lost(bingo_cards)
        if len(last_cards) == 0:
            return determine_winning_score(last_cards_backup, num)
        last_cards_backup = last_cards


game_nums, bingo_cards = read_game(data)

# solution part 1:
# print(play_round(game_nums, bingo_cards))

# solution part 2:
print(lose_round(game_nums, bingo_cards))
