Summary:	Command Line Tool for GDBM
Name:		dbtool
Version:	1.6
Release:	10
License:	GPLv2+
Group:		Databases
Url:		https://www.daemon.de/DBTOOL
Source0:	ftp://ftp.daemon.de/scip/Apps/dbtool/dbtool-%{version}.tar.bz2
Patch0:		dbtool.patch
Patch1:		dbtool-1.6-gcc411.diff
BuildRequires:	gdbm-devel
BuildRequires:	pkgconfig(libpcre)

%description
dbtool can be used to store and retrieve data in a key/value format
in a GDBM hash database. Perl compatible regular expressions are
supported both for storing and retrieving of data. It's main
advantages are the ability to maintain huge amounts of data and
speed. It also supports encrypted databases using the AES cipher
algorithm.

%files
%doc AUTHORS ChangeLog README samples
%{_bindir}/dbtool*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1

# fix attribs
find samples -type f | xargs chmod 644
find samples -type d | xargs chmod 755
find . -perm 0640 | xargs chmod 644
chmod 644 AUTHORS ChangeLog README

%build
# build the gdbm version
%configure2_5x --without-berkeley
%make CXXFLAGS="%{optflags} -Wall" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 dbtool %{buildroot}%{_bindir}/
install -m0644 dbtool.1 %{buildroot}%{_mandir}/man1/

