using Diff;

namespace MPlexHarness
{
    class DiffRunner
    {
        public static void Run()
        {
            string left = string.Join("\n", new string[]
            {
                "This",
                "is",
                "a",
                "test"
            });

            string right = string.Join("\n", new string[]
            {
                "This",
                "isn't",
                "a",
                "good",
                "test"
            });

            DiffEngine engine = new DiffEngine();
            DiffResult result = engine.Diff(left, right);
            foreach (DiffLine line in result.Lines)
            {
                System.Console.WriteLine(line.DiffChar + " " + line.Value);
            }
        }
    }
}
