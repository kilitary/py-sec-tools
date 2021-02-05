rule __PseudoSigner_0_2_WATCOM_CC__EXE_bwjxze
{
	meta:
		description = "_ PseudoSigner 0_2 _WATCOM CC__ EXE"
	strings:
		$a = {E900000000909090905741}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
