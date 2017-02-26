using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace MvvmDemo
{
    public class Genre : NotifyPropertyBase
    {
        private int _genreId;
        private string _name;
        private string _description;
        private List<Album> _albums;

        public int GenreId
        {
            get { return _genreId; }
            set
            {
                if (value == _genreId) return;
                _genreId = value;
                OnPropertyChanged("GenreId");
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

        public string Description
        {
            get { return _description; }
            set
            {
                if (value == _description) return;
                _description = value;
                OnPropertyChanged("Description");
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
