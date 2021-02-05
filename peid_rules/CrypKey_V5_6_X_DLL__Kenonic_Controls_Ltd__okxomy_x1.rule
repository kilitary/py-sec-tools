rule _CrypKey_V5_6_X_DLL__Kenonic_Controls_Ltd__okxomy
{
	meta:
		description = "CrypKey V5_6_X DLL __ Kenonic Controls Ltd_"
	strings:
		$a = {8B1D????????83FB00750AE8????????E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
