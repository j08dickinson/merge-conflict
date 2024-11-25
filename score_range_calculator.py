def calculate_score_range(scores):
  score_range = 0
  max_score = 0
  min_score = 100

  for score in scores:
    if int(score) > max_score:
      max_score = int(score)
    if int(score) < min_score:
      min_score = int(score)

  score_range = max_score - min_score
  return score_range

# ------------------------------------------------------
if __name__ == '__main__':
  scores = [10, 20, 30, 40, 50]
  score_range = calculate_score_range(scores)
  print(score_range)