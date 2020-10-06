Name: test_prog
Version: 0.1
Release: set1

Summary: test_prog
Group: Development/C++
License: GPL

%description
test_prog

%prep

%setup -T -c

%build
%make
%install
mkdir -p "%{buildroot}"

%post
%postun


%files
%_bindir/test_prog
