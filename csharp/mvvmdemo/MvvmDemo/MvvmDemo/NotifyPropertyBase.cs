using System.ComponentModel;

namespace MvvmDemo
{
    public class NotifyPropertyBase : INotifyPropertyChanged
    {
        #region INotifyPropertyChanged
        public void OnPropertyChanged(string propertyName)
        {
            if (PropertyChanged != null)
            {
                PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
            }
        }
        public event PropertyChangedEventHandler PropertyChanged;
        #endregion
    }
}
