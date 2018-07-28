using System;
using System.Collections.Generic;

namespace Diff.Backend
{
    internal class BridgeImpl : AbstractBridge
    {
        internal static readonly BridgeImpl INSTANCE = new BridgeImpl();

        public override void DiffText(string[] text1, int text1Length, string[] text2, int text2Length, List<string> textOut, List<int> changeOut)
        {
            PastelGeneratedNamespace.FunctionWrapper.GenerateTextDiff(text1, text1Length, text2, text2Length, textOut, changeOut);
        }
    }
}
