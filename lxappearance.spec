#
# Conditional build:
%bcond_with	gtk3	# use GTK+3 instead of GTK+2

Summary:	Desktop-independent theme switcher for GTK+
Summary(pl.UTF-8):	Niezależny od środowiska przełącznik motywów dla GTK+
Name:		lxappearance
Version:	0.6.3
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	f10345313e2c12bad51c1b58bd46b454
URL:		http://wiki.lxde.org/en/LXAppearance
BuildRequires:	dbus-devel >= 0.95
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
%{!?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	dbus-libs >= 0.95
Requires:	dbus-glib >= 0.70
%{!?with_gtk2:Requires:	gtk+2 >= 2:2.12.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXAppearance is part of LXDE project. It's a desktop-independent theme
switcher for GTK+.

%description -l pl.UTF-8
LXAppearance to część projektu LXDE. Jest to niezależny od środowiska
przełącznik motywów dla GTK+.

%package devel
Summary:	Header files for lxappearance plugins
Summary(pl.UTF-8):	Pliki nagłówkowe dla wtyczek lxappearance
Group:		Development/Libraries
Requires:	glib2-devel >= 2.0
%{!?with_gtk2:Requires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:Requires:	gtk+3-devel >= 3.0.0}
# doesn't require base

%description devel
Header files for lxappearance plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla wtyczek lxappearance.

%prep
%setup -q

%build
%configure \
	--enable-dbus \
	%{?with_gtk3:--enable-gtk3} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# directory for plugins
install -d $RPM_BUILD_ROOT%{_libdir}/lxappearance/plugins

# unify name
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{tt_RU,tt}
# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
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
