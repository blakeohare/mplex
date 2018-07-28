using OpenTK.Graphics.OpenGL;
using System;
using System.Collections.Generic;

namespace Game.Backend
{
    internal class OtkWindow
    {
        public OpenTK.GameWindow Window { get; set; }
        public int ScreenWidth { get; set; }
        public int ScreenHeight { get; set; }
        public int GameWidth { get; set; }
        public int GameHeight { get; set; }
        public string Title { get; set; }
        public int FPS { get; set; }
        public int[] RenderEvents { get; set; }
        public int RenderEventsSize { get; set; }
        public List<int> eventOutInt = new List<int>();
        public List<string> eventOutStr = new List<string>();
        public Func<int, int> GameImplCallback;

        public OtkWindow(string title, int fps, int gameWidth, int gameHeight, int screenWidth, int screenHeight)
        {
            this.RenderEvents = new int[256];
            this.RenderEventsSize = 0;
            this.Title = title;
            this.FPS = fps;
            this.GameWidth = gameWidth;
            this.GameHeight = gameHeight;
            this.ScreenWidth = screenWidth;
            this.ScreenHeight = screenHeight;
            this.GameImplCallback = null;
            this.SetClearColor(0, 0, 0);
        }

        public void Show()
        {
            this.Window = new OpenTK.GameWindow(this.ScreenWidth, this.ScreenHeight, OpenTK.Graphics.GraphicsMode.Default, this.Title, OpenTK.GameWindowFlags.Default);
            this.Window.UpdateFrame += this.GameLoopImpl;
            this.Window.RenderFrame += this.Render;
            this.Window.MouseDown += this.OnMouseDown;
            this.Window.Resize += this.OnResize;
            this.Window.Run(this.FPS, this.FPS);
        }

        private void Startup()
        {
            GL.ClearColor(1f, 1f, 1f, 1f);
            GL.BlendFunc(BlendingFactor.SrcAlpha, BlendingFactor.OneMinusSrcAlpha);
            GL.Enable(EnableCap.Blend);
            GL.Disable(EnableCap.ColorMaterial);
        }

        private void OnResize(object sender, EventArgs e)
        {
            this.ScreenWidth = this.Window.Width;
            this.ScreenHeight = this.Window.Height;


            GL.MatrixMode(MatrixMode.Projection);
            GL.LoadIdentity();
            GL.Ortho(0, this.ScreenWidth, this.ScreenHeight, 0, 10000, -10000);
            GL.Viewport(0, 0, this.ScreenWidth, this.ScreenHeight);
        }

        internal void SetClearColor(int r, int g, int b)
        {
            this.RenderEvents[0] = 1;
            this.RenderEvents[1] = 0;
            this.RenderEvents[2] = 0;
            // width and height get set on each game loop
            this.RenderEvents[5] = r;
            this.RenderEvents[6] = g;
            this.RenderEvents[7] = b;
            this.RenderEvents[8] = 255;
        }

        private void OnMouseDown(object sender, OpenTK.Input.MouseButtonEventArgs e)
        {
            int x = e.X * this.GameWidth / this.ScreenWidth;
            int y = e.Y * this.GameHeight / this.ScreenHeight;
            this.eventOutInt.AddRange(new int[] { 1, x, y, 1, 1, e.Button == OpenTK.Input.MouseButton.Left ? 1 : 0 });
        }

        internal void IncreaseRenderCapacity()
        {
            int[] newBuffer = new int[this.RenderEvents.Length * 2];
            Array.Copy(this.RenderEvents, newBuffer, this.RenderEvents.Length);
            this.RenderEvents = newBuffer;
        }

        private void Render(object sender, OpenTK.FrameEventArgs e)
        {
            GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);
            GL.ClearColor(0f, 0f, 0f, 1f);
            GL.MatrixMode(MatrixMode.Modelview);
            GL.LoadIdentity();
            OpenTkRenderer.render(this.RenderEvents, this.RenderEventsSize, null, this.GameWidth, this.GameHeight, this.ScreenWidth, this.ScreenHeight);
            this.Window.SwapBuffers();
        }

        public void SetCallback(Func<int, int> callback)
        {
            this.GameImplCallback = callback;
        }

        public void GameLoopImpl(object sender, OpenTK.FrameEventArgs e)
        {
            this.RenderEventsSize = 16; // the first 16-wide entry is set to the clear color
            this.RenderEvents[3] = this.GameWidth;
            this.RenderEvents[4] = this.GameHeight;

            this.GameImplCallback?.Invoke(0);

        }

        public int GetEvents(List<int> intOut, List<string> stringOut)
        {
            return 0;
        }
    }
}
