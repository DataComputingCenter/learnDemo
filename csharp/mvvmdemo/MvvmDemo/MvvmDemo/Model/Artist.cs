using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace MvvmDemo
{
    public class Artist : NotifyPropertyBase
    {
        private int _artistId;
        private string _name;
        private List<Album> _albums;

        public int ArtistId
        {
            get { return _artistId; }
            set
            {
                if (value == _artistId) return;
                _artistId = value;
                OnPropertyChanged("ArtistId");
            }
        }

        public string Name
        {
            get { return _name; }
            set
            {
                if (value == _name) return;
                _name = value;
                OnPropertyChanged("Name");
            }
        }

        public List<Album> Albums
        {
            get { return _albums; }
            set
            {
                if (Equals(value, _albums)) return;
                _albums = value;
                OnPropertyChanged("Albums");
            }
        }
    }
}
