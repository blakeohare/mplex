using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Game
{
    public sealed class Renderer2D
    {
        private readonly int windowId;
        private readonly ObjectUniverseItem windowHandle;

        internal Renderer2D(ObjectUniverseItem windowHandle)
        {
            this.windowHandle = windowHandle;
            this.windowId = windowHandle.ID;
        }

        public Renderer2D DrawRectangle(int x, int y, int width, int height, int r, int g, int b, int a)
        {
            Game.Backend.BridgeImpl.INSTANCE.DrawRectangle(this.windowId, x, y, width, height, r, g, b, a);
            return this;
        }

        public Renderer2D DrawRectangle(int x, int y, int width, int height, int r, int g, int b)
        {
            Game.Backend.BridgeImpl.INSTANCE.DrawRectangle(this.windowId, x, y, width, height, r, g, b, 255);
            return this;
        }
    }
}
