Summary:	Scribus Short Words plugin
Summary(pl):	Wtyczka Short Words dla Scribusa
Name:		scribus-short-words
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://www.yarpen.cz/scribus-short-words/%{name}-%{version}.tar.bz2
# Source0-md5:	192d90f6f165d1c5d337c330c8c09829
URL:		http://www.yarpen.cz/scribus-short-words/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	scribus-devel
Requires:	scribus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
Short Words for Scribus is a special plug-in for adding non-breaking
spaces before or after so called short words.

%description -l pl
Short Words dla Scribusa jest specjaln± wtyczk± automatyzuj±ca
dodawanie tzw. twardych spacji przed lub po "krótkich s³owach" w
dokumentach zgodnie z regu³ami polskiej typografii.

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
%dir %{_datadir}/scribus/doc/%{name}
%{_datadir}/scribus/doc/%{name}/*.html
%lang(cs) %dir %{_datadir}/scribus/doc/%{name}/cs
%lang(cs) %{_datadir}/scribus/doc/%{name}/cs/*
%lang(en) %dir %{_datadir}/scribus/doc/%{name}/en
%lang(en) %{_datadir}/scribus/doc/%{name}/en/*
%lang(fr) %dir %{_datadir}/scribus/doc/%{name}/fr
%lang(fr) %{_datadir}/scribus/doc/%{name}/fr/*
%lang(pl) %dir %{_datadir}/scribus/doc/%{name}/pl
%lang(pl) %{_datadir}/scribus/doc/%{name}/pl/*
