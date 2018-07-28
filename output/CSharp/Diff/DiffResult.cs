using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Diff
{
    public class DiffResult
    {
        public DiffLine[] Lines { get; private set; }

        internal DiffResult(List<string> lines, List<int> ops)
        {
            List<DiffLine> linesList = new List<DiffLine>();
            for (int i = 0; i < lines.Count; ++i)
            {
                DiffLine line = new DiffLine() { Value = lines[i] };
                switch (ops[i])
                {
                    case -1: line.Status = DiffStatus.Remove; break;
                    case 0: line.Status = DiffStatus.Same; break;
                    case 1: line.Status = DiffStatus.Add; break;
                }
                linesList.Add(line);
            }
            this.Lines = linesList.ToArray();
        }
    }
}
