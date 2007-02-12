Summary:	Scribus Short Words plugin
Summary(pl.UTF-8):   Wtyczka Short Words dla Scribusa
Name:		scribus-short-words
Version:	1.2.1
Release:	3
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://www.yarpen.cz/scribus-short-words/%{name}-%{version}.tar.bz2
# Source0-md5:	73eb46f3b1a4f702334e748f1fee2d39
URL:		http://www.yarpen.cz/scribus-short-words/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	scribus-devel >= 1.2.1
Requires:	scribus >= 1.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
Short Words for Scribus is a special plug-in for adding non-breaking
spaces before or after so called short words.

%description -l pl.UTF-8
Short Words dla Scribusa jest specjalną wtyczką automatyzująca
dodawanie tzw. twardych spacji przed lub po "krótkich słowach" w
dokumentach zgodnie z regułami polskiej typografii.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} admin/am_edit
%configure \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{_ulibdir}/scribus/plugins/scribus-short-words.rc
%attr(755,root,root) %{_ulibdir}/scribus/plugins/libscribusshortwords.so.*.*.*
%lang(cs) %{_ulibdir}/scribus/plugins/libscribusshortwords.cs.qm
%lang(fr) %{_ulibdir}/scribus/plugins/libscribusshortwords.fr.qm
%lang(pl) %{_ulibdir}/scribus/plugins/libscribusshortwords.pl.qm
%lang(sk) %{_ulibdir}/scribus/plugins/libscribusshortwords.sk.qm
%lang(cs) %dir %{_datadir}/scribus/doc/cs/tutorials/%{name}
%lang(cs) %{_datadir}/scribus/doc/cs/tutorials/%{name}/*
%lang(en) %dir %{_datadir}/scribus/doc/en/tutorials/%{name}
%lang(en) %{_datadir}/scribus/doc/en/tutorials/%{name}/*
%lang(fr) %dir %{_datadir}/scribus/doc/fr/tutorials/%{name}
%lang(fr) %{_datadir}/scribus/doc/fr/tutorials/%{name}/*
%lang(pl) %dir %{_datadir}/scribus/doc/pl/tutorials/%{name}
%lang(pl) %{_datadir}/scribus/doc/pl/tutorials/%{name}/*
