%define short_name negociation

Summary:	Negociation extensions for Narval
Summary(pl):	Rozszerzenie negocjacyjne dla Narvala
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
# Source0-md5:	03b06274505404a0c8b1416a7044d4a2
License:	GPL
Group:		Applications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval
Url:		http://www.logilab.org/narval/app.html

%description
The negociation package contains transforms and recipes that are
useful to build multi-agents negociation applications.

A sample of application can be found in the PIA package.

%description -l pl
Pakiet negociation zawiera przekszta³cenia i recepty u¿yteczne do
budowania aplikacji negocjuj±cych miêdzy agentami.

Przyk³adow± aplikacjê zawiera pakiet PIA.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
