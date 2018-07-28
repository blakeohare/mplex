using System;
using System.Collections.Generic;
using System.Linq;

namespace PastelGeneratedNamespace
{
    internal static class FunctionWrapper
    {
        public static int GenerateTextDiff(string[] text1, int size1, string[] text2, int size2, List<string> linesOut, List<int> lineOpOut)
        {
            int width = (size2 + 1);
            int height = (size1 + 1);
            int[] costs = new int[(width * height)];
            int[] source = new int[(width * height)];
            int x = 0;
            int y = 0;
            while ((x < width))
            {
                costs[x] = x;
                source[x] = (x - 1);
                x += 1;
            }
            while ((y < height))
            {
                costs[(y * width)] = y;
                source[(y * width)] = ((y - 1) * width);
                y += 1;
            }
            int index = 0;
            y = 1;
            while ((y < height))
            {
                x = 1;
                index = ((y * width) + x);
                while ((x < width))
                {
                    if ((text1[(y - 1)] == text2[(x - 1)]))
                    {
                        costs[index] = costs[(index - 1 - width)];
                        source[index] = 0;
                    }
                    else
                    {
                        if ((costs[(index - 1)] < costs[(index - width)]))
                        {
                            costs[index] = (costs[(index - 1)] + 1);
                            source[index] = 2;
                        }
                        else
                        {
                            costs[index] = (costs[(index - width)] + 1);
                            source[index] = 1;
                        }
                    }
                    x += 1;
                    index += 1;
                }
                y += 1;
            }
            x = (width - 1);
            y = (height - 1);
            int s = 0;
            while (((x != 0) || (y != 0)))
            {
                s = source[((y * width) + x)];
                if ((s == 0))
                {
                    linesOut.Add(text1[(y - 1)]);
                    lineOpOut.Add(0);
                    y -= 1;
                    x -= 1;
                }
                else
                {
                    if ((s == 1))
                    {
                        linesOut.Add(text1[(y - 1)]);
                        lineOpOut.Add(-1);
                        y -= 1;
                    }
                    else
                    {
                        linesOut.Add(text2[(x - 1)]);
                        lineOpOut.Add(1);
                        x -= 1;
                    }
                }
            }
            linesOut.Reverse();
            lineOpOut.Reverse();
            return 0;
        }

    }
}
