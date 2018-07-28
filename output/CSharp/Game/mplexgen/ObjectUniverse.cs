using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Game
{
    internal class ObjectUniverseItem
    {
        private static int idAlloc = 1;
        internal int ID { get; private set; }

        public ObjectUniverseItem(int id)
        {
            this.ID = id;
        }

        // When an ObjectUniverseItem gets GC'd, automatically remove it from the lookup
        ~ObjectUniverseItem()
        {
            objects.Remove(this.ID);
        }

        // Only call this from native code.
        internal static int RegisterObject(object obj)
        {
            int id = idAlloc++;
            objects[id] = obj;
            return id;
        }

        internal static Dictionary<int, object> objects = new Dictionary<int, object>();
    }
}
