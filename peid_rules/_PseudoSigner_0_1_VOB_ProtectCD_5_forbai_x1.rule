rule __PseudoSigner_0_1_VOB_ProtectCD_5_forbai
{
	meta:
		description = "_ PseudoSigner 0_1 _VOB ProtectCD 5"
	strings:
		$a = {363E268AC060E800000000E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
