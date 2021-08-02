Name:           birdtray
Version:        1.9.0
Release:        1%{?dist}
Summary:        System tray icon for Thunderbird

License:        GPLv3+
URL:            https://github.com/gyunaev/birdtray
Source0:        https://github.com/gyunaev/birdtray/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake, qt5-qtbase-devel, qt5-qtx11extras-devel, qt5-qtsvg-devel
Requires:       thunderbird

%description
Birdtray is a system tray new mail notification for Thunderbird, which does not require extensions.

%prep
%autosetup


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
rm -rf $RPM_BUILD_ROOT
%cmake_install


%files
%{_bindir}/birdtray
%{_datadir}/applications/com.ulduzsoft.Birdtray.desktop
%{_datadir}/ulduzsoft/birdtray/translations/
%{_datadir}/icons/*/*/apps/com.ulduzsoft.Birdtray.png
%{_datadir}/icons/*/*/apps/com.ulduzsoft.Birdtray.svg
%{_datadir}/metainfo/com.ulduzsoft.Birdtray.appdata.xml

%changelog
* Sat Jul 31 2021 RPM User - 1.9.0-1
- Initial version of the package
