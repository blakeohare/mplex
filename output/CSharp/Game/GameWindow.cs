namespace Game
{
    public sealed class GameWindow
    {
        internal ObjectUniverseItem NativeWindow { get; private set; }
        private int fps;
        private string title;
        private int gameWidth;
        private int gameHeight;
        private int screenWidth;
        private int screenHeight;
        private readonly AbstractGame gameCallbacks;
        private readonly Renderer2D renderer;

        public GameWindow(string title, int fps, AbstractGame game, int gameWidth, int gameHeight)
            : this(title, fps, game, gameWidth, gameHeight, gameWidth, gameHeight)
        { }

        public GameWindow(string title, int fps, AbstractGame game, int gameWidth, int gameHeight, int screenWidth, int screenHeight)
        {
            this.gameCallbacks = game;
            this.title = title;
            this.fps = fps;
            this.gameWidth = gameWidth;
            this.gameHeight = gameHeight;
            this.screenWidth = screenWidth;
            this.screenHeight = screenHeight;
            int windowId = Game.Backend.BridgeImpl.INSTANCE.CreateWindow(gameWidth, gameHeight, screenWidth, screenHeight, title, fps);
            this.NativeWindow = new ObjectUniverseItem(windowId);
            this.renderer = new Renderer2D(this.NativeWindow);
            Game.Backend.BridgeImpl.INSTANCE.SetGameLoopCallback(windowId, this.GameLoopCallback);
        }
        
        private int GameLoopCallback(int ignored)
        {
            this.gameCallbacks.Update();
            this.gameCallbacks.Render(this.renderer);
            return 0;
        }

        public GameWindow Show()
        {
            Game.Backend.BridgeImpl.INSTANCE.ShowWindow(this.NativeWindow.ID);
            return this;
        }

        public GameWindow Close()
        {
            Game.Backend.BridgeImpl.INSTANCE.DestroyWindow(this.NativeWindow.ID);
            return this;
        }

        public GameWindow SetClearColor(int r, int g, int b)
        {
            Game.Backend.BridgeImpl.INSTANCE.SetClearColor(this.NativeWindow.ID, r, g, b);
            return this;
        }
    }
}
