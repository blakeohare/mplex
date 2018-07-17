using MPlex.Native.Common;
using System.Collections.Generic;

namespace MPlex.Native.Drawing
{
    internal class DrawingNativeBridge : NativeBridge
    {
        // TODO: autogenerate this class with a common language metadata file.

        public override int Send(string cmd, params object[] args)
        {
            switch (cmd)
            {
                case "create-bitmap-file": return Methods.CreateBitmapPath((Dictionary<int, object>)args[0], (string)args[1]);
                case "create-bitmap-size": return Methods.CreateBitmapSize((Dictionary<int, object>)args[0], (int)args[1], (int)args[2]);
                case "save-bitmap": return Methods.SaveBitmap((Dictionary<int, object>)args[0], (string)args[1]);
            }
            return SetError(-1, "Unknown command.");
        }
    }
}
