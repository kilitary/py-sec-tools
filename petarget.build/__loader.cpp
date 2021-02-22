
/* Code to register embedded modules for meta path based loading if any. */

#include <Python.h>

#include "nuitka/constants_blob.h"

#include "nuitka/unfreezing.h"

/* Type bool */
#ifndef __cplusplus
#include "stdbool.h"
#endif

#if 598 > 0
static unsigned char *bytecode_data[598];
#else
static unsigned char **bytecode_data = NULL;
#endif

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
extern PyObject *modulecode___main__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_bcrypt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_bcrypt$__about__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_certifi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_certifi$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$big5freq(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$big5prober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$chardistribution(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$charsetgroupprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$charsetprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$codingstatemachine(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$cp949prober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$enums(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$escprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$escsm(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$eucjpprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$euckrfreq(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$euckrprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$euctwfreq(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$euctwprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$gb2312freq(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$gb2312prober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$hebrewprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$jisfreq(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$jpcntx(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$langbulgarianmodel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$langgreekmodel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$langhebrewmodel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$langrussianmodel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$langthaimodel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$langturkishmodel(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$latin1prober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$mbcharsetprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$mbcsgroupprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$mbcssm(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$sbcharsetprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$sbcsgroupprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$sjisprober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$universaldetector(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$utf8prober(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_chardet$version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_commctrl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_crawler(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_crawler_config(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$__about__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$fernet(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$_der(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$_oid(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$interfaces(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$aead(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$backend(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$ciphers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$cmac(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$decode_asn1(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$dh(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$dsa(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$ec(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$ed25519(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$ed448(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$encode_asn1(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$hashes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$hmac(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$ocsp(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$poly1305(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$rsa(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$x25519(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$x448(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$backends$openssl$x509(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$bindings(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$bindings$openssl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$bindings$openssl$_conditional(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$bindings$openssl$binding(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$dh(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$dsa(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$ec(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$ed25519(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$ed448(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$padding(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$rsa(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$x25519(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$asymmetric$x448(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$ciphers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$ciphers$aead(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$ciphers$algorithms(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$ciphers$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$ciphers$modes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$constant_time(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$hashes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$hmac(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$kdf(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$kdf$scrypt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$padding(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$serialization(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$serialization$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$serialization$pkcs7(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$hazmat$primitives$serialization$ssh(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$x509(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$x509$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$x509$certificate_transparency(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$x509$extensions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$x509$general_name(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$x509$name(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$x509$ocsp(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_cryptography$x509$oid(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$filetype(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$helpers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$match(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$types(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$types$archive(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$types$audio(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$types$base(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$types$font(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$types$image(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$types$isobmff(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$types$video(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_filetype$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_helpers(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$core(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$idnadata(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$intranges(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$package_data(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_idna$uts46data(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_magic(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_magic$magic(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ordlookup(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ordlookup$oleaut32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_ordlookup$ws2_32(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_outputdebugstring(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pefile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_common(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_psaix(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_psbsd(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_pslinux(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_psosx(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_psposix(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_pssunos(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_psutil$_pswindows(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyAesCrypt(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pyAesCrypt$crypto(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pythoncom(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$dialogs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$dialogs$list(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$dialogs$status(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc$dialog(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc$object(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc$thread(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin$mfc$window(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywin32_bootstrap(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_pywintypes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$__version__(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$_internal_utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$adapters(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$api(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$auth(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$certs(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$compat(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$cookies(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$hooks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$models(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$packages(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$sessions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$status_codes(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$structures(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_requests$utils(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_six(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_socks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$_collections(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$_version(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$connection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$connectionpool(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib$_appengine_environ(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib$appengine(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib$pyopenssl(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$contrib$socks(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$exceptions(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$fields(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$filepost(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages$backports(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages$backports$makefile(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages$six(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages$ssl_match_hostname(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$packages$ssl_match_hostname$_implementation(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$poolmanager(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$request(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$response(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$connection(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$proxy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$queue(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$request(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$response(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$retry(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$ssl_(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$ssltransport(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$timeout(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$url(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_urllib3$util$wait(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_var_dump(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_var_dump$_var_dump(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$CLSIDToClass(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$build(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$dynamic(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$gencache(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$genpy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$makepy(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$selecttlb(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32com$client$util(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_win32con(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_winerror(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);
extern PyObject *modulecode_wmi(PyObject *, struct Nuitka_MetaPathBasedLoaderEntry const *);

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] = {
    {"__main__", modulecode___main__, 0, 0, },
    {"_asyncio", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_bz2", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_cffi_backend", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_ctypes", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_decimal", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_elementtree", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_hashlib", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_lzma", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_msi", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_multiprocessing", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_overlapped", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_queue", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_socket", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_sqlite3", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_ssl", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_tkinter", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"_win32sysloader", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"abc", NULL, 0, 5299, NUITKA_BYTECODE_FLAG},
    {"base64", NULL, 1, 17036, NUITKA_BYTECODE_FLAG},
    {"bcrypt", modulecode_bcrypt, 0, 0, NUITKA_PACKAGE_FLAG},
    {"bcrypt.__about__", modulecode_bcrypt$__about__, 0, 0, },
    {"bcrypt._bcrypt", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"bisect", NULL, 2, 2319, NUITKA_BYTECODE_FLAG},
    {"calendar", NULL, 3, 27029, NUITKA_BYTECODE_FLAG},
    {"certifi", modulecode_certifi, 0, 0, NUITKA_PACKAGE_FLAG},
    {"certifi.core", modulecode_certifi$core, 0, 0, },
    {"chardet", modulecode_chardet, 0, 0, NUITKA_PACKAGE_FLAG},
    {"chardet.big5freq", modulecode_chardet$big5freq, 0, 0, },
    {"chardet.big5prober", modulecode_chardet$big5prober, 0, 0, },
    {"chardet.chardistribution", modulecode_chardet$chardistribution, 0, 0, },
    {"chardet.charsetgroupprober", modulecode_chardet$charsetgroupprober, 0, 0, },
    {"chardet.charsetprober", modulecode_chardet$charsetprober, 0, 0, },
    {"chardet.codingstatemachine", modulecode_chardet$codingstatemachine, 0, 0, },
    {"chardet.cp949prober", modulecode_chardet$cp949prober, 0, 0, },
    {"chardet.enums", modulecode_chardet$enums, 0, 0, },
    {"chardet.escprober", modulecode_chardet$escprober, 0, 0, },
    {"chardet.escsm", modulecode_chardet$escsm, 0, 0, },
    {"chardet.eucjpprober", modulecode_chardet$eucjpprober, 0, 0, },
    {"chardet.euckrfreq", modulecode_chardet$euckrfreq, 0, 0, },
    {"chardet.euckrprober", modulecode_chardet$euckrprober, 0, 0, },
    {"chardet.euctwfreq", modulecode_chardet$euctwfreq, 0, 0, },
    {"chardet.euctwprober", modulecode_chardet$euctwprober, 0, 0, },
    {"chardet.gb2312freq", modulecode_chardet$gb2312freq, 0, 0, },
    {"chardet.gb2312prober", modulecode_chardet$gb2312prober, 0, 0, },
    {"chardet.hebrewprober", modulecode_chardet$hebrewprober, 0, 0, },
    {"chardet.jisfreq", modulecode_chardet$jisfreq, 0, 0, },
    {"chardet.jpcntx", modulecode_chardet$jpcntx, 0, 0, },
    {"chardet.langbulgarianmodel", modulecode_chardet$langbulgarianmodel, 0, 0, },
    {"chardet.langgreekmodel", modulecode_chardet$langgreekmodel, 0, 0, },
    {"chardet.langhebrewmodel", modulecode_chardet$langhebrewmodel, 0, 0, },
    {"chardet.langrussianmodel", modulecode_chardet$langrussianmodel, 0, 0, },
    {"chardet.langthaimodel", modulecode_chardet$langthaimodel, 0, 0, },
    {"chardet.langturkishmodel", modulecode_chardet$langturkishmodel, 0, 0, },
    {"chardet.latin1prober", modulecode_chardet$latin1prober, 0, 0, },
    {"chardet.mbcharsetprober", modulecode_chardet$mbcharsetprober, 0, 0, },
    {"chardet.mbcsgroupprober", modulecode_chardet$mbcsgroupprober, 0, 0, },
    {"chardet.mbcssm", modulecode_chardet$mbcssm, 0, 0, },
    {"chardet.sbcharsetprober", modulecode_chardet$sbcharsetprober, 0, 0, },
    {"chardet.sbcsgroupprober", modulecode_chardet$sbcsgroupprober, 0, 0, },
    {"chardet.sjisprober", modulecode_chardet$sjisprober, 0, 0, },
    {"chardet.universaldetector", modulecode_chardet$universaldetector, 0, 0, },
    {"chardet.utf8prober", modulecode_chardet$utf8prober, 0, 0, },
    {"chardet.version", modulecode_chardet$version, 0, 0, },
    {"codecs", NULL, 4, 33921, NUITKA_BYTECODE_FLAG},
    {"collections", NULL, 5, 46391, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"commctrl", modulecode_commctrl, 0, 0, },
    {"configparser", NULL, 6, 45683, NUITKA_BYTECODE_FLAG},
    {"contextlib", NULL, 7, 20194, NUITKA_BYTECODE_FLAG},
    {"copy", NULL, 8, 6952, NUITKA_BYTECODE_FLAG},
    {"crawler", modulecode_crawler, 0, 0, },
    {"crawler_config", modulecode_crawler_config, 0, 0, },
    {"cryptography", modulecode_cryptography, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.__about__", modulecode_cryptography$__about__, 0, 0, },
    {"cryptography.exceptions", modulecode_cryptography$exceptions, 0, 0, },
    {"cryptography.fernet", modulecode_cryptography$fernet, 0, 0, },
    {"cryptography.hazmat", modulecode_cryptography$hazmat, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat._der", modulecode_cryptography$hazmat$_der, 0, 0, },
    {"cryptography.hazmat._oid", modulecode_cryptography$hazmat$_oid, 0, 0, },
    {"cryptography.hazmat.backends", modulecode_cryptography$hazmat$backends, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.backends.interfaces", modulecode_cryptography$hazmat$backends$interfaces, 0, 0, },
    {"cryptography.hazmat.backends.openssl", modulecode_cryptography$hazmat$backends$openssl, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.backends.openssl.aead", modulecode_cryptography$hazmat$backends$openssl$aead, 0, 0, },
    {"cryptography.hazmat.backends.openssl.backend", modulecode_cryptography$hazmat$backends$openssl$backend, 0, 0, },
    {"cryptography.hazmat.backends.openssl.ciphers", modulecode_cryptography$hazmat$backends$openssl$ciphers, 0, 0, },
    {"cryptography.hazmat.backends.openssl.cmac", modulecode_cryptography$hazmat$backends$openssl$cmac, 0, 0, },
    {"cryptography.hazmat.backends.openssl.decode_asn1", modulecode_cryptography$hazmat$backends$openssl$decode_asn1, 0, 0, },
    {"cryptography.hazmat.backends.openssl.dh", modulecode_cryptography$hazmat$backends$openssl$dh, 0, 0, },
    {"cryptography.hazmat.backends.openssl.dsa", modulecode_cryptography$hazmat$backends$openssl$dsa, 0, 0, },
    {"cryptography.hazmat.backends.openssl.ec", modulecode_cryptography$hazmat$backends$openssl$ec, 0, 0, },
    {"cryptography.hazmat.backends.openssl.ed25519", modulecode_cryptography$hazmat$backends$openssl$ed25519, 0, 0, },
    {"cryptography.hazmat.backends.openssl.ed448", modulecode_cryptography$hazmat$backends$openssl$ed448, 0, 0, },
    {"cryptography.hazmat.backends.openssl.encode_asn1", modulecode_cryptography$hazmat$backends$openssl$encode_asn1, 0, 0, },
    {"cryptography.hazmat.backends.openssl.hashes", modulecode_cryptography$hazmat$backends$openssl$hashes, 0, 0, },
    {"cryptography.hazmat.backends.openssl.hmac", modulecode_cryptography$hazmat$backends$openssl$hmac, 0, 0, },
    {"cryptography.hazmat.backends.openssl.ocsp", modulecode_cryptography$hazmat$backends$openssl$ocsp, 0, 0, },
    {"cryptography.hazmat.backends.openssl.poly1305", modulecode_cryptography$hazmat$backends$openssl$poly1305, 0, 0, },
    {"cryptography.hazmat.backends.openssl.rsa", modulecode_cryptography$hazmat$backends$openssl$rsa, 0, 0, },
    {"cryptography.hazmat.backends.openssl.utils", modulecode_cryptography$hazmat$backends$openssl$utils, 0, 0, },
    {"cryptography.hazmat.backends.openssl.x25519", modulecode_cryptography$hazmat$backends$openssl$x25519, 0, 0, },
    {"cryptography.hazmat.backends.openssl.x448", modulecode_cryptography$hazmat$backends$openssl$x448, 0, 0, },
    {"cryptography.hazmat.backends.openssl.x509", modulecode_cryptography$hazmat$backends$openssl$x509, 0, 0, },
    {"cryptography.hazmat.bindings", modulecode_cryptography$hazmat$bindings, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.bindings._openssl", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"cryptography.hazmat.bindings._padding", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"cryptography.hazmat.bindings.openssl", modulecode_cryptography$hazmat$bindings$openssl, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.bindings.openssl._conditional", modulecode_cryptography$hazmat$bindings$openssl$_conditional, 0, 0, },
    {"cryptography.hazmat.bindings.openssl.binding", modulecode_cryptography$hazmat$bindings$openssl$binding, 0, 0, },
    {"cryptography.hazmat.primitives", modulecode_cryptography$hazmat$primitives, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.primitives.asymmetric", modulecode_cryptography$hazmat$primitives$asymmetric, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.primitives.asymmetric.dh", modulecode_cryptography$hazmat$primitives$asymmetric$dh, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.dsa", modulecode_cryptography$hazmat$primitives$asymmetric$dsa, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.ec", modulecode_cryptography$hazmat$primitives$asymmetric$ec, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.ed25519", modulecode_cryptography$hazmat$primitives$asymmetric$ed25519, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.ed448", modulecode_cryptography$hazmat$primitives$asymmetric$ed448, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.padding", modulecode_cryptography$hazmat$primitives$asymmetric$padding, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.rsa", modulecode_cryptography$hazmat$primitives$asymmetric$rsa, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.utils", modulecode_cryptography$hazmat$primitives$asymmetric$utils, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.x25519", modulecode_cryptography$hazmat$primitives$asymmetric$x25519, 0, 0, },
    {"cryptography.hazmat.primitives.asymmetric.x448", modulecode_cryptography$hazmat$primitives$asymmetric$x448, 0, 0, },
    {"cryptography.hazmat.primitives.ciphers", modulecode_cryptography$hazmat$primitives$ciphers, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.primitives.ciphers.aead", modulecode_cryptography$hazmat$primitives$ciphers$aead, 0, 0, },
    {"cryptography.hazmat.primitives.ciphers.algorithms", modulecode_cryptography$hazmat$primitives$ciphers$algorithms, 0, 0, },
    {"cryptography.hazmat.primitives.ciphers.base", modulecode_cryptography$hazmat$primitives$ciphers$base, 0, 0, },
    {"cryptography.hazmat.primitives.ciphers.modes", modulecode_cryptography$hazmat$primitives$ciphers$modes, 0, 0, },
    {"cryptography.hazmat.primitives.constant_time", modulecode_cryptography$hazmat$primitives$constant_time, 0, 0, },
    {"cryptography.hazmat.primitives.hashes", modulecode_cryptography$hazmat$primitives$hashes, 0, 0, },
    {"cryptography.hazmat.primitives.hmac", modulecode_cryptography$hazmat$primitives$hmac, 0, 0, },
    {"cryptography.hazmat.primitives.kdf", modulecode_cryptography$hazmat$primitives$kdf, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.primitives.kdf.scrypt", modulecode_cryptography$hazmat$primitives$kdf$scrypt, 0, 0, },
    {"cryptography.hazmat.primitives.padding", modulecode_cryptography$hazmat$primitives$padding, 0, 0, },
    {"cryptography.hazmat.primitives.serialization", modulecode_cryptography$hazmat$primitives$serialization, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.hazmat.primitives.serialization.base", modulecode_cryptography$hazmat$primitives$serialization$base, 0, 0, },
    {"cryptography.hazmat.primitives.serialization.pkcs7", modulecode_cryptography$hazmat$primitives$serialization$pkcs7, 0, 0, },
    {"cryptography.hazmat.primitives.serialization.ssh", modulecode_cryptography$hazmat$primitives$serialization$ssh, 0, 0, },
    {"cryptography.utils", modulecode_cryptography$utils, 0, 0, },
    {"cryptography.x509", modulecode_cryptography$x509, 0, 0, NUITKA_PACKAGE_FLAG},
    {"cryptography.x509.base", modulecode_cryptography$x509$base, 0, 0, },
    {"cryptography.x509.certificate_transparency", modulecode_cryptography$x509$certificate_transparency, 0, 0, },
    {"cryptography.x509.extensions", modulecode_cryptography$x509$extensions, 0, 0, },
    {"cryptography.x509.general_name", modulecode_cryptography$x509$general_name, 0, 0, },
    {"cryptography.x509.name", modulecode_cryptography$x509$name, 0, 0, },
    {"cryptography.x509.ocsp", modulecode_cryptography$x509$ocsp, 0, 0, },
    {"cryptography.x509.oid", modulecode_cryptography$x509$oid, 0, 0, },
    {"csv", NULL, 9, 11875, NUITKA_BYTECODE_FLAG},
    {"ctypes", NULL, 10, 16328, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"ctypes.util", NULL, 11, 8026, NUITKA_BYTECODE_FLAG},
    {"datetime", NULL, 12, 57138, NUITKA_BYTECODE_FLAG},
    {"distutils", NULL, 13, 340, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"distutils.sysconfig", NULL, 14, 12066, NUITKA_BYTECODE_FLAG},
    {"dummy_threading", NULL, 15, 1075, NUITKA_BYTECODE_FLAG},
    {"email", NULL, 16, 1647, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"email.errors", NULL, 17, 5870, NUITKA_BYTECODE_FLAG},
    {"email.utils", NULL, 18, 9507, NUITKA_BYTECODE_FLAG},
    {"encodings", NULL, 19, 3859, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"encodings.idna", NULL, 20, 5582, NUITKA_BYTECODE_FLAG},
    {"enum", NULL, 21, 25899, NUITKA_BYTECODE_FLAG},
    {"filetype", modulecode_filetype, 0, 0, NUITKA_PACKAGE_FLAG},
    {"filetype.filetype", modulecode_filetype$filetype, 0, 0, },
    {"filetype.helpers", modulecode_filetype$helpers, 0, 0, },
    {"filetype.match", modulecode_filetype$match, 0, 0, },
    {"filetype.types", modulecode_filetype$types, 0, 0, NUITKA_PACKAGE_FLAG},
    {"filetype.types.archive", modulecode_filetype$types$archive, 0, 0, },
    {"filetype.types.audio", modulecode_filetype$types$audio, 0, 0, },
    {"filetype.types.base", modulecode_filetype$types$base, 0, 0, },
    {"filetype.types.font", modulecode_filetype$types$font, 0, 0, },
    {"filetype.types.image", modulecode_filetype$types$image, 0, 0, },
    {"filetype.types.isobmff", modulecode_filetype$types$isobmff, 0, 0, },
    {"filetype.types.video", modulecode_filetype$types$video, 0, 0, },
    {"filetype.utils", modulecode_filetype$utils, 0, 0, },
    {"functools", NULL, 22, 27866, NUITKA_BYTECODE_FLAG},
    {"getopt", NULL, 23, 6236, NUITKA_BYTECODE_FLAG},
    {"glob", NULL, 24, 4308, NUITKA_BYTECODE_FLAG},
    {"hashlib", NULL, 25, 6692, NUITKA_BYTECODE_FLAG},
    {"helpers", modulecode_helpers, 0, 0, },
    {"hmac", NULL, 26, 6353, NUITKA_BYTECODE_FLAG},
    {"http", NULL, 27, 6020, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"http.cookies", NULL, 28, 15233, NUITKA_BYTECODE_FLAG},
    {"idna", modulecode_idna, 0, 0, NUITKA_PACKAGE_FLAG},
    {"idna.core", modulecode_idna$core, 0, 0, },
    {"idna.idnadata", modulecode_idna$idnadata, 0, 0, },
    {"idna.intranges", modulecode_idna$intranges, 0, 0, },
    {"idna.package_data", modulecode_idna$package_data, 0, 0, },
    {"idna.uts46data", modulecode_idna$uts46data, 0, 0, },
    {"importlib", NULL, 29, 3714, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"importlib.machinery", NULL, 30, 927, NUITKA_BYTECODE_FLAG},
    {"importlib.resources", NULL, 31, 6445, NUITKA_BYTECODE_FLAG},
    {"importlib.util", NULL, 32, 9257, NUITKA_BYTECODE_FLAG},
    {"inspect", NULL, 33, 80558, NUITKA_BYTECODE_FLAG},
    {"io", NULL, 34, 3419, NUITKA_BYTECODE_FLAG},
    {"ipaddress", NULL, 35, 59533, NUITKA_BYTECODE_FLAG},
    {"json", NULL, 36, 12564, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"keyword", NULL, 37, 963, NUITKA_BYTECODE_FLAG},
    {"locale", NULL, 38, 34654, NUITKA_BYTECODE_FLAG},
    {"logging", NULL, 39, 65069, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"magic", modulecode_magic, 0, 0, NUITKA_PACKAGE_FLAG},
    {"magic.magic", modulecode_magic$magic, 0, 0, },
    {"mimetypes", NULL, 40, 15996, NUITKA_BYTECODE_FLAG},
    {"netrc", NULL, 41, 3742, NUITKA_BYTECODE_FLAG},
    {"ntpath", NULL, 42, 14622, NUITKA_BYTECODE_FLAG},
    {"operator", NULL, 43, 13656, NUITKA_BYTECODE_FLAG},
    {"optparse", NULL, 44, 48022, NUITKA_BYTECODE_FLAG},
    {"ordlookup", modulecode_ordlookup, 0, 0, NUITKA_PACKAGE_FLAG},
    {"ordlookup.oleaut32", modulecode_ordlookup$oleaut32, 0, 0, },
    {"ordlookup.ws2_32", modulecode_ordlookup$ws2_32, 0, 0, },
    {"outputdebugstring", modulecode_outputdebugstring, 0, 0, },
    {"pathlib", NULL, 45, 43899, NUITKA_BYTECODE_FLAG},
    {"pefile", modulecode_pefile, 0, 0, },
    {"pickle", NULL, 46, 46873, NUITKA_BYTECODE_FLAG},
    {"platform", NULL, 47, 24205, NUITKA_BYTECODE_FLAG},
    {"pprint", NULL, 48, 16246, NUITKA_BYTECODE_FLAG},
    {"psutil", modulecode_psutil, 0, 0, NUITKA_PACKAGE_FLAG},
    {"psutil._common", modulecode_psutil$_common, 0, 0, },
    {"psutil._compat", modulecode_psutil$_compat, 0, 0, },
    {"psutil._psaix", modulecode_psutil$_psaix, 0, 0, },
    {"psutil._psbsd", modulecode_psutil$_psbsd, 0, 0, },
    {"psutil._pslinux", modulecode_psutil$_pslinux, 0, 0, },
    {"psutil._psosx", modulecode_psutil$_psosx, 0, 0, },
    {"psutil._psposix", modulecode_psutil$_psposix, 0, 0, },
    {"psutil._pssunos", modulecode_psutil$_pssunos, 0, 0, },
    {"psutil._psutil_windows", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"psutil._pswindows", modulecode_psutil$_pswindows, 0, 0, },
    {"pyAesCrypt", modulecode_pyAesCrypt, 0, 0, NUITKA_PACKAGE_FLAG},
    {"pyAesCrypt.crypto", modulecode_pyAesCrypt$crypto, 0, 0, },
    {"pyexpat", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"pythoncom", modulecode_pythoncom, 0, 0, },
    {"pywin", modulecode_pywin, 0, 0, NUITKA_PACKAGE_FLAG},
    {"pywin.dialogs", modulecode_pywin$dialogs, 0, 0, NUITKA_PACKAGE_FLAG},
    {"pywin.dialogs.list", modulecode_pywin$dialogs$list, 0, 0, },
    {"pywin.dialogs.status", modulecode_pywin$dialogs$status, 0, 0, },
    {"pywin.mfc", modulecode_pywin$mfc, 0, 0, NUITKA_PACKAGE_FLAG},
    {"pywin.mfc.dialog", modulecode_pywin$mfc$dialog, 0, 0, },
    {"pywin.mfc.object", modulecode_pywin$mfc$object, 0, 0, },
    {"pywin.mfc.thread", modulecode_pywin$mfc$thread, 0, 0, },
    {"pywin.mfc.window", modulecode_pywin$mfc$window, 0, 0, },
    {"pywin32_bootstrap", modulecode_pywin32_bootstrap, 0, 0, },
    {"pywintypes", modulecode_pywintypes, 0, 0, },
    {"random", NULL, 49, 20073, NUITKA_BYTECODE_FLAG},
    {"re", NULL, 50, 14387, NUITKA_BYTECODE_FLAG},
    {"requests", modulecode_requests, 0, 0, NUITKA_PACKAGE_FLAG},
    {"requests.__version__", modulecode_requests$__version__, 0, 0, },
    {"requests._internal_utils", modulecode_requests$_internal_utils, 0, 0, },
    {"requests.adapters", modulecode_requests$adapters, 0, 0, },
    {"requests.api", modulecode_requests$api, 0, 0, },
    {"requests.auth", modulecode_requests$auth, 0, 0, },
    {"requests.certs", modulecode_requests$certs, 0, 0, },
    {"requests.compat", modulecode_requests$compat, 0, 0, },
    {"requests.cookies", modulecode_requests$cookies, 0, 0, },
    {"requests.exceptions", modulecode_requests$exceptions, 0, 0, },
    {"requests.hooks", modulecode_requests$hooks, 0, 0, },
    {"requests.models", modulecode_requests$models, 0, 0, },
    {"requests.packages", modulecode_requests$packages, 0, 0, },
    {"requests.sessions", modulecode_requests$sessions, 0, 0, },
    {"requests.status_codes", modulecode_requests$status_codes, 0, 0, },
    {"requests.structures", modulecode_requests$structures, 0, 0, },
    {"requests.utils", modulecode_requests$utils, 0, 0, },
    {"select", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"shutil", NULL, 51, 36741, NUITKA_BYTECODE_FLAG},
    {"signal", NULL, 52, 2808, NUITKA_BYTECODE_FLAG},
    {"six", modulecode_six, 0, 0, },
    {"socket", NULL, 53, 27752, NUITKA_BYTECODE_FLAG},
    {"socks", modulecode_socks, 0, 0, },
    {"ssl", NULL, 54, 44561, NUITKA_BYTECODE_FLAG},
    {"stat", NULL, 55, 4337, NUITKA_BYTECODE_FLAG},
    {"string", NULL, 56, 7265, NUITKA_BYTECODE_FLAG},
    {"struct", NULL, 57, 295, NUITKA_BYTECODE_FLAG},
    {"subprocess", NULL, 58, 41905, NUITKA_BYTECODE_FLAG},
    {"tempfile", NULL, 59, 23362, NUITKA_BYTECODE_FLAG},
    {"threading", NULL, 60, 39941, NUITKA_BYTECODE_FLAG},
    {"traceback", NULL, 61, 19832, NUITKA_BYTECODE_FLAG},
    {"typing", NULL, 62, 62385, NUITKA_BYTECODE_FLAG},
    {"unicodedata", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"urllib", NULL, 63, 84, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib.parse", NULL, 64, 33959, NUITKA_BYTECODE_FLAG},
    {"urllib.request", NULL, 65, 72518, NUITKA_BYTECODE_FLAG},
    {"urllib3", modulecode_urllib3, 0, 0, NUITKA_PACKAGE_FLAG},
    {"urllib3._collections", modulecode_urllib3$_collections, 0, 0, },
    {"urllib3._version", modulecode_urllib3$_version, 0, 0, },
    {"urllib3.connection", modulecode_urllib3$connection, 0, 0, },
    {"urllib3.connectionpool", modulecode_urllib3$connectionpool, 0, 0, },
    {"urllib3.contrib", modulecode_urllib3$contrib, 0, 0, NUITKA_PACKAGE_FLAG},
    {"urllib3.contrib._appengine_environ", modulecode_urllib3$contrib$_appengine_environ, 0, 0, },
    {"urllib3.contrib.appengine", modulecode_urllib3$contrib$appengine, 0, 0, },
    {"urllib3.contrib.pyopenssl", modulecode_urllib3$contrib$pyopenssl, 0, 0, },
    {"urllib3.contrib.socks", modulecode_urllib3$contrib$socks, 0, 0, },
    {"urllib3.exceptions", modulecode_urllib3$exceptions, 0, 0, },
    {"urllib3.fields", modulecode_urllib3$fields, 0, 0, },
    {"urllib3.filepost", modulecode_urllib3$filepost, 0, 0, },
    {"urllib3.packages", modulecode_urllib3$packages, 0, 0, NUITKA_PACKAGE_FLAG},
    {"urllib3.packages.backports", modulecode_urllib3$packages$backports, 0, 0, NUITKA_PACKAGE_FLAG},
    {"urllib3.packages.backports.makefile", modulecode_urllib3$packages$backports$makefile, 0, 0, },
    {"urllib3.packages.six", modulecode_urllib3$packages$six, 0, 0, },
    {"urllib3.packages.ssl_match_hostname", modulecode_urllib3$packages$ssl_match_hostname, 0, 0, NUITKA_PACKAGE_FLAG},
    {"urllib3.packages.ssl_match_hostname._implementation", modulecode_urllib3$packages$ssl_match_hostname$_implementation, 0, 0, },
    {"urllib3.poolmanager", modulecode_urllib3$poolmanager, 0, 0, },
    {"urllib3.request", modulecode_urllib3$request, 0, 0, },
    {"urllib3.response", modulecode_urllib3$response, 0, 0, },
    {"urllib3.util", modulecode_urllib3$util, 0, 0, NUITKA_PACKAGE_FLAG},
    {"urllib3.util.connection", modulecode_urllib3$util$connection, 0, 0, },
    {"urllib3.util.proxy", modulecode_urllib3$util$proxy, 0, 0, },
    {"urllib3.util.queue", modulecode_urllib3$util$queue, 0, 0, },
    {"urllib3.util.request", modulecode_urllib3$util$request, 0, 0, },
    {"urllib3.util.response", modulecode_urllib3$util$response, 0, 0, },
    {"urllib3.util.retry", modulecode_urllib3$util$retry, 0, 0, },
    {"urllib3.util.ssl_", modulecode_urllib3$util$ssl_, 0, 0, },
    {"urllib3.util.ssltransport", modulecode_urllib3$util$ssltransport, 0, 0, },
    {"urllib3.util.timeout", modulecode_urllib3$util$timeout, 0, 0, },
    {"urllib3.util.url", modulecode_urllib3$util$url, 0, 0, },
    {"urllib3.util.wait", modulecode_urllib3$util$wait, 0, 0, },
    {"var_dump", modulecode_var_dump, 0, 0, NUITKA_PACKAGE_FLAG},
    {"var_dump._var_dump", modulecode_var_dump$_var_dump, 0, 0, },
    {"warnings", NULL, 66, 13617, NUITKA_BYTECODE_FLAG},
    {"win32api", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"win32com", modulecode_win32com, 0, 0, NUITKA_PACKAGE_FLAG},
    {"win32com.client", modulecode_win32com$client, 0, 0, NUITKA_PACKAGE_FLAG},
    {"win32com.client.CLSIDToClass", modulecode_win32com$client$CLSIDToClass, 0, 0, },
    {"win32com.client.build", modulecode_win32com$client$build, 0, 0, },
    {"win32com.client.dynamic", modulecode_win32com$client$dynamic, 0, 0, },
    {"win32com.client.gencache", modulecode_win32com$client$gencache, 0, 0, },
    {"win32com.client.genpy", modulecode_win32com$client$genpy, 0, 0, },
    {"win32com.client.makepy", modulecode_win32com$client$makepy, 0, 0, },
    {"win32com.client.selecttlb", modulecode_win32com$client$selecttlb, 0, 0, },
    {"win32com.client.util", modulecode_win32com$client$util, 0, 0, },
    {"win32con", modulecode_win32con, 0, 0, },
    {"win32ui", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"winerror", modulecode_winerror, 0, 0, },
    {"wmi", modulecode_wmi, 0, 0, },
    {"xml", NULL, 67, 648, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.etree", NULL, 68, 87, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.etree.ElementTree", NULL, 69, 55599, NUITKA_BYTECODE_FLAG},
    {"yara", NULL, 0, 0, NUITKA_SHLIB_FLAG},
    {"zipfile", NULL, 70, 58479, NUITKA_BYTECODE_FLAG},
    {"__future__", NULL, 71, 4123, NUITKA_BYTECODE_FLAG},
    {"_bootlocale", NULL, 72, 1208, NUITKA_BYTECODE_FLAG},
    {"_collections_abc", NULL, 73, 28706, NUITKA_BYTECODE_FLAG},
    {"_compat_pickle", NULL, 74, 5466, NUITKA_BYTECODE_FLAG},
    {"_compression", NULL, 75, 4111, NUITKA_BYTECODE_FLAG},
    {"_dummy_thread", NULL, 76, 6002, NUITKA_BYTECODE_FLAG},
    {"_markupbase", NULL, 77, 7755, NUITKA_BYTECODE_FLAG},
    {"_osx_support", NULL, 78, 10277, NUITKA_BYTECODE_FLAG},
    {"_py_abc", NULL, 79, 4635, NUITKA_BYTECODE_FLAG},
    {"_pyio", NULL, 80, 74044, NUITKA_BYTECODE_FLAG},
    {"_sitebuiltins", NULL, 81, 3446, NUITKA_BYTECODE_FLAG},
    {"_strptime", NULL, 82, 16009, NUITKA_BYTECODE_FLAG},
    {"_threading_local", NULL, 83, 6411, NUITKA_BYTECODE_FLAG},
    {"_weakrefset", NULL, 84, 7565, NUITKA_BYTECODE_FLAG},
    {"abc", NULL, 0, 5299, NUITKA_BYTECODE_FLAG},
    {"aifc", NULL, 85, 25439, NUITKA_BYTECODE_FLAG},
    {"argparse", NULL, 86, 62242, NUITKA_BYTECODE_FLAG},
    {"ast", NULL, 87, 16728, NUITKA_BYTECODE_FLAG},
    {"asynchat", NULL, 88, 6816, NUITKA_BYTECODE_FLAG},
    {"asyncio", NULL, 89, 706, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"asyncio.base_events", NULL, 90, 50985, NUITKA_BYTECODE_FLAG},
    {"asyncio.base_futures", NULL, 91, 1863, NUITKA_BYTECODE_FLAG},
    {"asyncio.base_subprocess", NULL, 92, 9381, NUITKA_BYTECODE_FLAG},
    {"asyncio.base_tasks", NULL, 93, 1909, NUITKA_BYTECODE_FLAG},
    {"asyncio.constants", NULL, 94, 546, NUITKA_BYTECODE_FLAG},
    {"asyncio.coroutines", NULL, 95, 6619, NUITKA_BYTECODE_FLAG},
    {"asyncio.events", NULL, 96, 28022, NUITKA_BYTECODE_FLAG},
    {"asyncio.exceptions", NULL, 97, 2514, NUITKA_BYTECODE_FLAG},
    {"asyncio.format_helpers", NULL, 98, 2297, NUITKA_BYTECODE_FLAG},
    {"asyncio.futures", NULL, 99, 11158, NUITKA_BYTECODE_FLAG},
    {"asyncio.locks", NULL, 100, 16333, NUITKA_BYTECODE_FLAG},
    {"asyncio.log", NULL, 101, 191, NUITKA_BYTECODE_FLAG},
    {"asyncio.proactor_events", NULL, 102, 24110, NUITKA_BYTECODE_FLAG},
    {"asyncio.protocols", NULL, 103, 8579, NUITKA_BYTECODE_FLAG},
    {"asyncio.queues", NULL, 104, 8346, NUITKA_BYTECODE_FLAG},
    {"asyncio.runners", NULL, 105, 1912, NUITKA_BYTECODE_FLAG},
    {"asyncio.selector_events", NULL, 106, 29650, NUITKA_BYTECODE_FLAG},
    {"asyncio.sslproto", NULL, 107, 21583, NUITKA_BYTECODE_FLAG},
    {"asyncio.staggered", NULL, 108, 4083, NUITKA_BYTECODE_FLAG},
    {"asyncio.streams", NULL, 109, 20605, NUITKA_BYTECODE_FLAG},
    {"asyncio.subprocess", NULL, 110, 7323, NUITKA_BYTECODE_FLAG},
    {"asyncio.tasks", NULL, 111, 24246, NUITKA_BYTECODE_FLAG},
    {"asyncio.transports", NULL, 112, 12227, NUITKA_BYTECODE_FLAG},
    {"asyncio.trsock", NULL, 113, 8448, NUITKA_BYTECODE_FLAG},
    {"asyncio.windows_events", NULL, 114, 24548, NUITKA_BYTECODE_FLAG},
    {"asyncio.windows_utils", NULL, 115, 4436, NUITKA_BYTECODE_FLAG},
    {"asyncore", NULL, 116, 15993, NUITKA_BYTECODE_FLAG},
    {"base64", NULL, 1, 17036, NUITKA_BYTECODE_FLAG},
    {"bdb", NULL, 117, 24886, NUITKA_BYTECODE_FLAG},
    {"binhex", NULL, 118, 12099, NUITKA_BYTECODE_FLAG},
    {"bisect", NULL, 2, 2319, NUITKA_BYTECODE_FLAG},
    {"bz2", NULL, 119, 11410, NUITKA_BYTECODE_FLAG},
    {"cProfile", NULL, 120, 5340, NUITKA_BYTECODE_FLAG},
    {"calendar", NULL, 3, 27029, NUITKA_BYTECODE_FLAG},
    {"cgi", NULL, 121, 26272, NUITKA_BYTECODE_FLAG},
    {"cgitb", NULL, 122, 10115, NUITKA_BYTECODE_FLAG},
    {"chunk", NULL, 123, 4804, NUITKA_BYTECODE_FLAG},
    {"cmd", NULL, 124, 12591, NUITKA_BYTECODE_FLAG},
    {"code", NULL, 125, 9878, NUITKA_BYTECODE_FLAG},
    {"codecs", NULL, 4, 33921, NUITKA_BYTECODE_FLAG},
    {"codeop", NULL, 126, 6382, NUITKA_BYTECODE_FLAG},
    {"collections", NULL, 5, 46391, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"collections.abc", NULL, 127, 28705, NUITKA_BYTECODE_FLAG},
    {"colorsys", NULL, 128, 3205, NUITKA_BYTECODE_FLAG},
    {"compileall", NULL, 129, 9375, NUITKA_BYTECODE_FLAG},
    {"concurrent", NULL, 130, 88, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"concurrent.futures", NULL, 131, 1064, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"concurrent.futures._base", NULL, 132, 21865, NUITKA_BYTECODE_FLAG},
    {"concurrent.futures.process", NULL, 133, 20265, NUITKA_BYTECODE_FLAG},
    {"concurrent.futures.thread", NULL, 134, 5783, NUITKA_BYTECODE_FLAG},
    {"configparser", NULL, 6, 45683, NUITKA_BYTECODE_FLAG},
    {"contextlib", NULL, 7, 20194, NUITKA_BYTECODE_FLAG},
    {"contextvars", NULL, 135, 208, NUITKA_BYTECODE_FLAG},
    {"copy", NULL, 8, 6952, NUITKA_BYTECODE_FLAG},
    {"copyreg", NULL, 136, 4283, NUITKA_BYTECODE_FLAG},
    {"csv", NULL, 9, 11875, NUITKA_BYTECODE_FLAG},
    {"ctypes", NULL, 10, 16328, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"ctypes._aix", NULL, 137, 9809, NUITKA_BYTECODE_FLAG},
    {"ctypes._endian", NULL, 138, 1894, NUITKA_BYTECODE_FLAG},
    {"ctypes.macholib", NULL, 139, 255, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"ctypes.macholib.dyld", NULL, 140, 4342, NUITKA_BYTECODE_FLAG},
    {"ctypes.macholib.dylib", NULL, 141, 1881, NUITKA_BYTECODE_FLAG},
    {"ctypes.macholib.framework", NULL, 142, 2161, NUITKA_BYTECODE_FLAG},
    {"ctypes.util", NULL, 11, 8026, NUITKA_BYTECODE_FLAG},
    {"ctypes.wintypes", NULL, 143, 5068, NUITKA_BYTECODE_FLAG},
    {"dataclasses", NULL, 144, 23592, NUITKA_BYTECODE_FLAG},
    {"datetime", NULL, 12, 57138, NUITKA_BYTECODE_FLAG},
    {"dbm", NULL, 145, 4148, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"dbm.dumb", NULL, 146, 7738, NUITKA_BYTECODE_FLAG},
    {"decimal", NULL, 147, 160697, NUITKA_BYTECODE_FLAG},
    {"difflib", NULL, 148, 59403, NUITKA_BYTECODE_FLAG},
    {"dis", NULL, 149, 15773, NUITKA_BYTECODE_FLAG},
    {"distutils", NULL, 13, 340, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"distutils._msvccompiler", NULL, 150, 12931, NUITKA_BYTECODE_FLAG},
    {"distutils.archive_util", NULL, 151, 6504, NUITKA_BYTECODE_FLAG},
    {"distutils.bcppcompiler", NULL, 152, 6488, NUITKA_BYTECODE_FLAG},
    {"distutils.ccompiler", NULL, 153, 33262, NUITKA_BYTECODE_FLAG},
    {"distutils.cmd", NULL, 154, 13913, NUITKA_BYTECODE_FLAG},
    {"distutils.command", NULL, 155, 499, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"distutils.command.bdist", NULL, 156, 3631, NUITKA_BYTECODE_FLAG},
    {"distutils.command.bdist_dumb", NULL, 157, 3557, NUITKA_BYTECODE_FLAG},
    {"distutils.command.bdist_msi", NULL, 158, 19588, NUITKA_BYTECODE_FLAG},
    {"distutils.command.bdist_rpm", NULL, 159, 12393, NUITKA_BYTECODE_FLAG},
    {"distutils.command.bdist_wininst", NULL, 160, 8454, NUITKA_BYTECODE_FLAG},
    {"distutils.command.build", NULL, 161, 3846, NUITKA_BYTECODE_FLAG},
    {"distutils.command.build_clib", NULL, 162, 4779, NUITKA_BYTECODE_FLAG},
    {"distutils.command.build_ext", NULL, 163, 16102, NUITKA_BYTECODE_FLAG},
    {"distutils.command.build_py", NULL, 164, 10445, NUITKA_BYTECODE_FLAG},
    {"distutils.command.build_scripts", NULL, 165, 4289, NUITKA_BYTECODE_FLAG},
    {"distutils.command.check", NULL, 166, 4850, NUITKA_BYTECODE_FLAG},
    {"distutils.command.clean", NULL, 167, 2065, NUITKA_BYTECODE_FLAG},
    {"distutils.command.config", NULL, 168, 10192, NUITKA_BYTECODE_FLAG},
    {"distutils.command.install", NULL, 169, 13537, NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_data", NULL, 170, 2254, NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_egg_info", NULL, 171, 2961, NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_headers", NULL, 172, 1673, NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_lib", NULL, 173, 5078, NUITKA_BYTECODE_FLAG},
    {"distutils.command.install_scripts", NULL, 174, 2106, NUITKA_BYTECODE_FLAG},
    {"distutils.command.register", NULL, 175, 8420, NUITKA_BYTECODE_FLAG},
    {"distutils.command.sdist", NULL, 176, 14481, NUITKA_BYTECODE_FLAG},
    {"distutils.command.upload", NULL, 177, 4904, NUITKA_BYTECODE_FLAG},
    {"distutils.config", NULL, 178, 3474, NUITKA_BYTECODE_FLAG},
    {"distutils.core", NULL, 179, 6579, NUITKA_BYTECODE_FLAG},
    {"distutils.cygwinccompiler", NULL, 180, 8577, NUITKA_BYTECODE_FLAG},
    {"distutils.debug", NULL, 181, 159, NUITKA_BYTECODE_FLAG},
    {"distutils.dep_util", NULL, 182, 2679, NUITKA_BYTECODE_FLAG},
    {"distutils.dir_util", NULL, 183, 5788, NUITKA_BYTECODE_FLAG},
    {"distutils.dist", NULL, 184, 34457, NUITKA_BYTECODE_FLAG},
    {"distutils.errors", NULL, 185, 5215, NUITKA_BYTECODE_FLAG},
    {"distutils.extension", NULL, 186, 6888, NUITKA_BYTECODE_FLAG},
    {"distutils.fancy_getopt", NULL, 187, 10621, NUITKA_BYTECODE_FLAG},
    {"distutils.file_util", NULL, 188, 5898, NUITKA_BYTECODE_FLAG},
    {"distutils.filelist", NULL, 189, 9832, NUITKA_BYTECODE_FLAG},
    {"distutils.log", NULL, 190, 2280, NUITKA_BYTECODE_FLAG},
    {"distutils.msvc9compiler", NULL, 191, 17475, NUITKA_BYTECODE_FLAG},
    {"distutils.msvccompiler", NULL, 192, 14688, NUITKA_BYTECODE_FLAG},
    {"distutils.spawn", NULL, 193, 5071, NUITKA_BYTECODE_FLAG},
    {"distutils.sysconfig", NULL, 14, 12066, NUITKA_BYTECODE_FLAG},
    {"distutils.text_file", NULL, 194, 8404, NUITKA_BYTECODE_FLAG},
    {"distutils.unixccompiler", NULL, 195, 6583, NUITKA_BYTECODE_FLAG},
    {"distutils.util", NULL, 196, 15511, NUITKA_BYTECODE_FLAG},
    {"distutils.version", NULL, 197, 7276, NUITKA_BYTECODE_FLAG},
    {"distutils.versionpredicate", NULL, 198, 5100, NUITKA_BYTECODE_FLAG},
    {"doctest", NULL, 199, 75939, NUITKA_BYTECODE_FLAG},
    {"dummy_threading", NULL, 15, 1075, NUITKA_BYTECODE_FLAG},
    {"email", NULL, 16, 1647, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"email._encoded_words", NULL, 200, 5651, NUITKA_BYTECODE_FLAG},
    {"email._header_value_parser", NULL, 201, 79898, NUITKA_BYTECODE_FLAG},
    {"email._parseaddr", NULL, 202, 12419, NUITKA_BYTECODE_FLAG},
    {"email._policybase", NULL, 203, 14775, NUITKA_BYTECODE_FLAG},
    {"email.base64mime", NULL, 204, 3200, NUITKA_BYTECODE_FLAG},
    {"email.charset", NULL, 205, 11424, NUITKA_BYTECODE_FLAG},
    {"email.contentmanager", NULL, 206, 7326, NUITKA_BYTECODE_FLAG},
    {"email.encoders", NULL, 207, 1577, NUITKA_BYTECODE_FLAG},
    {"email.errors", NULL, 17, 5870, NUITKA_BYTECODE_FLAG},
    {"email.feedparser", NULL, 208, 10607, NUITKA_BYTECODE_FLAG},
    {"email.generator", NULL, 209, 12489, NUITKA_BYTECODE_FLAG},
    {"email.header", NULL, 210, 16404, NUITKA_BYTECODE_FLAG},
    {"email.headerregistry", NULL, 211, 22009, NUITKA_BYTECODE_FLAG},
    {"email.iterators", NULL, 212, 1885, NUITKA_BYTECODE_FLAG},
    {"email.message", NULL, 213, 37843, NUITKA_BYTECODE_FLAG},
    {"email.mime", NULL, 214, 88, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"email.mime.application", NULL, 215, 1424, NUITKA_BYTECODE_FLAG},
    {"email.mime.audio", NULL, 216, 2589, NUITKA_BYTECODE_FLAG},
    {"email.mime.base", NULL, 217, 1006, NUITKA_BYTECODE_FLAG},
    {"email.mime.image", NULL, 218, 1869, NUITKA_BYTECODE_FLAG},
    {"email.mime.message", NULL, 219, 1247, NUITKA_BYTECODE_FLAG},
    {"email.mime.multipart", NULL, 220, 1467, NUITKA_BYTECODE_FLAG},
    {"email.mime.nonmultipart", NULL, 221, 729, NUITKA_BYTECODE_FLAG},
    {"email.mime.text", NULL, 222, 1276, NUITKA_BYTECODE_FLAG},
    {"email.parser", NULL, 223, 5687, NUITKA_BYTECODE_FLAG},
    {"email.policy", NULL, 224, 9623, NUITKA_BYTECODE_FLAG},
    {"email.quoprimime", NULL, 225, 7643, NUITKA_BYTECODE_FLAG},
    {"email.utils", NULL, 18, 9507, NUITKA_BYTECODE_FLAG},
    {"encodings", NULL, 19, 3859, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"encodings.aliases", NULL, 226, 6295, NUITKA_BYTECODE_FLAG},
    {"encodings.ascii", NULL, 227, 1846, NUITKA_BYTECODE_FLAG},
    {"encodings.base64_codec", NULL, 228, 2364, NUITKA_BYTECODE_FLAG},
    {"encodings.big5", NULL, 229, 1374, NUITKA_BYTECODE_FLAG},
    {"encodings.big5hkscs", NULL, 230, 1384, NUITKA_BYTECODE_FLAG},
    {"encodings.bz2_codec", NULL, 231, 3255, NUITKA_BYTECODE_FLAG},
    {"encodings.charmap", NULL, 232, 2856, NUITKA_BYTECODE_FLAG},
    {"encodings.cp037", NULL, 233, 2387, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1006", NULL, 234, 2463, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1026", NULL, 235, 2391, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1125", NULL, 236, 8094, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1140", NULL, 237, 2377, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1250", NULL, 238, 2414, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1251", NULL, 239, 2411, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1252", NULL, 240, 2414, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1253", NULL, 241, 2427, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1254", NULL, 242, 2416, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1255", NULL, 243, 2435, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1256", NULL, 244, 2413, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1257", NULL, 245, 2421, NUITKA_BYTECODE_FLAG},
    {"encodings.cp1258", NULL, 246, 2419, NUITKA_BYTECODE_FLAG},
    {"encodings.cp273", NULL, 247, 2373, NUITKA_BYTECODE_FLAG},
    {"encodings.cp424", NULL, 248, 2417, NUITKA_BYTECODE_FLAG},
    {"encodings.cp437", NULL, 249, 7811, NUITKA_BYTECODE_FLAG},
    {"encodings.cp500", NULL, 250, 2387, NUITKA_BYTECODE_FLAG},
    {"encodings.cp720", NULL, 251, 2484, NUITKA_BYTECODE_FLAG},
    {"encodings.cp737", NULL, 252, 8133, NUITKA_BYTECODE_FLAG},
    {"encodings.cp775", NULL, 253, 7841, NUITKA_BYTECODE_FLAG},
    {"encodings.cp850", NULL, 254, 7472, NUITKA_BYTECODE_FLAG},
    {"encodings.cp852", NULL, 255, 7849, NUITKA_BYTECODE_FLAG},
    {"encodings.cp855", NULL, 256, 8102, NUITKA_BYTECODE_FLAG},
    {"encodings.cp856", NULL, 257, 2449, NUITKA_BYTECODE_FLAG},
    {"encodings.cp857", NULL, 258, 7452, NUITKA_BYTECODE_FLAG},
    {"encodings.cp858", NULL, 259, 7442, NUITKA_BYTECODE_FLAG},
    {"encodings.cp860", NULL, 260, 7790, NUITKA_BYTECODE_FLAG},
    {"encodings.cp861", NULL, 261, 7805, NUITKA_BYTECODE_FLAG},
    {"encodings.cp862", NULL, 262, 7994, NUITKA_BYTECODE_FLAG},
    {"encodings.cp863", NULL, 263, 7805, NUITKA_BYTECODE_FLAG},
    {"encodings.cp864", NULL, 264, 7949, NUITKA_BYTECODE_FLAG},
    {"encodings.cp865", NULL, 265, 7805, NUITKA_BYTECODE_FLAG},
    {"encodings.cp866", NULL, 266, 8138, NUITKA_BYTECODE_FLAG},
    {"encodings.cp869", NULL, 267, 7829, NUITKA_BYTECODE_FLAG},
    {"encodings.cp874", NULL, 268, 2515, NUITKA_BYTECODE_FLAG},
    {"encodings.cp875", NULL, 269, 2384, NUITKA_BYTECODE_FLAG},
    {"encodings.cp932", NULL, 270, 1376, NUITKA_BYTECODE_FLAG},
    {"encodings.cp949", NULL, 271, 1376, NUITKA_BYTECODE_FLAG},
    {"encodings.cp950", NULL, 272, 1376, NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jis_2004", NULL, 273, 1390, NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jisx0213", NULL, 274, 1390, NUITKA_BYTECODE_FLAG},
    {"encodings.euc_jp", NULL, 275, 1378, NUITKA_BYTECODE_FLAG},
    {"encodings.euc_kr", NULL, 276, 1378, NUITKA_BYTECODE_FLAG},
    {"encodings.gb18030", NULL, 277, 1380, NUITKA_BYTECODE_FLAG},
    {"encodings.gb2312", NULL, 278, 1378, NUITKA_BYTECODE_FLAG},
    {"encodings.gbk", NULL, 279, 1372, NUITKA_BYTECODE_FLAG},
    {"encodings.hex_codec", NULL, 280, 2351, NUITKA_BYTECODE_FLAG},
    {"encodings.hp_roman8", NULL, 281, 2588, NUITKA_BYTECODE_FLAG},
    {"encodings.hz", NULL, 282, 1370, NUITKA_BYTECODE_FLAG},
    {"encodings.idna", NULL, 20, 5582, NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp", NULL, 283, 1391, NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_1", NULL, 284, 1395, NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_2", NULL, 285, 1395, NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_2004", NULL, 286, 1401, NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_3", NULL, 287, 1395, NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_jp_ext", NULL, 288, 1399, NUITKA_BYTECODE_FLAG},
    {"encodings.iso2022_kr", NULL, 289, 1391, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_1", NULL, 290, 2386, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_10", NULL, 291, 2391, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_11", NULL, 292, 2485, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_13", NULL, 293, 2394, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_14", NULL, 294, 2412, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_15", NULL, 295, 2391, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_16", NULL, 296, 2393, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_2", NULL, 297, 2386, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_3", NULL, 298, 2393, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_4", NULL, 299, 2386, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_5", NULL, 300, 2387, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_6", NULL, 301, 2431, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_7", NULL, 302, 2394, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_8", NULL, 303, 2425, NUITKA_BYTECODE_FLAG},
    {"encodings.iso8859_9", NULL, 304, 2386, NUITKA_BYTECODE_FLAG},
    {"encodings.johab", NULL, 305, 1376, NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_r", NULL, 306, 2438, NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_t", NULL, 307, 2349, NUITKA_BYTECODE_FLAG},
    {"encodings.koi8_u", NULL, 308, 2424, NUITKA_BYTECODE_FLAG},
    {"encodings.kz1048", NULL, 309, 2401, NUITKA_BYTECODE_FLAG},
    {"encodings.latin_1", NULL, 310, 1858, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_arabic", NULL, 311, 7705, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_centeuro", NULL, 312, 2425, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_croatian", NULL, 313, 2433, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_cyrillic", NULL, 314, 2423, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_farsi", NULL, 315, 2367, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_greek", NULL, 316, 2407, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_iceland", NULL, 317, 2426, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_latin2", NULL, 318, 2567, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_roman", NULL, 319, 2424, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_romanian", NULL, 320, 2434, NUITKA_BYTECODE_FLAG},
    {"encodings.mac_turkish", NULL, 321, 2427, NUITKA_BYTECODE_FLAG},
    {"encodings.mbcs", NULL, 322, 1676, NUITKA_BYTECODE_FLAG},
    {"encodings.oem", NULL, 323, 1489, NUITKA_BYTECODE_FLAG},
    {"encodings.palmos", NULL, 324, 2414, NUITKA_BYTECODE_FLAG},
    {"encodings.ptcp154", NULL, 325, 2508, NUITKA_BYTECODE_FLAG},
    {"encodings.punycode", NULL, 326, 6280, NUITKA_BYTECODE_FLAG},
    {"encodings.quopri_codec", NULL, 327, 2380, NUITKA_BYTECODE_FLAG},
    {"encodings.raw_unicode_escape", NULL, 328, 1727, NUITKA_BYTECODE_FLAG},
    {"encodings.rot_13", NULL, 329, 2966, NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jis", NULL, 330, 1384, NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jis_2004", NULL, 331, 1394, NUITKA_BYTECODE_FLAG},
    {"encodings.shift_jisx0213", NULL, 332, 1394, NUITKA_BYTECODE_FLAG},
    {"encodings.tis_620", NULL, 333, 2476, NUITKA_BYTECODE_FLAG},
    {"encodings.undefined", NULL, 334, 2060, NUITKA_BYTECODE_FLAG},
    {"encodings.unicode_escape", NULL, 335, 1707, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16", NULL, 336, 4837, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16_be", NULL, 337, 1615, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_16_le", NULL, 338, 1615, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32", NULL, 339, 4730, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32_be", NULL, 340, 1508, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_32_le", NULL, 341, 1508, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_7", NULL, 342, 1536, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_8", NULL, 343, 1595, NUITKA_BYTECODE_FLAG},
    {"encodings.utf_8_sig", NULL, 344, 4511, NUITKA_BYTECODE_FLAG},
    {"encodings.uu_codec", NULL, 345, 3214, NUITKA_BYTECODE_FLAG},
    {"encodings.zlib_codec", NULL, 346, 3074, NUITKA_BYTECODE_FLAG},
    {"enum", NULL, 21, 25899, NUITKA_BYTECODE_FLAG},
    {"filecmp", NULL, 347, 8392, NUITKA_BYTECODE_FLAG},
    {"fileinput", NULL, 348, 13338, NUITKA_BYTECODE_FLAG},
    {"fnmatch", NULL, 349, 3297, NUITKA_BYTECODE_FLAG},
    {"formatter", NULL, 350, 17510, NUITKA_BYTECODE_FLAG},
    {"fractions", NULL, 351, 18704, NUITKA_BYTECODE_FLAG},
    {"ftplib", NULL, 352, 27814, NUITKA_BYTECODE_FLAG},
    {"functools", NULL, 22, 27866, NUITKA_BYTECODE_FLAG},
    {"genericpath", NULL, 353, 3966, NUITKA_BYTECODE_FLAG},
    {"getopt", NULL, 23, 6236, NUITKA_BYTECODE_FLAG},
    {"getpass", NULL, 354, 4143, NUITKA_BYTECODE_FLAG},
    {"gettext", NULL, 355, 17848, NUITKA_BYTECODE_FLAG},
    {"glob", NULL, 24, 4308, NUITKA_BYTECODE_FLAG},
    {"gzip", NULL, 356, 18156, NUITKA_BYTECODE_FLAG},
    {"hashlib", NULL, 25, 6692, NUITKA_BYTECODE_FLAG},
    {"heapq", NULL, 357, 14035, NUITKA_BYTECODE_FLAG},
    {"hmac", NULL, 26, 6353, NUITKA_BYTECODE_FLAG},
    {"html", NULL, 358, 3574, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"html.entities", NULL, 359, 50494, NUITKA_BYTECODE_FLAG},
    {"html.parser", NULL, 360, 11163, NUITKA_BYTECODE_FLAG},
    {"http", NULL, 27, 6020, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"http.client", NULL, 361, 34651, NUITKA_BYTECODE_FLAG},
    {"http.cookiejar", NULL, 362, 53607, NUITKA_BYTECODE_FLAG},
    {"http.cookies", NULL, 28, 15233, NUITKA_BYTECODE_FLAG},
    {"http.server", NULL, 363, 34357, NUITKA_BYTECODE_FLAG},
    {"imaplib", NULL, 364, 41307, NUITKA_BYTECODE_FLAG},
    {"imghdr", NULL, 365, 4083, NUITKA_BYTECODE_FLAG},
    {"imp", NULL, 366, 9774, NUITKA_BYTECODE_FLAG},
    {"importlib", NULL, 29, 3714, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"importlib._bootstrap", NULL, 367, 28570, NUITKA_BYTECODE_FLAG},
    {"importlib._bootstrap_external", NULL, 368, 43675, NUITKA_BYTECODE_FLAG},
    {"importlib.abc", NULL, 369, 13538, NUITKA_BYTECODE_FLAG},
    {"importlib.machinery", NULL, 30, 927, NUITKA_BYTECODE_FLAG},
    {"importlib.metadata", NULL, 370, 20841, NUITKA_BYTECODE_FLAG},
    {"importlib.resources", NULL, 31, 6445, NUITKA_BYTECODE_FLAG},
    {"importlib.util", NULL, 32, 9257, NUITKA_BYTECODE_FLAG},
    {"inspect", NULL, 33, 80558, NUITKA_BYTECODE_FLAG},
    {"io", NULL, 34, 3419, NUITKA_BYTECODE_FLAG},
    {"ipaddress", NULL, 35, 59533, NUITKA_BYTECODE_FLAG},
    {"json", NULL, 36, 12564, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"json.decoder", NULL, 371, 9809, NUITKA_BYTECODE_FLAG},
    {"json.encoder", NULL, 372, 11136, NUITKA_BYTECODE_FLAG},
    {"json.scanner", NULL, 373, 1916, NUITKA_BYTECODE_FLAG},
    {"json.tool", NULL, 374, 1861, NUITKA_BYTECODE_FLAG},
    {"keyword", NULL, 37, 963, NUITKA_BYTECODE_FLAG},
    {"lib2to3", NULL, 375, 85, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"lib2to3.btm_matcher", NULL, 376, 4842, NUITKA_BYTECODE_FLAG},
    {"lib2to3.btm_utils", NULL, 377, 6115, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixer_base", NULL, 378, 6218, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixer_util", NULL, 379, 12163, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes", NULL, 380, 91, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"lib2to3.fixes.fix_apply", NULL, 381, 1638, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_asserts", NULL, 382, 1237, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_basestring", NULL, 383, 621, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_buffer", NULL, 384, 766, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_dict", NULL, 385, 3293, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_except", NULL, 386, 2776, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_exec", NULL, 387, 1107, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_execfile", NULL, 388, 1655, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_exitfunc", NULL, 389, 2264, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_filter", NULL, 390, 2402, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_funcattrs", NULL, 391, 934, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_future", NULL, 392, 742, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_getcwdu", NULL, 393, 746, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_has_key", NULL, 394, 2897, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_idioms", NULL, 395, 3879, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_import", NULL, 396, 2745, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_imports", NULL, 397, 4353, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_imports2", NULL, 398, 504, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_input", NULL, 399, 908, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_intern", NULL, 400, 1092, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_isinstance", NULL, 401, 1509, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_itertools", NULL, 402, 1508, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_itertools_imports", NULL, 403, 1536, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_long", NULL, 404, 663, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_map", NULL, 405, 3055, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_metaclass", NULL, 406, 5305, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_methodattrs", NULL, 407, 896, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_ne", NULL, 408, 769, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_next", NULL, 409, 3041, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_nonzero", NULL, 410, 881, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_numliterals", NULL, 411, 981, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_operator", NULL, 412, 4178, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_paren", NULL, 413, 1348, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_print", NULL, 414, 2301, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_raise", NULL, 415, 2211, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_raw_input", NULL, 416, 753, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_reduce", NULL, 417, 1086, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_reload", NULL, 418, 1104, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_renames", NULL, 419, 1965, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_repr", NULL, 420, 803, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_set_literal", NULL, 421, 1641, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_standarderror", NULL, 422, 678, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_sys_exc", NULL, 423, 1369, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_throw", NULL, 424, 1766, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_tuple_params", NULL, 425, 4549, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_types", NULL, 426, 1795, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_unicode", NULL, 427, 1507, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_urllib", NULL, 428, 5957, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_ws_comma", NULL, 429, 1077, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_xrange", NULL, 430, 2487, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_xreadlines", NULL, 431, 1081, NUITKA_BYTECODE_FLAG},
    {"lib2to3.fixes.fix_zip", NULL, 432, 1541, NUITKA_BYTECODE_FLAG},
    {"lib2to3.main", NULL, 433, 8573, NUITKA_BYTECODE_FLAG},
    {"lib2to3.patcomp", NULL, 434, 5604, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2", NULL, 435, 121, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"lib2to3.pgen2.driver", NULL, 436, 5106, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.grammar", NULL, 437, 5630, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.literals", NULL, 438, 1519, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.parse", NULL, 439, 6463, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.pgen", NULL, 440, 9741, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.token", NULL, 441, 1852, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pgen2.tokenize", NULL, 442, 15237, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pygram", NULL, 443, 1225, NUITKA_BYTECODE_FLAG},
    {"lib2to3.pytree", NULL, 444, 24307, NUITKA_BYTECODE_FLAG},
    {"lib2to3.refactor", NULL, 445, 20405, NUITKA_BYTECODE_FLAG},
    {"linecache", NULL, 446, 3832, NUITKA_BYTECODE_FLAG},
    {"locale", NULL, 38, 34654, NUITKA_BYTECODE_FLAG},
    {"logging", NULL, 39, 65069, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"logging.config", NULL, 447, 23189, NUITKA_BYTECODE_FLAG},
    {"logging.handlers", NULL, 448, 43163, NUITKA_BYTECODE_FLAG},
    {"lzma", NULL, 449, 11983, NUITKA_BYTECODE_FLAG},
    {"mailbox", NULL, 450, 60229, NUITKA_BYTECODE_FLAG},
    {"mailcap", NULL, 451, 6441, NUITKA_BYTECODE_FLAG},
    {"mimetypes", NULL, 40, 15996, NUITKA_BYTECODE_FLAG},
    {"modulefinder", NULL, 452, 16080, NUITKA_BYTECODE_FLAG},
    {"msilib", NULL, 453, 15965, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"msilib.schema", NULL, 454, 52135, NUITKA_BYTECODE_FLAG},
    {"msilib.sequence", NULL, 455, 2565, NUITKA_BYTECODE_FLAG},
    {"msilib.text", NULL, 456, 8427, NUITKA_BYTECODE_FLAG},
    {"multiprocessing", NULL, 457, 618, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"multiprocessing.connection", NULL, 458, 25199, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.context", NULL, 459, 12983, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.dummy", NULL, 460, 3859, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"multiprocessing.dummy.connection", NULL, 461, 2513, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.forkserver", NULL, 462, 8324, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.heap", NULL, 463, 7602, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.managers", NULL, 464, 41511, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.pool", NULL, 465, 24990, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.popen_spawn_win32", NULL, 466, 3426, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.process", NULL, 467, 10966, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.queues", NULL, 468, 9519, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.reduction", NULL, 469, 8168, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.resource_sharer", NULL, 470, 5221, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.resource_tracker", NULL, 471, 5150, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.shared_memory", NULL, 472, 14355, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.sharedctypes", NULL, 473, 7014, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.spawn", NULL, 474, 6661, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.synchronize", NULL, 475, 11256, NUITKA_BYTECODE_FLAG},
    {"multiprocessing.util", NULL, 476, 11451, NUITKA_BYTECODE_FLAG},
    {"netrc", NULL, 41, 3742, NUITKA_BYTECODE_FLAG},
    {"nntplib", NULL, 477, 33939, NUITKA_BYTECODE_FLAG},
    {"ntpath", NULL, 42, 14622, NUITKA_BYTECODE_FLAG},
    {"nturl2path", NULL, 478, 1566, NUITKA_BYTECODE_FLAG},
    {"numbers", NULL, 479, 12167, NUITKA_BYTECODE_FLAG},
    {"opcode", NULL, 480, 5385, NUITKA_BYTECODE_FLAG},
    {"operator", NULL, 43, 13656, NUITKA_BYTECODE_FLAG},
    {"optparse", NULL, 44, 48022, NUITKA_BYTECODE_FLAG},
    {"os", NULL, 481, 31362, NUITKA_BYTECODE_FLAG},
    {"pathlib", NULL, 45, 43899, NUITKA_BYTECODE_FLAG},
    {"pdb", NULL, 482, 47157, NUITKA_BYTECODE_FLAG},
    {"pickle", NULL, 46, 46873, NUITKA_BYTECODE_FLAG},
    {"pickletools", NULL, 483, 67169, NUITKA_BYTECODE_FLAG},
    {"pipes", NULL, 484, 7760, NUITKA_BYTECODE_FLAG},
    {"pkgutil", NULL, 485, 16274, NUITKA_BYTECODE_FLAG},
    {"platform", NULL, 47, 24205, NUITKA_BYTECODE_FLAG},
    {"plistlib", NULL, 486, 27130, NUITKA_BYTECODE_FLAG},
    {"poplib", NULL, 487, 13424, NUITKA_BYTECODE_FLAG},
    {"posixpath", NULL, 488, 10393, NUITKA_BYTECODE_FLAG},
    {"pprint", NULL, 48, 16246, NUITKA_BYTECODE_FLAG},
    {"profile", NULL, 489, 14618, NUITKA_BYTECODE_FLAG},
    {"pstats", NULL, 490, 22031, NUITKA_BYTECODE_FLAG},
    {"py_compile", NULL, 491, 7317, NUITKA_BYTECODE_FLAG},
    {"pyclbr", NULL, 492, 10416, NUITKA_BYTECODE_FLAG},
    {"pydoc", NULL, 493, 84052, NUITKA_BYTECODE_FLAG},
    {"pydoc_data", NULL, 494, 88, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"pydoc_data.topics", NULL, 495, 425081, NUITKA_BYTECODE_FLAG},
    {"queue", NULL, 496, 10591, NUITKA_BYTECODE_FLAG},
    {"quopri", NULL, 497, 5713, NUITKA_BYTECODE_FLAG},
    {"random", NULL, 49, 20073, NUITKA_BYTECODE_FLAG},
    {"re", NULL, 50, 14387, NUITKA_BYTECODE_FLAG},
    {"reprlib", NULL, 498, 5268, NUITKA_BYTECODE_FLAG},
    {"rlcompleter", NULL, 499, 5720, NUITKA_BYTECODE_FLAG},
    {"runpy", NULL, 500, 8146, NUITKA_BYTECODE_FLAG},
    {"sched", NULL, 501, 6497, NUITKA_BYTECODE_FLAG},
    {"secrets", NULL, 502, 2155, NUITKA_BYTECODE_FLAG},
    {"selectors", NULL, 503, 16900, NUITKA_BYTECODE_FLAG},
    {"shelve", NULL, 504, 9455, NUITKA_BYTECODE_FLAG},
    {"shlex", NULL, 505, 7501, NUITKA_BYTECODE_FLAG},
    {"shutil", NULL, 51, 36741, NUITKA_BYTECODE_FLAG},
    {"signal", NULL, 52, 2808, NUITKA_BYTECODE_FLAG},
    {"site", NULL, 506, 13237, NUITKA_BYTECODE_FLAG},
    {"smtpd", NULL, 507, 26428, NUITKA_BYTECODE_FLAG},
    {"smtplib", NULL, 508, 35248, NUITKA_BYTECODE_FLAG},
    {"sndhdr", NULL, 509, 6954, NUITKA_BYTECODE_FLAG},
    {"socket", NULL, 53, 27752, NUITKA_BYTECODE_FLAG},
    {"socketserver", NULL, 510, 23972, NUITKA_BYTECODE_FLAG},
    {"sqlite3", NULL, 511, 116, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"sqlite3.dbapi2", NULL, 512, 2469, NUITKA_BYTECODE_FLAG},
    {"sqlite3.dump", NULL, 513, 1894, NUITKA_BYTECODE_FLAG},
    {"sre_compile", NULL, 514, 15107, NUITKA_BYTECODE_FLAG},
    {"sre_constants", NULL, 515, 6324, NUITKA_BYTECODE_FLAG},
    {"sre_parse", NULL, 516, 21612, NUITKA_BYTECODE_FLAG},
    {"ssl", NULL, 54, 44561, NUITKA_BYTECODE_FLAG},
    {"stat", NULL, 55, 4337, NUITKA_BYTECODE_FLAG},
    {"statistics", NULL, 517, 33618, NUITKA_BYTECODE_FLAG},
    {"string", NULL, 56, 7265, NUITKA_BYTECODE_FLAG},
    {"stringprep", NULL, 518, 10982, NUITKA_BYTECODE_FLAG},
    {"struct", NULL, 57, 295, NUITKA_BYTECODE_FLAG},
    {"subprocess", NULL, 58, 41905, NUITKA_BYTECODE_FLAG},
    {"sunau", NULL, 519, 17045, NUITKA_BYTECODE_FLAG},
    {"symbol", NULL, 520, 2369, NUITKA_BYTECODE_FLAG},
    {"symtable", NULL, 521, 11287, NUITKA_BYTECODE_FLAG},
    {"sysconfig", NULL, 522, 15633, NUITKA_BYTECODE_FLAG},
    {"tabnanny", NULL, 523, 6995, NUITKA_BYTECODE_FLAG},
    {"tarfile", NULL, 524, 62626, NUITKA_BYTECODE_FLAG},
    {"telnetlib", NULL, 525, 18202, NUITKA_BYTECODE_FLAG},
    {"tempfile", NULL, 59, 23362, NUITKA_BYTECODE_FLAG},
    {"textwrap", NULL, 526, 13484, NUITKA_BYTECODE_FLAG},
    {"this", NULL, 527, 1226, NUITKA_BYTECODE_FLAG},
    {"threading", NULL, 60, 39941, NUITKA_BYTECODE_FLAG},
    {"timeit", NULL, 528, 11742, NUITKA_BYTECODE_FLAG},
    {"tkinter", NULL, 529, 176253, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"tkinter.colorchooser", NULL, 530, 1090, NUITKA_BYTECODE_FLAG},
    {"tkinter.commondialog", NULL, 531, 1077, NUITKA_BYTECODE_FLAG},
    {"tkinter.constants", NULL, 532, 1619, NUITKA_BYTECODE_FLAG},
    {"tkinter.dialog", NULL, 533, 1437, NUITKA_BYTECODE_FLAG},
    {"tkinter.dnd", NULL, 534, 11227, NUITKA_BYTECODE_FLAG},
    {"tkinter.filedialog", NULL, 535, 12193, NUITKA_BYTECODE_FLAG},
    {"tkinter.font", NULL, 536, 6227, NUITKA_BYTECODE_FLAG},
    {"tkinter.messagebox", NULL, 537, 2956, NUITKA_BYTECODE_FLAG},
    {"tkinter.scrolledtext", NULL, 538, 2142, NUITKA_BYTECODE_FLAG},
    {"tkinter.simpledialog", NULL, 539, 10625, NUITKA_BYTECODE_FLAG},
    {"tkinter.tix", NULL, 540, 79372, NUITKA_BYTECODE_FLAG},
    {"tkinter.ttk", NULL, 541, 56663, NUITKA_BYTECODE_FLAG},
    {"token", NULL, 542, 2450, NUITKA_BYTECODE_FLAG},
    {"tokenize", NULL, 543, 17125, NUITKA_BYTECODE_FLAG},
    {"trace", NULL, 544, 19991, NUITKA_BYTECODE_FLAG},
    {"traceback", NULL, 61, 19832, NUITKA_BYTECODE_FLAG},
    {"tracemalloc", NULL, 545, 17328, NUITKA_BYTECODE_FLAG},
    {"turtle", NULL, 546, 129923, NUITKA_BYTECODE_FLAG},
    {"types", NULL, 547, 9142, NUITKA_BYTECODE_FLAG},
    {"typing", NULL, 62, 62385, NUITKA_BYTECODE_FLAG},
    {"unittest", NULL, 548, 3082, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"unittest.async_case", NULL, 549, 4148, NUITKA_BYTECODE_FLAG},
    {"unittest.case", NULL, 550, 50449, NUITKA_BYTECODE_FLAG},
    {"unittest.loader", NULL, 551, 14501, NUITKA_BYTECODE_FLAG},
    {"unittest.main", NULL, 552, 7499, NUITKA_BYTECODE_FLAG},
    {"unittest.mock", NULL, 553, 77331, NUITKA_BYTECODE_FLAG},
    {"unittest.result", NULL, 554, 7256, NUITKA_BYTECODE_FLAG},
    {"unittest.runner", NULL, 555, 6981, NUITKA_BYTECODE_FLAG},
    {"unittest.signals", NULL, 556, 2185, NUITKA_BYTECODE_FLAG},
    {"unittest.suite", NULL, 557, 9900, NUITKA_BYTECODE_FLAG},
    {"unittest.util", NULL, 558, 4396, NUITKA_BYTECODE_FLAG},
    {"urllib", NULL, 63, 84, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"urllib.error", NULL, 559, 2774, NUITKA_BYTECODE_FLAG},
    {"urllib.parse", NULL, 64, 33959, NUITKA_BYTECODE_FLAG},
    {"urllib.request", NULL, 65, 72518, NUITKA_BYTECODE_FLAG},
    {"urllib.response", NULL, 560, 3254, NUITKA_BYTECODE_FLAG},
    {"urllib.robotparser", NULL, 561, 7292, NUITKA_BYTECODE_FLAG},
    {"uu", NULL, 562, 3570, NUITKA_BYTECODE_FLAG},
    {"uuid", NULL, 563, 23648, NUITKA_BYTECODE_FLAG},
    {"venv", NULL, 564, 14387, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"warnings", NULL, 66, 13617, NUITKA_BYTECODE_FLAG},
    {"wave", NULL, 565, 18114, NUITKA_BYTECODE_FLAG},
    {"weakref", NULL, 566, 19483, NUITKA_BYTECODE_FLAG},
    {"webbrowser", NULL, 567, 17085, NUITKA_BYTECODE_FLAG},
    {"wsgiref", NULL, 568, 680, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"wsgiref.handlers", NULL, 569, 16411, NUITKA_BYTECODE_FLAG},
    {"wsgiref.headers", NULL, 570, 7721, NUITKA_BYTECODE_FLAG},
    {"wsgiref.simple_server", NULL, 571, 5226, NUITKA_BYTECODE_FLAG},
    {"wsgiref.util", NULL, 572, 5377, NUITKA_BYTECODE_FLAG},
    {"wsgiref.validate", NULL, 573, 14720, NUITKA_BYTECODE_FLAG},
    {"xdrlib", NULL, 574, 8186, NUITKA_BYTECODE_FLAG},
    {"xml", NULL, 67, 648, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.dom", NULL, 575, 5486, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.dom.NodeFilter", NULL, 576, 932, NUITKA_BYTECODE_FLAG},
    {"xml.dom.domreg", NULL, 577, 2815, NUITKA_BYTECODE_FLAG},
    {"xml.dom.expatbuilder", NULL, 578, 27306, NUITKA_BYTECODE_FLAG},
    {"xml.dom.minicompat", NULL, 579, 2707, NUITKA_BYTECODE_FLAG},
    {"xml.dom.minidom", NULL, 580, 55339, NUITKA_BYTECODE_FLAG},
    {"xml.dom.pulldom", NULL, 581, 10656, NUITKA_BYTECODE_FLAG},
    {"xml.dom.xmlbuilder", NULL, 582, 12459, NUITKA_BYTECODE_FLAG},
    {"xml.etree", NULL, 68, 87, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.etree.ElementInclude", NULL, 583, 1544, NUITKA_BYTECODE_FLAG},
    {"xml.etree.ElementPath", NULL, 584, 8399, NUITKA_BYTECODE_FLAG},
    {"xml.etree.ElementTree", NULL, 69, 55599, NUITKA_BYTECODE_FLAG},
    {"xml.etree.cElementTree", NULL, 585, 138, NUITKA_BYTECODE_FLAG},
    {"xml.parsers", NULL, 586, 261, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.parsers.expat", NULL, 587, 299, NUITKA_BYTECODE_FLAG},
    {"xml.sax", NULL, 588, 3175, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xml.sax._exceptions", NULL, 589, 5409, NUITKA_BYTECODE_FLAG},
    {"xml.sax.expatreader", NULL, 590, 12460, NUITKA_BYTECODE_FLAG},
    {"xml.sax.handler", NULL, 591, 12387, NUITKA_BYTECODE_FLAG},
    {"xml.sax.saxutils", NULL, 592, 12884, NUITKA_BYTECODE_FLAG},
    {"xml.sax.xmlreader", NULL, 593, 16809, NUITKA_BYTECODE_FLAG},
    {"xmlrpc", NULL, 594, 84, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG},
    {"xmlrpc.client", NULL, 595, 34504, NUITKA_BYTECODE_FLAG},
    {"xmlrpc.server", NULL, 596, 29373, NUITKA_BYTECODE_FLAG},
    {"zipapp", NULL, 597, 5819, NUITKA_BYTECODE_FLAG},
    {"zipfile", NULL, 70, 58479, NUITKA_BYTECODE_FLAG},
    {NULL, NULL, 0, 0, 0}
};


void setupMetaPathBasedLoader(void) {
    static bool init_done = false;
    if (init_done == false) {
        loadConstantsBlob((PyObject **)bytecode_data, ".bytecode", 598);
        registerMetaPathBasedUnfreezer(meta_path_loader_entries, bytecode_data);

        init_done = true;
    }


}

// This provides the frozen (compiled bytecode) files that are included if
// any.

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    int index;
    int size;
};

static struct frozen_desc _frozen_modules[] = {
    {"_collections_abc", 73, 28706},
    {"_compression", 75, 4111},
    {"_weakrefset", 84, 7565},
    {"abc", 0, 5299},
    {"base64", 1, 17036},
    {"bz2", 119, 11410},
    {"codecs", 4, 33921},
    {"collections", 5, -46391},
    {"collections.abc", 127, 28705},
    {"copyreg", 136, 4283},
    {"dis", 149, 15773},
    {"encodings", 19, -3859},
    {"encodings.aliases", 226, 6295},
    {"encodings.ascii", 227, 1846},
    {"encodings.base64_codec", 228, 2364},
    {"encodings.big5", 229, 1374},
    {"encodings.big5hkscs", 230, 1384},
    {"encodings.bz2_codec", 231, 3255},
    {"encodings.charmap", 232, 2856},
    {"encodings.cp037", 233, 2387},
    {"encodings.cp1006", 234, 2463},
    {"encodings.cp1026", 235, 2391},
    {"encodings.cp1125", 236, 8094},
    {"encodings.cp1140", 237, 2377},
    {"encodings.cp1250", 238, 2414},
    {"encodings.cp1251", 239, 2411},
    {"encodings.cp1252", 240, 2414},
    {"encodings.cp1253", 241, 2427},
    {"encodings.cp1254", 242, 2416},
    {"encodings.cp1255", 243, 2435},
    {"encodings.cp1256", 244, 2413},
    {"encodings.cp1257", 245, 2421},
    {"encodings.cp1258", 246, 2419},
    {"encodings.cp273", 247, 2373},
    {"encodings.cp424", 248, 2417},
    {"encodings.cp437", 249, 7811},
    {"encodings.cp500", 250, 2387},
    {"encodings.cp720", 251, 2484},
    {"encodings.cp737", 252, 8133},
    {"encodings.cp775", 253, 7841},
    {"encodings.cp850", 254, 7472},
    {"encodings.cp852", 255, 7849},
    {"encodings.cp855", 256, 8102},
    {"encodings.cp856", 257, 2449},
    {"encodings.cp857", 258, 7452},
    {"encodings.cp858", 259, 7442},
    {"encodings.cp860", 260, 7790},
    {"encodings.cp861", 261, 7805},
    {"encodings.cp862", 262, 7994},
    {"encodings.cp863", 263, 7805},
    {"encodings.cp864", 264, 7949},
    {"encodings.cp865", 265, 7805},
    {"encodings.cp866", 266, 8138},
    {"encodings.cp869", 267, 7829},
    {"encodings.cp874", 268, 2515},
    {"encodings.cp875", 269, 2384},
    {"encodings.cp932", 270, 1376},
    {"encodings.cp949", 271, 1376},
    {"encodings.cp950", 272, 1376},
    {"encodings.euc_jis_2004", 273, 1390},
    {"encodings.euc_jisx0213", 274, 1390},
    {"encodings.euc_jp", 275, 1378},
    {"encodings.euc_kr", 276, 1378},
    {"encodings.gb18030", 277, 1380},
    {"encodings.gb2312", 278, 1378},
    {"encodings.gbk", 279, 1372},
    {"encodings.hex_codec", 280, 2351},
    {"encodings.hp_roman8", 281, 2588},
    {"encodings.hz", 282, 1370},
    {"encodings.idna", 20, 5582},
    {"encodings.iso2022_jp", 283, 1391},
    {"encodings.iso2022_jp_1", 284, 1395},
    {"encodings.iso2022_jp_2", 285, 1395},
    {"encodings.iso2022_jp_2004", 286, 1401},
    {"encodings.iso2022_jp_3", 287, 1395},
    {"encodings.iso2022_jp_ext", 288, 1399},
    {"encodings.iso2022_kr", 289, 1391},
    {"encodings.iso8859_1", 290, 2386},
    {"encodings.iso8859_10", 291, 2391},
    {"encodings.iso8859_11", 292, 2485},
    {"encodings.iso8859_13", 293, 2394},
    {"encodings.iso8859_14", 294, 2412},
    {"encodings.iso8859_15", 295, 2391},
    {"encodings.iso8859_16", 296, 2393},
    {"encodings.iso8859_2", 297, 2386},
    {"encodings.iso8859_3", 298, 2393},
    {"encodings.iso8859_4", 299, 2386},
    {"encodings.iso8859_5", 300, 2387},
    {"encodings.iso8859_6", 301, 2431},
    {"encodings.iso8859_7", 302, 2394},
    {"encodings.iso8859_8", 303, 2425},
    {"encodings.iso8859_9", 304, 2386},
    {"encodings.johab", 305, 1376},
    {"encodings.koi8_r", 306, 2438},
    {"encodings.koi8_t", 307, 2349},
    {"encodings.koi8_u", 308, 2424},
    {"encodings.kz1048", 309, 2401},
    {"encodings.latin_1", 310, 1858},
    {"encodings.mac_arabic", 311, 7705},
    {"encodings.mac_centeuro", 312, 2425},
    {"encodings.mac_croatian", 313, 2433},
    {"encodings.mac_cyrillic", 314, 2423},
    {"encodings.mac_farsi", 315, 2367},
    {"encodings.mac_greek", 316, 2407},
    {"encodings.mac_iceland", 317, 2426},
    {"encodings.mac_latin2", 318, 2567},
    {"encodings.mac_roman", 319, 2424},
    {"encodings.mac_romanian", 320, 2434},
    {"encodings.mac_turkish", 321, 2427},
    {"encodings.mbcs", 322, 1676},
    {"encodings.oem", 323, 1489},
    {"encodings.palmos", 324, 2414},
    {"encodings.ptcp154", 325, 2508},
    {"encodings.punycode", 326, 6280},
    {"encodings.quopri_codec", 327, 2380},
    {"encodings.raw_unicode_escape", 328, 1727},
    {"encodings.rot_13", 329, 2966},
    {"encodings.shift_jis", 330, 1384},
    {"encodings.shift_jis_2004", 331, 1394},
    {"encodings.shift_jisx0213", 332, 1394},
    {"encodings.tis_620", 333, 2476},
    {"encodings.undefined", 334, 2060},
    {"encodings.unicode_escape", 335, 1707},
    {"encodings.utf_16", 336, 4837},
    {"encodings.utf_16_be", 337, 1615},
    {"encodings.utf_16_le", 338, 1615},
    {"encodings.utf_32", 339, 4730},
    {"encodings.utf_32_be", 340, 1508},
    {"encodings.utf_32_le", 341, 1508},
    {"encodings.utf_7", 342, 1536},
    {"encodings.utf_8", 343, 1595},
    {"encodings.utf_8_sig", 344, 4511},
    {"encodings.uu_codec", 345, 3214},
    {"encodings.zlib_codec", 346, 3074},
    {"enum", 21, 25899},
    {"functools", 22, 27866},
    {"genericpath", 353, 3966},
    {"heapq", 357, 14035},
    {"importlib", 29, -3714},
    {"importlib._bootstrap", 367, 28570},
    {"importlib._bootstrap_external", 368, 43675},
    {"importlib.machinery", 30, 927},
    {"inspect", 33, 80558},
    {"io", 34, 3419},
    {"keyword", 37, 963},
    {"linecache", 446, 3832},
    {"locale", 38, 34654},
    {"ntpath", 42, 14622},
    {"opcode", 480, 5385},
    {"operator", 43, 13656},
    {"os", 481, 31362},
    {"quopri", 497, 5713},
    {"re", 50, 14387},
    {"reprlib", 498, 5268},
    {"sre_compile", 514, 15107},
    {"sre_constants", 515, 6324},
    {"sre_parse", 516, 21612},
    {"stat", 55, 4337},
    {"stringprep", 518, 10982},
    {"struct", 57, 295},
    {"threading", 60, 39941},
    {"token", 542, 2450},
    {"tokenize", 543, 17125},
    {"types", 547, 9142},
    {"warnings", 66, 13617},
    {NULL, 0, 0}
};


void copyFrozenModulesTo(struct _frozen *destination) {
    loadConstantsBlob((PyObject **)bytecode_data, ".bytecode", 598);

    struct frozen_desc *current = _frozen_modules;

    for(;;) {
        destination->name = (char *)current->name;
        destination->code = bytecode_data[current->index];
        destination->size = current->size;

        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}


