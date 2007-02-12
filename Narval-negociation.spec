%define short_name negociation

Summary:	Negociation extensions for Narval
Summary(pl.UTF-8):	Rozszerzenie negocjacyjne dla Narvala
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
# Source0-md5:	03b06274505404a0c8b1416a7044d4a2
URL:		http://www.logilab.org/narval/app.html
Requires:	Narval
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The negociation package contains transforms and recipes that are
useful to build multi-agents negociation applications.
A sample of application can be found in the PIA package.

%description -l pl.UTF-8
Pakiet negociation zawiera przekształcenia i recepty użyteczne do
budowania aplikacji negocjujących między agentami.
Przykładową aplikację zawiera pakiet PIA.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/narval/apps/%{short_name}-%{version}.npm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
