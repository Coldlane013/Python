SIZE = 4
def bar():
  print("#" + "=" * (4 * SIZE) + "#")
def top():
  for line in range(1, SIZE + 1):
     print("|" + (-2 * line + 2 * SIZE) * " " +            "<>" + (4 * line - 4) * "." + "<>" +           (-2 * line + 2 * SIZE) * " " + "|")
def bottom():
  for line in range(SIZE, 0, -1):
      print("|" + (-2 * line + 2 * SIZE) * " " +            "<>" + (4 * line - 4) * "." + "<>" +            (-2 * line + 2 * SIZE) * " " + "|")
# main
bar()
top()
bottom()
bar()
