# TODO
# - gtk3 possible:   --enable-gtk3           enable to use gtk-3.0 instead of gtk-2.0
Summary:	Desktop-independent theme switcher for GTK+
Name:		lxappearance
Version:	0.5.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	34d157a7fe97ef0b93db8fab3f251e07
URL:		http://wiki.lxde.org/en/LXAppearance
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXAppearance is part of LXDE project. It's a desktop-independent theme
switcher for GTK+.

%package devel
Summary:	Header files for lxappearance
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for lxappearance.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxappearance
%{_mandir}/man1/lxappearance.1*
%{_desktopdir}/lxappearance.desktop
%{_datadir}/lxappearance

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/lxappearance
%{_includedir}/lxappearance/lxappearance.h
%{_pkgconfigdir}/lxappearance.pc
