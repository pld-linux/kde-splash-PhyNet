
%define		_splash		PhyNet

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	01
Release:	1
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=1706
Source0:	5549-phynet%{version}.tgz
Source1:	%{name}-themerc
URL:		http://www.kdelook.org/content/download.php?content=5549
Requires:	kdebase >= 3.2-0.030410
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"PhyNet" KDE splash screen.

%description -l pl
Ekran startowy KDE "PhyNet".

%prep
%setup  -q -n pics

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/Themes/%{_splash}

cp * $RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/Themes/%{_splash}

install %{SOURCE1} \
    $RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/Themes/%{_splash}/Theme.rc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
