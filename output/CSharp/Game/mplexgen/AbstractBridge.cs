namespace Game
{
    internal abstract class AbstractBridge
    {
        public abstract int CreateWindow(int gameWidth, int gameHeight, int pixelWidth, int pixelHeight, string title, int fps);
        public abstract void ShowWindow(int windowId);
        public abstract bool IsWindowCreationBlocking();
        public abstract void SetGameLoopCallback(int windowId, System.Func<int, int> callback);
        public abstract void DestroyWindow(int windowId);
        public abstract void SetClearColor(int windowId, int r, int g, int b);
        public abstract void DrawRectangle(int windowId, int x, int y, int width, int height, int r, int g, int b, int a);
        public abstract void DrawEllipse(int windowId, int x, int y, int width, int height, int r, int g, int b, int a);
        public abstract void DrawTriangle(int windowId, int x1, int y1, int x2, int y2, int x3, int y3, int r, int g, int b, int a);
        public abstract int PopEvents(int windowId, int[] intOut, string[] strOut);
    }
}

