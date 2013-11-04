%global packname  hmeasure
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0
Release:          1
Summary:          The H-measure and other scalar classification performance metrics
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz



Requires:         R-MASS R-class 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

BuildRequires:   R-MASS R-class 
%description
Scalar performance metrics, including the H-measure, based on
classification scores for several classifiers applied to the same dataset.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
