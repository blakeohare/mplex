using System;
using System.Collections.Generic;

namespace Drawing
{
    internal class BridgeImpl : AbstractBridge
    {
        public override void CreateBitmapFile(Dictionary<int, object> nativeData, string path)
        {
            throw new NotImplementedException();
        }

        public override void CreateBitmapSize(Dictionary<int, object> nativeData, int width, int height)
        {
            throw new NotImplementedException();
        }

        public override void DrawBitmap(Dictionary<int, object> pixelNativeData, Dictionary<int, object> bmp2NativeData, Dictionary<int, object> pixel2NativeData, int x, int y)
        {
            throw new NotImplementedException();
        }

        public override void DrawRectangle(Dictionary<int, object> nativeData, int x, int y, int r, int g, int b, int a)
        {
            throw new NotImplementedException();
        }

        public override void FlushBitmapEditSession(Dictionary<int, object> nativeData, Dictionary<int, object> bmpNativeData)
        {
            throw new NotImplementedException();
        }

        public override void GetBitmapEditSession(Dictionary<int, object> nativeData, Dictionary<int, object> bmpNativeData)
        {
            throw new NotImplementedException();
        }

        public override void SaveBitmap(Dictionary<int, object> nativeData, string path)
        {
            throw new NotImplementedException();
        }
    }
}
