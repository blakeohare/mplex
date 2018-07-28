using System;

namespace Game
{
    internal class BridgeImpl : AbstractBridge
    {
        public override void CreateWindow(int gameWidth, int gameHeight, int pixelWidth, int pixelHeight, string title, int fps)
        {
            throw new NotImplementedException();
        }

        public override void DestroyWindow(int windowId)
        {
            throw new NotImplementedException();
        }

        public override void DrawEllipse(int windowId, int x, int y, int width, int height, int r, int g, int b, int a)
        {
            throw new NotImplementedException();
        }

        public override void DrawRectangle(int windowId, int x, int y, int width, int height, int r, int g, int b, int a)
        {
            throw new NotImplementedException();
        }

        public override void DrawTriangle(int windowId, int x1, int y1, int x2, int y2, int x3, int y3, int r, int g, int b, int a)
        {
            throw new NotImplementedException();
        }

        public override bool IsWindowCreationBlocking()
        {
            throw new NotImplementedException();
        }

        public override int PopEvents(int windowId, int[] intOut, string[] strOut)
        {
            throw new NotImplementedException();
        }

        public override void SetClearColor(int windowId, int r, int g, int b)
        {
            throw new NotImplementedException();
        }

        public override void SetGameLoopCallback(int windowId, Func<int, int> callback)
        {
            throw new NotImplementedException();
        }

        public override void ShowWindow(int windowId)
        {
            throw new NotImplementedException();
        }
    }
}
