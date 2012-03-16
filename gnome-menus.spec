%define major	0
%define api		3
%define libname		%mklibname gnome-menu %{api} %{major}
%define gi_name		%mklibname gmenu-gir %{api}.0
%define develname	%mklibname -d gnome-menu

%define url_ver %(echo %{version} | cut -d. -f1,2)

Summary:	GNOME menu library
Name:		gnome-menus
Version:	3.2.0.1
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
# (fc) 2.16.0-2mdv unclutter preferences/settings menu
Patch1:		gnome-menus-3.0.0-uncluttermenu.patch
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.29.15
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(python)

Requires:	python-%{name}

%description
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:
http://www.freedesktop.org/Standards/menu-spec

Also contained here are the GNOME menu layout configuration files,
.directory files and assorted menu related utility programs.

%package -n python-%{name}
Group:		Development/Python
Summary:	Module to access XDG menu
Requires:	python-gi

%description -n python-%{name}
Python module to access XDG menu.

%package -n %{libname}
Group:		System/Libraries
Summary:	GNOME menu library
Conflicts:	gir-repository < 0.6.5-8

%description -n %{libname}
This package contains the shared libraries of %{name}.

%package -n %{gi_name}
Group:		System/Libraries
Summary:	GObject Introspection interface library for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{gi_name}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Group:		Development/C
Summary:	GNOME menu library development files
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d gnome-menu 2
Conflicts:	gir-repository < 0.6.5-8

%description -n %{develname}
This package contains the development libraries of %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

find %{buildroot} -name *.la | xargs rm

%find_lang %{name}-3.0

mkdir -p %{buildroot}%{_sysconfdir}/xdg/gnome
mv %{buildroot}%{_sysconfdir}/xdg/menus %{buildroot}%{_sysconfdir}/xdg/gnome

chmod 755 %{buildroot}%{_libdir}/python*/site-packages/GMenuSimpleEditor/*.py

%files -f %{name}-3.0.lang
%doc README NEWS HACKING AUTHORS ChangeLog
%{_datadir}/desktop-directories/*
%dir %{_sysconfdir}/xdg/gnome
%dir %{_sysconfdir}/xdg/gnome/menus
%config(noreplace) %{_sysconfdir}/xdg/gnome/menus/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}

%files -n python-%{name}
%{_libdir}/python*/site-packages/*

%files -n %{libname}
%{_libdir}/libgnome-menu-%{api}.so.%{major}*

%files -n %{gi_name}
%{_libdir}/girepository-1.0/GMenu-%{api}.0.typelib

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GMenu-%{api}.0.gir
