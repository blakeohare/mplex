using MPlex.Drawing;

namespace MPlexTestRunner
{
    class Program
    {
        static void Main(string[] args)
        {
            Bitmap bmp = new Bitmap(@"C:\Users\Blake\Desktop\test_image.png");
            bmp.Save(@"C:\Users\Blake\Desktop\test_image2.png");
        }
    }
}
