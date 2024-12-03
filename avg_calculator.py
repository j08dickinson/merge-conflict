def calculate_average_score(scores):
  average_score = 0
  total_score = 0

  for score in scores:
    total_score += score

  # moved count of scores to be calculated here
  average_score = total_score // len(scores)

  average_score = (total_score / len(scores))


  return average_score

# ------------------------------------------------------
if __name__ == '__main__':
  scores = [10, 20, 30, 40, 50]
  average_score = calculate_average_score(scores)
  print(average_score)