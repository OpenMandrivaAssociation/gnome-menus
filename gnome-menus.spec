%define major	0
%define api	3
%define gimajor	3.0
%define libname	%mklibname gnome-menu %{api} %{major}
%define girname	%mklibname gmenu-gir %{gimajor}
%define devname	%mklibname -d gnome-menu

Summary:	GNOME menu library
Name:		gnome-menus
Version:	3.6.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz
# (fc) 2.16.0-2mdv unclutter preferences/settings menu
Patch1:		gnome-menus-3.0.0-uncluttermenu.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(python)

Requires:	python-%{name}
Obsoletes:	gnome-menus2 < 3.4

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
Obsoletes:	python-gnome-menus2 < 3.4

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

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	GNOME menu library development files
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gnome-menu2-devel < 3.4
Conflicts:	gir-repository < 0.6.5-8

%description -n %{devname}
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
%{_libdir}/girepository-1.0/GMenu-%{gimajor}.typelib

%files -n %{devname}
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GMenu-%{gimajor}.gir

%changelog
* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Wed May 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 799221
- update to new version 3.4.2

* Thu Apr 26 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.0-1
+ Revision: 793678
- new version 3.4.0

* Tue Apr 03 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0.1-3
+ Revision: 788914
- rebuild to obsolete gnome-menus2 conflicting pkgs

* Fri Mar 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0.1-2
+ Revision: 785402
- rebuild to pull in python-gi instead of python-gobject

* Thu Nov 17 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0.1-1
+ Revision: 731477
- resync'd spec with mga
- cleaned up spec
- removed mkrel
- dropped back to 3.2.0.1 from 3.3.1

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.5-2
+ Revision: 664874
- mass rebuild

* Wed Nov 17 2010 Götz Waschk <waschk@mandriva.org> 2.30.5-1mdv2011.0
+ Revision: 598368
- update to new version 2.30.5

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 2.30.4-2mdv2011.0
+ Revision: 592123
- rebuild for py2.7

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.30.4-1mdv2011.0
+ Revision: 581285
- update to new version 2.30.4

* Tue Sep 14 2010 Götz Waschk <waschk@mandriva.org> 2.30.3-1mdv2011.0
+ Revision: 578281
- update to new version 2.30.3

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-3mdv2011.0
+ Revision: 577934
- rebuild for new g-i

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 2.30.2-2mdv2011.0
+ Revision: 563771
- rebuild for new gobject-introspection

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 550680
- update to new version 2.30.2

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528960
- update to new version 2.30.0

* Mon Mar 08 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-2mdv2010.1
+ Revision: 516563
- add conflict with old gir-repositry

* Mon Mar 08 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 515910
- new version
- add gobject introspection support

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509639
- update to new version 2.29.91

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 497394
- update to new version 2.29.6

* Thu Oct 01 2009 Götz Waschk <waschk@mandriva.org> 2.28.0.1-1mdv2010.0
+ Revision: 452127
- new version
- drop merged patches 2,3

* Tue Sep 29 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.0-2mdv2010.0
+ Revision: 450967
- Fix buildrequires
- Redo patch2
- Patch3: ensure name is correctly filled for comparison

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446788
- update to new version 2.28.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437400
- new version
- rediff patch 0

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 402529
- update to new version 2.27.5

* Wed Jul 15 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 396381
- new version
- rediff patch 0

* Tue Jun 30 2009 Götz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 390823
- new version
- update patch 2

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366937
- update to new version 2.26.1

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356295
- update to new version 2.26.0

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341226
- update to new version 2.25.91

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 2.25.5-4mdv2009.1
+ Revision: 333704
- link against python

* Mon Jan 19 2009 Götz Waschk <waschk@mandriva.org> 2.25.5-3mdv2009.1
+ Revision: 331455
- update to new version 2.25.5

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 2.25.2-3mdv2009.1
+ Revision: 319164
- rebuild with python 2.6

* Thu Dec 11 2008 Frederic Crozat <fcrozat@mandriva.com> 2.25.2-2mdv2009.1
+ Revision: 313355
- Update patch0 to not try to translate empty fields (Mdv bug #44964)

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 309073
- update to new version 2.25.2

* Tue Nov 25 2008 Götz Waschk <waschk@mandriva.org> 2.24.2-1mdv2009.1
+ Revision: 306601
- update to new version 2.24.2

* Wed Oct 22 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 296437
- update to new version 2.24.1

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287270
- new version

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282795
- new version

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278666
- new version

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263624
- new version

* Tue Jul 22 2008 Götz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 240982
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 231027
- new version
- rediff patch 1
- update license
- update buildrequires

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 Götz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211657
- new version
- rediff patch 1
- drop patch 2 (different fix upstream)

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192479
- new version

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183844
- new version

* Tue Feb 26 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175411
- new version

* Mon Feb 11 2008 Götz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165441
- fix rpmlint errors
- new version

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159049
- new version

* Tue Jan 15 2008 Götz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 152032
- new version
- drop patch 3

* Tue Jan 08 2008 Götz Waschk <waschk@mandriva.org> 2.21.3-2mdv2008.1
+ Revision: 146365
- fix build with new gio

* Sun Dec 23 2007 Götz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 137344
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 Götz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 108581
- new version

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98657
- new version

* Wed Oct 03 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-3mdv2008.0
+ Revision: 94945
- Update patch1 to no hide GNOME;Settings;System (Mdv bug #34269)

* Fri Sep 28 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-2mdv2008.0
+ Revision: 93618
- Resync with desktop-common-data

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89342
- new version

* Mon Sep 17 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.92-3mdv2008.0
+ Revision: 89162
- Patch2: fix separator handling (Mdv bug #32867)

* Mon Sep 10 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.92-2mdv2008.0
+ Revision: 84236
- Update patch1 to fill administration menu with System Tools menu content

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 79445
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 63211
- new version
- new devel name

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 56699
- new version

* Sun Jul 08 2007 Götz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 49937
- new version

* Sun Jun 17 2007 Götz Waschk <waschk@mandriva.org> 2.19.4-1mdv2008.0
+ Revision: 40592
- new version

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 2.19.3-2mdv2008.0
+ Revision: 36166
- rebuild with correct optflags

  + Götz Waschk <waschk@mandriva.org>
    - new version

* Mon May 28 2007 Götz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 32114
- new version


* Wed Mar 14 2007 Frederic Crozat <fcrozat@mandriva.com> 2.18.0-2mdv2007.1
+ Revision: 143667
- Update patch1 to correctly find all GNOME preferences dialogs

* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142066
- new version

* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 126137
- new version
- rediff the patch

* Thu Feb 15 2007 Frederic Crozat <fcrozat@mandriva.com> 2.17.91-1mdv2007.1
+ Revision: 121383
-Release 2.17.91
-update patch1 to show preferences/admin submenus and only GNOME settings applications

* Wed Jan 10 2007 Götz Waschk <waschk@mandriva.org> 2.17.5-1mdv2007.1
+ Revision: 106900
- new version
- update patch 1

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-2mdv2007.1
+ Revision: 88097
- rebuild

* Mon Nov 27 2006 Götz Waschk <waschk@mandriva.org> 2.17.2-1mdv2007.1
+ Revision: 87684
- new version
- unpack patches
- Import gnome-menus

* Fri Oct 06 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.0
- New version 2.16.1

* Thu Sep 14 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0-2mdv2007.0
- Patch1: unclutter preferences/settings menus

* Tue Sep 05 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Sat Aug 19 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.91-3mdv2007.0
- Update patch0, should fix bug mdv #24481

* Fri Aug 18 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.91-2mdv2007.0
- Patch0: grab translation from menu-messages if not available upstream

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1
- New release 2.15.90

* Tue Jul 18 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.4.1-2mdv2007.0
- Remove patch0, merged upstream

* Wed Jul 12 2006 G�tz Waschk <waschk@mandriva.org> 2.15.4.1-1mdv2007.0
- new major
- New release 2.15.4.1

* Wed Jul 12 2006 G�tz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- new major
- New release 2.15.4

* Fri Apr 14 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0

* Fri Apr 14 2006 Frederic Crozat <fcrozat@mandriva.com> 2.13.5-1mdk
- Release 2.13.5
- Patch0 (Fedora): break infinite loop

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-3mdk
- Use mkrel

* Mon Oct 10 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.12.0-2mdk
- add BuildRequires: libpython-devel

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.12.0
- Remove patch0 (merged upstream)

* Tue Sep 13 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.92-4mdk 
- Patch1: fix pending events being removed prematurely (Mdk bug #17632)

* Fri Aug 26 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.92-3mdk 
- Patch0 (CVS): fix monitoring

* Tue Aug 23 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.92-2mdk 
- Remove patch1, better fix has been included upstream

* Tue Aug 23 2005 G�tz Waschk <waschk@mandriva.org> 2.11.92-1mdk
- drop merged patch 0
- New release 2.11.92

* Wed Aug 17 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.91-3mdk 
- Patch1: fix monitoring of topdir directory

* Fri Aug 12 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.91-2mdk 
- Patch0 (markmc): don't access freed memory

* Wed Aug 10 2005 Götz Waschk <waschk@mandriva.org> 2.11.91-1mdk
- New release 2.11.91

* Wed Jul 27 2005 G�tz Waschk <waschk@mandriva.org> 2.11.90-1mdk
- New release 2.11.90

* Thu May 19 2005 G�tz Waschk <waschk@mandriva.org> 2.11.1.1-1mdk
- New release 2.11.1.1

* Thu May 19 2005 G�tz Waschk <waschk@mandriva.org> 2.11.1-1mdk
- final version

* Sat May 14 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.1-0.20050513.1mdk 
- new CVS snapshot, fix crash

* Fri May 13 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.1-0.20050512.1mdk 
- new CVS snapshot and this time, use the correct tarball :)

* Wed Apr 27 2005 G�tz Waschk <waschk@mandriva.org> 2.11.1-0.20050425.2mdk
- fix buildrequires

* Tue Apr 26 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.1-0.20050425.1mdk 
- new CVS snapshot, no longer uses gnome-vfs, use fam/gamin directly

* Fri Apr 22 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.1-0.20050420.3mdk
- add more provides

* Fri Apr 22 2005 G�tz Waschk <waschk@mandriva.org> 2.11.1-0.20050420.2mdk
- fix buildrequires

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.1-0.20050420.1mdk 
- Initial package based on G�tz Waschk package
- CVS snapshot of HEAD branch to get layout support

