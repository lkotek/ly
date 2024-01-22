Name:           ly
Version:        0.6.0
Release:        1%{?dist}
Summary:        Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD.

License:        WTFPL, Version 2, December 2004
URL:            https://github.com/fairyglade/%{name}

BuildRequires:  make 
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  kernel-devel
BuildRequires:  pam-devel
BuildRequires:  libxcb-devel
BuildRequires:  bash
BuildRequires:  systemd
BuildRequires:  tree
Requires:       pam

%description
Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD.
Ly should work with any X desktop environment, and provides basic wayland 
support (sway works very well, for example). The name "Ly" is a tribute 
to the fairy from the game Rayman.

%define lydir   %{name}-%{version}

%prep
rm -rf %{lydir}
git clone --recurse-submodules --branch v%{version} %{URL}.git --depth=1 %{lydir}
cd %{lydir}

%build
cd %{lydir}
make

%install
cd %{lydir}
mkdir -p %{buildroot}/usr/share/{licenses,doc}
cp license.md readme.md /builddir/build/BUILD/
make install installsystemd DESTDIR=%{buildroot}
systemctl disable getty@tty2.service

%files
/usr/bin/ly
/etc/ly/config.ini
/etc/ly/lang/cat.ini
/etc/ly/lang/cs.ini
/etc/ly/lang/de.ini
/etc/ly/lang/en.ini
/etc/ly/lang/es.ini
/etc/ly/lang/fr.ini
/etc/ly/lang/it.ini
/etc/ly/lang/pl.ini
/etc/ly/lang/pt.ini
/etc/ly/lang/pt_BR.ini
/etc/ly/lang/ro.ini
/etc/ly/lang/ru.ini
/etc/ly/lang/sr.ini
/etc/ly/lang/sv.ini
/etc/ly/lang/tr.ini
/etc/ly/lang/uk.ini
/etc/ly/wsetup.sh
/etc/ly/xsetup.sh
/etc/pam.d/ly
/usr/lib/systemd/system/ly.service
%doc readme.md
%license license.md

%changelog
* Mon Jan 15 2024 Lukas Kotek <lkotek@redhat.com>
- Inital build
