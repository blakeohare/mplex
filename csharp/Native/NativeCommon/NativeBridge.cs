namespace MPlex.Native.Common
{
    public abstract class NativeBridge
    {
        public virtual int Send(string cmd, params object[] args) { return -1; }

        public int SendOrThrow(string cmd, params object[] args)
        {
            int sc = this.Send(cmd, args);
            if (sc != 0)
            {
                throw new System.Exception(this.ErrorMessage);
            }
            return sc;
        }

        public string ErrorMessage { get; set; }

        public int SetError(int id, string message)
        {
            this.ErrorMessage = message;
            return id;
        }
    }
}
