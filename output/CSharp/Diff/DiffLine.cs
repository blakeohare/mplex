using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Diff
{
    public enum DiffStatus
    {
        Add,
        Remove,
        Same,
    }

    public sealed class DiffLine
    {
        internal DiffLine() { }

        public string Value { get; internal set; }
        public DiffStatus Status { get; internal set; }
        public char DiffChar
        {
            get
            {
                switch (this.Status)
                {
                    case DiffStatus.Add: return '+';
                    case DiffStatus.Remove: return '-';
                    case DiffStatus.Same: return ' ';
                    default: throw new Exception();
                }
            }
        }
    }
}
