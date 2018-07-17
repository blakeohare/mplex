using System;
using System.Collections.Generic;

namespace MPlex.Native.Drawing
{
    internal static class Methods
    {
        internal static int CreateBitmapFile(Dictionary<int, object> nativeData, string path)
        {
            if (!System.IO.File.Exists(path)) return Public.Bridge.SetError(1, "File does not exist.");
            System.Drawing.Bitmap bmp;
            try
            {
                bmp = new System.Drawing.Bitmap(path);
            }
            catch (Exception)
            {
                return Public.Bridge.SetError(1, "Invalid image file.");
            }
            nativeData[Public.BITMAP_BMP] = bmp;
            nativeData[Public.BITMAP_WIDTH] = bmp.Width;
            nativeData[Public.BITMAP_HEIGHT] = bmp.Height;
            nativeData[Public.BITMAP_PIXELS] = null;

            return 0;
        }

        internal static int CreateBitmapSize(Dictionary<int, object> nativeData, int width, int height)
        {
            if (width < 1 || height < 1 || width > 5000 || height > 5000)
                return Public.Bridge.SetError(1, "Image size is invalid.");

            System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(width, height);

            nativeData[Public.BITMAP_BMP] = bmp;
            nativeData[Public.BITMAP_WIDTH] = width;
            nativeData[Public.BITMAP_HEIGHT] = height;
            nativeData[Public.BITMAP_PIXELS] = null;

            return 0;
        }

        internal static int SaveBitmap(Dictionary<int, object> nativeData, string path)
        {
            System.Drawing.Bitmap bmp = (System.Drawing.Bitmap)nativeData[Public.BITMAP_BMP];
            try
            {
                bmp.Save(path);
            }
            catch (Exception)
            {
                return Public.Bridge.SetError(1, "Could not write to file.");
            }
            return 0;
        }
    }
}
