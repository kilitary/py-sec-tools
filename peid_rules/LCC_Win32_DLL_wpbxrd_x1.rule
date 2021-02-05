rule _LCC_Win32_DLL_wpbxrd
{
	meta:
		description = "LCC Win32 DLL"
	strings:
		$a = {5589E5535657837D0C017505E817??????FF7510FF750CFF7508A1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
