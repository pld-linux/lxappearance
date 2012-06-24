Summary:	Desktop-independent theme switcher for GTK+
Name:		lxappearance
Version:	0.4.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	751426a9c4b6090b9fabb8dde593c50a
URL:		http://wiki.lxde.org/en/LXAppearance
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXAppearance is part of LXDE project. It's a desktop-independent theme
switcher for GTK+.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxappearance
%{_desktopdir}/lxappearance.desktop
%{_datadir}/lxappearance
%{_mandir}/man1/lxappearance*
