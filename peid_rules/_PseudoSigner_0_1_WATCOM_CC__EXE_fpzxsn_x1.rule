rule __PseudoSigner_0_1_WATCOM_CC__EXE_fpzxsn
{
	meta:
		description = "_ PseudoSigner 0_1 _WATCOM CC__ EXE"
	strings:
		$a = {E900000000909090905741E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
