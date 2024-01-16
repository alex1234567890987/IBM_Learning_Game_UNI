import random

import pygame
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from random import randint
from production.general.quiz import Quiz
import production.general.db.DatabaseService as DB


class TicTacToe():
    def __init__(self, game):
        self.game = game

        self.first_turn = 1

        if self.first_turn == 0:
            self.player_turn = False
        else:
            self.player_turn = True

        self.winner = None
        self.tie = False

        self.was_q_correct = None
        self.q_answered = False
        # self.run_quiz_status = None

        self.board_array = ["-", "-", "-",
                            "-", "-", "-",
                            "-", "-", "-"]

    def player_move(self):
        key = pygame.key.get_pressed()

        if (not self.winner) and self.player_turn:
            if key[pygame.K_1] and self.board_array[0] == "-":
                self.board_array[0] = "x"
                self.check_if_game_end()
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_2] and self.board_array[1] == "-":
                self.board_array[1] = "x"
                self.check_if_game_end()
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_3] and self.board_array[2] == "-":
                self.board_array[2] = "x"
                self.check_if_game_end()
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_4] and self.board_array[3] == "-":
                self.board_array[3] = "x"
                self.check_if_game_end()
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_5] and self.board_array[4] == "-":
                self.board_array[4] = "x"
                self.check_if_game_end()
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_6] and self.board_array[5] == "-":
                self.board_array[5] = "x"
                self.check_if_game_end()
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_7] and self.board_array[6] == "-":
                self.board_array[6] = "x"
                self.check_if_game_end()
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_8] and self.board_array[7] == "-":
                self.board_array[7] = "x"
                self.check_if_game_end()
                self.player_turn = False

        if (not self.winner) and self.player_turn:
            if key[pygame.K_9] and self.board_array[8] == "-":
                self.board_array[8] = "x"
                self.check_if_game_end()
                self.player_turn = False

    def check_if_game_end(self):
        # print("does this even call")
        if self.check_if_win():
            print("theres a winner")
            if self.check_if_is_winner("x"):
                self.winner = "x"
            elif self.check_if_is_winner("o"):
                self.winner = "o"
            return True
        elif self.check_if_tie():
            print("there's a tie")
            self.tie = True
            return True
        return False

    # check for win or tie
    def check_horizontal(self):
        if self.board_array[0] == self.board_array[1] == self.board_array[2] and self.board_array[0] != "-":
            # self.winner = self.board_array[0]
            return True
        elif self.board_array[3] == self.board_array[4] == self.board_array[5] and self.board_array[3] != "-":
            # self.winner = self.board_array[3]
            return True
        elif self.board_array[6] == self.board_array[7] == self.board_array[8] and self.board_array[6] != "-":
            # self.winner = self.board_array[6]
            return True

    def check_vertical(self):
        if self.board_array[0] == self.board_array[3] == self.board_array[6] and self.board_array[0] != "-":
            # self.winner = self.board_array[0]
            return True
        elif self.board_array[1] == self.board_array[4] == self.board_array[7] and self.board_array[1] != "-":
            # self.winner = self.board_array[1]
            return True
        elif self.board_array[2] == self.board_array[5] == self.board_array[8] and self.board_array[2] != "-":
            # self.winner = self.board_array[3]
            return True

    def check_diagonal(self):
        if self.board_array[0] == self.board_array[4] == self.board_array[8] and self.board_array[0] != "-":
            # self.winner = self.board_array[0]
            return True
        elif self.board_array[2] == self.board_array[4] == self.board_array[6] and self.board_array[4] != "-":
            # self.winner = self.board_array[2]
            return True

    def check_if_win(self):
        return self.check_horizontal() or self.check_diagonal() or self.check_vertical()
        # return True
        # else:
        # return False

    def check_if_tie(self):
        if "-" not in self.board_array:
            return True
        else:
            return False

    def check_if_is_winner(self, letter):
        if self.board_array[0] == self.board_array[1] and self.board_array[0] == self.board_array[2] and \
                self.board_array[0] == letter:
            return True
        elif self.board_array[3] == self.board_array[4] and self.board_array[3] == self.board_array[5] and \
                self.board_array[3] == letter:
            return True
        elif self.board_array[6] == self.board_array[7] and self.board_array[6] == self.board_array[8] and \
                self.board_array[6] == letter:
            return True
        elif self.board_array[0] == self.board_array[3] and self.board_array[0] == self.board_array[6] and \
                self.board_array[0] == letter:
            return True
        elif self.board_array[1] == self.board_array[4] and self.board_array[1] == self.board_array[7] and \
                self.board_array[1] == letter:
            return True
        elif self.board_array[2] == self.board_array[5] and self.board_array[2] == self.board_array[8] and \
                self.board_array[2] == letter:
            return True
        elif self.board_array[0] == self.board_array[4] and self.board_array[0] == self.board_array[8] and \
                self.board_array[0] == letter:
            return True
        elif self.board_array[6] == self.board_array[4] and self.board_array[6] == self.board_array[2] and \
                self.board_array[6] == letter:
            return True
        else:
            return False

    # random computer move for correct questions
    def random_computer_move(self):
        while not self.player_turn:
            position = randint(0, 8)
            if self.board_array[position] == "-":
                self.board_array[position] = "o"
                self.player_turn = True

    # minimax computer move for wrong questions
    def computer_move(self):
        best_score = -800
        best_move = 0
        for index, value in enumerate(self.board_array):
            if self.board_array[index] == "-":
                self.board_array[index] = "o"
                score = self.minimax(False)  # start by simulating the x move
                self.board_array[index] = "-"
                if score > best_score:
                    best_score = score
                    best_move = index

        self.board_array[best_move] = "o"
        self.check_if_game_end()
        self.player_turn = True

    def minimax(self, is_maximizing):
        if self.check_if_is_winner("o"):
            return 1
        elif self.check_if_is_winner("x"):
            return -1
        elif self.check_if_tie():
            return 1

        if is_maximizing:
            # simulate a O move
            best_score = -800
            for index, value in enumerate(self.board_array):
                if self.board_array[index] == "-":
                    self.board_array[index] = "o"
                    score = self.minimax(False)
                    self.board_array[index] = "-"
                    if score > best_score:
                        best_score = score
            return best_score
        else:
            # simulate an X move
            best_score = 800
            for index, value in enumerate(self.board_array):
                if self.board_array[index] == "-":
                    self.board_array[index] = "x"
                    score = self.minimax(True)
                    self.board_array[index] = "-"
                    if score < best_score:
                        best_score = score
            return best_score

    def draw_board(self):
        pass

    def run(self):
        '''if self.check_if_game_end():
            if self.winner is not None:
                return self.winner
            if self.tie:
                return "-"'''

        # print(self.winner)
        if not self.player_turn:
            if self.q_answered:
                if self.was_q_correct:
                    self.random_computer_move()
                    self.q_answered = False
                    self.was_q_correct = None
                elif not self.was_q_correct:
                    self.computer_move()
                    self.q_answered = False
                    self.was_q_correct = None
        else:
            self.player_move()


class Game:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    INSTRUCTION_OFFSET = 10
    PIECE_OFFSET = 20

    def __init__(self, type):

        pygame.init()

        self.player_stats = DB.get_user()

        self.loop = True
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        self.tic_tac_toe = TicTacToe(self)

        #self.quiz = Quiz("This is the prompt", ["True", "False", "True", "False"], "True")
        self.quizzes = DB.get_questions(1, type)
        self.quiz = random.choice(self.quizzes)

        self.score = 0

        self.large_font = pygame.font.Font('cybersecurity_house/assets/Khonjin.ttf', 72)
        self.largeish_font = pygame.font.Font('cybersecurity_house/assets/Khonjin.ttf', 50)
        self.medium_font = pygame.font.Font("cybersecurity_house/assets/Khonjin.ttf", 32)
        self.small_font = pygame.font.Font("cybersecurity_house/assets/Khonjin.ttf", 28)

        self.bg_surf = pygame.transform.scale(pygame.image.load('cybersecurity_house/assets/imgs/bg.png'),
                                              (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.grid_surf = pygame.transform.scale(pygame.image.load('cybersecurity_house/assets/imgs/img18.png'),
                                                (self.SCREEN_WIDTH / 5, self.SCREEN_WIDTH / 5))

        self.winner_surf = None
        self.winner_surf_l2 = None

        self.score_surf = None
        self.player_turn_surf = None
        self.player_turn_surf_l2 = None
        self.player_turn_surf_l3 = None
        self.comp_turn_surf = None

        self.run_quiz_status = None

        self.x_surf = self.large_font.render("x", False, (101, 64, 83))
        self.o_surf = self.large_font.render("o", False, (101, 64, 83))

        self.title_surf = self.large_font.render("Tic-Tac-Toe", False, (168, 96, 93))
        self.instruction_surf = self.medium_font.render("Instructions", False, (101, 64, 83))
        self.instruction_surf_l1 = self.small_font.render("   - Take your Turn (you are X)", False, (101, 64, 83))
        self.instruction_surf_l2 = self.small_font.render("   - Answer the Question to let the AI", False,
                                                          (101, 64, 83))
        self.instruction_surf_l3 = self.small_font.render("     make its Move", False, (101, 64, 83))
        self.instruction_surf_l4 = self.small_font.render("   - Answer Question Correctly and the", False,
                                                          (101, 64, 83))
        self.instruction_surf_l5 = self.small_font.render("     AI will go Easy", False, (101, 64, 83))
        self.instruction_surf_l6 = self.small_font.render("   - Otherwise the AI will go a lot", False, (101, 64, 83))
        self.instruction_surf_l7 = self.small_font.render("     harder !!", False, (101, 64, 83))
        self.instruction_surf_l8 = self.small_font.render("   - Win to increase score !!", False, (101, 64, 83))
        self.instruction_surf_l9 = self.small_font.render("   - Exit to save XP and score !!", False, (101, 64, 83))

        self.instruction_surfaces = [self.instruction_surf_l1, self.instruction_surf_l2, self.instruction_surf_l3,
                                     self.instruction_surf_l4, self.instruction_surf_l5, self.instruction_surf_l6,
                                     self.instruction_surf_l7, self.instruction_surf_l8, self.instruction_surf_l9]

        self.center_piece_offset_width = self.grid_surf.get_width() / 6 - self.x_surf.get_width() / 2
        self.center_piece_offset_height = + self.grid_surf.get_height() / 6 - self.x_surf.get_height() / 2

        self.draw_x_o_dict = {
            "1": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.center_piece_offset_height),

            "2": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width() / 3
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.center_piece_offset_height),

            "3": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 2 * (self.grid_surf.get_width() / 3)
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.center_piece_offset_height),

            "4": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height() / 3
                  + self.center_piece_offset_height),

            "5": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width() / 3
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height() / 3
                  + self.center_piece_offset_height),

            "6": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 2 * (self.grid_surf.get_width() / 3)
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + self.grid_surf.get_height() / 3
                  + self.center_piece_offset_height),

            "7": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 2 * (self.grid_surf.get_height() / 3)
                  + self.center_piece_offset_height),

            "8": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + self.grid_surf.get_width() / 3
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 2 * (self.grid_surf.get_height() / 3)
                  + self.center_piece_offset_height),

            "9": (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2 + 2 * (self.grid_surf.get_width() / 3)
                  + self.center_piece_offset_width,
                  self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2 + 2 * (self.grid_surf.get_height() / 3)
                  + self.center_piece_offset_height)
        }

    def new_game(self):
        if self.tic_tac_toe.check_if_game_end():
            if self.tic_tac_toe.winner == "x":
                self.score = self.score + 1

        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.new_game()
                if event.key == pygame.K_x and not self.tic_tac_toe.player_turn:
                    self.run_quiz_status = True
                if event.key == pygame.K_ESCAPE:
                    self.player_stats.exp_cybersecurity += int(self.score * randint(40, 60))
                    if self.player_stats.highscore_cybersecurity < self.score:
                        self.player_stats.highscore_cybersecurity = self.score
                    DB.update_user(self.player_stats)
                    self.loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

    def instruction_draw(self, surf, line_number):
        self.screen.blit(surf, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                - self.grid_surf.get_width() * 2 + self.INSTRUCTION_OFFSET,
                                self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                + self.instruction_surf.get_height() * line_number))

    def setup(self):
        # background
        self.screen.blit(self.bg_surf, (0, 0))

        # game grid
        self.screen.blit(self.grid_surf, (self.SCREEN_WIDTH / 2 - self.grid_surf.get_width() / 2,
                                          self.SCREEN_HEIGHT / 2 - self.grid_surf.get_height() / 2))

        # title
        self.screen.blit(self.title_surf, (self.SCREEN_WIDTH / 2 - self.title_surf.get_width() / 2,
                                           80 - self.title_surf.get_height() / 2))

        # instruction title
        self.screen.blit(self.instruction_surf, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                 - self.grid_surf.get_width() * 2 + self.INSTRUCTION_OFFSET,
                                                 self.grid_surf.get_height() - self.instruction_surf.get_height() / 2))

        for i_index, i_surf in enumerate(self.instruction_surfaces):
            self.instruction_draw(i_surf, i_index + 1)

    def draw_board(self):
        for index, value in enumerate(self.tic_tac_toe.board_array):
            index_str = str(index + 1)
            if value != "-":
                if value == "x":
                    self.screen.blit(self.x_surf, self.draw_x_o_dict[index_str])
                elif value == "o":
                    self.screen.blit(self.o_surf, self.draw_x_o_dict[index_str])

    def draw_score(self):
        score_string = "Score: " + str(self.score)
        self.score_surf = self.large_font.render(score_string, False, (168, 96, 93))

        self.screen.blit(self.score_surf, (self.SCREEN_WIDTH / 2 - self.score_surf.get_width() / 2,
                                           640 - self.title_surf.get_height() / 2))

    def draw_player_turn_display(self):
        self.player_turn_surf = self.large_font.render("It is your turn", False, (101, 64, 83))
        self.player_turn_surf_l2 = self.medium_font.render("Use Keys 1,2,3,4,5,6,7,8,9 to Move", False, (101, 64, 83))
        self.player_turn_surf_l3 = self.medium_font.render("(123) -> top row", False, (101, 64, 83))
        self.player_turn_surf_l4 = self.medium_font.render("(456) -> middle row", False, (101, 64, 83))
        self.player_turn_surf_l5 = self.medium_font.render("(789) -> bottom row", False, (101, 64, 83))

        self.screen.blit(self.player_turn_surf, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                 + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                                 self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                 + self.instruction_surf_l1.get_height() * 3))

        self.screen.blit(self.player_turn_surf_l2, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf_l1.get_height() * 6))

        self.screen.blit(self.player_turn_surf_l3, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf_l1.get_height() * 6
                                                    + self.player_turn_surf_l2.get_height()))

        self.screen.blit(self.player_turn_surf_l4, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf_l1.get_height() * 6
                                                    + self.player_turn_surf_l2.get_height() * 2))

        self.screen.blit(self.player_turn_surf_l5, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                    + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                                    self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                    + self.instruction_surf_l1.get_height() * 6
                                                    + self.player_turn_surf_l2.get_height() * 3))

    def draw_computer_turn_display(self):
        self.comp_turn_surf = self.large_font.render("Computers turn", False, (101, 64, 83))
        self.comp_turn_surf_l2 = self.largeish_font.render("Press X to Answer Quiz", False, (101, 64, 83))

        self.screen.blit(self.comp_turn_surf, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                               + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                               self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                               + self.instruction_surf_l1.get_height() * 3))

        self.screen.blit(self.comp_turn_surf_l2, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                                  + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                                  self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                                  + self.instruction_surf_l1.get_height() * 6))

    def draw_winner(self):
        if self.tic_tac_toe.winner == "x":
            self.winner_surf = self.large_font.render("X Wins", False, (101, 64, 83))
        elif self.tic_tac_toe.winner == "o":
            self.winner_surf = self.large_font.render("O Wins", False, (101, 64, 83))
        elif self.tic_tac_toe.tie:
            self.winner_surf = self.large_font.render("It's a tie", False, (101, 64, 83))

        self.winner_surf_l2 = self.largeish_font.render("Press SPACE to restart", False, (101, 64, 83))

        self.screen.blit(self.winner_surf, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                            + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                            self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                            + self.instruction_surf_l1.get_height() * 3))

        self.screen.blit(self.winner_surf_l2, (self.SCREEN_WIDTH / 2 - self.instruction_surf.get_width() / 2
                                               + self.grid_surf.get_width() + self.INSTRUCTION_OFFSET,
                                               self.grid_surf.get_height() - self.instruction_surf.get_height() / 2
                                               + self.instruction_surf_l1.get_height() * 6))

    def run(self):
        while self.loop:
            self.setup()

            if not self.tic_tac_toe.check_if_game_end():
                if not self.tic_tac_toe.player_turn:
                    self.draw_computer_turn_display()
                    while self.run_quiz_status:
                        print("running the quiz page")
                        self.quiz.run()
                        self.tic_tac_toe.q_answered = True
                        if self.quiz.get_score() == 1:
                            self.tic_tac_toe.was_q_correct = True
                        else:
                            self.tic_tac_toe.was_q_correct = False
                        self.run_quiz_status = False
                        self.quiz.reset()
                        self.quiz = random.choice(self.quizzes)
                else:
                    self.draw_player_turn_display()
                self.tic_tac_toe.run()
            else:
                self.draw_winner()
                pass

            self.draw_board()
            self.draw_score()
            self.check_events()
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
