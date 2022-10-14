board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' ',

}
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-*-*-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-*-*-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(board)
        print("its your turn, "+ turn+" move to which place")
        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("its filled, which place to go?")
            continue

        if count >= 5:
            if board['7'] == board['8'] == board['9'] != " ":
                printboard(board)
                print('Game Over!')
                print(f"***the winner is {turn}***")
                break
            elif board['4'] == board['5'] == board['6'] != " ":
                printboard(board)
                print('Game Over!')
                print(f"***the winner is {turn}***")
                break
            elif board['1'] == board['2'] == board['3'] != " ":
                printboard(board)
                print('Game Over!')
                print(f"***the winner is {turn}***")
                break

            elif board['1'] == board['4'] == board['7'] != " ":
                printboard(board)
                print('Game Over!')
                print(f"***the winner is {turn}***")
                break
            elif board['2'] == board['5'] == board['8'] != " ":
                printboard(board)
                print('Game Over!')
                print(f"***the winner is {turn}***")
                break
            elif board['3'] == board['6'] == board['9'] != " ":
                printboard(board)
                print('Game Over!')
                print(f"***the winner is {turn}***")
                break

            elif board['1'] == board['5'] == board['9'] != " ":
                printboard(board)
                print('Game Over!')
                print(f"***the winner is {turn}***")
                break
            elif board['7'] == board['5'] == board['3'] != " ":
                printboard(board)
                print('Game Over!')
                print(f"***the winner is {turn}***")
                break
        if count == 9:
            print("Game Over")
            print("its a tie")
            break
        if turn == 'O':
            turn = 'X'
        else: turn = 'O'



if __name__ == '__main__':
    game()