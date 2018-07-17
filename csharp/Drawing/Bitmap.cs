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
            int sc = bridge.Send("create-bitmap-file", this.nativeData, path);
            if (sc == 0)
            {
                this.Width = (int)this.nativeData[Public.BITMAP_WIDTH];
                this.Height = (int)this.nativeData[Public.BITMAP_HEIGHT];
            }
            else
            {
                throw new Exception(bridge.ErrorMessage);
            }
        }

        public Bitmap(int width, int height)
        {
            int sc = bridge.Send("create-bitmap-size", this.nativeData, width, height);
            if (sc == 0)
            {
                this.Width = width;
                this.Height = height;
            }
            else
            {
                throw new Exception(bridge.ErrorMessage);
            }
        }

        public void Save(string path)
        {
            int sc = bridge.Send("save-bitmap", this.nativeData, path);
            if (sc != 0) throw new Exception(bridge.ErrorMessage);
        }
    }
}
