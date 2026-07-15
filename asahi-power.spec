Name:           asahi-power
Version:        1.0.0
Release:        1%{?dist}
Summary:        htop-style live power monitor for Apple Silicon under Asahi Linux

License:        MIT
URL:            https://github.com/FiedorPw/asahi-power
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       bash
Requires:       gawk
Requires:       ncurses

%description
Live terminal power monitor for Apple Silicon Macs running Asahi Linux.
Shows the whole power chain as colored htop-style meters refreshed 4x/second:
negotiated USB-PD contract limit, AC input flowing through the charging cable,
total system draw and battery charge/discharge power, plus a sparkline with
recent system-power history. Reads macsmc sensors from sysfs; no daemons,
no ncurses dependency beyond tput.

%prep
%setup -q

%install
install -Dm755 power %{buildroot}%{_bindir}/power

%files
%doc README.md
%{_bindir}/power

%changelog
* Wed Jul 15 2026 Mikołaj Fiedorczuk <vectorbaltic@gmail.com> - 1.0.0-1
- Initial package: htop-style meters, battery gauge, sparkline
