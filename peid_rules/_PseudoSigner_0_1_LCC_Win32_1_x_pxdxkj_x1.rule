rule __PseudoSigner_0_1_LCC_Win32_1_x_pxdxkj
{
	meta:
		description = "_ PseudoSigner 0_1 _LCC Win32 1_x"
	strings:
		$a = {64A1010000005589E56AFF68????????689A10409050E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
