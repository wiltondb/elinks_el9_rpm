%define DATE 0.4.2
%define rescue %{nil}
Name: elinks
Summary: text mode www browser with support for frames
Version: 0.4.2
%define rel 1
Release: %{rel}%{rescue}
Source: http://elinks.or.cz/download/elinks-0.4.2.tar.bz2
Source1: http://links.sourceforge.net/download/docs/manual-0.82-en.tar.bz2
Patch2: elinks-0.4.2-pkgconfig.patch
Patch3: elinks-0.4.2-textarea.patch
Group: Applications/Internet
URL: http://elinks.or.cz/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: autoconf, automake, openssl-devel, pkgconfig
License: GPL
Provides: webclient
Obsoletes: links
Provides: links

%description
Links is a text-based Web browser. Links does not display any images,
but it does support frames, tables and most other HTML tags. Links'
advantage over graphical browsers is its speed--Links starts and exits
quickly and swiftly displays Web pages.

%prep
%setup -q -a 1 -n %{name}-%{DATE}
%patch2 -p1 -b .pkgconfig

# Fix bug #62368.
%patch3 -p1 -b .textarea

aclocal
automake -a
autoconf

%build
%configure %{?rescue:--without-gpm}
%if "%{rescue}" != ""
perl -pi -e "s,-O2,-O2 -Os,g" Make* */Make*
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
ln -s %{_bindir}/elinks $RPM_BUILD_ROOT%{_bindir}/links
ln -s %{_mandir}/man1/elinks.1 $RPM_BUILD_ROOT%{_mandir}/man1/links.1

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README SITES TODO manual-0.82-en
%{_bindir}/links
%{_bindir}/elinks
%{_mandir}/man1/links.1*
%{_mandir}/man1/elinks.1*
%{_mandir}/man5/*

%changelog
* Wed Feb  5 2003 Tim Waugh <twaugh@redhat.com> 0.4.2-1
- 0.4.2 (bug #83273).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.3.2-5
- rebuilt

* Thu Jan 16 2003 Tim Waugh <twaugh@redhat.com>
- Fix URL (bug #81987).

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.3.2-4
- rebuild

* Mon Dec 23 2002 Tim Waugh <twaugh@redhat.com> 0.3.2-3
- Fix bug #62368.

* Thu Dec 12 2002 Nalin Dahyabhai <nalin@redhat.com>
- use openssl's pkg-config data, if available

* Wed Nov 20 2002 Tim Powers <timp@redhat.com> 0.3.2-2
- rebuild on all arches

* Tue Aug 20 2002 Jakub Jelinek <jakub@redhat.com> 0.3.2-1
- update to 0.3.2 to fix the DNS Ctrl-C segfaults
- update URLs, the project moved
- include man page

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jan 24 2002 Tim Powers <timp@redhat.com>
- rebuilt against new openssl

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Preston Brown <pbrown@redhat.com> 0.96-4
- cookie fix

* Thu Sep 13 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.96-3
- Save some more space in rescue mode

* Wed Jul 18 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.96-2
- Add the links manual from links.sourceforge.net (RFE #49228)

* Tue Jul  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.96-1
- update to 0.96

* Fri Jun 22 2001 Nalin Dahyabhai <nalin@redhat.com>
- actually run make in build phase

* Tue Jun 12 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Jan  9 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.95

* Mon Jan  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94 final

* Sun Dec 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- pre9

* Mon Dec 10 2000 Preston Brown <pbrown@redhat.com>
- Upgraded to pre8.

* Tue Dec  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94pre7
- Minor fixes to the specfile (s/Copyright:/License:/)
- merge rescue stuff

* Fri Nov 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94pre5

* Wed Nov 15 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94pre4

* Tue Oct 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.94pre1

* Wed Aug  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.92 (needed - prior versions won't display XHTML properly)

* Thu Jul 20 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment to work around bugs

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 15 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.84

* Sun Jun 11 2000 Preston Brown <pbrown@redhat.com>
- provides virtual package webclient.

* Thu Jan  6 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial RPM
