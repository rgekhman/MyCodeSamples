using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _0.Pre_test_questions
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 1, j = 10;
            do
            {
                if (i++ > --j) /* Line 4 */
                {
                    continue;
                }
            } while (i < 5);

            // i = 5, j = 6

            Console.WriteLine(String.Format("i={0}, j={1}", i, j));
            Console.ReadLine();
        }
    }
}
