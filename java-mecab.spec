%include	/usr/lib/rpm/macros.java
Summary:	MeCab module for Java
Summary(pl.UTF-8):	Moduł MeCab dla Javy
Name:		java-mecab
Version:	0.994
Release:	1
License:	GPL v2 or LGPL v2.1 or BSD
Group:		Libraries/Java
#Source0Download: http://code.google.com/p/mecab/downloads/list
Source0:	http://mecab.googlecode.com/files/mecab-java-%{version}.tar.gz
# Source0-md5:	c6e9e4b283519847b5c9c750710b7c85
Patch0:		%{name}-opt.patch
URL:		http://code.google.com/p/mecab/
%if %(locale -a | grep -q '^en_US\.UTF-8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	libstdc++-devel
BuildRequires:	mecab-devel
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MeCab module for Java.

%description -l pl.UTF-8
Moduł MeCab dla Javy.

%prep
%setup -q -n mecab-java-%{version}
%patch0 -p1

%build
# test.java contains UTF-8 string
export LC_ALL=en_US.UTF-8
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	INCLUDE=%{_jvmdir}/java/include

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir}}

cp -p MeCab.jar $RPM_BUILD_ROOT%{_javadir}
install libMeCab.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING README bindings.html
%attr(755,root,root) %{_libdir}/libMeCab.so
%{_javadir}/MeCab.jar
