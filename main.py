from entry import home_page
from quiz import quiz_page
from result import result_page

name, difficulty = home_page()

score, time_taken = quiz_page(difficulty)

result_page(name, difficulty, score, time_taken)