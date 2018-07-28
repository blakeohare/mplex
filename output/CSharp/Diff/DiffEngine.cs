using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Diff
{
    public class DiffEngine
    {
        public DiffEngine() {
            // TODO: configure options such as side-by-side, injecting ellipses, etc.
        }

        public DiffResult Diff(string left, string right)
        {
            string[] leftArray = left.Replace("\r\n", "\n").Split('\n');
            string[] rightArray = right.Replace("\r\n", "\n").Split('\n');
            List<string> linesOut = new List<string>();
            List<int> opsOut = new List<int>();
            Backend.BridgeImpl.INSTANCE.DiffText(leftArray, leftArray.Length, rightArray, rightArray.Length, linesOut, opsOut);
            return new DiffResult(linesOut, opsOut);
        }
    }
}
