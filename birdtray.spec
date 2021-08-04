%global longname com.ulduzsoft.Birdtray

Name:           birdtray
Version:        1.9.0
Release:        1%{?dist}
Summary:        System tray icon for Thunderbird

License:        GPLv3+
URL:            https://github.com/gyunaev/birdtray
Source0:        https://github.com/gyunaev/birdtray/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Recommends:     thunderbird

%description
Birdtray is a system tray new mail notification for Thunderbird, which does not
require extensions.

%prep
%autosetup


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install

#find translation files
%find_lang main --with-qt
%find_lang dynamic --with-qt

#rename and validate .desktop file
mv %{buildroot}/%{_datadir}/applications/%{longname}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

#rename and validate metainfo.xml
mv %{buildroot}/%{_metainfodir}/%{longname}.appdata.xml %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml


%files -f main.lang -f dynamic.lang
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml

#icons:
%{_datadir}/icons/*/*/apps/%{longname}.png
%{_datadir}/icons/*/*/apps/%{longname}.svg


%changelog
* Tue Aug 03 2021 Amirerfan Rafati <aerfanr@mailo.com> - 1.9.0-1
- Initial version of the package
