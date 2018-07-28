namespace Diff
{
    internal abstract class AbstractBridge
    {
        public abstract void DiffText(string[] text1, int text1Length, string[] text2, int text2Length, System.Collections.Generic.List<string> textOut, System.Collections.Generic.List<int> changeOut);
    }
}

