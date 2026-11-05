Name:           regolith-rofication
Version:        1.5.3
Release:        1%{?dist}
Summary:        Rofication notification system
# setup.py and debian/copyright say MIT; the repo has no license file.
License:        MIT
URL:            https://github.com/regolith-linux/regolith-rofication
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Pure Python, although Debian builds it as Architecture: any.
BuildArch:      noarch
# pyproject macros: with no pyproject.toml, setup.py builds through the
# setuptools legacy backend.
BuildRequires:  python3-devel

Requires:       python3-gobject
Requires:       python3-dbus

# Debian provides "notification-daemon", which on Fedora is the name of a
# real package (GNOME's daemon); Fedora's virtual name is
# desktop-notification-daemon.
Provides:       desktop-notification-daemon
# Debian conflicts with dunst (and notify-osd, which Fedora doesn't ship).
# mako and SwayNotificationCenter are in the same position on Fedora: each
# ships a D-Bus activation file for org.freedesktop.Notifications, so a
# notification sent while rofication-daemon isn't running starts them, and
# they keep the name.
Conflicts:      dunst
Conflicts:      mako
Conflicts:      SwayNotificationCenter

%description
Rofication provides an unobtrusive notification system: a notification
daemon, a status tool for the bar and a viewer.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rofication

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/rofication-daemon
%{_bindir}/rofication-gui
%{_bindir}/rofication-status

%changelog
* Thu Nov 05 2026 Regolith Fedora Port <port@regolith.invalid> - 1.5.3-1
- Initial package
