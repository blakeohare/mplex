namespace Drawing
{
    internal abstract class AbstractBridge
    {
        public abstract void CreateBitmapFile(System.Collections.Generic.Dictionary<int, object> nativeData, string path);
        public abstract void CreateBitmapSize(System.Collections.Generic.Dictionary<int, object> nativeData, int width, int height);
        public abstract void SaveBitmap(System.Collections.Generic.Dictionary<int, object> nativeData, string path);
        public abstract void GetBitmapEditSession(System.Collections.Generic.Dictionary<int, object> nativeData, System.Collections.Generic.Dictionary<int, object> bmpNativeData);
        public abstract void FlushBitmapEditSession(System.Collections.Generic.Dictionary<int, object> nativeData, System.Collections.Generic.Dictionary<int, object> bmpNativeData);
        public abstract void DrawRectangle(System.Collections.Generic.Dictionary<int, object> nativeData, int x, int y, int r, int g, int b, int a);
        public abstract void DrawBitmap(System.Collections.Generic.Dictionary<int, object> pixelNativeData, System.Collections.Generic.Dictionary<int, object> bmp2NativeData, System.Collections.Generic.Dictionary<int, object> pixel2NativeData, int x, int y);
    }
}

