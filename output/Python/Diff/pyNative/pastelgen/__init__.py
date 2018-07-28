TranslationHelper_NoneListOfOne = [None]

def GenerateTextDiff(text1, size1, text2, size2, linesOut, lineOpOut):
  width = (size2 + 1)
  height = (size1 + 1)
  costs = (TranslationHelper_NoneListOfOne * (width * height))
  source = (TranslationHelper_NoneListOfOne * (width * height))
  x = 0
  y = 0
  while (x < width):
    costs[x] = x
    source[x] = (x - 1)
    x += 1
  while (y < height):
    costs[(y * width)] = y
    source[(y * width)] = ((y - 1) * width)
    y += 1
  index = 0
  y = 1
  while (y < height):
    x = 1
    index = ((y * width) + x)
    while (x < width):
      if (text1[(y - 1)] == text2[(x - 1)]):
        costs[index] = costs[(index - 1 - width)]
        source[index] = 0
      elif (costs[(index - 1)] < costs[(index - width)]):
        costs[index] = (costs[(index - 1)] + 1)
        source[index] = 2
      else:
        costs[index] = (costs[(index - width)] + 1)
        source[index] = 1
      x += 1
      index += 1
    y += 1
  x = (width - 1)
  y = (height - 1)
  s = 0
  while ((x != 0) or (y != 0)):
    s = source[((y * width) + x)]
    if (s == 0):
      linesOut.append(text1[(y - 1)])
      lineOpOut.append(0)
      y -= 1
      x -= 1
    elif (s == 1):
      linesOut.append(text1[(y - 1)])
      lineOpOut.append(-1)
      y -= 1
    else:
      linesOut.append(text2[(x - 1)])
      lineOpOut.append(1)
      x -= 1
  linesOut.reverse()
  lineOpOut.reverse()
  return 0

