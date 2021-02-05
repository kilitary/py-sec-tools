rule __PseudoSigner_0_2_CrunchPE_Heuristic_ykdico
{
	meta:
		description = "_ PseudoSigner 0_2 _CrunchPE Heuristic"
	strings:
		$a = {55E80E0000005D83ED068BC5556089AD????????2B8500000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
