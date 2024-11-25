def calculate_average_score(scores):
  average_score = 0
  total_score = 0
  score_count = len(scores)

  for score in scores:
    total_score += int(score)

  average_score = total_score // score_count

  return average_score

# ------------------------------------------------------
if __name__ == '__main__':
  scores = [10, 20, 30, 40, 50]
  average_score = calculate_average_score(scores)
  print(average_score)