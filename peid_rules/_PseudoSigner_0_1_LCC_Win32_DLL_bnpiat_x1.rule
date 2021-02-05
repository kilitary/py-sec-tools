rule __PseudoSigner_0_1_LCC_Win32_DLL_bnpiat
{
	meta:
		description = "_ PseudoSigner 0_1 _LCC Win32 DLL"
	strings:
		$a = {5589E5535657837D0C017505E817909090FF7510FF750CFF7508A1????????E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
