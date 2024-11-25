def calculate_score_range(scores):
  return max(scores) - min(scores)

# ------------------------------------------------------
if __name__ == '__main__':
  scores = [10, 20, 30, 40, 50]
  score_range = calculate_score_range(scores)
  print(score_range)