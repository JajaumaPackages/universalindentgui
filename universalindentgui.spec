Name:           universalindentgui
Version:        1.2.0
Release:        1%{?dist}
Summary:        GUI for varius source code beautifiers

License:        GPL
URL:            http://universalindent.sourceforge.net
Source0:        https://downloads.sourceforge.net/project/universalindent/uigui/UniversalIndentGUI_%{version}/universalindentgui-%{version}.tar.gz

BuildRequires:  qt4-devel
BuildRequires:  qscintilla-devel

%description
A cross platform GUI for several code formatter, beautifier and indenter like
AStyle, GNU Indent, GreatCode, HTML Tidy, Uncrustify and many more. Main
feature is a live preview to directly see how the selected formatting option
affects the source code.


%prep
%setup -q


%build
%{qmake_qt4} UniversalIndentGUI.pro
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install INSTALL_ROOT=%{buildroot}


%files
%doc
%{_bindir}/*
%{_datadir}/universalindentgui/
%{_mandir}/man1/*.1*


%changelog
* Fri Jan 20 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.2.0-1
- Initial release
