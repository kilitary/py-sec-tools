rule _WATCOM_CC__DLL_ucvsll
{
	meta:
		description = "WATCOM CC__ DLL"
	strings:
		$a = {535657558B7424148B7C24188B6C241C83FF030F87}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
