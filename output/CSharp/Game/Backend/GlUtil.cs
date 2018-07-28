using OpenTK.Graphics.OpenGL;

namespace Game.Backend
{
    class GlUtil
    {
        public static void PrepareRenderPipeline()
        {
            GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);
            GL.ClearColor(0f, 0f, 0f, 1f);
            GL.MatrixMode(MatrixMode.Modelview);
            GL.LoadIdentity();
        }
    }
}
