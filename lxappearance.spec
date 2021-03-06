#
# Conditional build:
%bcond_with		gtk3		# build GTK+3 disables GTK+2
%bcond_without		gtk2	# build with GTK+2

%if %{with gtk3}
%undefine	with_gtk2
%endif

Summary:	Desktop-independent theme switcher for GTK+
Name:		lxappearance
Version:	0.5.5
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	a67113681d9d0a6d936289909aed5782
Patch0:		mate-desktop.patch
URL:		http://wiki.lxde.org/en/LXAppearance
BuildRequires:	gettext-tools
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%patch0 -p1

%build
%configure \
	%{?with_gtk3:--enable-gtk3}
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/lxappearance/plugins

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/tt_RU

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxappearance
%dir %{_libdir}/lxappearance
%dir %{_libdir}/lxappearance/plugins
%{_mandir}/man1/lxappearance.1*
%{_desktopdir}/lxappearance.desktop
%{_datadir}/lxappearance

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/lxappearance
%{_includedir}/lxappearance/lxappearance.h
%{_pkgconfigdir}/lxappearance.pc
