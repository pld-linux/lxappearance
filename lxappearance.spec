Summary:	Desktop-independent theme switcher for GTK+
Name:		lxappearance
Version:	0.5.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	7eabab6f4a358dbc6a84e260a0e7f6c2
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

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/lxappearance
%{_includedir}/lxappearance/lxappearance.h
%{_pkgconfigdir}/lxappearance.pc
