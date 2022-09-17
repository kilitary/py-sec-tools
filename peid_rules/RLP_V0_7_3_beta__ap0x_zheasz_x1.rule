rule _RLP_V0_7_3_beta__ap0x_zheasz
{
	meta:
		description = "RLP V0_7_3_beta __ ap0x"
	strings:
		$a = {2E726C700000000000500000????????????????????????000000000000000000000000200000E0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
