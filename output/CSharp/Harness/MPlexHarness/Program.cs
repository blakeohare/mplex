using Game;

namespace MPlexHarness
{
    class Program
    {
        private class MyGame : AbstractGame
        {
            private int x = 0;
            private int y = 0;

            public override void Update()
            {
                this.x = (this.x + 3) % 640;
                this.y = (this.y + 2) % 480;
            }

            public override void OnMouseLeftDown(int x, int y)
            {
                this.x = x;
                this.y = y;
            }

            public override void Render(Renderer2D renderer)
            {
                renderer.DrawRectangle(this.x, this.y, 100, 200, 0, 128, 255);
            }
        }

        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello, World!");

            GameWindow gameWindow = new GameWindow("Test Game", 60, new MyGame(), 640, 480);
            gameWindow.Show();
        }
    }
}
