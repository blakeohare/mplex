using System;

namespace Game.Backend
{
    internal class BridgeImpl : Game.AbstractBridge
    {
        internal static readonly BridgeImpl INSTANCE = new BridgeImpl();
        private OtkWindow windowCache;
        private int windowCacheId = 0;
        private OtkWindow GetWindow(int id)
        {
            if (windowCacheId == id) return windowCache;
            if (!ObjectUniverseItem.objects.ContainsKey(id)) return null;
            windowCache = (OtkWindow)ObjectUniverseItem.objects[id];
            windowCacheId = id;
            return windowCache;
        }

        public override int CreateWindow(int gameWidth, int gameHeight, int pixelWidth, int pixelHeight, string title, int fps)
        {
            object window = new OtkWindow(title, fps, gameWidth, gameHeight, pixelWidth, pixelHeight);
            return ObjectUniverseItem.RegisterObject(window);
        }

        public override void DestroyWindow(int windowId)
        {
            OtkWindow window = windowCacheId == windowId ? windowCache : GetWindow(windowId);
            throw new NotImplementedException();
        }

        public override void DrawEllipse(int windowId, int x, int y, int width, int height, int r, int g, int b, int a)
        {
            OtkWindow window = windowCacheId == windowId ? windowCache : GetWindow(windowId);
            int[] renderEvents = window.RenderEvents;
            if (window.RenderEventsSize == renderEvents.Length) window.IncreaseRenderCapacity();
            int renderSize = window.RenderEventsSize;
            renderEvents[renderSize] = 2;
            renderEvents[renderSize | 1] = x;
            renderEvents[renderSize | 2] = y;
            renderEvents[renderSize | 3] = width;
            renderEvents[renderSize | 4] = height;
            renderEvents[renderSize | 5] = r;
            renderEvents[renderSize | 6] = g;
            renderEvents[renderSize | 7] = b;
            renderEvents[renderSize | 8] = a;
            window.RenderEventsSize += 16;
        }

        public override void DrawRectangle(int windowId, int x, int y, int width, int height, int r, int g, int b, int a)
        {
            OtkWindow window = windowCacheId == windowId ? windowCache : GetWindow(windowId);
            int[] renderEvents = window.RenderEvents;
            if (window.RenderEventsSize == renderEvents.Length) window.IncreaseRenderCapacity();
            int renderSize = window.RenderEventsSize;
            renderEvents[renderSize] = 1;
            renderEvents[renderSize | 1] = x;
            renderEvents[renderSize | 2] = y;
            renderEvents[renderSize | 3] = width;
            renderEvents[renderSize | 4] = height;
            renderEvents[renderSize | 5] = r;
            renderEvents[renderSize | 6] = g;
            renderEvents[renderSize | 7] = b;
            renderEvents[renderSize | 8] = a;
            window.RenderEventsSize += 16;
        }

        public override void DrawTriangle(int windowId, int x1, int y1, int x2, int y2, int x3, int y3, int r, int g, int b, int a)
        {
            throw new NotImplementedException();
        }

        public override bool IsWindowCreationBlocking()
        {
            return false;
        }

        public override int PopEvents(int windowId, int[] intOut, string[] strOut)
        {
            throw new NotImplementedException();
        }

        public override void SetClearColor(int windowId, int r, int g, int b)
        {
            OtkWindow window = windowCacheId == windowId ? windowCache : GetWindow(windowId);
            window.SetClearColor(r, g, b);
        }

        public override void SetGameLoopCallback(int windowId, Func<int, int> callback)
        {
            OtkWindow window = windowCacheId == windowId ? windowCache : GetWindow(windowId);
            window.SetCallback(callback);
        }

        public override void ShowWindow(int windowId)
        {
            OtkWindow window = windowCacheId == windowId ? windowCache : GetWindow(windowId);
            window.Show();
        }
    }
}
