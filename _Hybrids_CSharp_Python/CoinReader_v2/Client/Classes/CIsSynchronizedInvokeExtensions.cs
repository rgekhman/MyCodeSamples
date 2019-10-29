using System;
using System.ComponentModel;

namespace Client.Classes
{
    public static class CIsSynchronizedInvokeExtensions
    {
        public static void InvokeEx<T>(this T @this, Action<T> action) where T : ISynchronizeInvoke
        {
            try { 
                if (@this.InvokeRequired)
                {
                    @this.Invoke(action, new object[] { @this });
                }
                else
                {
                    action(@this);
                }
            }
            catch
            {

            }
        }
    }
}
