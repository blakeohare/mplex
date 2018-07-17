using System;
using System.Collections.Generic;
using MPlex.Native.Common;
using MPlex.Native.Drawing;

namespace MPlex.Drawing
{
    public class Bitmap
    {
        public int Width { get; private set; }
        public int Height { get; private set; }
        private Dictionary<int, object> nativeData = new Dictionary<int, object>();

        private static readonly NativeBridge bridge = Public.Bridge;

        public Bitmap(string path)
        {
            bridge.SendOrThrow("create-bitmap-file", this.nativeData, path);
            this.Width = (int)this.nativeData[Public.BITMAP_WIDTH];
            this.Height = (int)this.nativeData[Public.BITMAP_HEIGHT];
        }

        public Bitmap(int width, int height)
        {
            bridge.SendOrThrow("create-bitmap-size", this.nativeData, width, height);
            this.Width = width;
            this.Height = height;
        }

        public void Save(string path)
        {
            bridge.SendOrThrow("save-bitmap", this.nativeData, path);
        }
    }
}
