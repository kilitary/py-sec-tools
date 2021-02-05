rule __PseudoSigner_0_2_LCC_Win32_1_x_hawocd
{
	meta:
		description = "_ PseudoSigner 0_2 _LCC Win32 1_x"
	strings:
		$a = {64A1010000005589E56AFF68????????689A10409050}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
