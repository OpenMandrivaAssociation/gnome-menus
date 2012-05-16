%define major		0
%define api		3
%define gir_major	3.0
%define libname		%mklibname gnome-menu %{api} %{major}
%define girname		%mklibname gmenu-gir %{gir_major}
%define develname	%mklibname -d gnome-menu

Summary:	GNOME menu library
Name:		gnome-menus
Version:	3.4.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
# (fc) 2.16.0-2mdv unclutter preferences/settings menu
Patch1:		gnome-menus-3.0.0-uncluttermenu.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(python)

Requires:	python-%{name}
Obsoletes:	gnome-menus2

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
Obsoletes:	python-gnome-menus2

%description -n python-%{name}
Python module to access XDG menu.

%package -n %{libname}
Group:		System/Libraries
Summary:	GNOME menu library
Conflicts:	gir-repository < 0.6.5-8

%description -n %{libname}
This package contains the shared libraries of %{name}.

%package -n %{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface library for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Group:		Development/C
Summary:	GNOME menu library development files
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gnome-menu2-devel
Conflicts:	gir-repository < 0.6.5-8

%description -n %{develname}
This package contains the development libraries of %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make LIBS='-lgmodule-2.0'

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

%files -n %{girname}
%{_libdir}/girepository-1.0/GMenu-%{gir_major}.typelib

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GMenu-%{gir_major}.gir

