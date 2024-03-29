
%define		_splash		PhyNet

Summary:	KDE splash screen
Summary(pl.UTF-8):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	01
Release:	3
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=1706
Source0:	5549-phynet%{version}.tgz
# Source0-md5:	9de90099d97648e3c6e79112fb559ff7
Source1:	%{name}-Preview.png
Source2:	%{name}-Theme.rc
URL:		http://www.kde-look.org/content/show.php?content=5549
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"PhyNet" is a splash screen for the phy.net website and contains a
picture of woman in biking.

%description -l pl.UTF-8
Ekran startowy KDE "PhyNet" ku reklamie strony phy.net zawiera obrazek
kobiety w bikini.

%prep
%setup -q -n pics

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

cp * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

install %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Preview.png

install %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}/Theme.rc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
