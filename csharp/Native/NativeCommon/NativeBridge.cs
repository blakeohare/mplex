namespace MPlex.Native.Common
{
    public abstract class NativeBridge
    {
        public virtual int Send(string cmd, params object[] args) { return -1; }
        public string ErrorMessage { get; set; }

        public int SetError(int id, string message)
        {
            this.ErrorMessage = message;
            return id;
        }
    }
}
