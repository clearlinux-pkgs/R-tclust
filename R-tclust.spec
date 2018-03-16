#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tclust
Version  : 1.3.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/tclust_1.3-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tclust_1.3-1.tar.gz
Summary  : Robust Trimmed Clustering
Group    : Development/Tools
License  : GPL-3.0
Requires: R-tclust-lib
Requires: R-mclust
Requires: R-mvtnorm
Requires: R-sn
BuildRequires : R-mclust
BuildRequires : R-mvtnorm
BuildRequires : R-sn
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-tclust package.
Group: Libraries

%description lib
lib components for the R-tclust package.


%prep
%setup -q -c -n tclust

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521226534

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521226534
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tclust
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tclust
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tclust
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tclust|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tclust/CITATION
/usr/lib64/R/library/tclust/DESCRIPTION
/usr/lib64/R/library/tclust/INDEX
/usr/lib64/R/library/tclust/Meta/Rd.rds
/usr/lib64/R/library/tclust/Meta/data.rds
/usr/lib64/R/library/tclust/Meta/features.rds
/usr/lib64/R/library/tclust/Meta/hsearch.rds
/usr/lib64/R/library/tclust/Meta/links.rds
/usr/lib64/R/library/tclust/Meta/nsInfo.rds
/usr/lib64/R/library/tclust/Meta/package.rds
/usr/lib64/R/library/tclust/Meta/vignette.rds
/usr/lib64/R/library/tclust/NAMESPACE
/usr/lib64/R/library/tclust/R/tclust
/usr/lib64/R/library/tclust/R/tclust.rdb
/usr/lib64/R/library/tclust/R/tclust.rdx
/usr/lib64/R/library/tclust/data/M5data.rda
/usr/lib64/R/library/tclust/data/geyser2.rda
/usr/lib64/R/library/tclust/data/swissbank.rda
/usr/lib64/R/library/tclust/doc/index.html
/usr/lib64/R/library/tclust/doc/tclust.R
/usr/lib64/R/library/tclust/doc/tclust.pdf
/usr/lib64/R/library/tclust/doc/tclust.rnw
/usr/lib64/R/library/tclust/help/AnIndex
/usr/lib64/R/library/tclust/help/aliases.rds
/usr/lib64/R/library/tclust/help/paths.rds
/usr/lib64/R/library/tclust/help/tclust.rdb
/usr/lib64/R/library/tclust/help/tclust.rdx
/usr/lib64/R/library/tclust/html/00Index.html
/usr/lib64/R/library/tclust/html/R.css
/usr/lib64/R/library/tclust/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tclust/libs/tclust.so
/usr/lib64/R/library/tclust/libs/tclust.so.avx2
/usr/lib64/R/library/tclust/libs/tclust.so.avx512
