using MPlex.Native.Common;

namespace MPlex.Native.Drawing
{
    public static class Public
    {
        public const int BITMAP_WIDTH = 0;
        public const int BITMAP_HEIGHT = 1;
        public const int BITMAP_BMP = 2;
        public const int BITMAP_PIXELS = 3;

        public static NativeBridge Bridge { get; private set; } = new DrawingNativeBridge();
    }
}
