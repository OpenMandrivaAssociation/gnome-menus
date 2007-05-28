%define major 2
%define libname %mklibname gnome-menu %major

Summary: GNOME menu library
Name: gnome-menus
Version: 2.18.2
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
# (fc) 2.15.91-2mdv grab translation from menu-messages if not in upstream file
Patch0: gnome-menus-2.15.91-l10n.patch
# (fc) 2.16.0-2mdv unclutter preferences/settings menu
Patch1: gnome-menus-2.18.0-uncluttermenu.patch
License: GPL/LGPL
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glib2-devel >= 2.5.6
BuildRequires: gamin-devel
BuildRequires: perl-XML-Parser
BuildRequires: libpython-devel
Requires: python-%{name}

%description
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:
http://www.freedesktop.org/Standards/menu-spec

Also contained here are the GNOME menu layout configuration files,
.directory files and assorted menu related utility programs.

%package -n python-%{name}
Group: Development/Python
Summary: Module to access XDG menu

%description -n python-%{name}
Python module to access XDG menu.

%package -n %libname
Group: System/Libraries
Summary: GNOME menu library

%description -n %libname
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:
http://www.freedesktop.org/Standards/menu-spec

%package -n %libname-devel
Group: Development/C
Summary: GNOME menu library development files
Requires: %libname = %version
Provides: libgnome-menu-devel = %version-%release
Provides: %{name}-devel = %{version}-%{release}

%description -n %libname-devel
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:
http://www.freedesktop.org/Standards/menu-spec

%prep
%setup -q
%patch0 -p1 -b .l10n
%patch1 -p1 -b .uncluttermenu

%build
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/xdg/gnome
mv $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus $RPM_BUILD_ROOT%{_sysconfdir}/xdg/gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -f %name.lang
%defattr(-,root,root)
%doc README NEWS HACKING AUTHORS ChangeLog
%_datadir/desktop-directories
%dir %_sysconfdir/xdg/gnome
%dir %_sysconfdir/xdg/gnome/menus
%config(noreplace) %_sysconfdir/xdg/gnome/menus/*
%_bindir/*
%_datadir/applications/*
%_datadir/%{name}

%files -n python-%{name}
%defattr(-,root,root)
%_libdir/python*/site-packages/*

%files -n %libname
%defattr(-,root,root)
%_libdir/libgnome-menu.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/lib*.so
%_libdir/lib*.la
%_libdir/lib*.a
%_includedir/gnome-menus/
%_libdir/pkgconfig/*.pc


