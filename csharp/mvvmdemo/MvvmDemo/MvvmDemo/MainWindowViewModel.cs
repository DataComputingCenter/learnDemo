using System;
using System.Collections.ObjectModel;
using System.Linq;
using System.Windows.Input;

namespace MvvmDemo
{
    public class MainWindowViewModel : NotifyPropertyBase
    {
        private ICommand _createAlbum;
        private ICommand _deleteAlbum;
        public Album _album;
        public ObservableCollection<Album> Albums
        {
            get
            {
                return SampleData.Albums;
            }
            set
            {
                SampleData.Albums = value;
                OnPropertyChanged("Albums");
            }
        }
        public Album Album
        {
            get
            {
                return _album;
            }
            set
            {
                _album = value;
                OnPropertyChanged("Album");
            }
        }
        public MainWindowViewModel()
        {
            SampleData.Seed();
        }
        public ICommand CreateAlbum
        {
            get
            {
                return this._createAlbum ?? (_createAlbum = new SimpleCommand { CanExecuteDelegate = x => true, ExecuteDelegate = x => this.CreateAlbumEvent(x) });

            }
        }
        public ICommand DeleteAlbum
        {
            get
            {
                return this._deleteAlbum ?? (_deleteAlbum = new SimpleCommand { CanExecuteDelegate = x => true, ExecuteDelegate = x => this.DeleteAlbumEvent(x) });

            }
        }

        private void DeleteAlbumEvent(object x)
        {
            Albums.Remove(Album);
        }

        private void CreateAlbumEvent(object x)
        {
            Album album = new Album { Title = "Title" + DateTime.Now.ToString("yyyyMMddHHmmss"), Genre = SampleData.Genres.First(g => g.Name == "Rock"), Price = 8.99M, Artist = SampleData.Artists.First(a => a.Name == "Men At Work"), AlbumArtUrl = "/Content/Images/placeholder.gif" };
            this.Albums.Add(album);
            Album = album;
        }

        // 
    }
}
