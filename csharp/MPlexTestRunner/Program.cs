using MPlex.Drawing;

namespace MPlexTestRunner
{
    class Program
    {
        static void Main(string[] args)
        {
            Bitmap bmp = new Bitmap(@"C:\Users\Blake\Desktop\twitter banner.jpg");
            bmp.Save(@"C:\Users\Blake\Desktop\tb.jpg");
        }
    }
}
