rule __PseudoSigner_0_1_MinGW_GCC_2_x_rqqbdo
{
	meta:
		description = "_ PseudoSigner 0_1 _MinGW GCC 2_x"
	strings:
		$a = {5589E5E802000000C9C39090455845E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
