Summary:	xdotool type for wayland
Name:		wtype
Version:	0.3
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/atx/wtype/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8101ad31af764c675e60bbb4330813a8
URL:		https://github.com/atx/wtype
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdotool type for wayland.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/wtype
%{_mandir}/man1/wtype.1*
