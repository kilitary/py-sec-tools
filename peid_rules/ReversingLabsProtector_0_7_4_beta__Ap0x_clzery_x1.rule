rule _ReversingLabsProtector_0_7_4_beta__Ap0x_clzery
{
	meta:
		description = "ReversingLabsProtector 0_7_4 beta __ Ap0x"
	strings:
		$a = {6800004100E801000000C3C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
