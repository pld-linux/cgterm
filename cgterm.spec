Summary:	A C/G graphics C64 BBS client
Summary(pl):	Klient C64 BBS obs³uguj±cy grafikê C/G
Name:		cgterm
Version:	1.6
Release:	1
License:	BSD-like (see docs)
Group:		Networking
Source0:	http://www.paradroid.net/cgterm/%{name}-%{version}.tar.gz
# Source0-md5:	5b8f81ea8a2c0612d2998f05fd87ec40
Patch0:		%{name}-Makefile.patch
URL:		http://www.paradroid.net/cgterm/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGTerm is a C/G telnet client that lets you connect to 8-bit C64 BBSes
via telnet gateways with the correct colours and the correct font.
Also included is a client for 64CHAT called CGChat. See
http://www.petscii.com for BBS list.

%description -l pl
CGTerm to klient C/G telnetu, który pozwala na po³±czenie siê z
internetowymi BBSami dzia³aj±cymi na 8-bitowych C64 przez bramy telnet
u¿ywaj±c prawid³owych kolorów i fontu. Pakiet zawiera równie¿ program
CGChat - klienta 64CHAT. Listê BBSów mo¿na znale¼æ na
http://www.petscii.com.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	CC="%{__cc}" \
	PREFIX="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}
ln -sf us.kbd $RPM_BUILD_ROOT%{_datadir}/cgterm/keyboard.kbd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc cgchat.txt cgterm.txt history.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/cgterm
