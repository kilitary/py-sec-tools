rule __PseudoSigner_0_2_VOB_ProtectCD_5_ipndlf
{
	meta:
		description = "_ PseudoSigner 0_2 _VOB ProtectCD 5"
	strings:
		$a = {363E268AC060E800000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
