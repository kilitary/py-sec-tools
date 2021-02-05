rule __PseudoSigner_0_2_Watcom_CC__DLL_mvrlqy
{
	meta:
		description = "_ PseudoSigner 0_2 _Watcom CC__ DLL"
	strings:
		$a = {535657558B7424148B7C24188B6C241C83FF030F8701000000F1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
