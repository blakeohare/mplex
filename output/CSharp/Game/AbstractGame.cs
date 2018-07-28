using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Game
{
    public abstract class AbstractGame
    {
        public AbstractGame() { }

        public virtual void OnMouseMove(int x, int y) { }
        public virtual void OnMouseLeftDown(int x, int y) { }
        public virtual void OnMouseLeftUp(int x, int y) { }
        public virtual void OnMouseRightDown(int x, int y) { }
        public virtual void OnMouseRightUp(int x, int y) { }
        public virtual void OnKeyDown(string key) { }
        public virtual void OnKeyUp(string key) { }
        public virtual void Update() { }
        public virtual void Render(Renderer2D renderer) { }
    }
}
